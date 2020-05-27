# **Course Models**
---
The following models are used for storing the information for a given course and its members.
 
- [Course](#course-model)
- [CourseMember](#coursemember-model)
- [CourseComplete](#coursecomplete-object)

<br>

<a name="course-model"></a>
### - Course (Table)
---
Courses are linked to the Order Model, course that have more then one teacher such as Step One will
have two separate course objects with the difference being in the name, either math or science.

##### *Fields*
---
| FIELD           | TYPE           | NOTES                           |
| :-------------- | :------------- | :------------------------------ |
| <img width=100> | <img width=75> | <img width=200>                 |
| teacher         | user           | master teacher of course        |
| code            | char           | code for class (ie: CSCE 4133)  |
| name            | char           | name of course (ie: Algorithms) |

<br>

##### *Code*
---
```python
    class Course(models.Model):
        teacher = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='teacher',
            null=False
        )
        code = models.CharField(max_length=10)
        name = models.CharField(max_length=50)
```

<br>


<a name="coursemember-model"></a>
### - CourseMember (Table)
---
Links users and courses. 
##### *Fields*
---
| FIELD           | TYPE                    | NOTES                           |
| :-------------- | :---------------------- | :------------------------------ |
| <img width=150> | <img width=75>          | <img width=200>                 |
| course          | [course](#course-model) | master teacher of course        |
| course_member   | user                    | code for class (ie: CSCE 4133)  |

<br>

##### *Code*
---
```python
    class CourseMember(models.Model):
        course = models.ForeignKey(
            Course,
            on_delete=models.CASCADE,
        )
        course_member = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='course_member',
            null=False
        )
```

<br>

<a name="coursecomplete-object"></a>
## - CourseComplete (Object)
---
CourseComplete is a local object that is used for storing all the values associated for a given course such as
the course itself, its members, and associated orders. See 
<a href="javascript:void(null);" onclick="getDocumentByPath('./documentation/documents/materials/Views/Helper-Views.md', 'coursecomplete');">
Helper Views 
</a>
for more on the function that builds the CourseComplete object.

<br>

##### *Code*
---
```python
    class CourseComplete:
        course = Course()
        members = []
        orders = []
```