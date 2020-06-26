echo "Enter message"
read message
echo "interval? (just press enter)"
read int

for i in {1..1};
do    
curl \
-H "Authorization: TOKEN" \
-H "User-Agent: WebKit" \
-H "Content-Type: application/json" \
-X POST \
-d "{\"content\": \"${message}\"}" \
https://discordapp.com/api/v6/channels/712795630447362059/messages
echo "message succesfully sent!"
sleep $int;
done
