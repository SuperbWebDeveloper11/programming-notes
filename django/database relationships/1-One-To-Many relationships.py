
#################### models declaration ##########################

class Author(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



# author creation
>>> amine = Author(name='amine' email='amine@gmail.com'); amine.save()
>>> ahmed = Author(name='ahmed' email='ahmed@gmail.com'); ahmed.save()
# post creation
>>> python_oop = Post(title='oop in python' author=amine); python_oop.save()
>>> python_inheritance = Post(title='inheritance in python' author=amine); python_inheritance.save()
>>> javascript_inheritance = Post(title='inheritance in javascript' author=ahmed); javascript_inheritance.save()
>>> javascript_oop = Post(title='oop in javascript' author=ahmed); javascript_oop.save()

# query post title and post author
>>> python_oop.title # 'oop in python'
>>> python_oop.author.name # 'amine'
>>> javascript_oop.title # 'oop in javascript'
>>> javascript_oop.author.name # 'ahmed'

# query author posts
>>> ahmed.post_set.all()
<QuerySet [<Post: inheritance in javascript>, <Post: oop in javascript>]>
>>> amine.post_set.all()
<QuerySet [<Post: inheritance in python>, <Post: oop in python>]>

# post cration using an author instance
>>> new_post = ahmed.post_set.create(title='javascript functional programming')
>>> new_post.title # 'javascript functional programming'
>>> new_post.author.name # 'ahmed'

# filtering results
>>> amine.post_set.all()
<QuerySet [<Post: inheritance in python>, <Post: oop in python>]>

>>> amine.post_set.count() # 2
>>> amine.post_set.filter(title='oop in python')
<QuerySet [<Post: oop in python>]>
>>> amine.post_set.filter(title__startswith='inheritance')
<QuerySet [<Post: inheritance in python>]>
>>> amine.post_set.filter(title__contains='oop')
<QuerySet [<Post: oop in python>]>

>>> Post.objects.all()
<QuerySet [
        <Post: inheritance in javascript>, 
        <Post: inheritance in python>, 
        <Post: javascript functional programming>, 
        <Post: oop in javascript>, 
        <Post: oop in python>
        ]>

>>> Post.objects.filter(author__name='amin')
<QuerySet []>
>>> Post.objects.filter(author__name='amine')
<QuerySet [<Post: inheritance in python>, <Post: oop in python>]>
>>> Post.objects.filter(author__pk=3)
<QuerySet [<Post: inheritance in python>, <Post: oop in python>]>
>>> Post.objects.filter(author=3)
<QuerySet [<Post: inheritance in python>, <Post: oop in python>]>
>>> Post.objects.filter(author__in=[3, 4])
<QuerySet [<Post: inheritance in javascript>, <Post: inheritance in python>, <Post: javascript functional programming>, <Post: oop in javascript>, <Post: oop in python>]>


