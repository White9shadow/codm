// GPC Online Library
// cod_black_ops_4__cross_over_edition_aim_assist_anti_recoil_auto_heal_amp_many_more.gpc


/*

               _____ _       _             ___                 
  /\/\  _   _  \_   \ |_ ___| |__  _   _  / __\_   _ _ __ ___  
 /    \| | | |  / /\/ __/ __| '_ \| | | |/__\// | | | '_ ` _ \ 
/ /\/\ \ |_| /\/ /_ | || (__| | | | |_| / \/  \ |_| | | | | | |
\/    \/\__, \____/  \__\___|_| |_|\__, \_____/\__,_|_| |_| |_|
        |___/                      |___/       PROUDLY PRESENTS

*******************************************************************************************************
   ____    _    _     _        ___  _____   ____  _   _ _______   __
  / ___|  / \  | |   | |      / _ \|  ___| |  _ \| | | |_   _\ \ / /
 | |     / _ \ | |   | |     | | | | |_    | | | | | | | | |  \ V / 
 | |___ / ___ \| |___| |___  | |_| |  _|   | |_| | |_| | | |   | |  
  \____/_/   \_\_____|_____|  \___/|_|     |____/ \___/  |_|   |_|  
  ____  _        _    ____ _  __   ___  ____  ____    _  _          
 | __ )| |      / \  / ___| |/ /  / _ \|  _ \/ ___|  | || |         
 |  _ \| |     / _ \| |   | ' /  | | | | |_) \___ \  | || |_        
 | |_) | |___ / ___ \ |___| . \  | |_| |  __/ ___) | |__   _|       
 |____/|_____/_/   \_\____|_|\_\  \___/|_|   |____/     |_|    
  __                _              __                  
 /   __ _  _  _    / \    _  __   |_  _| o _|_ o  _ __ 
 \__ | (_)_> _>    \_/\_/(/_ |    |__(_| |  |_ | (_)| |
 
******************************************************************************************************
 BUTTON LAYOUT            : TACTICAL & DEFAULT ARE SUPPORTED - OTHER LAYOUTS ON REQUEST                        
 BUMPERS / TRIGGERS        : DEFAULT & FLIPPED ARE SUPPORTED - OTHER CONFIGS ON REQUEST                
 STICKS                    : DEFAULT IS SUPPORTED - OTHER LAYOUTS ON REQUEST
 VERSION                : 1.9 BETA
 PLATFORM                : ALL CONSOLES
 CREDITS                : EXCALIBUR, XDOT22, LEX_HOST AND MANY OTHERS
 SUPPORT / REQUESTS        : HTTPS://TINYURL.COM/HELPGPC
 INSTRUCTIONS            : SEE LINK BELOW!!!
********************************************************************************************************
 READ THE INSTRUCTIONS BEFORE USING THE SCRIPT !! INSTRUCTIONS: https://pastebin.com/4qz5D7HN
********************************************************************************************************

//------ START USER SETTINGS AND PREFERENCES-------*/

int In_Game_Sens                 = 4;                 //ENTER VALUE OF YOUR IN-GAME SENSITIVITY SETTINGS
int Black_Out_OFF            = TRUE;                //BLACK OUT MODE OFF
int flipped                    = FALSE;            //TRIGGERS & BUMMPERS FLIPPED
int default                    = FALSE;            //DEFAULT BUTTON LAYOUT (CURRENTLY TACTICAL)
int Aim_Assist                = FALSE;             //AIM ASSIST
int easy_run                  = TRUE;                //AUTO SPRINT
int EASYMELEE                = TRUE;             //EASY_MELEE (WORKS WITH TACTICAL BTN LAYOUTS; CHANGE TO FALSE IF TACTICAL IS NOT USED)
int PS4_Compatible             = FALSE;             //ELITE CONTROLLER ON PS4? --> CHANGE "FALSE;" TO "TRUE;"
int hair_trigger            = TRUE;             //HAIRTRIGGERS
int ads_sens                 = FALSE;            //AIM CORRECTION
int AutoAim                    = FALSE;            //AUTO AIM 
int Auto_Heal                = FALSE;            //AUTO HEAL
int recoil_onoff              = FALSE;             //ANTI RECOIL (PLEASE READ TIP AND FOLLOW INSTRUCTIONS)
                                                //TIP: IN THE SCRIPT LOOK UP THE SECTION NAMED ANTI RECOIL PROFILES TO REPLACE ANTI RECOIL VALUES THAT MATCH YOUR WEAPONS OF CHOICE

