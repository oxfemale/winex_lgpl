#ifndef _LMSVC_
#define _LMSVC_

#if _MSC_VER > 1000
#pragma once
#endif

#ifdef __cplusplus
extern "C" {
#endif

#include <lmsname.h>

typedef struct _SERVICE_INFO_0 {
    LPWSTR  svci0_name;
} SERVICE_INFO_0, *PSERVICE_INFO_0, * LPSERVICE_INFO_0;

typedef struct _SERVICE_INFO_1 {
    LPWSTR  svci1_name;
    DWORD   svci1_status;
    DWORD   svci1_code;
    DWORD   svci1_pid;
} SERVICE_INFO_1, *PSERVICE_INFO_1, * LPSERVICE_INFO_1;

typedef struct _SERVICE_INFO_2 {
    LPWSTR  svci2_name;
    DWORD   svci2_status;
    DWORD   svci2_code;
    DWORD   svci2_pid;
    LPWSTR  svci2_text;
    DWORD   svci2_specific_error;
    LPWSTR  svci2_display_name;
} SERVICE_INFO_2, *PSERVICE_INFO_2, * LPSERVICE_INFO_2;

NET_API_STATUS NET_API_FUNCTION
NetServiceControl (
    IN  LPCWSTR servername OPTIONAL,
    IN  LPCWSTR service,
    IN  DWORD   opcode,
    IN  DWORD   arg,
    OUT LPBYTE  *bufptr
    );

NET_API_STATUS NET_API_FUNCTION
NetServiceEnum (
    IN  LPCWSTR     servername OPTIONAL,
    IN  DWORD       level,
    OUT LPBYTE      *bufptr,
    IN  DWORD       prefmaxlen,
    OUT LPDWORD     entriesread,
    OUT LPDWORD     totalentries,
    IN OUT LPDWORD  resume_handle OPTIONAL
    );

NET_API_STATUS NET_API_FUNCTION
NetServiceGetInfo (
    IN  LPCWSTR servername OPTIONAL,
    IN  LPCWSTR service,
    IN  DWORD   level,
    OUT LPBYTE   *bufptr
    );

NET_API_STATUS NET_API_FUNCTION
NetServiceInstall (
    IN  LPCWSTR servername OPTIONAL,
    IN  LPCWSTR service,
    IN  DWORD   argc,
    IN  LPCWSTR argv[],
    OUT LPBYTE  *bufptr
    );

#define SERVICE_INSTALL_STATE       0x03
#define SERVICE_UNINSTALLED         0x00
#define SERVICE_INSTALL_PENDING     0x01
#define SERVICE_UNINSTALL_PENDING   0x02
#define SERVICE_INSTALLED           0x03

#define SERVICE_PAUSE_STATE              0x0C
#define LM20_SERVICE_ACTIVE              0x00
#define LM20_SERVICE_CONTINUE_PENDING    0x04
#define LM20_SERVICE_PAUSE_PENDING       0x08
#define LM20_SERVICE_PAUSED              0x0C

#define SERVICE_NOT_UNINSTALLABLE   0x00
#define SERVICE_UNINSTALLABLE       0x10

#define SERVICE_NOT_PAUSABLE        0x00
#define SERVICE_PAUSABLE            0x20

#define SERVICE_REDIR_PAUSED        0x700
#define SERVICE_REDIR_DISK_PAUSED   0x100
#define SERVICE_REDIR_PRINT_PAUSED  0x200
#define SERVICE_REDIR_COMM_PAUSED   0x400

#define SERVICE_DOS_ENCRYPTION  L"ENCRYPT"

#define SERVICE_CTRL_INTERROGATE    0
#define SERVICE_CTRL_PAUSE          1
#define SERVICE_CTRL_CONTINUE       2
#define SERVICE_CTRL_UNINSTALL      3

#define SERVICE_CTRL_REDIR_DISK     0x1
#define SERVICE_CTRL_REDIR_PRINT    0x2
#define SERVICE_CTRL_REDIR_COMM     0x4

#define SERVICE_IP_NO_HINT          0x0
#define SERVICE_CCP_NO_HINT         0x0

#define SERVICE_IP_QUERY_HINT       0x10000
#define SERVICE_CCP_QUERY_HINT      0x10000

#define SERVICE_IP_CHKPT_NUM        0x0FF
#define SERVICE_CCP_CHKPT_NUM       0x0FF

#define SERVICE_IP_WAIT_TIME        0x0FF00
#define SERVICE_CCP_WAIT_TIME       0x0FF00

#define SERVICE_IP_WAITTIME_SHIFT   8
#define SERVICE_NTIP_WAITTIME_SHIFT 12

#define UPPER_HINT_MASK     0x0000FF00
#define LOWER_HINT_MASK     0x000000FF
#define UPPER_GET_HINT_MASK 0x0FF00000
#define LOWER_GET_HINT_MASK 0x0000FF00
#define SERVICE_NT_MAXTIME  0x0000FFFF
#define SERVICE_RESRV_MASK  0x0001FFFF
#define SERVICE_MAXTIME     0x000000FF

#define SERVICE_BASE                3050
#define SERVICE_UIC_NORMAL          0

#define SERVICE_UIC_BADPARMVAL          (SERVICE_BASE + 1)
#define SERVICE_UIC_MISSPARM            (SERVICE_BASE + 2)
#define SERVICE_UIC_UNKPARM             (SERVICE_BASE + 3)
#define SERVICE_UIC_RESOURCE            (SERVICE_BASE + 4)
#define SERVICE_UIC_CONFIG              (SERVICE_BASE + 5)
#define SERVICE_UIC_SYSTEM              (SERVICE_BASE + 6)
#define SERVICE_UIC_INTERNAL            (SERVICE_BASE + 7)
#define SERVICE_UIC_AMBIGPARM           (SERVICE_BASE + 8)
#define SERVICE_UIC_DUPPARM             (SERVICE_BASE + 9)
#define SERVICE_UIC_KILL                (SERVICE_BASE + 10)
#define SERVICE_UIC_EXEC                (SERVICE_BASE + 11)
#define SERVICE_UIC_SUBSERV             (SERVICE_BASE + 12)
#define SERVICE_UIC_CONFLPARM           (SERVICE_BASE + 13)
#define SERVICE_UIC_FILE                (SERVICE_BASE + 14)

#define SERVICE_UIC_M_NULL  0

#define SERVICE_UIC_M_MEMORY    (SERVICE_BASE + 20)     /* memory */
#define SERVICE_UIC_M_DISK      (SERVICE_BASE + 21)     /* disk space */
#define SERVICE_UIC_M_THREADS   (SERVICE_BASE + 22)     /* thread */
#define SERVICE_UIC_M_PROCESSES (SERVICE_BASE + 23)     /* process */

#define SERVICE_UIC_M_SECURITY          (SERVICE_BASE + 24)
#define SERVICE_UIC_M_LANROOT           (SERVICE_BASE + 25)
#define SERVICE_UIC_M_REDIR             (SERVICE_BASE + 26)
#define SERVICE_UIC_M_SERVER            (SERVICE_BASE + 27)
#define SERVICE_UIC_M_SEC_FILE_ERR      (SERVICE_BASE + 28)
#define SERVICE_UIC_M_FILES             (SERVICE_BASE + 29)
#define SERVICE_UIC_M_LOGS              (SERVICE_BASE + 30)
#define SERVICE_UIC_M_LANGROUP          (SERVICE_BASE + 31)
#define SERVICE_UIC_M_MSGNAME           (SERVICE_BASE + 32)
#define SERVICE_UIC_M_ANNOUNCE          (SERVICE_BASE + 33)
#define SERVICE_UIC_M_UAS               (SERVICE_BASE + 34)
#define SERVICE_UIC_M_SERVER_SEC_ERR    (SERVICE_BASE + 35)
#define SERVICE_UIC_M_WKSTA             (SERVICE_BASE + 37)
#define SERVICE_UIC_M_ERRLOG            (SERVICE_BASE + 38)
#define SERVICE_UIC_M_FILE_UW           (SERVICE_BASE + 39)
#define SERVICE_UIC_M_ADDPAK            (SERVICE_BASE + 40)
#define SERVICE_UIC_M_LAZY              (SERVICE_BASE + 41)
#define SERVICE_UIC_M_UAS_MACHINE_ACCT  (SERVICE_BASE + 42)
#define SERVICE_UIC_M_UAS_SERVERS_NMEMB (SERVICE_BASE + 43)
#define SERVICE_UIC_M_UAS_SERVERS_NOGRP (SERVICE_BASE + 44)
#define SERVICE_UIC_M_UAS_INVALID_ROLE  (SERVICE_BASE + 45)
#define SERVICE_UIC_M_NETLOGON_NO_DC    (SERVICE_BASE + 46)
#define SERVICE_UIC_M_NETLOGON_DC_CFLCT (SERVICE_BASE + 47)
#define SERVICE_UIC_M_NETLOGON_AUTH     (SERVICE_BASE + 48)
#define SERVICE_UIC_M_UAS_PROLOG        (SERVICE_BASE + 49)

#define SERVICE2_BASE    5600

#define SERVICE_UIC_M_NETLOGON_MPATH    (SERVICE2_BASE + 0)
#define SERVICE_UIC_M_LSA_MACHINE_ACCT  (SERVICE2_BASE + 1)
#define SERVICE_UIC_M_DATABASE_ERROR    (SERVICE2_BASE + 2)

#define SERVICE_IP_CODE(tt,nn) \
  ((long)SERVICE_IP_QUERY_HINT|(long)(nn|(tt<<SERVICE_IP_WAITTIME_SHIFT)))

#define SERVICE_CCP_CODE(tt,nn) \
  ((long)SERVICE_CCP_QUERY_HINT|(long)(nn|(tt<<SERVICE_IP_WAITTIME_SHIFT)))

#define SERVICE_UIC_CODE(cc,mm) \
  ((long)(((long)cc<<16)|(long)(unsigned short)mm))

#define SERVICE_NT_CCP_CODE(tt,nn)  \
  (  \
    ((long)SERVICE_CCP_QUERY_HINT)   | \
    ((long)(nn))   | \
    (((tt)&LOWER_HINT_MASK) << SERVICE_IP_WAITTIME_SHIFT)   | \
    (((tt)&UPPER_HINT_MASK) << SERVICE_NTIP_WAITTIME_SHIFT)   \
  )

#define SERVICE_NT_WAIT_GET(code) \
    (   \
      (((code) & UPPER_GET_HINT_MASK) >> SERVICE_NTIP_WAITTIME_SHIFT)  |  \
      (((code) & LOWER_GET_HINT_MASK) >> SERVICE_IP_WAITTIME_SHIFT)  \
    )

#ifdef __cplusplus
}
#endif

#endif
