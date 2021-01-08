
################### models declarations ##################
class Programmer(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Software(models.Model):
    title = models.CharField(max_length=300)
    programmers = models.ManyToManyField(Programmer)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



# programmers creation
>>> nabil = Programmer(name='nabil'); nabil.save()
>>> jamal = Programmer(name='jamal'); jamal.save()
# softwares creation
>>> medical_product = Software(title='medical product'); medical_product.save()
>>> management_product = Software(title='management product'); management_product.save()

# add programmers to a software
>>> medical_product.programmers.add(nabil, jamal)
>>> management_product.programmers.add(nabil, jamal)

# fetch software programmers
>>> medical_product.programmers.all()
<QuerySet [<Programmer: jamal>, <Programmer: nabil>]>
>>> management_product.programmers.all()
<QuerySet [<Programmer: jamal>, <Programmer: nabil>]>

# fetch softwares created by a programmer
>>> jamal.software_set.all()
<QuerySet [<Software: management product>, <Software: medical product>]>
>>> nabil.software_set.all()
<QuerySet [<Software: management product>, <Software: medical product>]>
                                                                       