//------ END USER SETTINGS AND PREFERENCES-------/

//HAVE YOU READ THE INSTRUCTIONS? PLEASE READ THEM FIRST! INSTRUCTIONS VIA LINK ABOVE

/*
********************************************************************************
SCRIPT STARTS HERE / MAKE NO CHANGES AFTER HERE UNLESS INSTRUCTED!!!
********************************************************************************
                
*/
define  FIRE_BTN               = 4; 
define  ADS_BTN                = 7; 
define  SPRINT_BTN             = 8; 
define  MELEE_BTN              = 18; 
define  JUMP_BTN               = 19;  
define  RELOAD_BTN             = 20;  
define  PRONE_BTN              = 5;  
define  SW_WEAPON_BTN          = 17;  
define  TACTICAL              = 6;  
define  LETHAL                 = 3;
define  UP                     = 13; 
define  RIGHT                  = 16; 
define  DOWN                   = 14; 
define  LEFT                   = 15; 
define  LY                     = 12;
define  LX                     = 11;
define  RY                     = 10;
define  RX                     = 9;
define  TOUCH                 = 27; 
define  SHARE                  = 1; 
define  save                  = 2;
define  reset                 = 1;
int ShotMode_KS = FALSE;
int hold_time   = 35;
int rest_time   = 35;
int KS_time= 0;
int easy_run_KS = FALSE;
//int hold1_time1;
//int rest1_time1;
//int RATE_OF_FIRE = 14; //Range: 1 to 25 RPS (Round/s)
int PrimaryWeapon   = TRUE;
int RF_KS   = FALSE;
int R2F_K2S    = TRUE;
// Aim Assist values: do not adjust them here, but change "In_Game_Sens" above!!!
//------------------------------------START AIM ASSIST VALUES-------------------------------------------------------------------------------
int valueA                 = 28;                  // Y-Axis & X-Axis AimAssist value
int delayA;     
//  int Correction_Activator   = 38;
//  int valueXP                = 36;
//  int valueXN                = -36;
//----------------------------------END AIM ASSIST VALUES-----------------------------------------------------------------------------------
//int value_XP;
//int value_XN;

//int DblClick_UP;

//int QuickScope = FALSE;
int akimbo_onoff = FALSE;
int RAPIDoff;
int ADS_SENS;      
int MIDPOINT;
int ads_sens2 = FALSE;
int Invert =  1;
int ANTI_RECOIL;               
int ANTI_RECOIL_H;              
int anti_recoil;                                      
int anti_recoil_H; 
int AR_Release;              
int profile;
int LedTime;
int record_check = 123;  //random value
int record;
//int Combo_UP;

int Col_ind;
int Blue       =  1;                                                           
int Red        =  2;                                                           
int Green      =  3;                                                           
int Pink       =  4;                                                           
int SkyBlue    =  5;                                                           
int Yellow     =  6;                                                           
int White      =  7;                                                          
//-------------------------------------------------------------------------------- 



