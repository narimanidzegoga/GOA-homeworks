const body = document.body

const title = document.createElement("h1")
title.innerText = "Welcome to My Personal Blog"
body.appendChild(title)

const br1 = document.createElement("br")
body.appendChild(br1)


const navigation = document.createElement("ul")
body.appendChild(navigation)

const home = document.createElement("li")
const home_link = document.createElement("a")
home_link.href = ""
home_link.innerText = "Home"
home.appendChild(home_link)
navigation.appendChild(home)

const about_me = document.createElement("li")
const about_me_link = document.createElement("a")
about_me_link.href = ""
about_me_link.innerText = "About Me"
about_me.appendChild(about_me_link)
navigation.appendChild(about_me)

const blog = document.createElement("li")
const blog_link = document.createElement("a")
blog_link.href = ''
blog_link.innerText = 'Blog Posts'
blog.appendChild(blog_link)
navigation.appendChild(blog)

const contact = document.createElement("li")
const contact_link = document.createElement('a')
contact_link.href = ''
contact_link.innerText = 'Contact'
contact.appendChild(contact_link)
navigation.appendChild(contact)

const introduction = document.createElement('h2')
introduction.innerText = 'Introduction'
body.appendChild(introduction)

const intro_text = document.createElement('p')
intro_text.innerText = 'This is a place where I share my thoughts and experiences. Stay tuned for more updates!'
body.appendChild(intro_text)


const about_title = document.createElement('h2')
about_title.innerText = 'About Me'
body.appendChild(about_title)

const about_text = document.createElement('p')
about_text.innerText = 'I am a passionate writer and developer who enjoys sharing knowledge on various topics.'
body.appendChild(about_text)


const latest_blog = document.createElement('h2')
latest_blog.innerText = 'Latest Blog Posts'
body.appendChild(latest_blog)

const first_blog = document.createElement('h3')
first_blog.innerText = 'My First Blog Post'
body.appendChild(first_blog)

const text1 = document.createElement('p')
text1.innerText = "Welcome to my first blog post, I'll be discussing web development basics and more."
body.appendChild(text1)

const read_more

