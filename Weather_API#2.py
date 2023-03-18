from cProfile import label
import requests
import time
import tkinter as tk
def get_Weather(canvas):
    city=textfield.get()
    API="api.openweathermap.org/data/2.5/weather?q="+city+"&appid=aea81102b99930f177dc9a7e6d3ba6a4"
    json_data=requests.get(api).json()
    weather=json_data['weather'][0]['main']
    
    temp=round(json_data["main"]["temp"]-273.15,2)


    

    
    
    
    min_temp=round(json_data["main"]["temp_min"]-273.15,2)
    max_temp=round(json_data["main"]["temp_max"]-273.15,2)
    pressure=round(json_data["main"]["pressure"],2)
    humidity=round(json_data["main"]["humidity"],2)
    wind=json_data["wind"]["speed"]
    final_info=weather+str(temp)+"C"
    final_data="\n"+"min_temp:"+str(min_temp)+"\n"+"Max_temp:"+str(max_temp)+"\n"+"Pressure:"+"\n"+str(pressure)+"\n"+"Humidity:"+str(humidity)+"\n"+"Wind:"+str(wind)+"\n"
    label1.config(text=final_info)
    label2.config(text=final_data) 

canvas=tk.Tk()
canvas.geometry("700x700")
canvas.title("Weather API")

f=("poppins",20,"italic")
t=("poppins",45,"italic")

textfield=tk.Entry(canvas,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',get_Weather)

label1=tk.Label(canvas,font=t)
label1.pack()
label2=tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()


