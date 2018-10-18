# The Basics of CSS 

After learning more about HTML, it is time for us to put the icing on the cake by learning CSS! 

**CSS** stands for **(C)**ascading **(S)**tyle **(S)**heet. It is what makes web pages look good and presentable. It is an essential part of modern web development and a  **must-have** skill for any web designer and developer.  

**There are 3 ways you can add CSS to your HTML elements:** 

* In-line: is using the style attribute in your HTML elements. For example: `<h1 style="font-family:'Arial'"`

* Internal: is using the `<style> ` tag/element inside of the `<head>` element of your HTML page.

* External: is used as a seperate CSS file. You will create a new file within your folder. For example: index.css (This is where all of my css code will go). In order for you to link this to your HTML page, you will always have to use the `<link rel="stylesheet" href="styles.css">`inside of your `head` tag.  This style sheet can be imported into other HTML files which is great for reusability. 


## CSS Selectors  
Since CSS is a design language that is used to style HTML elements. In order to style your elements, you have to first select them. We touch on this a little bit already but let’s dive a bit deeper. 


## ElEMENTS 
To select an HTML element you simply select them by their name. By selecting their name, you are then giving them different styling attributes that specifies the content even more. 

`
h1 {
    font-family: Arial;
    color: red;
}
p {
    color: green;
}
div {
    margin: 20px;
   }
`

## CLASS 
Another way to select an HTML element is by using the **class** attribute. It allows you to assign  **different classes to multiple elements.** 
`
//index.html
<div class='container'>
    <h1> About Me </h1>
</div>
//index.css
.container {
    margin: 15px;
}
`

## ID 
Similar to the class attribute, you can also use the **id** attribute to select HTML elements as well. However, using the **id** attribute **you are only allowed to assign it to one HTML element**

`
//index.html 
<div>
    <p id='bio'> This is a paragraph </p>
</div>
//index.css
#bio{
    color: blue;
    font-size: 12px;
} 
`

CSS gives you that power to design your site however you like. This is where you can manipulate the font, color, width, height, size and can even add animation in this file. 

## CSS Resources 

[Best CSS Resources To Use](https://github.com/twilsonpierce/DisruptHarlemCode/tree/master/intro_to_css)

