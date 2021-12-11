from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
	pass

	def __str__(self):
		return self.username

		

#Esto es el models para el Post.
class Post(models.Model):
	title= models.CharField(max_length=100) #Esto es el titulo, que puede tener como maximo 100 caracteres.
	content= models.TextField() #Esto es el contenido que tiene el post.
	thumbnail= models.ImageField()#Esto es una imagen que puede tener el post.
	publish_date= models.DateTimeField(auto_now_add=True)#Esta es la fecha de publicacion del post.
	last_updated= models.DateTimeField(auto_now=True)#Esto es la fecha en la que se actualizo el post.
	author= models.ForeignKey(User, on_delete=models.CASCADE)  #Esto es el autor del post.
	slug= models.SlugField()


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={
			'slug': self.slug
		})

	def get_like_url(self):
		return reverse("like", kwargs={
			'slug': self.slug
		})

	@property
	def comments(self):
		return self.comment_set.all()

	@property
	def get_comment_count(self):
		return self.comment_set.all().count()

	@property
	def get_view_count(self):
		return self.postview_set.all().count()

	@property
	def get_like_count(self):
		return self.like_set.all().count()


#Esto es el models para los comentarios.
class Comment(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE) #Usuario que hace el comment.
	post= models.ForeignKey(Post, on_delete= models.CASCADE) #Define a que post pertenece el comentario. El on_delete hace que se borre cuando se borre el post.
	timestamp= models.DateTimeField(auto_now_add=True) #ESTO ES PARA QUE MUESTRE EL TIEMPO QUE TIENE EL COMENTARIO
	content= models.TextField() #Este es el contenido que tiene el comment en si.

	def __str__(self):
		return self.user.username
	

#Esto muestra cuantas vistas tiene el post.
class PostView(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	post= models.ForeignKey(Post, on_delete=models.CASCADE)
	timestamp= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

#Esto muestra los likes del post.
class Like(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	post= models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username