init{                                                                                 


    record = get_pvar(SPVAR_16,0,124,100);
    if(record != record_check) {
       set_pvar(SPVAR_2,50);
       set_pvar(SPVAR_5,100);
       set_pvar(SPVAR_16,record_check);
    }
 
     MIDPOINT = get_pvar (SPVAR_2, 0, 100, 50);
     ADS_SENS = get_pvar (SPVAR_5, 0, 327, 100);
     ANTI_RECOIL   = get_pvar(SPVAR_4, -100,+100, 0);   
    ANTI_RECOIL_H = get_pvar(SPVAR_3, -100,+100, 0);  
    delayA = (3 * valueA ) / In_Game_Sens; set_val(TRACE_2, delayA); 

}
//------------------------------------------------------------------------------ 
//============================= MAIN BLOCK       =============================== 
main { // begin of main block
set_val(TRACE_1,R2F_K2S);
set_val(TRACE_2,akimbo_onoff);
set_val(TRACE_3,RF_KS);
set_val(TRACE_4,RAPIDoff);
set_val(TRACE_5,ads_sens);
set_val(TRACE_6,Aim_Assist);
//set_val(TRACE_6,profile);



//--------------------------------------------------------------
     
///////////////////////////////////////////////////////////////
///   MENU SYSTEM / HOLD ADS + ///////////////////////////////
/////////////////////////////////////////////////////////////

if(get_val(ADS_BTN)){//  hold ADS button + D pad buttons
    
////////////////////////////////
// SAVE TO EPROM

    if(event_press(save)){        // XB1 START / PS4 OPTIONS
            save_pvars();
            combo_run(STANDARD_ON)
            set_val(2, 0);      
        }
////////////////////////////////
// RESET EPROM TO DEFAULT ADS & MID POINT
        
 
    if(event_press(reset)){     // XB1 VIEW / PS4 SHARE
        MIDPOINT = 50;
        ADS_SENS = 100;
        ANTI_RECOIL = 0;               
        ANTI_RECOIL_H = 0;
        set_pvar (SPVAR_2, MIDPOINT);
        set_pvar (SPVAR_5, ADS_SENS);
        set_pvar (SPVAR_4, ANTI_RECOIL); 
        set_pvar (SPVAR_3, ANTI_RECOIL_H);         
           set_pvar (SPVAR_16,record_check);//--validation key
        set_val(1, 0);
        combo_run(STANDARD_OFF)
    }
    
////////////////////////////////
// STANDARD SET UP

    if(event_press(UP)){// D pad UP
            RF_KS  = FALSE;
            R2F_K2S  = TRUE;
            akimbo_onoff = FALSE;
            RAPIDoff = FALSE;            
        }
////////////////////////////////
// AKIMBO SET UP

    if(event_press(DOWN)) {// D pad DOWN  
            RF_KS  = FALSE;
            R2F_K2S  = FALSE;
            akimbo_onoff = TRUE; 
              RAPIDoff = FALSE;
        }                                      
////////////////////////////////
// RAPID FIRE SET UP

    if(event_press(RIGHT)) {// D pad RIGHT
            RF_KS  = TRUE;
            R2F_K2S  = TRUE;
            akimbo_onoff = FALSE;
            RAPIDoff = FALSE;
        }
////////////////////////////////
// RAPID FIRE OFF

    if(event_press(LEFT)) {// D pad LEFT
            RF_KS  = FALSE;
            R2F_K2S  = FALSE;
            akimbo_onoff = FALSE;
            RAPIDoff = TRUE;
        }
////////////////////////////////
// STOP CONTROLLER INPUT

//    if(event_press(0)){ 
//            Combo_UP = !Combo_UP;
//                  if(Combo_UP == TRUE){combo_run(STANDARD_ON)}
//                 if(Combo_UP == FALSE){combo_run(STANDARD_OFF)}    
//                set_val(0,0);
}

///////////////////////////////////////////////////////////////
///   MENU SYSTEM / HOLD DOWN + ///////////////////////////////
/////////////////////////////////////////////////////////////

if(get_val(DOWN)){                                    //  hold D pad button DOWN +
    

////////////////////////////////
// EASY DROP

    if (event_press(PRONE_BTN))  {                     // PRONE 
            ShotMode_KS = !ShotMode_KS;  
        }
        
///////////////////////////////
// ADS SENS
    if(event_press(FIRE_BTN)){                        // FIRE BUTTON
            ads_sens = !ads_sens;// ads_sens2 = !ads_sens2 
        }
///////////////////////////////
// ADS ASSIST        
        
    if(event_press(ADS_BTN)){                        //ADS BUTTON
        Aim_Assist = !Aim_Assist;       
        }
        
////////////////////////////////
// EASY MELEE

    if (event_press(MELEE_BTN))  {                     // MELEE 
            EASYMELEE = !EASYMELEE; 
        }
////////////////////////////////
// EASY SPRINT

    if (event_press(SPRINT_BTN))  {                 // SPRINT
            easy_run = !easy_run;  
        }
        
////////////////////////////////
// SECONDARY WEAPON

    if (event_press(SW_WEAPON_BTN))  {                 // SW_WEAPON_BTN
            Black_Out_OFF = !Black_Out_OFF;  
        }
////////////////////////////////
// AUTO_AIM

    if (event_press(TACTICAL))  {                     // TACTICAL
            AutoAim =! AutoAim;
        }

        }
///////////////////////////////////////////////////////////////
///   MIDPOINT / ADS SENS ON THE FLY /// HOLD JUMP_BTN + /////
/////////////////////////////////////////////////////////////

 if(get_val(JUMP_BTN)){ //      hold JUMP button +    
 
        if(event_press(RIGHT)){                                    
            MIDPOINT = MIDPOINT + 2;        // RIGHT                  
        }                                                        
        if(event_press(LEFT)) {                                   
            MIDPOINT = MIDPOINT - 2;        // LEFT                         
        }                                                         
       set_val(RIGHT,0); set_val(LEFT,0);                         
                                                                 
        if(event_press(UP)){                                   
            ADS_SENS = ADS_SENS + 2;        // UP          
        }                                                       
        if(event_press(DOWN)){                                   
            ADS_SENS = ADS_SENS - 2;        // DOWN                 
        }    
        set_val(UP,0); set_val(DOWN,0);                       
                                                             
 }
///////////////////////////////////////////////////////////////////
// ANTI RECOIL PROFILES ///////// ///ANIT RECOIL PROFILES ////////
/////////////////////////////////////////////////////////////////  
                          
if (get_val(RELOAD_BTN)){         
 
/*REPLACE CURRENT ANTI_RECOIL & ANTI_RECOIL_H VALUES WITH ANTI RECOIL VALUES THAT MATCH YOUR WEAPONS OF CHOICE
------------/
// CHANGE VALUES ANTI RECOIL IN BOTH LINES BELOW -------------------------------------*/
    if(event_press(UP))       {recoil_onoff = TRUE; ANTI_RECOIL = 30; ANTI_RECOIL_H = 0; profile = 1; LedTime= 100; AR_Release = ANTI_RECOIL + 1;}  //  ANTI_RECOIL = 30; ANTI_RECOIL_H = 0
    if(event_press(RIGHT))     {recoil_onoff = TRUE; ANTI_RECOIL = 34; ANTI_RECOIL_H = -20; profile = 2; LedTime= 300; AR_Release = ANTI_RECOIL + 1;} // ANTI_RECOIL = 34; ANTI_RECOIL_H = -20

/* DO NOT CHANGE PROFILE VALUES AFTER HERE !!!-----------------------------------------*/
    if(event_press(DOWN))      {recoil_onoff = TRUE; set_pvar(SPVAR_4,  ANTI_RECOIL); set_pvar(SPVAR_3,  ANTI_RECOIL_H); profile = 3; LedTime= 500; AR_Release = ANTI_RECOIL + 1;} // ON THE FLY (START VALUES ARE THE SAME AS LAST USED PROFILE)
    if(event_press(LEFT))     {recoil_onoff = FALSE; profile = 4; } // AR OFF

///////////////////////////////////////////////////////////////////
//RELOAD TIMES /////////HOLD X + /////////////////RELOAD TIMES////
/////////////////////////////////////////////////////////////////  
}                         
if (get_val(reset)){
//
    if(event_press(DOWN))  {KS_time= 0; easy_run_KS = FALSE;}//            
    if(event_press(RIGHT)) {KS_time= 2000;}// RIGHT: 2000  
//     if(event_press(LEFT))  {KS_time= 1500;}// DOWN    : 1500  
//    if(event_press(UP))    {KS_time= 5000;}// UP    : 5000 
        
///////////////////////////////////////////////////////////////////
////////////////// KILL SWITCH EASY RUN + other KILL SWITCHES ////
/////////////////////////////////////////////////////////////////  

}else {

    if (event_press (LEFT) && !get_val (ADS_BTN)) combo_run(SwitchOFF);}
//    if (event_press (ADS_BTN)) {combo_stop(STOP_SPRINT) easy_run_KS =FALSE;}
//    if (event_press (FIRE_BTN)) {combo_stop(STOP_SPRINT) easy_run_KS =FALSE;}
    if (get_val (FIRE_BTN)) {combo_stop(STOP_SPRINT) easy_run_KS =FALSE;} 
    if (get_val (ADS_BTN)) {combo_stop(STOP_SPRINT) easy_run_KS =FALSE;} 

///////////////////////////////////////////////////////////////////
////////////////// ON THE FLY ANTI RECOIL HOLD B + ///////////////
/////////////////////////////////////////////////////////////////  

  
   if(get_val(XB1_B)){                                              
        if(event_press(XB1_UP)){                                    
            ANTI_RECOIL = ANTI_RECOIL + 1;                       
        }                                                        
        if(event_press(XB1_DOWN)) {                                   
            ANTI_RECOIL = ANTI_RECOIL - 1;                         
        }                                                         
        set_val(XB1_UP,0); set_val(XB1_DOWN,0);                          
                                                                 
        if(event_press(XB1_RIGHT)){                                   
            ANTI_RECOIL_H = ANTI_RECOIL_H + 1;                   
        }                                                       
        if(event_press(XB1_LEFT)) {                                
            ANTI_RECOIL_H = ANTI_RECOIL_H - 1;                   
        }    
        set_val(XB1_RIGHT,0); set_val(XB1_LEFT,0);                       
          }
    //------------------------------------------------
    //------------------------------------------------ 
    // ANTI RECOIL 
  if(recoil_onoff) { 
    if(get_val(ADS_BTN) && get_val(FIRE_BTN )) { 
        combo_run(AntiRecoil);                     
    }                                                 
 
    if( abs(get_val(RY)) > AR_Release || abs(get_val(RX)) > AR_Release) {
        combo_stop (AntiRecoil);                       
    }  
   }
///////////////////////////////////////////////////////////////////
///////////////////////////////////// FLIP BUMPERS <-> TRIGGERS///
/////////////////////////////////////////////////////////////////  

    if(flipped) {
        swap( 7, 6 );
        swap( 4, 3 );
        }
///////////////////////////////////////////////////////////////////
///////////////////////////////////// DEFAULT ////////////////////
/////////////////////////////////////////////////////////////////  

    if(default) {
        swap( 5, 18 );
        }
///////////////////////////////////////////////////////////////////
//////////////////////////////////////////////// HAIR TRIGGERS ///
/////////////////////////////////////////////////////////////////  

    if(hair_trigger) {
        if(get_val(FIRE_BTN)){set_val(FIRE_BTN,100);}
        if(get_val(ADS_BTN)){set_val(ADS_BTN,100);} 
        }   
   
///////////////////////////////////////////////////////////////////
///////////////////////////////////////////// EASY SLIDE ///////// 
/////////////////////////////////////////////////////////////////  

    if(!ShotMode_KS){                                                      
        if(get_val(PRONE_BTN)) combo_run(DROP_SHOT);                    
        }   
        
///////////////////////////////////////////////////////////////////
/////////////////////////////////////////////// AUTO AIM ///////// 
/////////////////////////////////////////////////////////////////  
    if(AutoAim){
           if(get_val(FIRE_BTN)) {set_val(ADS_BTN,100);} 
      }     
    
        
///////////////////////////////////////////////////////////////////
//  AKIMBO    ////////////////////////////////////AKIMBO//////////
/////////////////////////////////////////////////////////////////  

    if(akimbo_onoff && !PrimaryWeapon) {
        if(get_val(FIRE_BTN) && !get_val(ADS_BTN)){combo_run (RAPID_AKIMBO);
        }
//        if(get_val(ADS_BTN) && !get_val(FIRE_BTN)){combo_run (RAPID_AKIMBO);
//        } 
    }
        if(akimbo_onoff && !Black_Out_OFF) {
        if(get_val(FIRE_BTN) && !get_val(ADS_BTN)){combo_run (RAPID_AKIMBO);
        }
//        if(get_val(ADS_BTN) && !get_val(FIRE_BTN)){combo_run (RAPID_AKIMBO);
//        } 
    }
    
 
///////////////////////////////////////////////////////////////////
//  EASY MELEE    ////////////////////////////////////EASYMELEE///
/////////////////////////////////////////////////////////////////        
                
    if (EASYMELEE)    {
        if (get_val(SPRINT_BTN)) set_val(MELEE_BTN, 100)
        }           
///////////////////////////////////////////////////////////////////
//  Combo_UP   ////////////////////////////////////Combo_UP //////
/////////////////////////////////////////////////////////////////        
                
//    if (Combo_UP)    {
//        combo_run (ComboUP);
        
//        }
//    if (!Combo_UP)    {
//        combo_stop (ComboUP); 
//        }
///////////////////////////////////////////////////////////////////
//EASY RUN  //////////////////////////////////////EASY RUN////////
/////////////////////////////////////////////////////////////////  
                        
    if(easy_run && !easy_run_KS){                               
        if(get_val(LY) < -5) combo_run(EASY_RUN); 
        }
        if(event_release(RELOAD_BTN) && get_ptime(RELOAD_BTN)< 200){combo_run(STOP_SPRINT);}
        
//////////////////////////////////////////////////////////////////////////
////////////   AUTO HEAL     /////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
    if (Auto_Heal){ 
    if(event_release(RELOAD_BTN) && get_ptime(RELOAD_BTN)< 200){combo_run(AUTO_HEAL);  
        }
     }
///////////////////////////////////////////////////////////////////
// LED COLOURS  /////////////////////////// LED COLOURS //////////
///////////////////////////////////////////////////////////////// 

     
    if(PrimaryWeapon) colourled (Blue); 
    if (!PrimaryWeapon && R2F_K2S) colourled (Red);
    if(PrimaryWeapon && RF_KS) colourled (White);
    if(akimbo_onoff && !PrimaryWeapon) colourled(SkyBlue);
    if(akimbo_onoff && !Black_Out_OFF) colourled(SkyBlue);
    if(Aim_Assist && get_val (ADS_BTN)) colourled(Pink);
    if(ads_sens && get_val (FIRE_BTN)) colourled(Pink);
    if(recoil_onoff)combo_run(BLINK3);
          
          
/////////////////////////////////////////////////////////////////////
////////////////////////////////////////// SWITCH WEAPON ///////////
/////////////////////////////////////////////////////////////////// 
if (Black_Out_OFF){ 
    if(event_press(SW_WEAPON_BTN)){                         
        PrimaryWeapon = !PrimaryWeapon;
        }
         }
/////////////////////////////////////////////////////////////////////
/////////////////////////////////// RAPID FIRE 1 ///////////////////
/////////////////////////////////////////////////////////////////// 
 
    if (PrimaryWeapon && RF_KS && get_val(FIRE_BTN))combo_run (RAPID_FIRE);   
        
        

  
//////////////////////////////////////////////////////////////////////
////////////////////////////////////////// RAPID FIRE 2 /////////////
////////////////////////////////////////////////////////////////////   
 
    if(!PrimaryWeapon && R2F_K2S)                     
        if(get_val(FIRE_BTN)) {                                    
        combo_run (RAPID_FIRE);
        }  
        
//////////////////////////////////////////////////////////////////////
////////////////////////////////////////// RESET ////////////////////
////////////////////////////////////////////////////////////////////  

// reset script when you die                             
    if(get_val(RELOAD_BTN) && get_ptime(RELOAD_BTN)> 200){combo_run (STANDARD_ON); PrimaryWeapon = TRUE; }
    
    //////////////////////////////
////////////////////////////////////////// PS4 Compatible ///////////
////////////////////////////////////////////////////////////////////  
    
    if(PS4_Compatible){       
            // XBOX ELITE Paddle Left down PL2             
            if(get_val(PS4_TOUCH)) set_val(PS4_TOUCH,0);  
                                                          
          if(get_val(PS4_SHARE)) {                        
                if(!get_val(PS4_R3)) {                      
                          set_val(PS4_TOUCH, 100);              
                          set_val(PS4_SHARE, 0);          
                  }                           
                set_val(PS4_R3, 0);     
          }
          }  

//////////////////////////////////////////////////////////////////////
////////////////////////////////////////// AIM ASSIST ///////////////
////////////////////////////////////////////////////////////////////  
   
if(Aim_Assist){
   if(get_val(ADS_BTN)){
      combo_run(ASSY);
      combo_run(ASSX);                 
      if(ads_sens) sensitivity(9, MIDPOINT, ADS_SENS); sensitivity(10, MIDPOINT, ADS_SENS);
         }      
         if((get_val(RY)) > valueA || (get_val(RY)) < valueA*(-1)){
             combo_stop(ASSY);
            }
         if((get_val(RX)) > valueA || (get_val(RX)) < valueA*(-1)){
             combo_stop(ASSX);
            }  
 //     if(ads_sens2){      
 //        if(get_val(ADS_BTN) && get_val(LX) < Correction_Activator*(-1)){
   //         combo_run(Correction_right);
   //         combo_stop(ASSX);
   //         }
   //      if(get_val(ADS_BTN) && get_val(LX) > Correction_Activator){
   //         combo_run(Correction_left); 
   //         combo_stop(ASSX);
   //         }         
   //      if(abs (get_val(RX)) > valueXP || get_val(RX) < valueXN ){
   //         combo_stop(Correction_left);
   //         combo_stop(Correction_right);
    //        }
         }   
         }   


