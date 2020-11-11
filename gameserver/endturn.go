// endturn.go
package main

import (
	"database/sql"
	"fmt"
	"io/ioutil" //required for io with filesystem
	"log"       //required for log
	"strings"   //required for Split database/sql
	"net/http"  //required for http
	_ "github.com/go-sql-driver/mysql"
)

type Account struct {
	id    int
	login string
	pass  string
}

func char_create(rw http.ResponseWriter, req *http.Request) {
	rw.Write([]byte("char created"))
}

func main() {
	log.Println("log.PrintLn test")
	config_auth_b, err := ioutil.ReadFile("config_auth.txt")
	if err != nil {
		log.Fatal(err)
	}
	config_auth_s := string(config_auth_b)
	var config_auth_a [5]string
	iterator := 0
	for _, line := range strings.Split(strings.TrimSuffix(config_auth_s, "\n"), "\n") {
		fmt.Println(line)
		config_auth_a[iterator] = line
		iterator += 1
	}
	connect_string := "%user:%pass@tcp(%host:%port)/%db"
	connect_string = strings.Replace(connect_string, "%user", config_auth_a[3], 1)
	connect_string = strings.Replace(connect_string, "%pass", config_auth_a[4], 1)
	connect_string = strings.Replace(connect_string, "%host", config_auth_a[0], 1)
	connect_string = strings.Replace(connect_string, "%port", config_auth_a[1], 1)
	connect_string = strings.Replace(connect_string, "%db", config_auth_a[2], 1)
	fmt.Println(connect_string)
	db, err := sql.Open("mysql", connect_string)

	if err != nil {
		fmt.Println("error connecting to db")
		panic(err.Error())
	}
	// defer the close till after the main function has finished
	// executing
	defer db.Close()

	results, err := db.Query("SELECT * FROM dbstat;")
	if err != nil {
		panic(err.Error()) // proper error handling instead of panic in your app
	}

	
	http.Handle("/char_create", http.HandlerFunc(char_create))
	log.Fatal(http.ListenAndServe(":6199", nil))

	for results.Next() {
		var account Account
		// for each row, scan the result into our tag composite object
		err = results.Scan(&account.id, &account.login)
		if err != nil {
			panic(err.Error()) // proper error handling instead of panic in your app
		}
		//and then print out the tag's Name attribute
		log.Printf(account.login)
	}
	//fmt.Println(account.login)
}
