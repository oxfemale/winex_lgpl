name	ole2
type	win16
owner	ole32

1 pascal OleBuildVersion() OleBuildVersion
2 pascal OleInitialize(ptr) OleInitialize
3 pascal OleUninitialize() OleUninitialize
4 stub DLLGETCLASSOBJECT
#5 WEP
6 stub OLEQUERYLINKFROMDATA
7 stub OLEQUERYCREATEFROMDATA
8 stub OLECREATEFROMDATA
9 stub OLECREATELINKFROMDATA
10 stub OLECREATE
11 stub OLECREATELINK
12 stub OLELOAD
13 stub OLESAVE
14 stub OLERUN
#15 ___EXPORTEDSTUB
16 stub OLEISRUNNING
17 stub OLELOCKRUNNING
18 stub READCLASSSTG
19 stub WRITECLASSSTG
20 stub READCLASSSTM
21 stub WRITECLASSSTM
22 stub BINDMONIKER
23 stub MKPARSEDISPLAYNAME
24 stub OLESAVETOSTREAM
25 stub OLELOADFROMSTREAM
26 stub CREATEBINDCTX
27 stub CREATEITEMMONIKER
28 pascal CreateFileMoniker(str ptr) CreateFileMoniker16
29 stub CREATEGENERICCOMPOSITE
30 pascal GetRunningObjectTable(long ptr) GetRunningObjectTable16
31 stub OLEGETMALLOC
32 stub RELEASESTGMEDIUM
33 stub READSTRINGSTREAM
34 stub WRITESTRINGSTREAM
35 pascal RegisterDragDrop(word segptr) RegisterDragDrop16
36 pascal RevokeDragDrop(word) RevokeDragDrop16
37 stub DODRAGDROP
38 stub CREATEOLEADVISEHOLDER
39 stub CREATEDATAADVISEHOLDER
40 stub OLECREATEMENUDESCRIPTOR
41 stub OLESETMENUDESCRIPTOR
42 stub OLEDESTROYMENUDESCRIPTOR
43 stub OPENORCREATESTREAM
44 stub CREATEANTIMONIKER
45 stub CREATEPOINTERMONIKER
46 stub MONIKERRELATIVEPATHTO
47 stub MONIKERCOMMONPREFIXWITH
48 stub ISACCELERATOR
49 stub OLESETCLIPBOARD
50 stub OLEGETCLIPBOARD
51 stub OLEDUPLICATEDATA
52 stub OLEGETICONOFFILE
53 stub OLEGETICONOFCLASS
54 stub CREATEILOCKBYTESONHGLOBAL
55 stub GETHGLOBALFROMILOCKBYTES
56 pascal16 OleMetaFilePictFromIconAndLabel(word str str word) OleMetaFilePictFromIconAndLabel16
57 stub GETCLASSFILE
58 stub OLEDRAW
59 stub OLECREATEDEFAULTHANDLER
60 stub OLECREATEEMBEDDINGHELPER
61 stub OLECONVERTISTORAGETOOLESTREAMEX
62 stub OLECONVERTOLESTREAMTOISTORAGEEX
63 stub SETDOCUMENTBITSTG
64 stub GETDOCUMENTBITSTG
65 stub WRITEOLESTG
66 stub READOLESTG
67 stub OLECREATEFROMFILE
68 stub OLECREATELINKTOFILE
69 stub CREATEDATACACHE
70 stub OLECONVERTISTORAGETOOLESTREAM
71 stub OLECONVERTOLESTREAMTOISTORAGE
74 stub READFMTUSERTYPESTG
75 stub WRITEFMTUSERTYPESTG
76 pascal16 OleFlushClipboard() OleFlushClipboard16
77 stub OLEISCURRENTCLIPBOARD
78 stub OLETRANSLATEACCELERATOR
79 stub OLEDOAUTOCONVERT
80 stub OLEGETAUTOCONVERT
81 stub OLESETAUTOCONVERT
82 stub GETCONVERTSTG
83 stub SETCONVERTSTG
84 stub CREATESTREAMONHGLOBAL
85 stub GETHGLOBALFROMSTREAM
86 stub OLESETCONTAINEDOBJECT
87 stub OLENOTEOBJECTVISIBLE
88 stub OLECREATESTATICFROMDATA
89 stub OLEREGGETUSERTYPE
90 stub OLEREGGETMISCSTATUS
91 stub OLEREGENUMFORMATETC
92 stub OLEREGENUMVERBS
93 stub OLEGETENUMFORMATETC
100 stub MAKEDEBUGSTREAM
104 stub DBGLOGOPEN
105 stub DBGLOGCLOSE
106 stub DBGLOGOUTPUTDEBUGSTRING
107 stub DBGLOGWRITE
108 stub DBGLOGTIMESTAMP
109 stub DBGLOGWRITEBANNER
110 stub DBGDUMPOBJECT
111 stub DBGISOBJECTVALID
112 stub DUMPALLOBJECTS
113 stub VALIDATEALLOBJECTS
114 stub DBGDUMPCLASSNAME
115 stub DBGDUMPEXTERNALOBJECT
120 stub _IID_IENUMUNKNOWN
121 stub _IID_IENUMSTRING
122 stub _IID_IENUMMONIKER
123 stub _IID_IENUMFORMATETC
124 stub _IID_IENUMOLEVERB
125 stub _IID_IENUMSTATDATA
126 stub _IID_IENUMGENERIC
127 stub _IID_IENUMHOLDER
128 stub _IID_IENUMCALLBACK
129 stub _IID_IPERSISTSTREAM
130 stub _IID_IPERSISTSTORAGE
131 stub _IID_IPERSISTFILE
132 stub _IID_IPERSIST
133 stub _IID_IVIEWOBJECT
134 stub _IID_IDATAOBJECT
135 stub _IID_IADVISESINK
136 stub _IID_IDATAADVISEHOLDER
137 stub _IID_IOLEADVISEHOLDER
138 stub _IID_IOLEOBJECT
139 stub _IID_IOLEINPLACEOBJECT
140 stub _IID_IOLEWINDOW
141 stub _IID_IOLEINPLACEUIWINDOW
142 stub _IID_IOLEINPLACEFRAME
143 stub _IID_IOLEINPLACEACTIVEOBJECT
144 stub _IID_IOLECLIENTSITE
145 stub _IID_IOLEINPLACESITE
146 stub _IID_IPARSEDISPLAYNAME
147 stub _IID_IOLECONTAINER
148 stub _IID_IOLEITEMCONTAINER
149 stub _IID_IOLELINK
150 stub _IID_IOLECACHE
151 stub _IID_IOLEMANAGER
152 stub _IID_IOLEPRESOBJ
153 stub _IID_IDROPSOURCE
154 stub _IID_IDROPTARGET
155 stub _IID_IDEBUG
156 stub _IID_IDEBUGSTREAM
157 stub _IID_IADVISESINK2
158 stub _IID_IVIEWOBJECT2
159 stub _IID_IOLECACHE2
160 stub _IID_IOLECACHECONTROL
161 stub _IID_IRUNNABLEOBJECT
