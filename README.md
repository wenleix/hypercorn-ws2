# Start Hypercorn Server
```
pip install -r requirements.txt
hypercorn app:app -b 127.0.0.1:8765
```

# Run Client that Close after Sending Text Message
```
python client.py
```

# Results

Server side log shows the connection was succesfully established and was able to receiving "Hello World!" string. However, the connection close code was considered as 1006 (abonormal close without close frame), albeit client side indeed send the close frame with close code 1000.

```
Received: Hello World!
Client disconnected with code 1006
```
