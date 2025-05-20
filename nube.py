from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields as F

api= Api("patL2yxUscnqr5Jh1.32c1bc3880d3d682470945cc89b4332148a62e02d2025584a92692551a65bdd7")
table= api.table("appPIGX9uzEsCr0jC","receta")

class Receta(Model):
    medicamento= F.TextField("medicamento")
    interacciones= F.TextField("interacciones")
    class Meta:
        api_key= "patL2yxUscnqr5Jh1.32c1bc3880d3d682470945cc89b4332148a62e02d2025584a92692551a65bdd7"
        base_id= "appPIGX9uzEsCr0jC"
        table_name= "receta"
        
