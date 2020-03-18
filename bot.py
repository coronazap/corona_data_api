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
    if 'dados' in incoming_message: 
        # GET request for the updated data 
        r = requests.get('https://pomber.github.io/covid19/timeseries.json') 

        if r.status_code == 200: 
            data = r.json() 
            # Get brazilian data 
            brazilData = data["Brazil"] 

            # Generate response
            response = "Até o momento, no *Brasil*, temos os seguintes casos: \n \n - Confirmados: " + \
                            str(brazilData[-1]['confirmed']) + " \n - Óbitos: " + \
                            str(brazilData[-1]['deaths']) + " \n - Recuperados: " + \
                            str(brazilData[-1]['recovered'])

        msg.body(response)
        responded = True
    
    if not responded: 
        msg.body('Infelizmente, *por enquanto*, só posso te oferecer dados! \n \n Se quiser visualizá-los, envie "Dados".')

    return(str(resp))

if __name__ == '__main__':
   app.run(debug=True)


