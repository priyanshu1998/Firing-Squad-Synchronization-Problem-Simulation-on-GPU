#include <iostream>
#include <cuda.h>
#include <cuda_runtime.h>
#include <algorithm>
#include <stdio.h>

constexpr int ids = 557432;
int trans[ids];

void trans_init() {
    trans[557312] = 1;
    trans[528384] = 3;
    trans[65536] = 4;
    trans[0] = 0;
    trans[8] = 0;
    trans[136] = 0;
    trans[557364] = 1;
    trans[529216] = 7;
    trans[78848] = 4;
    trans[212992] = 3;
    trans[262144] = 4;
    trans[557428] = 1;
    trans[530243] = 3;
    trans[95284] = 7;
    trans[475968] = 3;
    trans[275456] = 4;
    trans[557367] = 1;
    trans[529267] = 3;
    trans[79668] = 4;
    trans[226115] = 6;
    trans[472116] = 4;
    trans[213824] = 3;
    trans[529222] = 7;
    trans[78948] = 3;
    trans[214595] = 7;
    trans[287796] = 4;
    trans[410435] = 3;
    trans[275508] = 4;
    trans[530231] = 7;
    trans[95092] = 4;
    trans[472899] = 3;
    trans[226356] = 7;
    trans[475971] = 3;
    trans[213827] = 3;
    trans[95287] = 6;
    trans[476019] = 3;
    trans[276276] = 4;
    trans[213000] = 3;
    trans[262280] = 1;
    trans[557366] = 1;
    trans[529251] = 3;
    trans[79412] = 7;
    trans[222022] = 3;
    trans[406628] = 3;
    trans[275505] = 5;
    trans[213784] = 0;
    trans[274824] = 1;
    trans[79667] = 7;
    trans[226103] = 3;
    trans[471924] = 4;
    trans[210755] = 3;
    trans[472119] = 3;
    trans[213875] = 3;
    trans[472117] = 5;
    trans[275717] = 5;
    trans[217175] = 0;
    trans[329073] = 7;
    trans[22296] = 0;
    trans[356744] = 1;
    trans[78947] = 3;
    trans[214579] = 6;
    trans[287540] = 4;
    trans[406342] = 3;
    trans[210021] = 5;
    trans[214608] = 1;
    trans[288005] = 4;
    trans[413776] = 0;
    trans[328967] = 5;
    trans[20592] = 6;
    trans[329473] = 5;
    trans[28696] = 0;
    trans[459144] = 1;
    trans[557427] = 1;
    trans[530230] = 7;
    trans[95076] = 3;
    trans[472643] = 7;
    trans[222261] = 7;
    trans[410449] = 0;
    trans[275732] = 7;
    trans[217408] = 1;
    trans[332805] = 7;
    trans[82006] = 3;
    trans[263525] = 7;
    trans[22096] = 7;
    trans[353537] = 0;
    trans[413720] = 7;
    trans[275509] = 5;
    trans[213840] = 0;
    trans[275713] = 5;
    trans[217112] = 7;
    trans[328072] = 1;
    trans[95095] = 7;
    trans[472944] = 1;
    trans[227079] = 1;
    trans[487537] = 7;
    trans[460567] = 7;
    trans[29043] = 1;
    trans[464695] = 7;
    trans[460568] = 7;
    trans[29064] = 1;
    trans[557431] = 2;
    trans[530289] = 2;
    trans[96017] = 2;
    trans[487703] = 2;
    trans[463223] = 2;
    trans[71537] = 2;
    trans[96023] = 2;
    trans[487799] = 2;
    trans[464753] = 2;
    trans[96024] = 2;
    trans[487816] = 2;
    trans[95281] = 1;
    trans[475928] = 0;
    trans[557361] = 2;
    trans[529168] = 2;
    trans[78081] = 2;
    trans[200728] = 2;
    trans[65928] = 2;
    trans[472113] = 5;
    trans[78949] = 7;
    trans[288001] = 7;
    trans[226357] = 1;
    trans[475984] = 0;
    trans[475920] = 0;
    trans[274693] = 1;
    trans[200791] = 3;
    trans[66929] = 1;
    trans[200723] = 2;
    trans[65841] = 2;
    trans[4880] = 2;
    trans[406629] = 5;
    trans[413783] = 0;
    trans[79669] = 1;
    trans[226129] = 1;
    trans[472340] = 0;
    trans[332807] = 3;
    trans[82032] = 1;
    trans[263937] = 1;
    trans[529169] = 2;
    trans[78096] = 2;
    trans[200961] = 2;
    trans[69651] = 2;
    trans[4881] = 2;
    trans[69656] = 2;
    trans[213776] = 0;
    trans[200784] = 3;
    trans[66823] = 4;
    trans[413715] = 7;
    trans[327988] = 1;
    trans[4934] = 7;
    trans[528392] = 3;
    trans[65672] = 1;
    trans[529176] = 2;
    trans[78216] = 2;
    trans[210020] = 3;
    trans[222259] = 3;
    trans[410423] = 3;
    trans[275316] = 4;
    trans[217168] = 0;
    trans[95091] = 3;
    trans[472883] = 7;
    trans[226100] = 4;
    trans[471875] = 3;
    trans[209969] = 5;
    trans[66821] = 4;
    trans[20566] = 0;
    trans[329061] = 5;
    trans[217107] = 7;
    trans[4928] = 7;
    trans[78853] = 4;
    trans[213079] = 3;
    trans[263536] = 1;
    trans[22279] = 0;
    trans[356465] = 5;
    trans[22295] = 0;
    trans[356724] = 1;
    trans[464707] = 3;
    trans[209975] = 3;
    trans[226355] = 6;
    trans[475955] = 3;
    trans[275252] = 4;
    trans[209734] = 3;
    trans[328965] = 5;
    trans[95286] = 6;
    trans[476003] = 3;
    trans[276020] = 7;
    trans[222019] = 3;
    trans[406581] = 5;
    trans[213841] = 0;
    trans[82000] = 3;
    trans[263429] = 4;
    trans[20567] = 0;
    trans[329072] = 7;
    trans[79415] = 6;
    trans[222067] = 3;
    trans[407349] = 1;
    trans[226128] = 1;
    trans[472327] = 0;
    trans[217201] = 6;
    trans[329495] = 0;
    trans[464692] = 3;
    trans[95040] = 6;
    trans[472071] = 3;
    trans[213104] = 1;
    trans[263941] = 1;
    trans[28759] = 0;
    trans[460145] = 6;
    trans[79409] = 1;
    trans[221969] = 0;
    trans[405776] = 1;
    trans[200966] = 1;
    trans[69728] = 3;
    trans[67073] = 1;
    trans[24595] = 0;
    trans[393526] = 1;
    trans[4963] = 3;
    trans[24600] = 0;
    trans[393608] = 1;
    trans[200721] = 2;
    trans[65811] = 2;
    trans[4401] = 2;
    trans[70416] = 2;
    trans[406579] = 3;
    trans[213815] = 3;
    trans[407347] = 7;
    trans[226099] = 3;
    trans[471860] = 4;
    trans[209731] = 3;
    trans[20560] = 0;
    trans[407348] = 4;
    trans[213072] = 3;
    trans[263431] = 4;
    trans[329477] = 5;
    trans[475974] = 3;
    trans[275557] = 5;
    trans[288006] = 4;
    trans[413792] = 0;
    trans[329217] = 7;
    trans[28691] = 0;
    trans[4979] = 3;
    trans[459063] = 1;
    trans[472115] = 3;
    trans[213811] = 3;
    trans[406627] = 3;
    trans[406339] = 3;
    trans[209973] = 5;
    trans[226102] = 3;
    trans[471908] = 3;
    trans[210499] = 7;
    trans[275719] = 5;
    trans[410448] = 0;
    trans[472069] = 4;
    trans[213078] = 3;
    trans[353542] = 0;
    trans[471927] = 5;
    trans[210800] = 1;
    trans[227077] = 1;
    trans[487510] = 4;
    trans[460128] = 0;
    trans[22017] = 7;
    trans[352275] = 0;
    trans[4964] = 3;
    trans[79427] = 7;
    trans[222263] = 3;
    trans[410487] = 5;
    trans[276336] = 1;
    trans[227072] = 1;
    trans[487431] = 4;
    trans[1793] = 7;
    trans[458864] = 0;
    trans[472337] = 0;
    trans[70663] = 3;
    trans[217364] = 1;
    trans[332096] = 1;
    trans[70417] = 2;
    trans[69649] = 2;
    trans[410419] = 3;
    trans[209971] = 3;
    trans[210739] = 7;
    trans[471923] = 3;
    trans[356359] = 5;
    trans[275461] = 4;
    trans[22272] = 0;
    trans[472118] = 3;
    trans[213859] = 3;
    trans[287543] = 3;
    trans[406387] = 3;
    trans[28752] = 0;
    trans[460039] = 0;
    trans[472325] = 0;
    trans[217174] = 0;
    trans[329056] = 5;
    trans[210741] = 1;
    trans[222260] = 4;
    trans[410432] = 3;
    trans[275463] = 3;
    trans[95075] = 3;
    trans[472627] = 6;
    trans[222001] = 5;
    trans[406289] = 0;
    trans[209168] = 1;
    trans[200960] = 1;
    trans[65623] = 4;
    trans[1392] = 6;
    trans[22273] = 0;
    trans[356371] = 7;
    trans[69637] = 3;
    trans[4980] = 7;
    trans[79683] = 3;
    trans[475953] = 5;
    trans[275217] = 0;
    trans[69638] = 3;
    trans[65637] = 4;
    trans[1616] = 6;
    trans[25857] = 0;
    trans[95077] = 7;
    trans[472656] = 1;
    trans[222465] = 7;
    trans[413713] = 7;
    trans[327955] = 1;
    trans[4404] = 1;
    trans[70470] = 7;
    trans[78944] = 7;
    trans[395031] = 7;
    trans[214535] = 1;
    trans[286833] = 7;
    trans[395032] = 7;
    trans[464694] = 7;
    trans[222007] = 3;
    trans[210740] = 4;
    trans[327781] = 5;
    trans[413702] = 0;
    trans[288000] = 4;
    trans[222004] = 4;
    trans[213830] = 3;
    trans[352369] = 0;
    trans[22023] = 7;
    trans[263520] = 7;
    trans[287797] = 7;
    trans[210019] = 3;
    trans[353536] = 0;
    trans[410422] = 3;
    trans[275300] = 3;
    trans[471863] = 3;
    trans[209783] = 5;
    trans[487504] = 4;
    trans[460037] = 0;
    trans[213879] = 5;
    trans[1376] = 0;
    trans[458838] = 0;
    trans[487429] = 4;
    trans[275511] = 3;
    trans[471889] = 0;
    trans[28785] = 0;
    trans[81927] = 3;
    trans[1799] = 7;
    trans[262256] = 7;
    trans[70656] = 7;
    trans[226101] = 7;
    trans[210193] = 7;
    trans[460561] = 7;
    trans[463219] = 1;
    trans[28951] = 1;
    trans[71479] = 7;
    trans[209779] = 3;
    trans[209780] = 4;
    trans[356357] = 5;
    trans[66816] = 4;
    trans[20487] = 0;
    trans[327792] = 5;
    trans[209974] = 3;
    trans[275255] = 3;
    trans[460032] = 0;
    trans[406321] = 5;
    trans[209681] = 0;
    trans[87] = 0;
    trans[65541] = 4;
    trans[69632] = 3;
    trans[276019] = 6;
    trans[222003] = 3;
    trans[65616] = 4;
    trans[1287] = 0;
    trans[329479] = 5;
    trans[472884] = 4;
    trans[213809] = 5;
    trans[79414] = 6;
    trans[222051] = 3;
    trans[222032] = 0;
    trans[406785] = 5;
    trans[217105] = 7;
    trans[407093] = 1;
    trans[394609] = 6;
    trans[24663] = 0;
    trans[70464] = 7;
    trans[78854] = 4;
    trans[213093] = 3;
    trans[263685] = 1;
    trans[213088] = 3;
    trans[263760] = 1;
    trans[413809] = 6;
    trans[25863] = 0;
    trans[95046] = 6;
    trans[472163] = 3;
    trans[214581] = 1;
    trans[287568] = 0;
    trans[221968] = 0;
    trans[200800] = 3;
    trans[405765] = 1;
    trans[274694] = 1;
    trans[22289] = 0;
    trans[463220] = 1;
    trans[71491] = 3;
    trans[356631] = 1;
    trans[406327] = 3;
    trans[407091] = 6;
    trans[406324] = 4;
    trans[413696] = 0;
    trans[327685] = 5;
    trans[407092] = 7;
    trans[263430] = 4;
    trans[329221] = 7;
    trans[20576] = 0;
    trans[276277] = 1;
    trans[460289] = 6;
    trans[28768] = 0;
    trans[263942] = 1;
    trans[213814] = 3;
    trans[471859] = 3;
    trans[209719] = 3;
    trans[458832] = 0;
    trans[1286] = 0;
    trans[471861] = 5;
    trans[209745] = 0;
    trans[81925] = 3;
    trans[262230] = 4;
    trans[1381] = 0;
    trans[353543] = 0;
    trans[472164] = 3;
    trans[287795] = 3;
    trans[410421] = 5;
    trans[275281] = 0;
    trans[81920] = 3;
    trans[262151] = 4;
    trans[1798] = 7;
    trans[112] = 0;
    trans[329489] = 0;
    trans[71476] = 3;
    trans[24593] = 0;
    trans[393491] = 1;
    trans[70499] = 3;
    trans[4406] = 1;
    trans[327687] = 5;
    trans[20480] = 0;
    trans[329478] = 5;
    trans[287539] = 3;
    trans[406323] = 3;
    trans[209713] = 5;
    trans[1285] = 0;
    trans[275507] = 3;
    trans[80] = 0;
    trans[210483] = 6;
    trans[471907] = 3;
    trans[406352] = 0;
    trans[210177] = 5;
    trans[222005] = 5;
    trans[212997] = 3;
    trans[262231] = 4;
    trans[22278] = 0;
    trans[356448] = 5;
    trans[222068] = 4;
    trans[407363] = 3;
    trans[275280] = 0;
    trans[475957] = 5;
    trans[212998] = 3;
    trans[262245] = 4;
    trans[25862] = 0;
    trans[471909] = 5;
    trans[210512] = 1;
    trans[222469] = 4;
    trans[275552] = 5;
    trans[214533] = 1;
    trans[286806] = 4;
    trans[394592] = 0;
    trans[222262] = 3;
    trans[410469] = 5;
    trans[276048] = 1;
    trans[214528] = 1;
    trans[286727] = 4;
    trans[393328] = 0;
    trans[28689] = 0;
    trans[70515] = 3;
    trans[459027] = 1;
    trans[4407] = 1;
    trans[209716] = 4;
    trans[263424] = 4;
    trans[20486] = 0;
    trans[22016] = 7;
    trans[352263] = 0;
    trans[275251] = 3;
    trans[1280] = 0;
    trans[209717] = 5;
    trans[262224] = 4;
    trans[213813] = 5;
    trans[262149] = 4;
    trans[86] = 0;
    trans[471888] = 0;
    trans[210183] = 5;
    trans[472064] = 4;
    trans[212999] = 3;
    trans[1797] = 7;
    trans[28758] = 0;
    trans[410483] = 3;
    trans[276275] = 7;
    trans[28679] = 0;
    trans[1792] = 7;
    trans[352273] = 0;
    trans[70500] = 3;
    trans[209715] = 3;
    trans[406325] = 5;
    trans[209744] = 0;
    trans[287542] = 3;
    trans[406371] = 3;
    trans[210485] = 1;
    trans[406789] = 5;
    trans[275462] = 4;
    trans[24656] = 0;
    trans[394503] = 0;
    trans[25856] = 0;
    trans[413703] = 0;
    trans[471878] = 3;
    trans[406288] = 0;
    trans[209157] = 1;
    trans[274688] = 1;
    trans[200709] = 3;
    trans[275216] = 0;
    trans[200710] = 3;
    trans[210484] = 7;
    trans[222006] = 3;
    trans[28678] = 0;
    trans[458853] = 0;
    trans[263936] = 1;
    trans[287537] = 5;
    trans[65632] = 4;
    trans[1543] = 6;
    trans[24689] = 0;
    trans[28677] = 0;
    trans[458839] = 0;
    trans[475959] = 3;
    trans[275315] = 3;
    trans[458848] = 0;
    trans[356369] = 7;
    trans[70516] = 7;
    trans[395025] = 7;
    trans[71478] = 7;
    trans[329472] = 5;
    trans[327776] = 5;
    trans[275299] = 3;
    trans[210181] = 5;
    trans[471862] = 3;
    trans[209765] = 5;
    trans[329223] = 7;
    trans[286800] = 4;
    trans[394502] = 0;
    trans[213861] = 5;
    trans[472628] = 7;
    trans[406582] = 3;
    trans[286725] = 4;
    trans[393302] = 0;
    trans[210196] = 7;
    trans[332800] = 7;
    trans[209763] = 3;
    trans[209764] = 3;
    trans[352261] = 0;
    trans[275319] = 5;
    trans[487424] = 4;
    trans[458759] = 0;
    trans[460038] = 0;
    trans[406583] = 3;
    trans[28672] = 0;
    trans[356352] = 5;
    trans[275254] = 3;
    trans[394496] = 0;
    trans[209680] = 0;
    trans[200704] = 3;
    trans[406326] = 3;
    trans[458757] = 0;
    trans[275249] = 5;
    trans[65542] = 4;
    trans[96] = 0;
    trans[1541] = 6;
    trans[276021] = 1;
    trans[263686] = 1;
    trans[394753] = 6;
    trans[24672] = 0;
    trans[458758] = 0;
    trans[101] = 0;
    trans[1542] = 6;
    trans[327686] = 5;
    trans[329222] = 7;
    trans[209718] = 3;
    trans[393296] = 0;
    trans[22022] = 7;
    trans[352352] = 0;
    trans[407107] = 7;
    trans[222052] = 3;
    trans[458752] = 0;
    trans[7] = 0;
    trans[6] = 0;
    trans[287541] = 5;
    trans[262240] = 4;
    trans[1536] = 6;
    trans[24583] = 0;
    trans[5] = 0;
    trans[24662] = 0;
    trans[410467] = 3;
    trans[327680] = 5;
    trans[275253] = 5;
    trans[262150] = 4;
    trans[263680] = 1;
    trans[24582] = 0;
    trans[393317] = 0;
    trans[24581] = 0;
    trans[393303] = 0;
    trans[475958] = 3;
    trans[393312] = 0;
    trans[329216] = 7;
    trans[356358] = 5;
    trans[406388] = 4;
    trans[275301] = 5;
    trans[286720] = 4;
    trans[393223] = 0;
    trans[24576] = 0;
    trans[352256] = 0;
    trans[393221] = 0;
    trans[393222] = 0;
    trans[393216] = 0;
    trans[352262] = 0;
    trans[406372] = 3;
    trans[557320] = 2;
    trans[528520] = 2;
    trans[65544] = 4;
    trans[78856] = 7;
    trans[213128] = 1;
    trans[262152] = 4;
    trans[275464] = 5;
    trans[472344] = 0;
    trans[217480] = 1;
    trans[275736] = 7;
    trans[329496] = 0;
    trans[352280] = 0;
    trans[356376] = 7;
}

