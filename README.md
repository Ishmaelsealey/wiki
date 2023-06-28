# Wiki

This is the second project of the CS50 course that I am doing.

## How to move on

To create an input field for creating a new entry I need to make a new **url**, **view** and **html** page. Going over the python lecture or notes will help.

Putting an edit url or view has to go in the entries.html file.

### Search Bar Function

```py
     def search1(query):
         for item in items:
            if query == item:
                print(f'exact match -> {item}')
            elif item.__contains__(query):
                print(item)
```

May have to implement the functionality of the function above in one of my `views.py` file functions
I might have to create a new function in `views.py` specifically for the search button.
It would have to use the list_entries function in the `util.py` file if the query is not an exact match
Otherwise it would use the get_entry function to open the file once it is an exact match
