const meet = document.createElement("img")
meet.src = "logo.svg"
document.body.appendChild(meet)

meet.style.width = "119px"
meet.style.height = "28px"
meet.style.marginTop = "80px"
meet.style.marginLeft = "661px"

const container = document.createElement("div")
container.style.marginTop = "169px"
container.style.display = "flex"
container.style.flexDirection = "row"
container.style.alignItems = "center"
container.style.justifyContent = "space-between"

document.body.appendChild(container)

const leftimg = document.createElement("img")
leftimg.src = "image-hero-left.png"
container.appendChild(leftimg)

const containerGC = document.createElement("div")
containerGC.style.width = "540px"
containerGC.style.marginTop = "216px"
containerGC.style.display = "flex"
containerGC.style.flexDirection = "column"
containerGC.style.alignItems = "center"
containerGC.style.justifyContent = "center"

container.appendChild(containerGC)

const groupchat = document.createElement("h2")
groupchat.innerText = "Group Chat for Everyone"
groupchat.style.width = "445px"
groupchat.style.fontSize = "64px"
groupchat.style.letterSpacing = "0px"

containerGC.appendChild(groupchat)

const text1 = document.createElement("p")
text1.innerText = "Meet makes it easy to connect with others face-to-face virtually and collaborate across any device."
text1.style.opacity = "60%"
containerGC.appendChild(text1)

const buttondiv = document.createElement("div")
buttondiv.style.display = "flex"
buttondiv.style.flexDirection = "row"
buttondiv.style.gap = "16px"

const button1 = document.createElement("button")
button1.style.backgroundColor = "#4D96A9"
button1.style.borderRadius = "29px"
button1.style.padding = "16px 40px"
button1.style.border = "none"
button1.style.outline = "none"
button1.style.cursor = "pointer"
button1.style.color = "#FFFFFF"
button1.style.fontSize = "16px"
button1.style.fontWeight = "700"

const b1_main_text = document.createTextNode("Download ")
const b1_v_text = document.createElement("span")
b1_v_text.innerText = "v1.3"
b1_v_text.style.color = "#8FE3F9"

button1.appendChild(b1_main_text)
button1.appendChild(b1_v_text)
buttondiv.appendChild(button1)

const button2 = document.createElement("button")
button2.innerText = "What is it?"
button2.style.backgroundColor = "#855FB1"
button2.style.color = "#FFFFFF"
button2.style.fontSize = "16px"
button2.style.fontWeight = "700"
button2.style.borderRadius = "29px"
button2.style.padding = "16px 40px"
button2.style.border = "none"
button2.style.outline = "none"
button2.style.cursor = "pointer"
buttondiv.appendChild(button2)

containerGC.appendChild(buttondiv)

const rightimg = document.createElement("img")
rightimg.src = "image-hero-right.png"
container.appendChild(rightimg)

const line1 = document.createElement("div")
line1.style.width = "1px"
line1.style.height = "84px"
line1.style.backgroundColor = "#87879D"
line1.style.opacity = "0.25"
line1.style.marginTop = "80px"
line1.style.marginLeft = "720px"
document.body.appendChild(line1)

const circle1 = document.createElement("div")
circle1.innerText = "01"
circle1.style.width = "56px"
circle1.style.height = "56px"
circle1.style.borderRadius = "28px"
circle1.style.borderWidth = "1px"
circle1.style.borderStyle = "solid"
circle1.style.borderColor = "#DCDCE1"
circle1.style.display = "flex"
circle1.style.alignItems = "center"
circle1.style.justifyContent = "center"
circle1.style.marginLeft = "692px"
circle1.style.color = "#87879D"
circle1.style.fontWeight = "700"
document.body.appendChild(circle1)

const imgcontainer = document.createElement("div")
imgcontainer.style.display = "flex"
imgcontainer.style.flexDirection = "row"
imgcontainer.style.justifyContent = "center"
imgcontainer.style.gap = "30px"
imgcontainer.style.marginTop = "64px"
document.body.appendChild(imgcontainer)

const img1 = document.createElement("img")
img1.src = "image-woman-in-videocall.jpg"
img1.style.width = "255px"
img1.style.height = "242px"
img1.style.borderRadius = "8px"
imgcontainer.appendChild(img1)

const img2 = document.createElement("img")
img2.src = "image-women-videochatting.jpg"
img2.style.width = "255px"
img2.style.height = "242px"
img2.style.borderRadius = "8px"
imgcontainer.appendChild(img2)

