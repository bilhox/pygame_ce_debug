# buildconfig/stubs/gen_stubs.py
# A script to auto-generate locals.pyi, constants.pyi and __init__.pyi typestubs
# IMPORTANT NOTE: Do not edit this file by hand!


from typing import Tuple, NoReturn

def Overlay(format: int, size: Tuple[int, int]) -> NoReturn: ...

from pygame import (
    display as display,
    draw as draw,
    event as event,
    font as font,
    image as image,
    key as key,
    mixer as mixer,
    mouse as mouse,
    time as time,
    cursors as cursors,
    joystick as joystick,
    math as math,
    mask as mask,
    pixelcopy as pixelcopy,
    sndarray as sndarray,
    sprite as sprite,
    surfarray as surfarray,
    transform as transform,
    scrap as scrap,
    threads as threads,
    version as version,
    base as base,
    bufferproxy as bufferproxy,
    color as color,
    colordict as colordict,
    mixer_music as mixer_music,
    pixelarray as pixelarray,
    rect as rect,
    rwobject as rwobject,
    surface as surface,
    surflock as surflock,
    sysfont as sysfont,
    _debug as _debug,
)

from .rect import Rect as Rect
from .surface import Surface as Surface, SurfaceType as SurfaceType
from .color import Color as Color
from .pixelarray import PixelArray as PixelArray
from .math import Vector2 as Vector2, Vector3 as Vector3
from .cursors import Cursor as Cursor
from .bufferproxy import BufferProxy as BufferProxy
from .mask import Mask as Mask
from ._debug import print_debug_info as print_debug_info
from .event import Event as Event
from .font import Font as Font
from .mixer import Channel as Channel
from .time import Clock as Clock
from .joystick import Joystick as Joystick
from .base import (
    BufferError as BufferError,
    HAVE_NEWBUF as HAVE_NEWBUF,
    error as error,
    get_array_interface as get_array_interface,
    get_error as get_error,
    get_init as get_init,
    get_sdl_byteorder as get_sdl_byteorder,
    get_sdl_version as get_sdl_version,
    init as init,
    quit as quit,
    register_quit as register_quit,
    set_error as set_error,
)

from .rwobject import (
    encode_file_path as encode_file_path,
    encode_string as encode_string,
)