//------------------------------------------------------------------------------
//    end of main block     
//------------------------------------------------------------------------------


//------------------------------------------------------------------------------
//    COMBO BLOCKS                                                               
//------------------------------------------------------------------------------


//combo Correction_right {
//   set_val(RX, valueXP);
//    wait(1);
//   set_val(RX, valueXP);
//} 

//combo Correction_left {
//     set_val(RX, valueXN);
//     wait(1);
//     set_val(RX, valueXN);
//} 

combo ASSY {
     wait(delayA);
     set_val(RY, valueA);
     wait(delayA);
     set_val(RY, valueA*(-1));
     wait(delayA);
}

combo ASSX {   
     wait(delayA/1.5);
     set_val(RX, valueA);
     wait(delayA/1.5);
     set_val(RX, valueA*(-1));
     wait(delayA/1.5);
}  

//combo ComboUP    {
//    set_val (0,0); set_val (1,0); set_val (2,0); set_val (3,0); set_val (4,0);
//    set_val (5,0); set_val (6,0); set_val (7,0): set_val (8,0); set_val (9,0);
//    set_val (10,0); set_val (11,0); set_val (12,0); set_val (13,0); set_val (14,0);
//    set_val (15,0); set_val (16,0); set_val (17,0); set_val (18,0); set_val (19,0);
//}    

