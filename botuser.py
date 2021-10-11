import telethon
import asyncio
import time
from telethon import TelegramClient, events

api_id =7663658
api_hash='af02fdc5732e6bb700bb382498eb9076'
bot=TelegramClient('session', api_id, api_hash)
bot.start()

print('Запуск...')

print('УСПЕШНО!')
@bot.on(events.NewMessage)
async def my_event_handler(event):
    if "✅" in event.raw_text:
         bot.send_message(1991258107, event.raw_text)
         
        
        
        		
        
         

         
            
           
            
            	
            
    	
       
bot.run_until_disconnected()