from .version import SDL as SDL, rev as rev, ver as ver, vernum as vernum
from .constants import (
    ACTIVEEVENT as ACTIVEEVENT,
    ANYFORMAT as ANYFORMAT,
    APPACTIVE as APPACTIVE,
    APPINPUTFOCUS as APPINPUTFOCUS,
    APPMOUSEFOCUS as APPMOUSEFOCUS,
    APP_DIDENTERBACKGROUND as APP_DIDENTERBACKGROUND,
    APP_DIDENTERFOREGROUND as APP_DIDENTERFOREGROUND,
    APP_LOWMEMORY as APP_LOWMEMORY,
    APP_TERMINATING as APP_TERMINATING,
    APP_WILLENTERBACKGROUND as APP_WILLENTERBACKGROUND,
    APP_WILLENTERFOREGROUND as APP_WILLENTERFOREGROUND,
    ASYNCBLIT as ASYNCBLIT,
    AUDIODEVICEADDED as AUDIODEVICEADDED,
    AUDIODEVICEREMOVED as AUDIODEVICEREMOVED,
    AUDIO_ALLOW_ANY_CHANGE as AUDIO_ALLOW_ANY_CHANGE,
    AUDIO_ALLOW_CHANNELS_CHANGE as AUDIO_ALLOW_CHANNELS_CHANGE,
    AUDIO_ALLOW_FORMAT_CHANGE as AUDIO_ALLOW_FORMAT_CHANGE,
    AUDIO_ALLOW_FREQUENCY_CHANGE as AUDIO_ALLOW_FREQUENCY_CHANGE,
    AUDIO_S16 as AUDIO_S16,
    AUDIO_S16LSB as AUDIO_S16LSB,
    AUDIO_S16MSB as AUDIO_S16MSB,
    AUDIO_S16SYS as AUDIO_S16SYS,
    AUDIO_S8 as AUDIO_S8,
    AUDIO_U16 as AUDIO_U16,
    AUDIO_U16LSB as AUDIO_U16LSB,
    AUDIO_U16MSB as AUDIO_U16MSB,
    AUDIO_U16SYS as AUDIO_U16SYS,
    AUDIO_U8 as AUDIO_U8,
    BIG_ENDIAN as BIG_ENDIAN,
    BLENDMODE_ADD as BLENDMODE_ADD,
    BLENDMODE_BLEND as BLENDMODE_BLEND,
    BLENDMODE_MOD as BLENDMODE_MOD,
    BLENDMODE_NONE as BLENDMODE_NONE,
    BLEND_ADD as BLEND_ADD,
    BLEND_ALPHA_SDL2 as BLEND_ALPHA_SDL2,
    BLEND_MAX as BLEND_MAX,
    BLEND_MIN as BLEND_MIN,
    BLEND_MULT as BLEND_MULT,
    BLEND_PREMULTIPLIED as BLEND_PREMULTIPLIED,
    BLEND_RGBA_ADD as BLEND_RGBA_ADD,
    BLEND_RGBA_MAX as BLEND_RGBA_MAX,
    BLEND_RGBA_MIN as BLEND_RGBA_MIN,
    BLEND_RGBA_MULT as BLEND_RGBA_MULT,
    BLEND_RGBA_SUB as BLEND_RGBA_SUB,
    BLEND_RGB_ADD as BLEND_RGB_ADD,
    BLEND_RGB_MAX as BLEND_RGB_MAX,
    BLEND_RGB_MIN as BLEND_RGB_MIN,
    BLEND_RGB_MULT as BLEND_RGB_MULT,
    BLEND_RGB_SUB as BLEND_RGB_SUB,
    BLEND_SUB as BLEND_SUB,
    BUTTON_LEFT as BUTTON_LEFT,
    BUTTON_MIDDLE as BUTTON_MIDDLE,
    BUTTON_RIGHT as BUTTON_RIGHT,
    BUTTON_WHEELDOWN as BUTTON_WHEELDOWN,
    BUTTON_WHEELUP as BUTTON_WHEELUP,
    BUTTON_X1 as BUTTON_X1,
    BUTTON_X2 as BUTTON_X2,
    CLIPBOARDUPDATE as CLIPBOARDUPDATE,
    CONTROLLERAXISMOTION as CONTROLLERAXISMOTION,
    CONTROLLERBUTTONDOWN as CONTROLLERBUTTONDOWN,
    CONTROLLERBUTTONUP as CONTROLLERBUTTONUP,
    CONTROLLERDEVICEADDED as CONTROLLERDEVICEADDED,
    CONTROLLERDEVICEREMAPPED as CONTROLLERDEVICEREMAPPED,
    CONTROLLERDEVICEREMOVED as CONTROLLERDEVICEREMOVED,
    CONTROLLERSENSORUPDATE as CONTROLLERSENSORUPDATE,
    CONTROLLERTOUCHPADDOWN as CONTROLLERTOUCHPADDOWN,
    CONTROLLERTOUCHPADMOTION as CONTROLLERTOUCHPADMOTION,
    CONTROLLERTOUCHPADUP as CONTROLLERTOUCHPADUP,
    CONTROLLER_AXIS_INVALID as CONTROLLER_AXIS_INVALID,
    CONTROLLER_AXIS_LEFTX as CONTROLLER_AXIS_LEFTX,
    CONTROLLER_AXIS_LEFTY as CONTROLLER_AXIS_LEFTY,
    CONTROLLER_AXIS_MAX as CONTROLLER_AXIS_MAX,
    CONTROLLER_AXIS_RIGHTX as CONTROLLER_AXIS_RIGHTX,
    CONTROLLER_AXIS_RIGHTY as CONTROLLER_AXIS_RIGHTY,
    CONTROLLER_AXIS_TRIGGERLEFT as CONTROLLER_AXIS_TRIGGERLEFT,
    CONTROLLER_AXIS_TRIGGERRIGHT as CONTROLLER_AXIS_TRIGGERRIGHT,
    CONTROLLER_BUTTON_A as CONTROLLER_BUTTON_A,
    CONTROLLER_BUTTON_B as CONTROLLER_BUTTON_B,
    CONTROLLER_BUTTON_BACK as CONTROLLER_BUTTON_BACK,
    CONTROLLER_BUTTON_DPAD_DOWN as CONTROLLER_BUTTON_DPAD_DOWN,
    CONTROLLER_BUTTON_DPAD_LEFT as CONTROLLER_BUTTON_DPAD_LEFT,
    CONTROLLER_BUTTON_DPAD_RIGHT as CONTROLLER_BUTTON_DPAD_RIGHT,
    CONTROLLER_BUTTON_DPAD_UP as CONTROLLER_BUTTON_DPAD_UP,
    CONTROLLER_BUTTON_GUIDE as CONTROLLER_BUTTON_GUIDE,
    CONTROLLER_BUTTON_INVALID as CONTROLLER_BUTTON_INVALID,
    CONTROLLER_BUTTON_LEFTSHOULDER as CONTROLLER_BUTTON_LEFTSHOULDER,
    CONTROLLER_BUTTON_LEFTSTICK as CONTROLLER_BUTTON_LEFTSTICK,
    CONTROLLER_BUTTON_MAX as CONTROLLER_BUTTON_MAX,
    CONTROLLER_BUTTON_RIGHTSHOULDER as CONTROLLER_BUTTON_RIGHTSHOULDER,
    CONTROLLER_BUTTON_RIGHTSTICK as CONTROLLER_BUTTON_RIGHTSTICK,
    CONTROLLER_BUTTON_START as CONTROLLER_BUTTON_START,
    CONTROLLER_BUTTON_X as CONTROLLER_BUTTON_X,
    CONTROLLER_BUTTON_Y as CONTROLLER_BUTTON_Y,
    DOUBLEBUF as DOUBLEBUF,
    DROPBEGIN as DROPBEGIN,
    DROPCOMPLETE as DROPCOMPLETE,
    DROPFILE as DROPFILE,
    DROPTEXT as DROPTEXT,
    FINGERDOWN as FINGERDOWN,
    FINGERMOTION as FINGERMOTION,
    FINGERUP as FINGERUP,
    FONT_CENTER as FONT_CENTER,
    FONT_LEFT as FONT_LEFT,
    FONT_RIGHT as FONT_RIGHT,
    FULLSCREEN as FULLSCREEN,
    GL_ACCELERATED_VISUAL as GL_ACCELERATED_VISUAL,
    GL_ACCUM_ALPHA_SIZE as GL_ACCUM_ALPHA_SIZE,
    GL_ACCUM_BLUE_SIZE as GL_ACCUM_BLUE_SIZE,
    GL_ACCUM_GREEN_SIZE as GL_ACCUM_GREEN_SIZE,
    GL_ACCUM_RED_SIZE as GL_ACCUM_RED_SIZE,
    GL_ALPHA_SIZE as GL_ALPHA_SIZE,
    GL_BLUE_SIZE as GL_BLUE_SIZE,
    GL_BUFFER_SIZE as GL_BUFFER_SIZE,
    GL_CONTEXT_DEBUG_FLAG as GL_CONTEXT_DEBUG_FLAG,
    GL_CONTEXT_FLAGS as GL_CONTEXT_FLAGS,
    GL_CONTEXT_FORWARD_COMPATIBLE_FLAG as GL_CONTEXT_FORWARD_COMPATIBLE_FLAG,
    GL_CONTEXT_MAJOR_VERSION as GL_CONTEXT_MAJOR_VERSION,
    GL_CONTEXT_MINOR_VERSION as GL_CONTEXT_MINOR_VERSION,
    GL_CONTEXT_PROFILE_COMPATIBILITY as GL_CONTEXT_PROFILE_COMPATIBILITY,
    GL_CONTEXT_PROFILE_CORE as GL_CONTEXT_PROFILE_CORE,
    GL_CONTEXT_PROFILE_ES as GL_CONTEXT_PROFILE_ES,
    GL_CONTEXT_PROFILE_MASK as GL_CONTEXT_PROFILE_MASK,
    GL_CONTEXT_RELEASE_BEHAVIOR as GL_CONTEXT_RELEASE_BEHAVIOR,
    GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH as GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH,
    GL_CONTEXT_RELEASE_BEHAVIOR_NONE as GL_CONTEXT_RELEASE_BEHAVIOR_NONE,
    GL_CONTEXT_RESET_ISOLATION_FLAG as GL_CONTEXT_RESET_ISOLATION_FLAG,
    GL_CONTEXT_ROBUST_ACCESS_FLAG as GL_CONTEXT_ROBUST_ACCESS_FLAG,
    GL_DEPTH_SIZE as GL_DEPTH_SIZE,
    GL_DOUBLEBUFFER as GL_DOUBLEBUFFER,
    GL_FRAMEBUFFER_SRGB_CAPABLE as GL_FRAMEBUFFER_SRGB_CAPABLE,
    GL_GREEN_SIZE as GL_GREEN_SIZE,
    GL_MULTISAMPLEBUFFERS as GL_MULTISAMPLEBUFFERS,
    GL_MULTISAMPLESAMPLES as GL_MULTISAMPLESAMPLES,
    GL_RED_SIZE as GL_RED_SIZE,
    GL_SHARE_WITH_CURRENT_CONTEXT as GL_SHARE_WITH_CURRENT_CONTEXT,
    GL_STENCIL_SIZE as GL_STENCIL_SIZE,
    GL_STEREO as GL_STEREO,
    GL_SWAP_CONTROL as GL_SWAP_CONTROL,
    HAT_CENTERED as HAT_CENTERED,
    HAT_DOWN as HAT_DOWN,
    HAT_LEFT as HAT_LEFT,
    HAT_LEFTDOWN as HAT_LEFTDOWN,
    HAT_LEFTUP as HAT_LEFTUP,
    HAT_RIGHT as HAT_RIGHT,
    HAT_RIGHTDOWN as HAT_RIGHTDOWN,
    HAT_RIGHTUP as HAT_RIGHTUP,
    HAT_UP as HAT_UP,
    HIDDEN as HIDDEN,
    HWACCEL as HWACCEL,
    HWPALETTE as HWPALETTE,
    HWSURFACE as HWSURFACE,
    IS_CE as IS_CE,
    JOYAXISMOTION as JOYAXISMOTION,
    JOYBALLMOTION as JOYBALLMOTION,
    JOYBUTTONDOWN as JOYBUTTONDOWN,
    JOYBUTTONUP as JOYBUTTONUP,
    JOYDEVICEADDED as JOYDEVICEADDED,
    JOYDEVICEREMOVED as JOYDEVICEREMOVED,
    JOYHATMOTION as JOYHATMOTION,
    KEYDOWN as KEYDOWN,
    KEYMAPCHANGED as KEYMAPCHANGED,
    KEYUP as KEYUP,
    KMOD_ALT as KMOD_ALT,
    KMOD_CAPS as KMOD_CAPS,
    KMOD_CTRL as KMOD_CTRL,
    KMOD_GUI as KMOD_GUI,
    KMOD_LALT as KMOD_LALT,
    KMOD_LCTRL as KMOD_LCTRL,
    KMOD_LGUI as KMOD_LGUI,
    KMOD_LMETA as KMOD_LMETA,
    KMOD_LSHIFT as KMOD_LSHIFT,
    KMOD_META as KMOD_META,
    KMOD_MODE as KMOD_MODE,
    KMOD_NONE as KMOD_NONE,
    KMOD_NUM as KMOD_NUM,
    KMOD_RALT as KMOD_RALT,
    KMOD_RCTRL as KMOD_RCTRL,
    KMOD_RGUI as KMOD_RGUI,
    KMOD_RMETA as KMOD_RMETA,
    KMOD_RSHIFT as KMOD_RSHIFT,
    KMOD_SHIFT as KMOD_SHIFT,
    KSCAN_0 as KSCAN_0,
    KSCAN_1 as KSCAN_1,
    KSCAN_2 as KSCAN_2,
    KSCAN_3 as KSCAN_3,
    KSCAN_4 as KSCAN_4,
    KSCAN_5 as KSCAN_5,
    KSCAN_6 as KSCAN_6,
    KSCAN_7 as KSCAN_7,
    KSCAN_8 as KSCAN_8,
    KSCAN_9 as KSCAN_9,
    KSCAN_A as KSCAN_A,
    KSCAN_AC_BACK as KSCAN_AC_BACK,
    KSCAN_APOSTROPHE as KSCAN_APOSTROPHE,
    KSCAN_B as KSCAN_B,
    KSCAN_BACKSLASH as KSCAN_BACKSLASH,
    KSCAN_BACKSPACE as KSCAN_BACKSPACE,
    KSCAN_BREAK as KSCAN_BREAK,
    KSCAN_C as KSCAN_C,
    KSCAN_CAPSLOCK as KSCAN_CAPSLOCK,
    KSCAN_CLEAR as KSCAN_CLEAR,
    KSCAN_COMMA as KSCAN_COMMA,
    KSCAN_CURRENCYSUBUNIT as KSCAN_CURRENCYSUBUNIT,
    KSCAN_CURRENCYUNIT as KSCAN_CURRENCYUNIT,
    KSCAN_D as KSCAN_D,
    KSCAN_DELETE as KSCAN_DELETE,
    KSCAN_DOWN as KSCAN_DOWN,
    KSCAN_E as KSCAN_E,
    KSCAN_END as KSCAN_END,
    KSCAN_EQUALS as KSCAN_EQUALS,
    KSCAN_ESCAPE as KSCAN_ESCAPE,
    KSCAN_EURO as KSCAN_EURO,
    KSCAN_F as KSCAN_F,
    KSCAN_F1 as KSCAN_F1,
    KSCAN_F10 as KSCAN_F10,
    KSCAN_F11 as KSCAN_F11,
    KSCAN_F12 as KSCAN_F12,
    KSCAN_F13 as KSCAN_F13,
    KSCAN_F14 as KSCAN_F14,
    KSCAN_F15 as KSCAN_F15,
    KSCAN_F2 as KSCAN_F2,
    KSCAN_F3 as KSCAN_F3,
    KSCAN_F4 as KSCAN_F4,
    KSCAN_F5 as KSCAN_F5,
    KSCAN_F6 as KSCAN_F6,
    KSCAN_F7 as KSCAN_F7,
    KSCAN_F8 as KSCAN_F8,
    KSCAN_F9 as KSCAN_F9,
    KSCAN_G as KSCAN_G,
    KSCAN_GRAVE as KSCAN_GRAVE,
    KSCAN_H as KSCAN_H,
    KSCAN_HELP as KSCAN_HELP,
    KSCAN_HOME as KSCAN_HOME,
    KSCAN_I as KSCAN_I,
    KSCAN_INSERT as KSCAN_INSERT,
    KSCAN_INTERNATIONAL1 as KSCAN_INTERNATIONAL1,
    KSCAN_INTERNATIONAL2 as KSCAN_INTERNATIONAL2,
    KSCAN_INTERNATIONAL3 as KSCAN_INTERNATIONAL3,
    KSCAN_INTERNATIONAL4 as KSCAN_INTERNATIONAL4,
    KSCAN_INTERNATIONAL5 as KSCAN_INTERNATIONAL5,
    KSCAN_INTERNATIONAL6 as KSCAN_INTERNATIONAL6,
    KSCAN_INTERNATIONAL7 as KSCAN_INTERNATIONAL7,
    KSCAN_INTERNATIONAL8 as KSCAN_INTERNATIONAL8,
    KSCAN_INTERNATIONAL9 as KSCAN_INTERNATIONAL9,
    KSCAN_J as KSCAN_J,
    KSCAN_K as KSCAN_K,
    KSCAN_KP0 as KSCAN_KP0,
    KSCAN_KP1 as KSCAN_KP1,
    KSCAN_KP2 as KSCAN_KP2,
    KSCAN_KP3 as KSCAN_KP3,
    KSCAN_KP4 as KSCAN_KP4,
    KSCAN_KP5 as KSCAN_KP5,
    KSCAN_KP6 as KSCAN_KP6,
    KSCAN_KP7 as KSCAN_KP7,
    KSCAN_KP8 as KSCAN_KP8,
    KSCAN_KP9 as KSCAN_KP9,
    KSCAN_KP_0 as KSCAN_KP_0,
    KSCAN_KP_1 as KSCAN_KP_1,
    KSCAN_KP_2 as KSCAN_KP_2,
    KSCAN_KP_3 as KSCAN_KP_3,
    KSCAN_KP_4 as KSCAN_KP_4,
    KSCAN_KP_5 as KSCAN_KP_5,
    KSCAN_KP_6 as KSCAN_KP_6,
    KSCAN_KP_7 as KSCAN_KP_7,
    KSCAN_KP_8 as KSCAN_KP_8,
    KSCAN_KP_9 as KSCAN_KP_9,
    KSCAN_KP_DIVIDE as KSCAN_KP_DIVIDE,
    KSCAN_KP_ENTER as KSCAN_KP_ENTER,
    KSCAN_KP_EQUALS as KSCAN_KP_EQUALS,
    KSCAN_KP_MINUS as KSCAN_KP_MINUS,
    KSCAN_KP_MULTIPLY as KSCAN_KP_MULTIPLY,
    KSCAN_KP_PERIOD as KSCAN_KP_PERIOD,
    KSCAN_KP_PLUS as KSCAN_KP_PLUS,
    KSCAN_L as KSCAN_L,
    KSCAN_LALT as KSCAN_LALT,
    KSCAN_LANG1 as KSCAN_LANG1,
    KSCAN_LANG2 as KSCAN_LANG2,
    KSCAN_LANG3 as KSCAN_LANG3,
    KSCAN_LANG4 as KSCAN_LANG4,
    KSCAN_LANG5 as KSCAN_LANG5,
    KSCAN_LANG6 as KSCAN_LANG6,
    KSCAN_LANG7 as KSCAN_LANG7,
    KSCAN_LANG8 as KSCAN_LANG8,
    KSCAN_LANG9 as KSCAN_LANG9,
    KSCAN_LCTRL as KSCAN_LCTRL,
    KSCAN_LEFT as KSCAN_LEFT,
    KSCAN_LEFTBRACKET as KSCAN_LEFTBRACKET,
    KSCAN_LGUI as KSCAN_LGUI,
    KSCAN_LMETA as KSCAN_LMETA,
    KSCAN_LSHIFT as KSCAN_LSHIFT,
    KSCAN_LSUPER as KSCAN_LSUPER,
    KSCAN_M as KSCAN_M,
    KSCAN_MENU as KSCAN_MENU,
    KSCAN_MINUS as KSCAN_MINUS,
    KSCAN_MODE as KSCAN_MODE,
    KSCAN_N as KSCAN_N,
    KSCAN_NONUSBACKSLASH as KSCAN_NONUSBACKSLASH,
    KSCAN_NONUSHASH as KSCAN_NONUSHASH,
    KSCAN_NUMLOCK as KSCAN_NUMLOCK,
    KSCAN_NUMLOCKCLEAR as KSCAN_NUMLOCKCLEAR,
    KSCAN_O as KSCAN_O,
    KSCAN_P as KSCAN_P,
    KSCAN_PAGEDOWN as KSCAN_PAGEDOWN,
    KSCAN_PAGEUP as KSCAN_PAGEUP,
    KSCAN_PAUSE as KSCAN_PAUSE,
    KSCAN_PERIOD as KSCAN_PERIOD,
    KSCAN_POWER as KSCAN_POWER,
    KSCAN_PRINT as KSCAN_PRINT,
    KSCAN_PRINTSCREEN as KSCAN_PRINTSCREEN,
    KSCAN_Q as KSCAN_Q,
    KSCAN_R as KSCAN_R,
    KSCAN_RALT as KSCAN_RALT,
    KSCAN_RCTRL as KSCAN_RCTRL,
    KSCAN_RETURN as KSCAN_RETURN,
    KSCAN_RGUI as KSCAN_RGUI,
    KSCAN_RIGHT as KSCAN_RIGHT,
    KSCAN_RIGHTBRACKET as KSCAN_RIGHTBRACKET,
    KSCAN_RMETA as KSCAN_RMETA,
    KSCAN_RSHIFT as KSCAN_RSHIFT,
    KSCAN_RSUPER as KSCAN_RSUPER,
    KSCAN_S as KSCAN_S,
    KSCAN_SCROLLLOCK as KSCAN_SCROLLLOCK,
    KSCAN_SCROLLOCK as KSCAN_SCROLLOCK,
    KSCAN_SEMICOLON as KSCAN_SEMICOLON,
    KSCAN_SLASH as KSCAN_SLASH,
    KSCAN_SPACE as KSCAN_SPACE,
    KSCAN_SYSREQ as KSCAN_SYSREQ,
    KSCAN_T as KSCAN_T,
    KSCAN_TAB as KSCAN_TAB,
    KSCAN_U as KSCAN_U,
    KSCAN_UNKNOWN as KSCAN_UNKNOWN,
    KSCAN_UP as KSCAN_UP,
    KSCAN_V as KSCAN_V,
    KSCAN_W as KSCAN_W,
    KSCAN_X as KSCAN_X,
    KSCAN_Y as KSCAN_Y,
    KSCAN_Z as KSCAN_Z,
    K_0 as K_0,
    K_1 as K_1,
    K_2 as K_2,
    K_3 as K_3,
    K_4 as K_4,
    K_5 as K_5,
    K_6 as K_6,
    K_7 as K_7,
    K_8 as K_8,
    K_9 as K_9,
    K_AC_BACK as K_AC_BACK,
    K_AMPERSAND as K_AMPERSAND,
    K_ASTERISK as K_ASTERISK,
    K_AT as K_AT,
    K_BACKQUOTE as K_BACKQUOTE,
    K_BACKSLASH as K_BACKSLASH,
    K_BACKSPACE as K_BACKSPACE,
    K_BREAK as K_BREAK,
    K_CAPSLOCK as K_CAPSLOCK,
    K_CARET as K_CARET,
    K_CLEAR as K_CLEAR,
    K_COLON as K_COLON,
    K_COMMA as K_COMMA,
    K_CURRENCYSUBUNIT as K_CURRENCYSUBUNIT,
    K_CURRENCYUNIT as K_CURRENCYUNIT,
    K_DELETE as K_DELETE,
    K_DOLLAR as K_DOLLAR,
    K_DOWN as K_DOWN,
    K_END as K_END,
    K_EQUALS as K_EQUALS,
    K_ESCAPE as K_ESCAPE,
    K_EURO as K_EURO,
    K_EXCLAIM as K_EXCLAIM,
    K_F1 as K_F1,
    K_F10 as K_F10,
    K_F11 as K_F11,
    K_F12 as K_F12,
    K_F13 as K_F13,
    K_F14 as K_F14,
    K_F15 as K_F15,
    K_F2 as K_F2,
    K_F3 as K_F3,
    K_F4 as K_F4,
    K_F5 as K_F5,
    K_F6 as K_F6,
    K_F7 as K_F7,
    K_F8 as K_F8,
    K_F9 as K_F9,
    K_GREATER as K_GREATER,
    K_HASH as K_HASH,
    K_HELP as K_HELP,
    K_HOME as K_HOME,
    K_INSERT as K_INSERT,
    K_KP0 as K_KP0,
    K_KP1 as K_KP1,
    K_KP2 as K_KP2,
    K_KP3 as K_KP3,
    K_KP4 as K_KP4,
    K_KP5 as K_KP5,
    K_KP6 as K_KP6,
    K_KP7 as K_KP7,
    K_KP8 as K_KP8,
    K_KP9 as K_KP9,
    K_KP_0 as K_KP_0,
    K_KP_1 as K_KP_1,
    K_KP_2 as K_KP_2,
    K_KP_3 as K_KP_3,
    K_KP_4 as K_KP_4,
    K_KP_5 as K_KP_5,
    K_KP_6 as K_KP_6,
    K_KP_7 as K_KP_7,
    K_KP_8 as K_KP_8,
    K_KP_9 as K_KP_9,
    K_KP_DIVIDE as K_KP_DIVIDE,
    K_KP_ENTER as K_KP_ENTER,
    K_KP_EQUALS as K_KP_EQUALS,
    K_KP_MINUS as K_KP_MINUS,
    K_KP_MULTIPLY as K_KP_MULTIPLY,
    K_KP_PERIOD as K_KP_PERIOD,
    K_KP_PLUS as K_KP_PLUS,
    K_LALT as K_LALT,
    K_LCTRL as K_LCTRL,
    K_LEFT as K_LEFT,
    K_LEFTBRACKET as K_LEFTBRACKET,
    K_LEFTPAREN as K_LEFTPAREN,
    K_LESS as K_LESS,
    K_LGUI as K_LGUI,
    K_LMETA as K_LMETA,
    K_LSHIFT as K_LSHIFT,
    K_LSUPER as K_LSUPER,
    K_MENU as K_MENU,
    K_MINUS as K_MINUS,
    K_MODE as K_MODE,
    K_NUMLOCK as K_NUMLOCK,
    K_NUMLOCKCLEAR as K_NUMLOCKCLEAR,
    K_PAGEDOWN as K_PAGEDOWN,
    K_PAGEUP as K_PAGEUP,
    K_PAUSE as K_PAUSE,
    K_PERCENT as K_PERCENT,
    K_PERIOD as K_PERIOD,
    K_PLUS as K_PLUS,
    K_POWER as K_POWER,
    K_PRINT as K_PRINT,
    K_PRINTSCREEN as K_PRINTSCREEN,
    K_QUESTION as K_QUESTION,
    K_QUOTE as K_QUOTE,
    K_QUOTEDBL as K_QUOTEDBL,
    K_RALT as K_RALT,
    K_RCTRL as K_RCTRL,
    K_RETURN as K_RETURN,
    K_RGUI as K_RGUI,
    K_RIGHT as K_RIGHT,
    K_RIGHTBRACKET as K_RIGHTBRACKET,
    K_RIGHTPAREN as K_RIGHTPAREN,
    K_RMETA as K_RMETA,
    K_RSHIFT as K_RSHIFT,
    K_RSUPER as K_RSUPER,
    K_SCROLLLOCK as K_SCROLLLOCK,
    K_SCROLLOCK as K_SCROLLOCK,
    K_SEMICOLON as K_SEMICOLON,
    K_SLASH as K_SLASH,
    K_SPACE as K_SPACE,
    K_SYSREQ as K_SYSREQ,
    K_TAB as K_TAB,
    K_UNDERSCORE as K_UNDERSCORE,
    K_UNKNOWN as K_UNKNOWN,
    K_UP as K_UP,
    K_a as K_a,
    K_b as K_b,
    K_c as K_c,
    K_d as K_d,
    K_e as K_e,
    K_f as K_f,
    K_g as K_g,
    K_h as K_h,
    K_i as K_i,
    K_j as K_j,
    K_k as K_k,
    K_l as K_l,
    K_m as K_m,
    K_n as K_n,
    K_o as K_o,
    K_p as K_p,
    K_q as K_q,
    K_r as K_r,
    K_s as K_s,
    K_t as K_t,
    K_u as K_u,
    K_v as K_v,
    K_w as K_w,
    K_x as K_x,
    K_y as K_y,
    K_z as K_z,
    LIL_ENDIAN as LIL_ENDIAN,
    LOCALECHANGED as LOCALECHANGED,
    MIDIIN as MIDIIN,
    MIDIOUT as MIDIOUT,
    MOUSEBUTTONDOWN as MOUSEBUTTONDOWN,
    MOUSEBUTTONUP as MOUSEBUTTONUP,
    MOUSEMOTION as MOUSEMOTION,
    MOUSEWHEEL as MOUSEWHEEL,
    MULTIGESTURE as MULTIGESTURE,
    NOEVENT as NOEVENT,
    NOFRAME as NOFRAME,
    NUMEVENTS as NUMEVENTS,
    OPENGL as OPENGL,
    OPENGLBLIT as OPENGLBLIT,
    PREALLOC as PREALLOC,
    QUIT as QUIT,
    RENDER_DEVICE_RESET as RENDER_DEVICE_RESET,
    RENDER_TARGETS_RESET as RENDER_TARGETS_RESET,
    RESIZABLE as RESIZABLE,
    RLEACCEL as RLEACCEL,
    RLEACCELOK as RLEACCELOK,
    SCALED as SCALED,
    SCRAP_BMP as SCRAP_BMP,
    SCRAP_CLIPBOARD as SCRAP_CLIPBOARD,
    SCRAP_PBM as SCRAP_PBM,
    SCRAP_PPM as SCRAP_PPM,
    SCRAP_SELECTION as SCRAP_SELECTION,
    SCRAP_TEXT as SCRAP_TEXT,
    SHOWN as SHOWN,
    SRCALPHA as SRCALPHA,
    SRCCOLORKEY as SRCCOLORKEY,
    SWSURFACE as SWSURFACE,
    SYSTEM_CURSOR_ARROW as SYSTEM_CURSOR_ARROW,
    SYSTEM_CURSOR_CROSSHAIR as SYSTEM_CURSOR_CROSSHAIR,
    SYSTEM_CURSOR_HAND as SYSTEM_CURSOR_HAND,
    SYSTEM_CURSOR_IBEAM as SYSTEM_CURSOR_IBEAM,
    SYSTEM_CURSOR_NO as SYSTEM_CURSOR_NO,
    SYSTEM_CURSOR_SIZEALL as SYSTEM_CURSOR_SIZEALL,
    SYSTEM_CURSOR_SIZENESW as SYSTEM_CURSOR_SIZENESW,
    SYSTEM_CURSOR_SIZENS as SYSTEM_CURSOR_SIZENS,
    SYSTEM_CURSOR_SIZENWSE as SYSTEM_CURSOR_SIZENWSE,
    SYSTEM_CURSOR_SIZEWE as SYSTEM_CURSOR_SIZEWE,
    SYSTEM_CURSOR_WAIT as SYSTEM_CURSOR_WAIT,
    SYSTEM_CURSOR_WAITARROW as SYSTEM_CURSOR_WAITARROW,
    SYSWMEVENT as SYSWMEVENT,
    TEXTEDITING as TEXTEDITING,
    TEXTINPUT as TEXTINPUT,
    TIMER_RESOLUTION as TIMER_RESOLUTION,
    USEREVENT as USEREVENT,
    USEREVENT_DROPFILE as USEREVENT_DROPFILE,
    VIDEOEXPOSE as VIDEOEXPOSE,
    VIDEORESIZE as VIDEORESIZE,
    WINDOWCLOSE as WINDOWCLOSE,
    WINDOWDISPLAYCHANGED as WINDOWDISPLAYCHANGED,
    WINDOWENTER as WINDOWENTER,
    WINDOWEXPOSED as WINDOWEXPOSED,
    WINDOWFOCUSGAINED as WINDOWFOCUSGAINED,
    WINDOWFOCUSLOST as WINDOWFOCUSLOST,
    WINDOWHIDDEN as WINDOWHIDDEN,
    WINDOWHITTEST as WINDOWHITTEST,
    WINDOWICCPROFCHANGED as WINDOWICCPROFCHANGED,
    WINDOWLEAVE as WINDOWLEAVE,
    WINDOWMAXIMIZED as WINDOWMAXIMIZED,
    WINDOWMINIMIZED as WINDOWMINIMIZED,
    WINDOWMOVED as WINDOWMOVED,
    WINDOWRESIZED as WINDOWRESIZED,
    WINDOWRESTORED as WINDOWRESTORED,
    WINDOWSHOWN as WINDOWSHOWN,
    WINDOWSIZECHANGED as WINDOWSIZECHANGED,
    WINDOWTAKEFOCUS as WINDOWTAKEFOCUS,
)
