class Motorcycle:
    is_engine_on = False
    is_headlight_on = False
    make = None
    model = None

    def __init__(self,make,model):
        self.make = make
        self.model =model

    
    def __repr__(self):
        return(f'{self.make} {self.model} with engine '
               f'{"on" if self.is_engine_on else "off"} and headlight '
               f'{"on" if self.is_headlight_on else "off"}')    
    
    def turn_engine_on(self):
        self.is_engine_on = True
        
 
moto = Motorcycle('Triumph' , 'Thruxton')
print(moto)
print(moto.is_engine_on)

moto.turn_engine_on()
print(moto.is_engine_on)