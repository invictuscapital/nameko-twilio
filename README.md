# nameko-twilio

Twilio dependency for nameko services

## Installation
```python
pip install nameko-twilio
```

## Usage
```python
from nameko.rpc import rpc
from nameko_twilio import Twilio


class Service:
    name = "service"
    
    twilio = Twilio()
    
    @rpc
    def send_sms(self, number, message):
        msg = self.twilio.messages.create(
            number,
            body=f"Your mobile verification code for Invictus Capital is {payload['code']}.",
            from_="+1234567890"
        )
        return f"Message {msg.sid}"
```

Specify your configuration like this:
```yaml
TWILIO:
  SID: abcd
  TOKEN: efgh
```
