@Subroutine
def PreInit():
    CharacterID('ta')

@Subroutine
def MatchInit():
    Health(200000)
    ComboRate(70)
    HeatGainFactor(20)
    NegativePenaltyResistance(2)
    Unknown12054(0, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 540, 600)
    FootstepType(2)
    FootstepSE(0)
    TakemikazuchiIntroFlag()
    Move_Register('Atk_Punch', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Atk_Punch')
    MovePriority(1000)
    Move_EndRegister()
    Move_Register('Atk_Shot', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(INPUT_PRESS_B)
    CallFunction('Func_Atk_Shot')
    MovePriority(1000)
    Move_EndRegister()
    Move_Register('Atk_Land', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(INPUT_PRESS_C)
    CallFunction('Func_Atk_Land')
    MovePriority(1000)
    Move_EndRegister()
    Move_Register('Atk_Rain', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Atk_Rain')
    MovePriority(500)
    Move_EndRegister()
    Move_Register('Atk_Rain_R', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Atk_Rain_R')
    MovePriority(500)
    Move_EndRegister()
    Move_Register('Atk_Eat', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_C)
    CallFunction('Func_Atk_Eat')
    MovePriority(1000)
    Move_EndRegister()
    Move_Register('Atk_Quake', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x44)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Atk_Quake')
    MovePriority(1000)
    Move_EndRegister()
    Move_Register('Atk_Thunder', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(INPUT_PRESS_D)
    CallFunction('Func_Atk_Thunder')
    MovePriority(1000)
    Move_EndRegister()
    Move_Register('Atk_Move', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x44)
    Move_Input_(INPUT_PRESS_B)
    CallFunction('Func_Atk_Move')
    MovePriority(500)
    Move_EndRegister()
    Move_Register('Atk_MK_Funnel', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x92)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    Move_Condition(0x302f)
    CallFunction('Func_Atk_MK_Funnel')
    MovePriority(10000)
    Move_EndRegister()
    Move_Register('Atk_MK_Ball', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    IndependentInput(1, 0, 0)
    Move_Input_(0x78)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x302e)
    CallFunction('Func_Atk_MK_Ball')
    MovePriority(10000)
    Move_EndRegister()
    Move_Register('Atk_Sp_Beam', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    Move_Condition(0x2003)
    IndependentInput(1, 0, 0)
    Move_Input_(0x92)
    Move_Input_(INPUT_PRESS_A)
    CallFunction('Func_Atk_Sp_Beam')
    MovePriority(20000)
    Move_EndRegister()
    Move_Register('Atk_Sp_Laser', 0x1)
    CallSkillConditions('CheckTakemiAtkSpLaser')
    Move_Condition(0x2003)
    IndependentInput(1, 0, 0)
    Move_Input_(0x92)
    Move_Input_(INPUT_PRESS_B)
    CallFunction('Func_Atk_Sp_Laser')
    MovePriority(20000)
    Move_EndRegister()
    Move_Register('Atk_AstralHeat', 0x1)
    CallSkillConditions('CheckTakemiAtk')
    Move_Condition(0x304a)
    IndependentInput(1, 0, 0)
    Move_Input_(0x92)
    Move_Input_(INPUT_PRESS_D)
    CallFunction('Func_Atk_AstralHeat')
    MovePriority(20000)
    Move_EndRegister()
    Move_Register('OverDrive', 0x1)
    CallSkillConditions('CheckTakemiOverDrive')
    IndependentInput(1, 0, 0)
    Move_Input_(0xfd)
    CallFunction('Func_OverDrive')
    MovePriority(1000000)
    Move_EndRegister()
    ResourceGauge(0, 0, 1, 1, 1800, 0, -6291456, -192)
    ResourceGauge(1, 0, 1, 1, 1800, 1800, -6291456, -192)
    CreateObject('MikadoCreate', -1)
    RegisterObject(11, 1)

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_21:
            SLOT_31 = (SLOT_31 + 1)
            if (SLOT_31 >= 1800):
                SLOT_31 = 1800
            SLOT_32 = (SLOT_32 + 1)
            if (SLOT_32 >= 1800):
                SLOT_32 = 1800
        else:
            PassbackAddActionMarkToFunction('EffAtkBall', 32)
            PassbackAddActionMarkToFunction('EffAtkFunnel', 32)

@Subroutine
def DefSetting():
    ExternalForcesRate(0, 0)
    PreventBlocking(1)
    setInvincible(1)
    EnableCollision(0)
    ScreenCollision(0)
    WallCollisionDetection(0)
    Visibility(1)
    NoDamageAction(1)
    SetActionMark(481)

@State
def CmnActStand():

    def upon_IMMEDIATE():
        callSubroutine('DefSetting')
    sprite('null', 32767)
    loopRest()

@Subroutine
def CheckTakemiAtk():
    SLOT_47 = 0
    if (SLOT_4 == 0):
        if (SLOT_5 == 0):
            SLOT_47 = 1

@Subroutine
def CheckTakemiAtkSpLaser():
    SLOT_47 = 0
    if (SLOT_4 == 0):
        if (SLOT_5 == 0):
            if (SLOT_7 == 1):
                SLOT_47 = 1

@Subroutine
def CheckTakemiOverDrive():
    SLOT_47 = 0
    if (SLOT_4 == 0):
        if (SLOT_5 == 0):
            if (SLOT_6 == 1):
                SLOT_47 = 1
            if (SLOT_6 == 3):
                SLOT_47 = 1

@Subroutine
def Func_Atk_Punch():
    ObjectUpon2(11, 101, 0)

@Subroutine
def Func_Atk_Shot():
    ObjectUpon2(11, 102, 0)

@Subroutine
def Func_Atk_Land():
    ObjectUpon2(11, 103, 0)

@Subroutine
def Func_Atk_Rain():
    ObjectUpon2(11, 104, 0)

@Subroutine
def Func_Atk_Rain_R():
    ObjectUpon2(11, 105, 0)

@Subroutine
def Func_Atk_Eat():
    ObjectUpon2(11, 106, 0)

@Subroutine
def Func_Atk_Quake():
    ObjectUpon2(11, 107, 0)

@Subroutine
def Func_Atk_Move():
    ObjectUpon2(11, 108, 0)

@Subroutine
def Func_Atk_Thunder():
    ObjectUpon2(11, 109, 0)

@Subroutine
def Func_Atk_MK_Funnel():
    SLOT_32 = 0
    ObjectUpon2(11, 200, 0)

@Subroutine
def Func_Atk_MK_Ball():
    SLOT_31 = 0
    ObjectUpon2(11, 201, 0)

@Subroutine
def Func_Atk_Sp_Beam():
    SLOT_7 = 1
    ObjectUpon2(11, 301, 0)

@Subroutine
def Func_Atk_Sp_Laser():
    SLOT_7 = 0
    ObjectUpon2(11, 302, 0)

@Subroutine
def Func_Atk_AstralHeat():
    ObjectUpon2(11, 400, 0)

@Subroutine
def Func_OverDrive():
    ObjectUpon2(11, 600, 0)

@Subroutine
def MouthTableInit():
    Unknown18011('rg502', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 12643, 24884, 25399, 24887, 25399, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():

    def upon_IMMEDIATE():
        callSubroutine('DefSetting')
    sprite('null', 480)
    ObjectUpon2(11, 800, 0)
    DemoTimer(480)
    loopRest()
    sprite('keep', 100)
    enterState('CmnActStand')

@State
def CmnActRoundWin():

    def upon_IMMEDIATE():
        callSubroutine('DefSetting')
    sprite('null', 32767)
    ObjectUpon2(11, 810, 0)
    DemoTimer(240)

@State
def CmnActMatchWin():

    def upon_IMMEDIATE():
        callSubroutine('DefSetting')
    sprite('null', 32767)
    ObjectUpon2(11, 810, 0)
    DemoTimer(300)

@State
def CmnActLose():

    def upon_IMMEDIATE():
        callSubroutine('DefSetting')
    sprite('null', 32767)
    ObjectUpon2(11, 820, 0)
    DemoTimer(90)