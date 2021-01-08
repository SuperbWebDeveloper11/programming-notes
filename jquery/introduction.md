
## what is jquery:
jQuery is an open source JavaScript library that simplifies the interactions between an HTML document, or more precisely the Document Object Model (aka the DOM), and JavaScript.


## why jquery:
 - It’s small (18 KB minified) and gzipped (114 KB, uncompressed).
 - It normalizes the differences between web browsers so that you don’t have to.
 - It has remained a JavaScript library (as opposed to a framework)
 - Its learning curve is approachable because it builds upon concepts that most developers and designers already understand (e.g., CSS and HTML)


## The jQuery Philosophy
 - Finding some elements (via CSS selectors) and doing something with them 
 - Chaining multiple jQuery methods on a set of elements
 - Using the jQuery wrapper and implicit iteration


## Including the jQuery Library Code in an HTML Page
 - Use the Google-hosted content delivery network (CDN)
 - Download your own version of jQuery from jQuery.com and host it on your own server or local filesystem.


## Executing jQuery/JavaScript Coded After the DOM Has Loaded but Before Complete Page Load

ex1: inside head tag
```
<script type="text/JavaScript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script type="text/JavaScript">
jQuery(document).ready(function(){//DOM not loaded, must use ready event
    alert(jQuery('p').text());
});
</script>
```

ex2: inside head tag (with shortcut)
```
<script type="text/JavaScript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script type="text/JavaScript">
jQuery(function(){ //DOM not loaded, must use ready event
    alert(jQuery('p').text());
});
</script>
```

### better choice:
placing all JavaScript includes and inline code before the closing <body> element, have to benifits:
 1- pages load faster
 2- less code 

ex3: before closing the body
```
<script type="text/JavaScript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script type="text/JavaScript">
    alert(jQuery('p').text());//go for it the DOM is loaded
</script>
```


## Selecting DOM Elements Within a Specified Context

```
alert('selected ' + jQuery('input',$('form')).length + ' inputs');
alert('selected' + jQuery('input',document.forms[0]).length + ' inputs');
alert('selected' + jQuery('input','body').length + ' inputs');
```


## Filtering a Wrapper Set of DOM Elements
```
alert(jQuery('a').filter('.external').length + ' external links');
```
or
```
alert(
    jQuery('a')
    .filter(function(index){ return $(this).hasClass('external');})
    .length + ' external links'
);
```


## Finding Descendant Elements Within the Currently Selected Wrapper Set
```
alert('paragraphs in all contain ' + jQuery('p').find('em').length + ' italic words');
alert('paragraphs in all contain ' + jQuery('em',$('p')).length + ' italic words');
alert('paragraphs in all contain ' + jQuery('p em').length + ' italic words');
```


## Returning to the Prior Selection Before a Destructive Change
```
alert(jQuery('p').filter('.middle').end().length);
```


## Traversing the DOM Based on Your Current Context to Acquire a New Set of DOM Elements
```
jQuery('li:eq(1)'); //selects the second element
jQuery('li:eq(1)').next() //selects the third <li>
jQuery('li:eq(1)').prev() //selects the first <li>
jQuery('li:eq(1)').parent() //selects the <ul>
jQuery('li:eq(1)').parent().children() //selects all <li>s
jQuery('li:eq(1)').nextAll() //selects all the <li>s after the second <li>
jQuery('li:eq(1)').prevAll() //selects all the <li>s before the second <li>
```


## Creating, Operating on, and Inserting DOM Elements
appendTo, html, replaceWith, text, ...
```
jQuery('<p><a>jQuery</a></p>').find('a').attr('href','http://www.jquery.com').end().appendTo('body');
```


## Replacing DOM Elements
```
jQuery('li.remove').replaceWith('<li>removed</li>');
```


## Removing DOM Elements
```
jQuery('a').remove();
```


## Cloning DOM Elements
```
jQuery('ul').clone().appendTo('body');
```


##  Getting, Setting, and Removing DOM Element Attributes
```
jQuery('a').attr('href','http://www.jquery.com').attr('href')
jQuery('a').attr({'href':'http://www.jquery.com','title':'jquery.com'}).attr('href')
jQuery('a')removeAttr('title')
```

## Getting and Setting HTML Content
```
jQuery('p').html('<strong>Hello World</strong>, I am a <em>&lt;p&gt;</em> element.'); 
alert(jQuery('p').html());
```


## Getting and Setting Text Content
```
jQuery('p').text('Hello World, I am a <p> element.');
alert(jQuery('p').text());
```


##  Using the $ Alias Without Creating Global Conflicts
```
(function($){ //function to create private scope with $ parameter
    //private scope and using $ without worry of conflict
})(jQuery); //invoke nameless function and pass it the jQuery object
```

