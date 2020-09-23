#include <SDL2/SDL.h>
#include <stdio.h>

const int S_WIDTH = 640;
const int S_HEIGHT = 480;
const int S_X = SDL_WINDOWPOS_UNDEFINED;
const int S_Y = SDL_WINDOWPOS_UNDEFINED;


// don't take any shortcuts on main. SDL will freak...
int main(int argc, char* args[]){
  // create pointers for window and surface

  SDL_Window* window = NULL;
  SDL_Surface* surface = NULL;

  if (SDL_Init( SDL_INIT_VIDEO) < 0){
    printf("SDL initialization error: %s", SDL_GetError());
  } else {
    window = SDL_CreateWindow("Practice", S_X, S_Y, S_WIDTH, S_HEIGHT, SDL_WINDOW_SHOWN);
    if (window == NULL){
      printf("Window creation error: %s", SDL_GetError());
    } else {
      surface = SDL_GetWindowSurface(window);
      SDL_FillRect( surface, NULL, SDL_MapRGB(surface->format, 0x00, 0x00, 0xFF));

      SDL_UpdateWindowSurface(window);
      SDL_Delay(1000);


    } // end 'window creation' if
  } // end 'SDL initialization' if 
  return(0);
} // end main
