name	compobj
type	win16
owner	ole32

1 pascal CoBuildVersion() CoBuildVersion
2 pascal CoInitialize(long) CoInitialize16
3 pascal CoUninitialize() CoUninitialize16
4 pascal CoGetMalloc(long ptr) CoGetMalloc16
5 pascal CoRegisterClassObject(ptr ptr long long ptr) CoRegisterClassObject16
6 pascal CoRevokeClassObject(long) CoRevokeClassObject16
7 pascal CoGetClassObject(ptr long ptr ptr ptr) CoGetClassObject
8 stub COMARSHALINTERFACE
9 stub COUNMARSHALINTERFACE
10 stub COLOADLIBRARY
11 stub COFREELIBRARY
12 stub COFREEALLLIBRARIES
13 pascal CoCreateInstance(ptr ptr long ptr ptr) CoCreateInstance
14 stub STRINGFROMIID
15 pascal CoDisconnectObject(ptr long) CoDisconnectObject
16 stub CORELEASEMARSHALDATA
17 pascal16 CoFreeUnusedLibraries() CoFreeUnusedLibraries
18 pascal16 IsEqualGUID(ptr ptr) IsEqualGUID16
19 pascal StringFromCLSID(ptr ptr) StringFromCLSID16
20 pascal CLSIDFromString(str ptr) CLSIDFromString16
21 stub ISVALIDPTRIN
22 stub ISVALIDPTROUT
23 stub ISVALIDINTERFACE
24 stub ISVALIDIID
25 stub RESULTFROMSCODE
26 stub GETSCODE
27 pascal CoRegisterMessageFilter(ptr ptr) CoRegisterMessageFilter16
28 stub COISHANDLERCONNECTED
29 stub SHRADDREF
30 pascal16 CoFileTimeToDosDateTime(ptr ptr ptr) CoFileTimeToDosDateTime16
31 pascal16 CoDosDateTimeToFileTime(word word ptr) CoDosDateTimeToFileTime16
32 stub COMARSHALHRESULT
33 stub COUNMARSHALHRESULT
34 pascal CoGetCurrentProcess() CoGetCurrentProcess
35 stub SHRCREATE
36 stub COISOLE1CLASS
37 stub _GUID_NULL
38 stub _IID_IUNKNOWN
39 stub _IID_ICLASSFACTORY
40 stub _IID_IMALLOC
41 stub _IID_IMARSHAL
42 stub _IID_IRPCCHANNEL
43 stub _IID_IRPCSTUB
44 stub _IID_ISTUBMANAGER
45 stub _IID_IRPCPROXY
46 stub _IID_IPROXYMANAGER
47 stub _IID_IPSFACTORY
48 stub _IID_ILOCKBYTES
49 stub _IID_ISTORAGE
50 stub _IID_ISTREAM
51 stub _IID_IENUMSTATSTG
52 stub _IID_IBINDCTX
53 stub _IID_IMONIKER
54 stub _IID_IRUNNINGOBJECTTABLE
55 stub _IID_IINTERNALMONIKER
56 stub _IID_IROOTSTORAGE
57 stub _IID_IDFRESERVED1
58 stub _IID_IDFRESERVED2
59 stub _IID_IDFRESERVED3
60 stub _IID_IMESSAGEFILTER
61 pascal CLSIDFromProgID(str ptr) CLSIDFromProgID16
62 stub PROGIDFROMCLSID
63 pascal CoLockObjectExternal(segptr word word) CoLockObjectExternal16
64 stub _CLSID_STDMARSHAL
65 stub COGETTREATASCLASS
66 stub COTREATASCLASS
67 stub COGETSTANDARDMARSHAL
68 stub PROPAGATERESULT
69 stub IIDFROMSTRING
70 stub _IID_ISTDMARSHALINFO
71 pascal CoCreateStandardMalloc(long ptr) CoCreateStandardMalloc16
72 stub _IID_IEXTERNALCONNECTION
73 stub COCREATEGUID
75 stub FNASSERT
76 pascal StringFromGUID2(ptr ptr word) StringFromGUID2
77 stub COGETCLASSEXT
78 stub OLE1CLASSFROMCLSID2
79 stub CLSIDFROMOLE1CLASS
80 stub COOPENCLASSKEY
81 stub GUIDFROMSTRING
82 pascal CoFileTimeNow(ptr) CoFileTimeNow
83 stub REMALLOCOID
84 stub REMFREEOID
85 stub REMCREATEREMOTEHANDLER
86 stub REMCONNECTTOOBJECT
87 stub REMGETINFOFORCID
88 stub LRPCCALL
89 stub LRPCDISPATCH
90 stub LRPCREGISTERMONITOR
91 stub LRPCREVOKEMONITOR
92 stub LRPCGETTHREADWINDOW
93 stub TIMERCALLBACKPROC
94 pascal LookupETask(ptr ptr) LookupETask16
95 pascal16 SetETask(word ptr) SetETask16
96 stub LRPCFREEMONITORDATA
97 stub REMLOOKUPSHUNK
98 stub SHRGETSIZE
99 stub CALLTHKMGRUNINITIALIZE
100 stub ??0CARRAYFVALUE@@REC@KI@Z
101 stub ??1CARRAYFVALUE@@REC@XZ
102 stub ?ASSERTVALID@CARRAYFVALUE@@RFCXXZ
103 stub ?FREEEXTRA@CARRAYFVALUE@@RECXXZ
104 stub ?_GETAT@CARRAYFVALUE@@RFCPEXH@Z
105 stub ?GETSIZE@CARRAYFVALUE@@RFCHXZ
106 stub ?REMOVEALL@CARRAYFVALUE@@RECXXZ
107 stub SHRDESTROY
108 stub ?INDEXOF@CARRAYFVALUE@@RECHPEXII@Z
109 stub ?INSERTAT@CARRAYFVALUE@@RECHHPEXH@Z
110 stub COSETSTATE
111 stub ?REMOVEAT@CARRAYFVALUE@@RECXHH@Z
112 stub ?SETAT@CARRAYFVALUE@@RECXHPEX@Z
113 stub ?SETATGROW@CARRAYFVALUE@@RECHHPEX@Z
114 stub ?SETSIZE@CARRAYFVALUE@@RECHHH@Z
115 pascal CoGetState(ptr) CoGetState16
116 pascal DllEntryPoint(long word word word long word) COMPOBJ_DllEntryPoint
117 stub ?RELEASE@CSTDMALLOC@@VEAKXZ
118 stub ?ALLOC@CSTDMALLOC@@VEAPEXK@Z
119 stub SHRRELEASE
120 stub ?GETASSOCAT@CMAPKEYTOVALUE@@BFCPEUCASSOC@1@PEXIAEI@Z
121 stub ?SETASSOCKEY@CMAPKEYTOVALUE@@BFCHPEUCASSOC@1@PEXI@Z
122 stub ??1CMAPKEYTOVALUE@@REC@XZ
123 stub ?GETASSOCKEYPTR@CMAPKEYTOVALUE@@BFCXPEUCASSOC@1@PEPEXPEI@Z
124 stub ?NEWASSOC@CMAPKEYTOVALUE@@BECPEUCASSOC@1@IPEXI0@Z
125 stub ?SIZEASSOC@CMAPKEYTOVALUE@@BFCIXZ
126 stub ?FREEASSOC@CMAPKEYTOVALUE@@BECXPEUCASSOC@1@@Z
127 stub ?GETSTARTPOSITION@CMAPKEYTOVALUE@@RFCPEXXZ
128 stub ?GETNEXTASSOC@CMAPKEYTOVALUE@@RFCXPEPEXPEXPEI1@Z
129 stub ?COMPAREASSOCKEY@CMAPKEYTOVALUE@@BFCHPEUCASSOC@1@PEXI@Z
130 stub ?REMOVEHKEY@CMAPKEYTOVALUE@@RECHK@Z
131 stub ?GETHKEY@CMAPKEYTOVALUE@@RFCKPEXI@Z
132 stub ?GETCOUNT@CMAPKEYTOVALUE@@RFCHXZ
133 stub ?LOOKUP@CMAPKEYTOVALUE@@RFCHPEXI0@Z
134 stub ?GETASSOCVALUE@CMAPKEYTOVALUE@@BFCXPEUCASSOC@1@PEX@Z
135 stub ?REMOVEKEY@CMAPKEYTOVALUE@@RECHPEXI@Z
136 stub ?REMOVEALL@CMAPKEYTOVALUE@@RECXXZ
137 stub SHRALLOC
138 stub ?FREEASSOCKEY@CMAPKEYTOVALUE@@BFCXPEUCASSOC@1@@Z
139 stub ?SETAT@CMAPKEYTOVALUE@@RECHPEXI0@Z
140 stub ?LOOKUPHKEY@CMAPKEYTOVALUE@@RFCHKPEX@Z
141 stub ?ASSERTVALID@CMAPKEYTOVALUE@@RFCXXZ
142 stub ?SETASSOCVALUE@CMAPKEYTOVALUE@@BFCXPEUCASSOC@1@PEX@Z
143 stub ?SETATHKEY@CMAPKEYTOVALUE@@RECHKPEX@Z
144 stub ??0CMAPKEYTOVALUE@@REC@KIIHP7CIPEXI@ZI@Z
145 stub ?INITHASHTABLE@CMAPKEYTOVALUE@@BECHXZ
146 stub ?GETASSOCVALUEPTR@CMAPKEYTOVALUE@@BFCXPEUCASSOC@1@PEPEX@Z
147 stub ?LOOKUPADD@CMAPKEYTOVALUE@@RFCHPEXI0@Z
148 stub MKVDEFAULTHASHKEY
149 stub DELETE16
150 stub COMEMCTXOF
151 stub COMEMALLOC
152 stub COMEMFREE
153 stub SHRREALLOC
154 stub ___EXPORTEDSTUB
155 stub LRPCREGISTERWIN32SMONITOR
156 stub MYREMGETINFOFORCID
157 stub SHRFREE
158 stub OPNEW16
159 stub ADDCOINFO
160 stub CORUNMODALLOOP
161 stub COHANDLEINCOMINGCALL
162 stub COSETACKSTATE
163 stub SHRDIDALLOC
164 stub ?GETAT@CARRAYFVALUE@@RFCPEXH@Z
165 stub ?GETUPPERBOUND@CARRAYFVALUE@@RFCHXZ
166 stub OPDELETE16
167 stub ?GETSIZEVALUE@CARRAYFVALUE@@RFCHXZ
168 stub ?PROXY1632ADDREF@@ZAKPEVCPROXY1632@@@Z
# FIXME: 169 is a duplicate of 97
169 stub REMLOOKUPSHUNK_dup
170 stub ?ISEMPTY@CMAPKEYTOVALUE@@RFCHXZ
171 stub ?FREE@CSTDMALLOC@@VEAXPEX@Z
172 stub CALLTHKMGRINITIALIZE
173 stub ?REALLOC@CSTDMALLOC@@VEAPEXPEXK@Z
174 stub ?SM16RHQI@@ZAPEXPEVCSM16RELEASEHANDLER@@AFUGUID@@PEPEX@Z
175 stub ?PROXY1632METHOD10@@ZAKPEVCPROXY1632@@@Z
# FIXME: 176 is a duplicate of 154
176 stub ___EXPORTEDSTUB_dup
177 stub ?PROXY1632METHOD20@@ZAKPEVCPROXY1632@@@Z
178 stub ?PROXY1632METHOD11@@ZAKPEVCPROXY1632@@@Z
179 stub ?PROXY1632METHOD30@@ZAKPEVCPROXY1632@@@Z
180 stub ?PROXY1632METHOD21@@ZAKPEVCPROXY1632@@@Z
181 stub ?PROXY1632METHOD12@@ZAKPEVCPROXY1632@@@Z
182 stub ?PROXY1632METHOD31@@ZAKPEVCPROXY1632@@@Z
183 stub ?PROXY1632METHOD22@@ZAKPEVCPROXY1632@@@Z
184 stub ?PROXY1632METHOD13@@ZAKPEVCPROXY1632@@@Z
185 stub ?GETSIZE@CSTDMALLOC@@VEAKPEX@Z
186 stub ?PROXY1632METHOD23@@ZAKPEVCPROXY1632@@@Z
187 stub ?PROXY1632METHOD14@@ZAKPEVCPROXY1632@@@Z
188 stub ?PROXY1632METHOD24@@ZAKPEVCPROXY1632@@@Z
189 stub ?PROXY1632METHOD15@@ZAKPEVCPROXY1632@@@Z
190 stub ?PROXY1632METHOD25@@ZAKPEVCPROXY1632@@@Z
191 stub ?PROXY1632METHOD16@@ZAKPEVCPROXY1632@@@Z
192 stub ?PROXY1632METHOD26@@ZAKPEVCPROXY1632@@@Z
193 stub ?PROXY1632METHOD17@@ZAKPEVCPROXY1632@@@Z
194 stub ?PROXY1632METHOD27@@ZAKPEVCPROXY1632@@@Z
195 stub ?PROXY1632METHOD18@@ZAKPEVCPROXY1632@@@Z
196 stub ?PROXY1632METHOD28@@ZAKPEVCPROXY1632@@@Z
197 stub ?ADDREF@CSTDMALLOC@@VEAKXZ
198 stub ?PROXY1632METHOD19@@ZAKPEVCPROXY1632@@@Z
199 stub ?PROXY1632METHOD29@@ZAKPEVCPROXY1632@@@Z
200 stub CALL32INITIALIZE
201 pascal CALLOBJECTINWOW(ptr ptr) CallObjectInWOW
203 stub CALLOBJECTINWOWCHECKINIT
204 stub CALLOBJECTINWOWCHECKTHKMGR
205 stub CONVERTHR1632
206 stub CONVERTHR3216
207 stub ADDAPPCOMPATFLAG

# WINE internal relays (for Win16 interfaces)
500 cdecl IMalloc16_QueryInterface(ptr ptr ptr) IMalloc16_fnQueryInterface
501 cdecl IMalloc16_AddRef(ptr) IMalloc16_fnAddRef
502 cdecl IMalloc16_Release(ptr) IMalloc16_fnRelease
503 cdecl IMalloc16_Alloc(ptr long) IMalloc16_fnAlloc
504 cdecl IMalloc16_Realloc(ptr segptr long) IMalloc16_fnRealloc
505 cdecl IMalloc16_Free(ptr segptr) IMalloc16_fnFree
506 cdecl IMalloc16_GetSize(ptr segptr) IMalloc16_fnGetSize
507 cdecl IMalloc16_DidAlloc(ptr segptr) IMalloc16_fnDidAlloc
508 cdecl IMalloc16_HeapMinimize(ptr) IMalloc16_fnHeapMinimize
