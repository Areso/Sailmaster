apt get purge golang*  
download binary&unpack to /usr/local/go  
nano /etc/profile  
export GOPATH=/usr/local/go/bin  
export PATH=$PATH:/usr/local/go/bin  
export GOROTT=/usr/local/go  
source /etc/profile  
go env  
go get github.com/go-sql-driver/mysql


