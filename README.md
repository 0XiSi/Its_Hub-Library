<h1>Intro </h1>
<p>
Its_Hub library. <br />
This is a library with Other Libraries! (; <br />
U Can Use This Library For Use Few Other Library. 4 Example:
<b>
<ul>
    <li>Faker</li>
    <li>Tkinter</li>
    <li>CV2</li>
    <li>Tkhtmlview</li>
    <li>...</li>
</ul>
</b>

My name is Farbod Parkhooi(Or you can call me Tik Ten) <br />
This is my Github link: <a href="https://www.github.com/tik-ten/">`https://www.github.com/tik-ten/`</a> <br />
Thanks for use.<br />
</p>
<h2>Use Libraries </h2>
    For use Its_Hub you can use This:

```python
hub = Its_Hub()
````

# How to use ... library
<ul>
    <li><a href="#Faker">Faker</a></li>
    <li><a href="#Fake_profile">Fake_profile</a></li>
    <li><a href="#Mini">Mini</a></li>
</ul>

# Faker
For use Faker:
```python
Its_Hub.Faker(target="") # "first_name" or "last_name" or "name" or "phone_number" or "address" or "profile" or "job" or "company" or "website" or "blood_group"

# You can print that:
print(Its_Hub.Faker(target="name"))
# and you can save taht in a value
name = Its_Hub.Faker(target="name") 
```

# Fake_profile 
### Show a digital fake profile
```python
profile = hub.Fake_profile() # You can coustomise job, company, name, and ...
profile.Create_result(profile.Create_profile()) 
```
output:

<img src="Files\out1.png">

### Create list of a fake profile
```python
profile = hub.Fake_profile()
Profile_list = profile.Create_profile()
print(Profile_list)
```
# Mini
### Plus
You can use this function for num1 + num2 (:
```python
ans = hub.Mini.Plus(number=8, plus=10)
print(ans)
```
### Count
You can count and plus with this function.
```python
count_ans = hub.Mini.Count(0, 5)
print(count_ans)
```
