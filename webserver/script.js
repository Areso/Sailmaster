import http from "k6/http";
import { check } from "k6";

export const options = {
  vus: 3,
  duration: "10s"
};

export default function() {
  const res = http.get("http://localhost:6689/api/v1.0/heartbeat");
  check(res, { "status was 200": r => r.status == 200 })
};
