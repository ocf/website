<!-- Prototype JavaScript framework, version 1.4.0_rc3; (c) 2005 Sam Stephenson <sam@conio.net> -->	

	function $() {
	var elements = new Array();
  	for (var i = 0; i < arguments.length; i++) {
    var element = arguments[i];
    if (typeof element == 'string')
      element = document.getElementById(element);
    if (arguments.length == 1)
      return element;
    elements.push(element);
  }
  return elements;
}

	function showTab(show){
	$(show).style.display='';
	$('nav_'+show).className='active';
	var args = showTab.arguments;	  
	for (var i = 1; i < args.length; i++) {		
		$(args[i]).style.display='none';
		$('nav_'+args[i]).className = $('nav_'+args[i]).className.replace('active','');
	}
	
} 