#define KNRM  "\x1B[90m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"

using namespace std;

extern int trans[];
extern const int ids;

void dbug(const char* format){
    std::cout << format;
}

template<typename T, typename... Targs>
void dbug(const char* format, T value, Targs... Fargs){
    for ( ; *format != '\0'; format++ ) {
        if ( *format == '%' ) {
            std::cout << value;
            dbug(format+1, Fargs...); // recursive call
            return;
        }
        std::cout << *format;
    }
}

//__device__ int get_state_id(int far_left, int near_left, int current, int near_right, int far_right){
//    return ((far_left<<16) + (near_left<<12) + (current<<8) + (near_right<<4) + (far_right));
//}

__global__ void FSSP_init(int *d_ptr, int squad_size){
    int id = blockDim.x * blockIdx.x + threadIdx.x;
    if(id < squad_size+4) {
        if (id == 0 || id == 1 || id == squad_size + 2 || id == squad_size + 3) {
            d_ptr[id] = 8; // 0b1000
        }
        else if (id == 2) {
            d_ptr[id] = 1;
        }
        else {
            d_ptr[id] = 0;
        }
    }
}

__global__ void get_next_state(int *d_squad, int *d_temp, int *d_trans, int n){
    int id = blockDim.x * blockIdx.x + threadIdx.x;
    if(id>=2 && id < n+2) {
        int state_id = ((d_squad[id-2]<<16) + (d_squad[id-1]<<12) + (d_squad[id]<<8) + (d_squad[id+1]<<4) + (d_squad[id+2]));
        d_temp[id] = d_trans[state_id];
    }
}

