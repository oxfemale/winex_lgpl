name msdmo
type win32

import ole32.dll
import user32.dll
import advapi32.dll
import kernel32.dll
import ntdll.dll


@ stdcall DMOEnum(ptr long long ptr long ptr ptr)
@ stdcall DMOGetName(ptr wstr)
@ stdcall DMOGetTypes(ptr long ptr ptr long ptr ptr)
@ stub    DMOGuidToStrA
@ stub    DMOGuidToStrW
@ stdcall DMORegister(wstr ptr ptr long long ptr long ptr)
@ stub    DMOStrToGuidA
@ stub    DMOStrToGuidW
@ stdcall DMOUnregister(ptr ptr)
@ stdcall MoCopyMediaType(ptr ptr)
@ stdcall MoCreateMediaType(ptr long)
@ stdcall MoDeleteMediaType(ptr)
@ stdcall MoDuplicateMediaType(ptr ptr)
@ stdcall MoFreeMediaType(ptr)
@ stdcall MoInitMediaType(ptr long)