combo STOP_SPRINT {     
  easy_run_KS = TRUE;  
     wait(KS_time);
  easy_run_KS = FALSE; 
//    combo_run (STANDARD_OFF);
}        

combo RAPID_FIRE {  
    set_val(FIRE_BTN,100);
    wait(hold_time);       
    set_val(FIRE_BTN,  0); 
    wait(rest_time);      
}  
          
combo BLINK3{
    colourled(Green)
        wait (LedTime)             
    if(PrimaryWeapon) colourled (Blue); 
    if (!PrimaryWeapon && R2F_K2S) colourled (Red);
    if(PrimaryWeapon && RF_KS) colourled (White);
    if(akimbo_onoff && !PrimaryWeapon) colourled(SkyBlue);
    if(akimbo_onoff && !Black_Out_OFF) colourled(SkyBlue);
    if(Aim_Assist && get_val (ADS_BTN)) colourled(Pink);
    if(ads_sens && get_val (FIRE_BTN)) colourled(Pink);
    if(recoil_onoff)combo_run(BLINK3);
          wait (900)
}

combo SwitchOFF {  
//   set_rumble(RUMBLE_A,100);
//    wait(200);
//    reset_rumble();
    ShotMode_KS = TRUE;    
    wait(30000);
    combo_run (STANDARD_OFF);
    ShotMode_KS = FALSE;
 }

