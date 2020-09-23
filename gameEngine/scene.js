// sample scene implementation in JS

function Scene(){
    //Scene that encapsulates the animation background

    //determine if it's a touchscreen device
    this.touchable = 'createTouch' in document;
    
    //dynamically create a canvas element
    this.canvas = document.createElement("canvas");
    this.canvas.style.backgroundColor = "yellow";
    document.body.appendChild(this.canvas);
    this.context = this.canvas.getContext("2d");
    
    this.clear = function(){
      this.context.clearRect(0, 0, this.width, this.height);
    }

    this.start = function(){
      //set up keyboard reader if not a touch screen.
      // removed this test as it was breaking on machines with both
      // touch and keyboard input
      //if (!this.touchable){
			this.initKeys();
			document.onkeydown = this.updateKeys;
			document.onkeyup = this.clearKeys;
      //} // end if
      this.intID = setInterval(localUpdate, 50);
      document.onmousemove = this.updateMousePos;
      document.mouseClicked = false;
      document.onmousedown = function(){
				this.mouseDown = true;
				this.mouseClicked = true;
      }
      document.onmouseup = function(){
				this.mouseDown = false;
				this.mouseClicked  = false;
      }
    } 

    this.stop = function(){
      clearInterval(this.intID);
    }

    this.updateKeys = function(e){      
      //set current key
      currentKey = e.keyCode;
      //console.log(e.keyCode);
      keysDown[e.keyCode] = true;
    } // end updateKeys
    
    this.clearKeys = function(e){
      currentKey = null;
      keysDown[e.keyCode] = false;
    } // end clearKeys
    
    this.initKeys = function(){
      //initialize keys array to all false
      for (keyNum = 0; keyNum < 256; keyNum++){
	      keysDown[keyNum] = false;
      } // end for
    } // end initKeys
    
    this.setSizePos = function(height, width, top, left){
      //convenience function.  Cals setSize and setPos
      this.setSize(height, width);
      this.setPos(top, left);
    } // end setSizePos

    this.setSize = function(width, height){
      //set the width and height of the canvas in pixels
      this.width = width;
      this.height = height;
      this.canvas.width = this.width;
      this.canvas.height = this.height;
    } // end setSize
    
    this.setPos = function(left, top){
      //set the left and top position of the canvas
      //offset from the page
      this.left = left;
      this.top = top;

      //CSS3 transform to move elements.
      //Cross-browser compatibility would be awesome, guys...
      this.canvas.style.MozTransform = "translate(" + left + "px, " + top + "px)";
      this.canvas.style.WebkitTransform = "translate(" + left + "px, " + top + "px)";
      this.canvas.style.OTransform = "translate(" + left + "px, " + top + "px)";

    } // end setPos
    
    this.setBG = function(color){
      this.canvas.style.backgroundColor = color;
    } // end this.setBG
    
    this.updateMousePos = function(e){
      this.mouseX = e.pageX;
      this.mouseY = e.pageY;
    } // end function
    
    this.hideCursor = function(){
      this.canvas.style.cursor = "none";
    }
    
    this.showCursor = function(){
      this.canvas.style.cursor = "default";
    }
    
    this.getMouseX = function(){
      //incorporate offset for canvas position
      return document.mouseX - this.left;
    }
    
    this.getMouseY = function(){
      //incorporate offset for canvas position
      return document.mouseY - this.top;
    }
    
    this.getMouseClicked = function(){
      return document.mouseClicked;
    }
    
    this.hide = function(){
      this.canvas.style.display = "none";
    }
    
    this.show = function(){
      this.canvas.style.display = "block";
    }
    
    this.setSize(800, 600);
    this.setPos(10, 10);
    this.setBG("lightgray");
    
} // end Scene class def

function localUpdate(){
    //will be called once per frame
    //calls the update function defined by
    //the user
    update();
} // end localUpdate


//keyboard constants
K_A = 65; K_B = 66; K_C = 67; K_D = 68; K_E = 69; K_F = 70; K_G = 71;
K_H = 72; K_I = 73; K_J = 74; K_K = 75; K_L = 76; K_M = 77; K_N = 78;
K_O = 79; K_P = 80; K_Q = 81; K_R = 82; K_S = 83; K_T = 84; K_U = 85;
K_V = 86; K_W = 87; K_X = 88; K_Y = 89; K_Z = 90;
K_LEFT = 37; K_RIGHT = 39; K_UP = 38;K_DOWN = 40; K_SPACE = 32;
K_ESC = 27; K_PGUP = 33; K_PGDOWN = 34; K_HOME = 36; K_END = 35;
K_0 = 48; K_1 = 49; K_2 = 50; K_3 = 51; K_4 = 52; K_5 = 53;
K_6 = 54; K_7 = 55; K_8 = 56; K_9 = 57; 

