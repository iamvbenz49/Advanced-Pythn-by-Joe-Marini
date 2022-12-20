# demonstrate template string functions
from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders
    temp1 = Template("You're watchin ${title} by ${author}")
    # TODO: use the substitute method with keyword arguments
    str2= temp1.substitute(title="interstellar",author="nolan")
    print(str2)
    # TODO: use the substitute method with a 
    d = {
        "author":"vj benz",
        "title":"end of the world"
    }
    str3 = temp1.substitute(d)
    print(str3)

    
if __name__ == "__main__":
    main()
    