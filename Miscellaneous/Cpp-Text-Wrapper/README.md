# Text Wrapper
Library to wrap text. Available options are: _tprintf(char * str, int width, char delimiter)_ and
_cprintf(char * str, int width)_.

---

## tprintf(char * str, int width, char delimiter)
Wraps text within the given width on word delineated by the given delimiter

If the delimiter field is set to 'NULL', then it is assumed to be the [SPACE] character.

If the delimiter field is not a whitespace character, then it is assumed to be the [SPACE] character.

___Usage Example:___
<pre>
tprintf("This is a string of characters to be wrapped within 80, and split on the [SPACE] character. \  
		This is some more text, to fill up some more space! \  
		Look at this! Even more text! Can you believe this?!?!?! \  
		Thisisareallylongstringtoshowthatstringsthatarelongerthanthewidthwithnodelimetersarewrapped
		onthecharactersafterfirstbeingputontoanewline",  
		80,  
		NULL);  
</pre>
___Output:___  
<pre>
This is a string of characters to be wrapped within 80, and split on the [SPACE]  
character. This is some more text, to fill up some more space! Look at this!
Even more text! Can you believe this?!?!?!
Thisisareallylongstringtoshowthatstringsthatarelongerthanthewidthwithnodelimeter
sarewrappedonthecharactersafterfirstbeingputontoanewline
</pre>

---

## cprintf(char * str, int width)
Wraps text on characters at the given width.

---

## TODO
+ tprintf
+ cprintf
+ split
+ strlen