combo DROP_SHOT{    
    set_val(PRONE_BTN,100); 
    wait(500);  
} 

combo AUTO_HEAL {    
    wait(1500); 
    set_val(TACTICAL,100);
//  combo_run (STANDARD_ON);
    wait(100);      
}
 
combo RAPID_AKIMBO {      
   set_val(FIRE_BTN,100); 
   set_val( ADS_BTN,100); 
   wait(hold_time);      
   set_val( ADS_BTN,0);   
   set_val(FIRE_BTN,0);   
   wait(rest_time);      
}
combo EASY_RUN {                  
    set_val(SPRINT_BTN,100);       
    wait(30);                     
    wait(100);                   
}  

combo STANDARD_ON {
   set_rumble(RUMBLE_A,100);
   wait(250);
   reset_rumble();
   wait(2000);
}

combo STANDARD_OFF {
   set_rumble(RUMBLE_B,100);
// set_val (0,0);
   wait(250);
   reset_rumble();
   wait(2000);
}



combo AntiRecoil {                     
    if(recoil_onoff) {                   
        anti_recoil = get_val(RY) + (ANTI_RECOIL * Invert); 
        if(anti_recoil > 100) anti_recoil = 100;
        set_val(10, anti_recoil);                
        anti_recoil_H = get_val(RX) + ANTI_RECOIL_H; 
        if(anti_recoil_H > 100) anti_recoil_H = 100; 
        set_val(9, anti_recoil_H);                 
    }                                          
}    
// COLOR LED function                                  


function colourled(Colour) {          
    Col_ind=(Colour*4)- 3;            
    set_led(LED_1,dbyte(Col_ind  ));  
    set_led(LED_2,dbyte(Col_ind+ 1)); 
    set_led(LED_3,dbyte(Col_ind+ 2)); 
    set_led(LED_4,dbyte(Col_ind+ 3)); 
}// End

function save_pvars(){
set_pvar(SPVAR_2, MIDPOINT);
set_pvar(SPVAR_5, ADS_SENS);
set_pvar(SPVAR_4, ANTI_RECOIL);                          
set_pvar(SPVAR_3, ANTI_RECOIL_H);  
set_pvar(SPVAR_16,record_check); //--validation key
}

