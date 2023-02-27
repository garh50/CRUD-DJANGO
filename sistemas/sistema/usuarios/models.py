from django.db import models
class Usuario(models.Model):
    rowid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255)
    Apellidos = models.CharField(max_length=255, blank=True, null=True)
    Nombres = models.CharField(max_length=255, blank=True, null=True)
    Nacimiento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    #countryid = models.IntegerField(blank=True, null=True)
    #cityid = models.IntegerField(blank=True, null=True)
    #stateid = models.IntegerField(blank=True, null=True)
    #address = models.CharField(max_length=255, blank=True, null=True)
    #positionid = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    #legalid = models.CharField(max_length=255, blank=True, null=True)
    #image = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='imagen',null=True)
    createdate = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        fila = ' Nombre: '+str(self.Apellidos) +', '+str(self.Nombres)
        return fila
    #'rowid: '+str(self.rowid)+' Id: '+str(self.id)+
    
    def delete(self, using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



#'rowid:'+str(self.rowid)+' Id:'+str(self.id)+ 
