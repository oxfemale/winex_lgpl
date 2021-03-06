/*
 * Help Viewer
 *
 * Copyright 1996 Ulrich Schmid
 */

#include "winnt.h"
#include "windef.h"
#include "winbase.h"
#include "winuser.h"
#include "wingdi.h"
#include "shellapi.h"

VOID MACRO_ExecuteMacro(LPCSTR);

INT  yyparse(VOID);
INT  yylex(VOID);
VOID yyerror(LPCSTR);

VOID MACRO_About(VOID);
VOID MACRO_AddAccelerator(LONG, LONG, LPCSTR);
VOID MACRO_ALink(LPCSTR, LONG, LPCSTR);
VOID MACRO_Annotate(VOID);
VOID MACRO_AppendItem(LPCSTR, LPCSTR, LPCSTR, LPCSTR);
VOID MACRO_Back(VOID);
VOID MACRO_BackFlush(VOID);
VOID MACRO_BookmarkDefine(VOID);
VOID MACRO_BookmarkMore(VOID);
VOID MACRO_BrowseButtons(VOID);
VOID MACRO_ChangeButtonBinding(LPCSTR, LPCSTR);
VOID MACRO_ChangeEnable(LPCSTR, LPCSTR);
VOID MACRO_ChangeItemBinding(LPCSTR, LPCSTR);
VOID MACRO_CheckItem(LPCSTR);
VOID MACRO_CloseSecondarys(VOID);
VOID MACRO_CloseWindow(LPCSTR);
VOID MACRO_Compare(LPCSTR);
VOID MACRO_Contents(VOID);
VOID MACRO_ControlPanel(LPCSTR, LPCSTR, LONG);
VOID MACRO_CopyDialog(VOID);
VOID MACRO_CopyTopic(VOID);
VOID MACRO_CreateButton(LPCSTR, LPCSTR, LPCSTR);
VOID MACRO_DeleteItem(LPCSTR);
VOID MACRO_DeleteMark(LPCSTR);
VOID MACRO_DestroyButton(LPCSTR);
VOID MACRO_DisableButton(LPCSTR);
VOID MACRO_DisableItem(LPCSTR);
VOID MACRO_EnableButton(LPCSTR);
VOID MACRO_EnableItem(LPCSTR);
VOID MACRO_EndMPrint(VOID);
VOID MACRO_ExecFile(LPCSTR, LPCSTR, LONG, LPCSTR);
VOID MACRO_ExecProgram(LPCSTR, LONG);
VOID MACRO_Exit(VOID);
VOID MACRO_ExtAbleItem(LPCSTR, LONG);
VOID MACRO_ExtInsertItem(LPCSTR, LPCSTR, LPCSTR, LPCSTR, LONG, LONG);
VOID MACRO_ExtInsertMenu(LPCSTR, LPCSTR, LPCSTR, LONG, LONG);
BOOL MACRO_FileExist(LPCSTR);
VOID MACRO_FileOpen(VOID);
VOID MACRO_Find(VOID);
VOID MACRO_Finder(VOID);
VOID MACRO_FloatingMenu(VOID);
VOID MACRO_Flush(VOID);
VOID MACRO_FocusWindow(LPCSTR);
VOID MACRO_Generate(LPCSTR, WPARAM, LPARAM);
VOID MACRO_GotoMark(LPCSTR);
VOID MACRO_HelpOn(VOID);
VOID MACRO_HelpOnTop(VOID);
VOID MACRO_History(VOID);
BOOL MACRO_InitMPrint(VOID);
VOID MACRO_InsertItem(LPCSTR, LPCSTR, LPCSTR, LPCSTR, LONG);
VOID MACRO_InsertMenu(LPCSTR, LPCSTR, LONG);
BOOL MACRO_IsBook(VOID);
BOOL MACRO_IsMark(LPCSTR);
BOOL MACRO_IsNotMark(LPCSTR);
VOID MACRO_JumpContents(LPCSTR, LPCSTR);
VOID MACRO_JumpContext(LPCSTR, LPCSTR, LONG);
VOID MACRO_JumpHash(LPCSTR, LPCSTR, LONG);
VOID MACRO_JumpHelpOn(VOID);
VOID MACRO_JumpID(LPCSTR, LPCSTR, LPCSTR);
VOID MACRO_JumpKeyword(LPCSTR, LPCSTR, LPCSTR);
VOID MACRO_KLink(LPCSTR, LONG, LPCSTR, LPCSTR);
VOID MACRO_Menu(VOID);
VOID MACRO_MPrintHash(LONG);
VOID MACRO_MPrintID(LPCSTR);
VOID MACRO_Next(VOID);
VOID MACRO_NoShow(VOID);
VOID MACRO_PopupContext(LPCSTR, LONG);
VOID MACRO_PopupHash(LPCSTR, LONG);
VOID MACRO_PopupId(LPCSTR, LPCSTR);
VOID MACRO_PositionWindow(LONG, LONG, LONG, LONG, LONG, LPCSTR);
VOID MACRO_Prev(VOID);
VOID MACRO_Print(VOID);
VOID MACRO_PrinterSetup(VOID);
VOID MACRO_RegisterRoutine(LPCSTR, LPCSTR, LPCSTR);
VOID MACRO_RemoveAccelerator(LONG, LONG);
VOID MACRO_ResetMenu(VOID);
VOID MACRO_SaveMark(LPCSTR);
VOID MACRO_Search(VOID);
VOID MACRO_SetContents(LPCSTR, LONG);
VOID MACRO_SetHelpOnFile(LPCSTR);
VOID MACRO_SetPopupColor(LONG, LONG, LONG);
VOID MACRO_ShellExecute(LPCSTR, LPCSTR, LONG, LONG, LPCSTR, LPCSTR);
VOID MACRO_ShortCut(LPCSTR, LPCSTR, WPARAM, LPARAM, LPCSTR);
VOID MACRO_TCard(LONG);
VOID MACRO_Test(LONG);
BOOL MACRO_TestALink(LPCSTR);
BOOL MACRO_TestKLink(LPCSTR);
VOID MACRO_UncheckItem(LPCSTR);
VOID MACRO_UpdateWindow(LPCSTR, LPCSTR);

/* Local Variables:    */
/* c-file-style: "GNU" */
/* End:                */