__global__ void print_the_state(int *d_squad, int *d_temp, int n, int y){
    int id = blockDim.x * blockIdx.x + threadIdx.x;


    if(id >=2 && id < n+2) {
        d_squad[id] = d_temp[id];

        if (d_squad[id] == 0)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KNRM);
        else if (d_squad[id] == 1)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KGRN);
        else if (d_squad[id] == 2)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KRED);
        else if (d_squad[id] == 3)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KYEL);
        else if (d_squad[id] == 4)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KMAG);
        else if (d_squad[id] == 5)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KBLU);
        else if (d_squad[id] == 6)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KCYN);
        else if (d_squad[id] == 7)
            printf("\033[%d;%dH%s\u2612",  y + 1, id - 1, KWHT);
        else
            printf("");

    }
    __syncthreads();
}

int main() {
    trans_init();
    int n;
    cout<<"Enter the length of the firing squad: "<<endl;
    cin>>n;

    int *d_squad;
    int *d_trans;
    int *d_temp;

    if(cudaMalloc(&d_squad,sizeof(int)* (n+4)) != cudaSuccess){
        dbug("Allocation Error | var: % | size: %. \n", "d_squad", n+4);
    }

    if(cudaMalloc(&d_trans, sizeof(int)* ids) != cudaSuccess){
        dbug("Allocation Error | var: % | size: %. \n", "d_trans", ids);
    }

    if(cudaMemcpy(d_trans, trans, sizeof(int)*ids, cudaMemcpyHostToDevice)){
        dbug("Memcopy Error | % -> % \n", "trans", "d_trans");
    }


    FSSP_init<<<1,n+4>>>(d_squad, n);

    if(cudaMalloc(&d_temp,sizeof(int)*(n+4))!= cudaSuccess){
        dbug("Allocation Error | var: % | size: %. \n", "d_temp", n+4);
    }


    //Print initial state

    for(int i=2; i<n+2; i++){
        if(i == 2){
            printf("%s\033[%d;%dH\u2612",KGRN, 1, i-1 );
        }
        else{
            printf("%s\033[%d;%dH\u2612",KWHT, 1, i-1 );
        }
    }
    cout<<endl;

    for(int i=1; i<n; i++) {
        get_next_state<<<1, n + 4>>>(d_squad, d_temp, d_trans, n);
        cudaDeviceSynchronize();

        print_the_state<<<1, n + 4>>>(d_squad, d_temp, n, i);
        cudaDeviceSynchronize();

        printf("\n");
    }


    cudaFree(d_squad);
    cudaFree(d_temp);
    cudaFree(d_trans);
    return 0;
}