const img3 = document.createElement("img")
img3.src = "image-men-in-meeting.jpg"
img3.style.width = "255px"
img3.style.height = "242px"
img3.style.borderRadius = "8px"
imgcontainer.appendChild(img3)

const img4 = document.createElement("img")
img4.src = "image-man-texting.jpg"
img4.style.width = "255px"
img4.style.height = "242px"
img4.style.borderRadius = "8px"
imgcontainer.appendChild(img4)

const containerGC2 = document.createElement("div")
containerGC2.style.width = "540px"
containerGC2.style.display = "flex"
containerGC2.style.flexDirection = "column"
containerGC2.style.alignItems = "center"
containerGC2.style.marginTop = "64px"
containerGC2.style.marginLeft = "450px"
document.body.appendChild(containerGC2)

const texttag = document.createElement("p")
texttag.innerText = "BUILT FOR MODERN USE"
texttag.style.color = "#4D96A9"
texttag.style.letterSpacing = "4px"
texttag.style.fontWeight = "700"
texttag.style.fontSize = "16px"
containerGC2.appendChild(texttag)

const groupchat2 = document.createElement("h2")
groupchat2.innerText = "Smarter meetings, all in one place"
groupchat2.style.fontSize = "40px"
groupchat2.style.color = "#28283D"
groupchat2.style.marginTop = "16px"
groupchat2.style.width = "445px"
groupchat2.style.textAlign = "center"
containerGC2.appendChild(groupchat2)

const text2 = document.createElement("p")
text2.innerText = "Send messages, share files, show your screen, and record your meetings — all in one workspace. Control who can join with invite-only team access, data encryption, and data export."
text2.style.color = "#87879D"
text2.style.fontSize = "18px"
text2.style.width = "540px"
text2.style.textAlign = "center"
text2.style.marginTop = "32px"
containerGC2.appendChild(text2)

const line2 = document.createElement("div")
line2.style.width = "1px"
line2.style.height = "84px"
line2.style.backgroundColor = "#87879D"
line2.style.opacity = "0.25"
line2.style.marginTop = "80px"
line2.style.marginLeft = "720px"
document.body.appendChild(line2)

const circle2 = document.createElement("div")
circle2.innerText = "02"
circle2.style.width = "56px"
circle2.style.height = "56px"
circle2.style.borderRadius = "28px"
circle2.style.borderWidth = "1px"
circle2.style.borderStyle = "solid"
circle2.style.borderColor = "#DCDCE1"
circle2.style.display = "flex"
circle2.style.alignItems = "center"
circle2.style.justifyContent = "center"
circle2.style.color = "#87879D"
circle2.style.fontWeight = "700"
circle2.style.backgroundColor = "#FAFAFA"

document.body.appendChild(circle2)

const footer = document.createElement("div")
footer.style.background = "url('image-footer.jpg')"
footer.style.backgroundSize = "cover"
footer.style.height = "308px"
footer.style.display = "flex"
footer.style.flexDirection = "row"
footer.style.alignItems = "center"
footer.style.justifyContent = "space-around"
document.body.appendChild(footer)

const footertitle = document.createElement("h2")
footertitle.innerText = "Experience more together"
footertitle.style.color = "#FFFFFF"
footertitle.style.fontSize = "40px"
footertitle.style.width = "350px"
footer.appendChild(footertitle)

const footertext = document.createElement("p")
footertext.innerText = "Stay connected with reliable HD meetings and unlimited one-on-one and group video sessions."
footertext.style.color = "#FFFFFF"
footertext.style.fontSize = "18px"
footertext.style.width = "350px"
footertext.style.opacity = "0.8"
footer.appendChild(footertext)

const footerbutton = document.createElement("button")
footerbutton.style.backgroundColor = "#855FB1"
footerbutton.style.borderRadius = "29px"
footerbutton.style.width = "193px"
footerbutton.style.height = "58px"
footerbutton.style.borderWidth = "0px"
footerbutton.style.cursor = "pointer"
footerbutton.style.fontSize = "16px"
footerbutton.style.fontWeight = "700"
footerbutton.style.color = "#FFFFFF"

const f_main_text = document.createTextNode("Download ")
const f_v_text = document.createElement("span")
f_v_text.innerText = "v1.3"
f_v_text.style.color = "#8FE3F9"

footerbutton.appendChild(f_main_text)
footerbutton.appendChild(f_v_text)
footer.appendChild(footerbutton)