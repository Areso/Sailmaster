import http from "k6/http";
import { check } from "k6";

export const options = {
  vus: 1,
  duration: "4s"
};

export default function() {
  const res = http.get("http://cosmodream.ga");
  check(res, { "status was 200": r => r.status == 200 })
};

