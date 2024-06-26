from django.db import models

# Create your models here.

class PhoneNumber(models.Model):
    number = models.CharField(max_length=200)
    def __str__(self):
        return self.number
    

class Email(models.Model):
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.email
    
class Location(models.Model):
    location=models.TextField(blank=True,null=True)

class Map(models.Model):
    map_link=models.TextField(blank=True,null=True)
    

class OpeningHours(models.Model):
    Days = models.CharField(max_length=200)
    def __str__(self):
        return self.Days
    
class Hours(models.Model):
    days=models.ForeignKey(OpeningHours,on_delete=models.CASCADE)
    Hours = models.CharField(max_length=200)




class HomePage(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)

class PTagHome(models.Model):
    home=models.ForeignKey(HomePage,on_delete=models.CASCADE)
    parag=models.TextField(blank=True,null=True)




class FensterPage(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)

class Fenster(models.Model):
    fensterpage=models.ForeignKey(FensterPage,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    innerTitle=models.CharField(max_length=250,blank=True,null=True)
    text=models.TextField(blank=True,null=True)
    bottom=models.CharField(max_length=250,blank=True,null=True)

class FensterPoints(models.Model):
    fenster=models.ForeignKey(Fenster,on_delete=models.CASCADE)
    point=models.CharField(max_length=250,blank=True,null=True)



class KunAluFensterPage(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)

class AluFenster(models.Model):
    fensterpage=models.ForeignKey(KunAluFensterPage,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    innerTitle=models.CharField(max_length=250,blank=True,null=True)
    text=models.TextField(blank=True,null=True)
    bottom=models.CharField(max_length=250,blank=True,null=True)



class HolzAluFensterPage(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.title

class HolzAluFenster(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)
    #innerTitle=models.CharField(max_length=250,blank=True,null=True)
    #text=models.TextField(blank=True,null=True)
    #bottom=models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.title

class HolzAluImages(models.Model):
    holzalufenster=models.ForeignKey(HolzAluFenster,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)

    class Meta:
        verbose_name='Carousel Image'

class HolzAluSidePoints(models.Model):
    holzalufenster=models.ForeignKey(HolzAluFenster,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)
    description=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)

    class Meta:
        verbose_name='Side Point'


class HolzAluBottomImage(models.Model):
    holzalufenster=models.ForeignKey(HolzAluFenster,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)
    description=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)

    class Meta:
        verbose_name='Bottom Image'





class HolzFenster(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)
    #innerTitle=models.CharField(max_length=250,blank=True,null=True)
    #text=models.TextField(blank=True,null=True)
    #bottom=models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.title

class HolzImages(models.Model):
    holzfenster=models.ForeignKey(HolzFenster,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)

    class Meta:
        verbose_name='Carousel Image'

class HolzSidePoints(models.Model):
    holzfenster=models.ForeignKey(HolzFenster,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)
    description=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)

    class Meta:
        verbose_name='Side Point'


class HolzBottomImage(models.Model):
    holzfenster=models.ForeignKey(HolzFenster,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)
    description=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)

    class Meta:
        verbose_name='Bottom Image'






class TurenPage(models.Model):
    text=models.TextField(blank=True,null=True)
    button_text=models.CharField(max_length=250,blank=True,null=True)
    button_link=models.CharField(max_length=250,blank=True,null=True)





class ToranLagenPage(models.Model):
    title=models.CharField(max_length=250,blank=True,null=True)
    subtitle=models.CharField(max_length=250,blank=True,null=True)
    inner_title=models.CharField(max_length=250,blank=True,null=True)

class ToranLangenImage(models.Model):
    toranpage=models.ForeignKey(ToranLagenPage,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)