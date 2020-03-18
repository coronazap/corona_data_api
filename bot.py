from flask import Flask, request 
import requests 
from twilio.twiml.messaging_response import MessagingResponse 


app = Flask(__name__) 

@app.route('/bot', methods=['POST'])
def bot(): 
    # Get received message
    incoming_message = request.values.get('Body', '').lower() 
    
    # Create response instance 
    resp = MessagingResponse()
    msg = resp.message() 
    responded = False 

    # BOT LOGIC COMES HERE 

    # msg.body(string) -> Returns a text message 

    # msg.media(media_url) -> Returns a media 
    if 'ping' in incoming_message: 
        msg.body('Pong!') 
        responded = True 
    
    if not responded: 
        msg.body('Diga ping!')

    return(str(resp))

if __name__ == '__main__':
   app.run(debug=True)


