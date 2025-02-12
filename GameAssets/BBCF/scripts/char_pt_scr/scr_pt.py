@Subroutine
def PreInit():
    CharacterID('pt')
    EnableDashBuffer(1)


@Subroutine
def ChainLandDrive():
    SetActionMark(0)
    HitOrBlockCancel('NmlAtk5D')
    HitOrBlockCancel('NmlAtk5D_Hanmmer')
    HitOrBlockCancel('NmlAtk5D_Cat')
    HitOrBlockCancel('NmlAtk5D_Harisen')
    HitOrBlockCancel('NmlAtk5D_Bat')
    HitOrBlockCancel('NmlAtk5D_Bomb')
    HitOrBlockCancel('NmlAtk5D_Missaile')
    HitOrBlockCancel('NmlAtk5D_Box')
    HitOrBlockCancel('NmlAtk5D_Boomerang')


@Subroutine
def ChainAirDrive():
    SetActionMark(0)
    HitOrBlockCancel('NmlAtkAIR5D')
    HitOrBlockCancel('NmlAtkAIR5D_Hanmmer')
    HitOrBlockCancel('NmlAtkAIR5D_Cat')
    HitOrBlockCancel('NmlAtkAIR5D_Harisen')
    HitOrBlockCancel('NmlAtkAIR5D_Bat')
    HitOrBlockCancel('NmlAtkAIR5D_Bomb')
    HitOrBlockCancel('NmlAtkAIR5D_Missaile')
    HitOrBlockCancel('NmlAtkAIR5D_Box')
    HitOrBlockCancel('NmlAtkAIR5D_Boomerang')


@Subroutine
def TrapUpDate():
    if CheckObjectPresence(6):
        if not CheckObjectPresence(5):
            RegisterObject(5, 6)
        else:
            ObjectUpon(6, 32)
    if CheckObjectPresence(5):
        RegisterObject(6, 5)
    CreateObject('Trap', 0)
    RegisterObject(5, 1)


@Subroutine
def SpTrapUpDate():
    if CheckObjectPresence(6):
        if not CheckObjectPresence(5):
            RegisterObject(5, 6)
        else:
            ObjectUpon(6, 32)
    if CheckObjectPresence(5):
        RegisterObject(6, 5)
    CreateObject('SpTrap', 0)
    RegisterObject(5, 1)


@Subroutine
def BombThrowCtrl():
    if CheckInput(0x6c):
        ObjectUpon(FALLING, 35)
    if CheckInput(0x5f):
        ObjectUpon(FALLING, 36)
    if CheckInput(0x79):
        ObjectUpon(FALLING, 37)


@Subroutine
def OnActionBegin():
    SLOT_59 = SLOT_4
    CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)


@Subroutine
def MatchInit():
    Health(11000)
    WalkFSpeed(6200)
    WalkBSpeed(4800)
    DashFInitialVelocity(17000)
    DashFAccel(440)
    DashFMaxVelocity(28000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(41000)
    Gravity(1850)
    AirDashFSpeed(26000)
    AirFDashDuration(30)
    AirDashBSpeed(22000)
    AirBDashDuration(24)
    HeatGainFactor(20)
    ComboRate(60)
    NegativePenaltyResistance(4)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 220000, -100000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMaxChainRepeat(2)
    DamageStunPriority(1)
    MoveComboPriority(1)
    AirborneOpponentPriority(5000)
    SkillEstimateRange(0, 450000, 0, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    MoveLow()
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    DamageStunPriority(1)
    SkillEstimateRange(250000, 500000, -100000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    MoveMid()
    SkillEstimateRange(0, 350000, -100000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    SkillEstimateRange(100000, 350000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    SkillEstimateRange(0, 350000, -200000, 150000, 1000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    MoveComboPriority(1)
    DamageStunPriority(10000)
    SkillEstimateRange(0, 250000, -200000, 0, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    DamageStunPriority(1)
    MoveComboPriority(1)
    AirborneOpponentPriority(3000)
    MoveCancellableFrames(30, 35)
    SkillEstimateRange(-50000, 200000, 100000, 550000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(1)
    SkillEstimateRange(200000, 500000, 100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    MoveMid()
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', INPUT_J5A)
    FollowupOnly(1)
    MoveMid()
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A3rd', INPUT_J5A)
    FollowupOnly(1)
    MoveMid()
    OpponentAttackPriority(5000)
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    MoveMid()
    SkillEstimateRange(-100000, 200000, -350000, 0, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    MoveMid()
    SkillEstimateRange(50000, 400000, -150000, 250000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2C', INPUT_J2C)
    MoveMid()
    SkillEstimateRange(-100000, 250000, -400000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', 0x1)
    Move_Condition(0x2000)
    Move_Condition(0x3024)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(300000, 800000, -200000, 500000, 15000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    Move_Condition(0x3024)
    SkillEstimateRange(300000, 800000, -500000, 500000, 15000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Hanmmer', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateHanmmer')
    MoveMaxChainRepeat(3)
    GuardStunPriority(10000)
    SkillEstimateRange(50000, 250000, -200000, 100000, 2500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Hanmmer', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateHanmmer')
    SharedGatling('NmlAtk5D_Hanmmer')
    GuardStunPriority(10000)
    SkillEstimateRange(-150000, 150000, -600000, -100000, 20000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Cat', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateCat')
    MoveMaxChainRepeat(3)
    MovePriority(10000)
    DamageStunPriority(1)
    SkillEstimateRange(200000, 600000, -200000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Cat', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateCat')
    MoveMaxChainRepeat(3)
    MovePriority(10000)
    DamageStunPriority(1)
    SkillEstimateRange(200000, 600000, -300000, 200000, 5000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Harisen', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateHarisen')
    MoveMaxChainRepeat(3)
    DamageStunPriority(4000)
    SkillEstimateRange(50000, 250000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Harisen', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateHarisen')
    MoveMaxChainRepeat(3)
    DamageStunPriority(4000)
    SkillEstimateRange(50000, 300000, -300000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Bat', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBat')
    MoveMaxChainRepeat(3)
    OpponentAttackPriority(4000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-50000, 350000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Bat', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBat')
    MoveMaxChainRepeat(3)
    OpponentAttackPriority(4000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-50000, 350000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Bomb', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBomb')
    MoveMaxChainRepeat(3)
    MovePriority(5000)
    SkillEstimateRange(550000, 950000, -200000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Bomb', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBomb')
    MoveMaxChainRepeat(3)
    MovePriority(5000)
    SkillEstimateRange(550000, 1150000, -400000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Missaile', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateMissaile')
    MoveMaxChainRepeat(3)
    MovePriority(5000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(700000, 1300000, -200000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Missaile', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateMissaile')
    MoveMaxChainRepeat(3)
    MovePriority(5000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(700000, 1300000, -400000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Box', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBox')
    MoveMaxChainRepeat(3)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(50000, 500000, -200000, 100000, 250, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Box', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBox')
    MoveMaxChainRepeat(3)
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(50000, 500000, -200000, 100000, 500, 1000)
    Move_EndRegister()
    Move_Register('NmlAtk5D_Boomerang', 0x1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBoomerang')
    MoveMaxChainRepeat(3)
    MovePriority(5000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(700000, 1300000, -200000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D_Boomerang', 0x1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_D)
    CallSkillConditions('CheckActivateBoomerang')
    MoveMaxChainRepeat(3)
    MovePriority(5000)
    JumpAvoidPriority(10000)
    SkillEstimateRange(700000, 1300000, -200000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x600)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x604)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(0, 200000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAirThrow', 0x601)
    MoveThrow()
    DamageStunPriority(1)
    SkillEstimateRange(100000, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('WeaponThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Condition(0x3000)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(INPUT_214)
    TempPriorityMultiplierInterval(0, 1, 2, 1000, 0)
    Move_EndRegister()
    Move_Register('WeaponThrow_Bomb', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(INPUT_214)
    CallSkillConditions('CheckActivateBomb')
    MovePriority(3000)
    SkillEstimateRange(400000, 900000, -200000, 600000, 3000, 1)
    Move_EndRegister()
    Move_Register('WeaponThrow_Missaile', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(INPUT_214)
    CallSkillConditions('CheckActivateMissaile')
    MovePriority(1)
    Move_EndRegister()
    Move_Register('WeaponThrow_Box', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_D)
    Move_Input_(INPUT_214)
    CallSkillConditions('CheckActivateBox')
    DamageStunPriority(1)
    GuardStunPriority(2000)
    SkillEstimateRange(400000, 900000, -200000, 200000, 1000, 500)
    Move_EndRegister()
    Move_Register('Oiuchi', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x307f)
    MovePriority(1)
    Move_EndRegister()
    Move_Register('Shabon_A', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    SkillEstimateRange(800000, 1500000, -200000, 500000, 2000, 1)
    Move_EndRegister()
    Move_Register('Shabon_B', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    GuardStunPriority(5000)
    SkillEstimateRange(400000, 700000, -250000, 0, 500, 1)
    Move_EndRegister()
    Move_Register('Shabon_C', INPUT_SPECIALMOVE)
    Move_Condition(0x300b)
    Move_Condition(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    SkillEstimateRange(800000, 1500000, -200000, 500000, 2000, 1)
    Move_EndRegister()
    Move_Register('Hopping', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    MovePriority(1)
    AirborneOpponentPriority(2500)
    SkillEstimateRange(50000, 300000, -250000, 50000, 1000, 0)
    Move_EndRegister()
    Move_Register('HoppingPlus_A', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Move_Condition(0x3036)
    MovePriority(1)
    SkillEstimateRange(50000, 300000, -300000, 100000, 20000, 50)
    Move_EndRegister()
    Move_Register('HoppingPlus_B', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x3036)
    MovePriority(1)
    SkillEstimateRange(-150000, 150000, -300000, -50000, 10000, 50)
    Move_EndRegister()
    Move_Register('HoppingPlus_C', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3036)
    MovePriority(1)
    SkillEstimateRange(-200000, 50000, -300000, -50000, 10000, 50)
    Move_EndRegister()
    Move_Register('AirHopping', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    MovePriority(1)
    MoveComboPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(-50000, 300000, -250000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('SurfingU', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    MoveLow()
    GuardStunPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 500000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('SurfingV', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    MoveMid()
    GuardStunPriority(1)
    DamageStunPriority(1)
    SkillEstimateRange(0, 400000, -200000, 400000, 250, 0)
    Move_EndRegister()
    Move_Register('CommandThrow', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_41236)
    Move_Input_(INPUT_PRESS_D)
    MoveThrow()
    DamageStunPriority(0)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('AirSlide', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3002)
    SkillEstimateRange(-200000, 200000, -400000, -100000, 7000, 50)
    Move_EndRegister()
    Move_Register('Atemi', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_2HOLD8)
    Move_Input_(INPUT_PRESS_C)
    NeutralOnly(1)
    MoveComboPriority(1)
    OpponentAttackPriority(1500)
    MoveCPULevel(500, 1000, 100, 1000)
    SkillEstimateRange(0, 300000, -150000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('HiWeapon', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    TempPriorityMultiplierInterval(0, 1, 4, 1000, 0)
    SkillEstimateRange(300000, 1500000, -200000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('HiWeapon_OD', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    TempPriorityMultiplierInterval(0, 1, 4, 1000, 0)
    SkillEstimateRange(300000, 1500000, -200000, 200000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateAssault', INPUT_DISTORTION)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    MovePriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-130000, 130000, -200000, 150000, 10000, 50)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', INPUT_DISTORTION)
    Move_Condition(0x2002)
    Move_Input_(INPUT_632146)
    Move_Input_(INPUT_PRESS_C)
    Move_Condition(0x3081)
    MovePriority(1)
    GuardStunPriority(1)
    DamageStunPriority(1000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-130000, 130000, -200000, 150000, 10000, 50)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(30000)
    OpponentAttackPriority(10000)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(800000, 1500000, -200000, 200000, 1000, 1)
    Move_EndRegister()
    Move_Register('BurstDD_Easy', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    Move_Input_(INPUT_HOLD_B)
    Move_Input_(INPUT_HOLD_C)
    Move_Input_(INPUT_HOLD_D)
    Move_Condition(0x3081)
    CallSkillConditions('Func_BurstDD_Easy')
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('BurstDD_Cancel', INPUT_SPECIALMOVE)
    StateCall('BurstDD_Easy')
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('BurstDD', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(INPUT_PRESS_D)
    Move_Condition(0x3081)
    NeutralOnly(1)
    OpponentAttackPriority(6000)
    DamageStunPriority(1)
    GuardStunPriority(1)
    SkillEstimateRange(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6A', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk2A', 'NmlAtk2B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'Shabon_A', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'Oiuchi', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'SurfingU', 10000000)
    TempPriorityMultiplier('NmlAtk6A', 'SurfingV', 10000000)
    TempPriorityMultiplier('NmlAtk6C', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'AirHopping', 10000000)
    TempPriorityMultiplier('Hopping', 'HoppingPlus_A', 10000000)
    TempPriorityMultiplier('AirHopping', 'HoppingPlus_A', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk5D_Hanmmer', 20000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk5D_Cat', 20000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D_Cat', 10000000)
    TempPriorityMultiplier('NmlAtk5D_Cat', 'SurfingU', 20000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk5D_Harisen', 20000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D_Harisen', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5A', 'NmlAtkAIR5D_Bat', 20000000)
    TempPriorityMultiplier('NmlAtkAIR5A2nd', 'NmlAtkAIR5D_Bat', 20000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D_Bomb', 20000000)
    TempPriorityMultiplier('NmlAtkAIR5C', 'NmlAtkAIR5D_Missaile', 20000000)
    StylishModeSpecialButton('SurfingV', 0x4, 0xea)
    StylishModeSpecialButton('AirHopping', 0x4, 0xea)
    StylishModeSpecialButton('SurfingU', 0x4, 0x79)
    StylishModeSpecialButton('UltimateAssault', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateAssault_OD', 0x4, 0x5f)
    StylishModeSpecialButton('CommandThrow', 0x4, 0x45)
    StylishModeSpecialButton('AirSlide', 0x4, 0x79)
    StylishModeSpecialButton('HoppingPlus_A', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5D_Hanmmer', 13, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk5C', 1, 180000)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk3C', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6C', 8, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6A', 12, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk5D_Hanmmer', 13, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5C', 0, 0)
    StylishModeCancels('NmlAtk6A', 'SurfingV', 12, 0)
    StylishModeCancels('NmlAtk6A', 'NmlAtk5C', 13, 0)
    StylishModeCancels('NmlAtk6C', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk2B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk2C', 'Shabon_B', 0, 0)
    StylishModeCancels('NmlAtk2C', 'SurfingV', 6, 0)
    StylishModeCancels('NmlAtk3C', 'SurfingU', 0, 0)
    StylishModeCancels('NmlAtk3C', 'NmlAtk5D_Cat', 6, 0)
    StylishModeCancels('NmlAtk3C', 'HiWeapon', 10, 400000)
    StylishModeCancels('NmlAtk3C', 'Shabon_B', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5D_Hanmmer', 6, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 12, 0)
    StylishModeCancels('NmlAtkAIR5C', 'AirHopping', 0, 0)
    StylishModeCancels('NmlAtkAIR5C', 'NmlAtkAIR5D_Harisen', 6, 0)
    StylishModeCancels('NmlAtkAIR5C', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk5D_Hanmmer', 'Shabon_B', 0, 0)
    StylishModeCancels('NmlAtk5D_Hanmmer', 'SurfingU', 6, 0)
    StylishModeCancels('NmlAtk5D_Hanmmer', 'AstralHeat', 6, 0)
    StylishModeCancels('NmlAtk5D_Hanmmer', 'SurfingU', 12, 0)
    StylishModeCancels('NmlAtkAIR5D_Hanmmer', 'Shabon_B', 0, 0)
    StylishModeCancels('NmlAtkAIR5D_Hanmmer', 'SurfingU', 6, 0)
    StylishModeCancels('NmlAtk5D_Cat', 'Shabon_B', 0, 0)
    StylishModeCancels('NmlAtk5D_Cat', 'SurfingU', 6, 0)
    StylishModeCancels('NmlAtkAIR5D_Cat', 'Oiuchi', 0, 0)
    StylishModeCancels('ThrowExe', 'Shabon_B', 0, 0)
    StylishModeCancels('ThrowExe', 'AstralHeat', 6, 0)
    StylishModeCancels('BackThrowExeAdd', 'Shabon_B', 0, 0)
    StylishModeCancels('BackThrowExeAdd', 'AstralHeat', 6, 0)
    HitSprites(0, 'pt062_01')
    HitSprites(1, 'pt062_03')
    HitSprites(2, 'pt062_04')
    HitSprites(3, 'pt062_05')
    HitSprites(4, 'pt062_05')
    HitSprites(5, 'pt062_06')
    HitSprites(6, 'pt062_07')
    HitSprites(7, 'pt041_02')
    HitSprites(8, 'pt040_02')
    HitSprites(9, 'pt045_02')
    HitSprites(10, 'pt060_00')
    HitSprites(11, 'pt060_01')
    HitSprites(12, 'pt060_03')
    HitSprites(13, 'pt060_05')
    HitSprites(14, 'pt060_07')
    HitSprites(15, 'pt060_14')
    HitSprites(16, 'pt050_00')
    HitSprites(17, 'pt052_00')
    HitSprites(18, 'pt054_00')
    HitSprites(19, 'pt000_00')
    HitSprites(20, 'pt000_00')
    HitSprites(25, 'pt063_00')
    HitSprites(26, 'pt063_01')
    HitSprites(27, 'pt063_02')
    HitSprites(28, 'pt063_04')
    HitSprites(29, 'pt063_10')
    HitSprites(30, 'pt077_00')
    HitSprites(31, 'pt077_01')
    HitSprites(32, 'pt077_00ex00')
    HitSprites(33, 'pt077_01ex00')
    HitSprites(34, 'pt077_00ex01')
    HitSprites(35, 'pt077_01ex01')
    HitSprites(36, 'pt077_00ex02')
    HitSprites(37, 'pt077_01ex02')
    HitSprites(24, 'pt073_01')
    CommonVoicelines(0, 'pt000')
    CommonVoicelines(1, 'pt001')
    CommonVoicelines(2, 'pt002')
    CommonVoicelines(3, 'pt003')
    CommonVoicelines(4, 'pt004')
    CommonVoicelines(5, 'pt005')
    CommonVoicelines(6, 'pt006')
    CommonVoicelines(7, 'pt007')
    CommonVoicelines(8, 'pt008')
    CommonVoicelines(9, 'pt009')
    CommonVoicelines(10, 'pt010')
    CommonVoicelines(11, 'pt011')
    CommonVoicelines(12, 'pt012')
    CommonVoicelines(13, 'pt013')
    CommonVoicelines(14, 'pt014')
    CommonVoicelines(15, 'pt015')
    CommonVoicelines(16, 'pt016')
    CommonVoicelines(17, 'pt017')
    CommonVoicelines(18, 'pt018')
    CommonVoicelines(19, 'pt019')
    CommonVoicelines(20, 'pt020')
    CommonVoicelines(21, 'pt021')
    CommonVoicelines(22, 'pt022')
    CommonVoicelines(23, 'pt023')
    CommonVoicelines(24, 'pt024')
    CommonVoicelines(25, 'pt025')
    CommonVoicelines(26, 'pt026')
    CommonVoicelines(27, 'pt027')
    CommonVoicelines(28, 'pt028')
    CommonVoicelines(29, 'pt029')
    CommonVoicelines(30, 'pt030')
    CommonVoicelines(31, 'pt031')
    CommonVoicelines(32, 'pt032')
    CommonVoicelines(33, 'pt033')
    CommonVoicelines(34, 'pt034')
    CommonVoicelines(35, 'pt035')
    CommonVoicelines(36, 'pt036')
    CommonVoicelines(37, 'pt037')
    CommonVoicelines(38, 'pt038')
    CommonVoicelines(39, 'pt039')
    CommonVoicelines(40, 'pt040')
    CommonVoicelines(41, 'pt041')
    CommonVoicelines(42, 'pt042')
    CommonVoicelines(43, 'pt043')
    CommonVoicelines(44, 'pt044')
    CommonVoicelines(45, 'pt045')
    CommonVoicelines(46, 'pt046')
    CommonVoicelines(47, 'pt047')
    CommonVoicelines(48, 'pt048')
    CommonVoicelines(49, 'pt049')
    CommonVoicelines(50, 'pt050')
    CommonVoicelines(51, 'pt051')
    CommonVoicelines(52, 'pt052')
    CommonVoicelines(53, 'pt053')
    CommonVoicelines(54, 'pt100')
    CommonVoicelines(55, 'pt101')
    CommonVoicelines(56, 'pt102')
    CommonVoicelines(57, 'pt103')
    CommonVoicelines(58, 'pt104')
    CommonVoicelines(59, 'pt105')
    CommonVoicelines(60, 'pt106')
    CommonVoicelines(61, 'pt107')
    CommonVoicelines(62, 'pt108')
    CommonVoicelines(63, 'pt109')
    CommonVoicelines(64, 'pt150')
    CommonVoicelines(65, 'pt151')
    CommonVoicelines(66, 'pt152')
    CommonVoicelines(67, 'pt153')
    CommonVoicelines(68, 'pt154')
    CommonVoicelines(69, 'pt155')
    CommonVoicelines(70, 'pt156')
    CommonVoicelines(71, 'pt157')
    CommonVoicelines(72, 'pt158')
    CommonVoicelines(75, 'pt160')
    CommonVoicelines(73, 'pt402')
    CommonVoicelines(74, 'pt403')
    CreateObject('PaletteControlObj1', -1)
    CreateObject('PaletteControlObj2', -1)
    CreateObject('PaletteControlObj3', -1)
    CreateObject('PaletteControlObj4', -1)
    CreateObject('PaletteControlObj5', -1)
    CreateObject('PaletteControlObj6', -1)
    CreateObject('PaletteControlObj7', -1)
    CreateObject('PaletteControlObj8', -1)
    CreateObject('SphereLight', -1)


@Subroutine
def CheckActivateHanmmer():
    SLOT_47 = 0
    if SLOT_4 == 1:
        SLOT_47 = 1
    elif SLOT_4 == 2:
        SLOT_47 = 1


@Subroutine
def CheckActivateCat():
    SLOT_47 = 0
    if SLOT_4 == 3:
        SLOT_47 = 1
    elif SLOT_4 == 4:
        SLOT_47 = 1


@Subroutine
def CheckActivateHarisen():
    SLOT_47 = 0
    if SLOT_4 == 5:
        SLOT_47 = 1
    elif SLOT_4 == 6:
        SLOT_47 = 1


@Subroutine
def CheckActivateBat():
    SLOT_47 = 0
    if SLOT_4 == 7:
        SLOT_47 = 1
    elif SLOT_4 == 8:
        SLOT_47 = 1


@Subroutine
def CheckActivateBomb():
    SLOT_47 = 0
    if SLOT_4 == 9:
        SLOT_47 = 1
    elif SLOT_4 == 10:
        SLOT_47 = 1


@Subroutine
def CheckActivateMissaile():
    SLOT_47 = 0
    if SLOT_4 == 11:
        SLOT_47 = 1
    elif SLOT_4 == 12:
        SLOT_47 = 1


@Subroutine
def CheckActivateBox():
    SLOT_47 = 0
    if SLOT_4 == 13:
        SLOT_47 = 1
    elif SLOT_4 == 14:
        SLOT_47 = 1


@Subroutine
def CheckActivateBoomerang():
    SLOT_47 = 0
    if SLOT_4 == 15:
        SLOT_47 = 1
    elif SLOT_4 == 16:
        SLOT_47 = 1


@Subroutine
def MatchInit2():
    ResourceGauge(1, 1, 16, 1, 2, 2, -16711936, -16711936)
    ResourceGauge(0, 1, 3, 1, 4, 4, -1, -1)
    NumberGauge(0, 1)
    BackupGaugeText(1, 1)
    TrainingModeSLOT('TRI_PTItemA', 2, 67)
    if SLOT_67:
        SLOT_0 = SLOT_67
    else:
        Unknown61(0, 1, 0, 8, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    callSubroutine('ItemCheck')
    op(2, 2, 8, 0, 2)
    op(1, 2, 0, 0, 1)
    SLOT_5 = SLOT_0
    SLOT_4 = 0
    callSubroutine('UpdateIcon')


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@Subroutine
def ItemCheck():
    SLOT_8 = SLOT_0
    if not PreviousStateCheck('CmnActOverDriveEnd'):
        if not PreviousStateCheck('CmnActOverDriveEnd'):
            if SLOT_8 == 1:
                SLOT_9 and 1
                if SLOT_0 == 1:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 1)
            elif SLOT_8 == 2:
                SLOT_9 and 2
                if SLOT_0 == 2:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 2)
            elif SLOT_8 == 3:
                SLOT_9 and 4
                if SLOT_0 == 4:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 4)
            elif SLOT_8 == 4:
                SLOT_9 and 8
                if SLOT_0 == 8:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 8)
            elif SLOT_8 == 5:
                SLOT_9 and 16
                if SLOT_0 == 16:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 16)
            elif SLOT_8 == 6:
                SLOT_9 and 32
                if SLOT_0 == 32:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 32)
            elif SLOT_8 == 7:
                SLOT_9 and 64
                if SLOT_0 == 64:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 64)
            elif SLOT_8 == 8:
                SLOT_9 and 128
                if SLOT_0 == 128:
                    callSubroutine('ItemReSelect')
                else:
                    ModifyVar_(8, 2, 9, 0, 128)
            SLOT_9 and 255
            if SLOT_0 == 255:
                SLOT_9 = 0


@Subroutine
def ItemReSelect():
    SLOT_9 and 1
    if not SLOT_0 == 1:
        SLOT_8 = 1
        ModifyVar_(8, 2, 9, 0, 1)
    else:
        SLOT_9 and 2
        if not SLOT_0 == 2:
            SLOT_8 = 2
            ModifyVar_(8, 2, 9, 0, 2)
        else:
            SLOT_9 and 4
            if not SLOT_0 == 4:
                SLOT_8 = 3
                ModifyVar_(8, 2, 9, 0, 4)
            else:
                SLOT_9 and 8
                if not SLOT_0 == 8:
                    SLOT_8 = 4
                    ModifyVar_(8, 2, 9, 0, 8)
                else:
                    SLOT_9 and 16
                    if not SLOT_0 == 16:
                        SLOT_8 = 5
                        ModifyVar_(8, 2, 9, 0, 16)
                    else:
                        SLOT_9 and 32
                        if not SLOT_0 == 32:
                            SLOT_8 = 6
                            ModifyVar_(8, 2, 9, 0, 32)
                        else:
                            SLOT_9 and 64
                            if not SLOT_0 == 64:
                                SLOT_8 = 7
                                ModifyVar_(8, 2, 9, 0, 64)
                            else:
                                SLOT_9 and 128
                                if not SLOT_0 == 128:
                                    SLOT_8 = 8
                                    ModifyVar_(8, 2, 9, 0, 128)


@Subroutine
def ItemShuffle():
    SLOT_4 = SLOT_5
    if SLOT_61:
        TrainingModeSLOT('TRI_PTItemA', 2, 67)
        if SLOT_67:
            SLOT_0 = SLOT_67
        else:
            op(0, 2, 5, 0, 1)
            op(3, 2, 0, 0, 2)
            Unknown61(0, 1, 0, 8, 0, 0, 2, 0, 0, 9999, 0, 9999)
        SLOT_61 = 0
    else:
        TrainingModeSLOT('TRI_PTItemB', 2, 67)
        if SLOT_67:
            SLOT_0 = SLOT_67
        else:
            op(0, 2, 5, 0, 1)
            op(3, 2, 0, 0, 2)
            Unknown61(0, 1, 0, 8, 0, 0, 2, 0, 0, 9999, 0, 9999)
        SLOT_61 = 1
    callSubroutine('ItemCheck')
    op(2, 2, 8, 0, 2)
    op(1, 2, 0, 0, 1)
    SLOT_5 = SLOT_0
    callSubroutine('UpdateIcon')
    SLOT_31 = 9999
    SLOT_32 = 9999
    SLOT_59 = SLOT_4
    CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)


@Subroutine
def ItemShufflePowerUP():
    SLOT_4 = SLOT_5
    SLOT_4 % 2
    if not SLOT_0 == 0:
        SLOT_4 = SLOT_4 + 1
    if SLOT_61:
        TrainingModeSLOT('TRI_PTItemA', 2, 67)
        if SLOT_67:
            SLOT_0 = SLOT_67
        else:
            op(0, 2, 5, 0, 1)
            op(3, 2, 0, 0, 2)
            Unknown61(0, 1, 0, 8, 0, 0, 2, 0, 0, 9999, 0, 9999)
        SLOT_61 = 0
    else:
        TrainingModeSLOT('TRI_PTItemB', 2, 67)
        if SLOT_67:
            SLOT_0 = SLOT_67
        else:
            op(0, 2, 5, 0, 1)
            op(3, 2, 0, 0, 2)
            Unknown61(0, 1, 0, 8, 0, 0, 2, 0, 0, 9999, 0, 9999)
        SLOT_61 = 1
    callSubroutine('ItemCheck')
    op(2, 2, 8, 0, 2)
    op(1, 2, 0, 0, 1)
    SLOT_5 = SLOT_0
    if SLOT_58:
        SLOT_5 = SLOT_5 + 1
    callSubroutine('UpdateIcon')
    SLOT_31 = 9999
    SLOT_32 = 9999
    SLOT_59 = SLOT_4
    CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)


@Subroutine
def ItemDiscard():
    SLOT_4 = 0
    callSubroutine('UpdateIcon')


@Subroutine
def ItemConsume():
    if not SLOT_OverdriveTimer:
        SLOT_31 = SLOT_31 - 1
        if not SLOT_31:
            SLOT_4 = 0
        callSubroutine('UpdateIcon')


@Subroutine
def ItemConsume_Throw():
    SLOT_31 = SLOT_31 - 1
    if not SLOT_31:
        SLOT_4 = 0
    callSubroutine('UpdateIcon')


@Subroutine
def UpdateIcon():
    ResourceBarVisibility2(0, 1)
    if SLOT_4 == 0:
        ResourceBarVisibility2(0, 0)
    if SLOT_4 == 1:
        ResourceBarIcon(0, 23)
        ResourceItemAmount(0, 2)
    if SLOT_4 == 2:
        ResourceBarIcon(0, 24)
        ResourceItemAmount(0, 2)
    if SLOT_4 == 3:
        ResourceBarIcon(0, 25)
        ResourceItemAmount(0, 5)
    if SLOT_4 == 4:
        ResourceBarIcon(0, 26)
        ResourceItemAmount(0, 5)
    if SLOT_4 == 5:
        ResourceBarIcon(0, 27)
        ResourceItemAmount(0, 4)
    if SLOT_4 == 6:
        ResourceBarIcon(0, 28)
        ResourceItemAmount(0, 4)
    if SLOT_4 == 7:
        ResourceBarIcon(0, 29)
        ResourceItemAmount(0, 3)
    if SLOT_4 == 8:
        ResourceBarIcon(0, 30)
        ResourceItemAmount(0, 3)
    if SLOT_4 == 9:
        ResourceBarIcon(0, 31)
        ResourceItemAmount(0, 3)
    if SLOT_4 == 10:
        ResourceBarIcon(0, 32)
        ResourceItemAmount(0, 6)
    if SLOT_4 == 11:
        ResourceBarIcon(0, 33)
        ResourceItemAmount(0, 3)
    if SLOT_4 == 12:
        ResourceBarIcon(0, 34)
        ResourceItemAmount(0, 3)
    if SLOT_4 == 13:
        ResourceBarIcon(0, 43)
        ResourceItemAmount(0, 2)
    if SLOT_4 == 14:
        ResourceBarIcon(0, 44)
        ResourceItemAmount(0, 4)
    if SLOT_4 == 15:
        ResourceBarIcon(0, 51)
        ResourceItemAmount(0, 1)
    if SLOT_4 == 16:
        ResourceBarIcon(0, 52)
        ResourceItemAmount(0, 1)
    if SLOT_5 == 0:
        ResourceBarIcon(1, 0)
        ResourceItemAmount(1, 0)
    if SLOT_5 == 1:
        ResourceBarIcon(1, 23)
        ResourceItemAmount(1, 2)
    if SLOT_5 == 2:
        ResourceBarIcon(1, 24)
        ResourceItemAmount(1, 2)
    if SLOT_5 == 3:
        ResourceBarIcon(1, 25)
        ResourceItemAmount(1, 5)
    if SLOT_5 == 4:
        ResourceBarIcon(1, 26)
        ResourceItemAmount(1, 5)
    if SLOT_5 == 5:
        ResourceBarIcon(1, 27)
        ResourceItemAmount(1, 20)
    if SLOT_5 == 6:
        ResourceBarIcon(1, 28)
        ResourceItemAmount(1, 60)
    if SLOT_5 == 7:
        ResourceBarIcon(1, 29)
        ResourceItemAmount(1, 30)
    if SLOT_5 == 8:
        ResourceBarIcon(1, 30)
        ResourceItemAmount(1, 70)
    if SLOT_5 == 9:
        ResourceBarIcon(1, 31)
        ResourceItemAmount(1, 40)
    if SLOT_5 == 10:
        ResourceBarIcon(1, 32)
        ResourceItemAmount(1, 80)
    if SLOT_5 == 11:
        ResourceBarIcon(1, 33)
        ResourceItemAmount(1, 50)
    if SLOT_5 == 12:
        ResourceBarIcon(1, 34)
        ResourceItemAmount(1, 90)
    if SLOT_5 == 13:
        ResourceBarIcon(1, 43)
        ResourceItemAmount(1, 4)
    if SLOT_5 == 14:
        ResourceBarIcon(1, 44)
        ResourceItemAmount(1, 4)
    if SLOT_5 == 15:
        ResourceBarIcon(1, 51)
        ResourceItemAmount(1, 1)
    if SLOT_5 == 16:
        ResourceBarIcon(1, 52)
        ResourceItemAmount(1, 10)


@Subroutine
def OnFrameStep():
    if SLOT_InNeutral:
        TrainingModeSLOT('TRI_PTItemRecover', 2, 67)
        if SLOT_67:
            SLOT_31 = SLOT_31 + 9999
    if SLOT_IsGrounded:
        SLOT_6 = 1

    def upon_VALUE_RECEIVED():
        if SLOT_ReceivedValue == 0:
            if SLOT_4 == 0:
                SLOT_4 = 15
                SLOT_31 = 1
                callSubroutine('UpdateIcon')
                SLOT_59 = SLOT_4
                CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        if SLOT_ReceivedValue == 1:
            if SLOT_4 == 0:
                SLOT_4 = 16
                SLOT_31 = 1
                callSubroutine('UpdateIcon')
                SLOT_59 = SLOT_4
                CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_62:
        if not SLOT_28:
            SLOT_62 = 1
    elif SLOT_28:
        SLOT_62 = 0
        if not SLOT_63:
            CreateObject('SphereLight_Shutsugen', 108)
            SLOT_63 = 34
    if SLOT_63:
        SLOT_63 = SLOT_63 + -1


@State
def CmnActStand():
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('pt001_00', 7)
    SLOT_88 = 960
    SmartVoiceline('pt000')
    sprite('pt001_01', 5)
    sprite('pt001_02', 8)
    sprite('pt001_03', 8)
    sprite('pt001_04', 8)
    sprite('pt001_05', 8)
    sprite('pt001_06', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('pt003_00', 3)
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)


@State
def CmnActStand2Crouch():
    sprite('pt010_00', 4)
    sprite('pt010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('pt010_02', 6)
    sprite('pt010_03', 6)
    sprite('pt010_04', 6)
    sprite('pt010_05', 6)
    sprite('pt010_06', 6)
    sprite('pt010_07', 6)
    sprite('pt010_08', 6)
    sprite('pt010_09', 6)
    sprite('pt010_10', 6)
    sprite('pt010_11', 6)
    sprite('pt010_12', 6)
    sprite('pt010_13', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('pt013_00', 3)
    sprite('pt013_01', 3)
    sprite('pt013_02', 3)


@State
def CmnActCrouch2Stand():
    sprite('pt010_01', 4)
    sprite('pt010_00', 4)


@State
def CmnActJumpPre():
    sprite('pt023_00', 2)
    sprite('pt023_01', 2)


@State
def CmnActJumpUpper():
    if SLOT_IsMovingBackward:
        conditionalSendToLabel(1)
    if SLOT_IsMovingForward:
        conditionalSendToLabel(2)
    sprite('pt020_00', 4)
    sprite('pt020_01', 4)
    SmartVoiceline('pt002')
    gotoLabel(0)
    label(1)
    sprite('pt020_00', 4)
    sprite('pt020_01', 4)
    SmartVoiceline('pt002')
    gotoLabel(0)
    label(2)
    sprite('pt020_00', 4)
    sprite('pt020_01', 4)
    SmartVoiceline('pt003')
    gotoLabel(0)
    label(0)
    sprite('pt020_00', 4)
    sprite('pt020_01', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('pt020_02', 3)
    sprite('pt020_03', 3)
    sprite('pt020_04', 3)


@State
def CmnActJumpDown():
    sprite('pt020_05', 3)
    sprite('pt020_06', 3)
    label(0)
    sprite('pt020_07', 4)
    sprite('pt020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('pt024_00', 3)
    sprite('pt024_01', 3)
    sprite('pt024_02', 3)


@State
def CmnActLandingStiffLoop():
    sprite('pt024_00', 4)
    sprite('pt024_01', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('pt024_02', 6)


@State
def CmnActFWalk():
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    label(0)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('pt031_00', 7)
    sprite('pt031_01', 7)
    label(0)
    sprite('pt031_02', 7)
    sprite('pt031_03', 7)
    sprite('pt031_04', 7)
    sprite('pt031_05', 7)
    sprite('pt031_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt031_07', 7)
    sprite('pt031_08', 7)
    sprite('pt031_09', 7)
    sprite('pt031_10', 7)
    sprite('pt031_11', 7)
    sprite('pt031_12', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt031_13', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('pt032_00', 2)
    sprite('pt032_01', 2)
    label(0)
    sprite('pt032_02', 4)
    sprite('pt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_04', 4)
    sprite('pt032_05', 4)
    sprite('pt032_06', 4)
    sprite('pt032_07', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('pt032_09', 4)
    sprite('pt032_10', 4)
    sprite('pt032_11', 4)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        InvincibilityDuration(7)
        EndMomentum(1)
        uponSendToLabel(LANDING, 1)
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
    sprite('pt033_00', 1)
    sprite('pt033_01', 2)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    JumpSoundEffects()
    SmartVoiceline('pt005')
    sprite('pt033_02', 2)
    sprite('pt033_02', 1)
    sprite('pt033_03', 3)
    loopRest()
    label(0)
    sprite('pt033_02', 3)
    sprite('pt033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt033_04', 2)
    sprite('pt033_05', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('pt033_06', 2)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('pt035_00', 3)
    SmartVoiceline('pt004')
    label(0)
    sprite('pt035_01', 4)
    sprite('pt035_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('pt036_00', 3)
    SmartVoiceline('pt006')
    label(0)
    sprite('pt036_01', 4)
    sprite('pt036_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('pt050_00', 1)
    sprite('pt050_01', 1)
    sprite('pt050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('pt050_01', 1)
    sprite('pt050_02', 1)
    sprite('pt050_01', 2)
    sprite('pt050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('pt050_02', 1)
    sprite('pt050_03', 1)
    sprite('pt050_02', 2)
    sprite('pt050_01', 2)
    sprite('pt050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('pt050_03', 1)
    sprite('pt050_04', 1)
    sprite('pt050_03', 2)
    sprite('pt050_02', 2)
    sprite('pt050_01', 2)
    sprite('pt050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('pt050_04', 1)
    sprite('pt050_04', 1)
    sprite('pt050_04', 2)
    sprite('pt050_03', 2)
    sprite('pt050_02', 2)
    sprite('pt050_01', 2)
    sprite('pt050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('pt052_00', 1)
    sprite('pt052_01', 1)
    sprite('pt052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('pt052_01', 1)
    sprite('pt052_02', 1)
    sprite('pt052_01', 2)
    sprite('pt052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('pt052_02', 1)
    sprite('pt052_03', 1)
    sprite('pt052_02', 2)
    sprite('pt052_01', 2)
    sprite('pt052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('pt052_03', 1)
    sprite('pt052_04', 1)
    sprite('pt052_03', 2)
    sprite('pt052_02', 2)
    sprite('pt052_01', 2)
    sprite('pt052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('pt052_04', 1)
    sprite('pt052_04', 1)
    sprite('pt052_04', 2)
    sprite('pt052_03', 2)
    sprite('pt052_02', 2)
    sprite('pt052_01', 2)
    sprite('pt052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('pt054_00', 1)
    sprite('pt054_01', 1)
    sprite('pt054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('pt054_01', 1)
    sprite('pt054_02', 1)
    sprite('pt054_01', 2)
    sprite('pt054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('pt054_02', 1)
    sprite('pt054_03', 1)
    sprite('pt054_02', 2)
    sprite('pt054_01', 2)
    sprite('pt054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('pt054_03', 1)
    sprite('pt054_04', 1)
    sprite('pt054_03', 2)
    sprite('pt054_02', 2)
    sprite('pt054_01', 2)
    sprite('pt054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('pt054_04', 1)
    sprite('pt054_04', 1)
    sprite('pt054_04', 2)
    sprite('pt054_03', 2)
    sprite('pt054_02', 2)
    sprite('pt054_01', 2)
    sprite('pt054_00', 2)


@State
def CmnActBDownUpper():
    sprite('pt060_00', 4)
    label(0)
    sprite('pt060_01', 4)
    sprite('pt060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('pt060_03', 4)


@State
def CmnActBDownDown():
    sprite('pt060_04', 4)
    label(0)
    sprite('pt060_05', 4)
    sprite('pt060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('pt060_07', 2)
    sprite('pt060_08', 2)


@State
def CmnActBDownBound():
    sprite('pt060_09', 3)
    sprite('pt060_10', 3)
    sprite('pt060_11', 3)
    sprite('pt060_12', 3)
    sprite('pt060_13', 3)


@State
def CmnActBDownLoop():
    sprite('pt060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('pt061_00', 3)
    sprite('pt061_01', 3)
    sprite('pt061_02', 3)
    sprite('pt061_03', 3)
    sprite('pt061_04', 3)
    sprite('pt061_05', 3)
    sprite('pt061_06', 2)
    sprite('pt061_07', 2)
    sprite('pt061_08', 2)
    sprite('pt061_09', 2)


@State
def CmnActFDownUpper():
    sprite('pt063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('pt063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('pt063_02', 3)
    sprite('pt063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('pt063_04', 3)
    sprite('pt063_05', 3)


@State
def CmnActFDownBound():
    sprite('pt063_06', 2)
    sprite('pt063_07', 2)
    sprite('pt063_08', 3)
    sprite('pt063_09', 3)
    sprite('pt063_10', 3)


@State
def CmnActFDownLoop():
    sprite('pt063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('pt064_00', 2)
    sprite('pt064_01', 2)
    sprite('pt064_02', 2)
    sprite('pt064_03', 2)
    sprite('pt064_04', 2)
    sprite('pt064_05', 2)
    sprite('pt064_06', 2)
    sprite('pt064_07', 2)
    sprite('pt064_08', 2)
    sprite('pt064_09', 2)
    sprite('pt064_10', 2)


@State
def CmnActVDownUpper():
    sprite('pt062_00', 3)
    label(0)
    sprite('pt062_01', 3)
    sprite('pt062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('pt062_03', 3)
    sprite('pt062_04', 3)


@State
def CmnActVDownDown():
    sprite('pt062_05', 3)
    sprite('pt062_06', 3)
    label(0)
    sprite('pt062_07', 3)
    sprite('pt062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('pt062_09', 2)
    sprite('pt062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('pt062_09', 2)
    sprite('pt062_10', 2)


@State
def CmnActBlowoff():
    sprite('pt072_00', 3)
    sprite('pt072_01', 3)
    sprite('pt072_02', 3)
    label(0)
    sprite('pt072_01', 3)
    sprite('pt072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('pt074_00', 3)
    sprite('pt074_01', 3)
    sprite('pt074_02', 3)
    sprite('pt074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('pt082_00', 2)
    sprite('pt082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('pt071_06', 1)


@State
def CmnActWallBound():
    sprite('pt073_00', 3)
    sprite('pt073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('pt073_02', 3)
    label(0)
    sprite('pt073_03', 3)
    sprite('pt073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('pt070_00', 2)
    sprite('pt070_01', 2)
    label(0)
    sprite('pt070_02', 3)
    sprite('pt070_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerDown():
    sprite('pt070_04', 3)
    sprite('pt070_05', 3)
    CreateObject('StaggerSoul', -1)
    sprite('pt070_06', 2)
    sprite('pt070_07', 6)
    sprite('pt070_08', 6)
    sprite('pt070_09', 5)


@State
def CmnActUkemiStagger():
    sprite('pt070_10', 5)
    sprite('pt070_11', 2)
    sprite('pt070_12', 3)
    sprite('pt070_13', 3)


@State
def CmnActUkemiAirF():
    sprite('pt113_00', 3)
    sprite('pt113_01', 3)
    sprite('pt113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('pt113_00', 3)
    sprite('pt113_01', 3)
    sprite('pt113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('pt113_00', 3)
    sprite('pt113_01', 3)
    sprite('pt113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('pt110_00', 2)
    sprite('pt110_01', 2)
    sprite('pt110_02', 2)
    sprite('pt110_03', 2)
    sprite('pt110_04', 2)
    sprite('pt110_05', 2)
    sprite('pt110_06', 2)
    sprite('pt110_07', 2)
    sprite('pt110_08', 200)
    sprite('pt110_09', 6)


@State
def CmnActUkemiLandB():
    sprite('pt111_00', 3)
    sprite('pt111_01', 3)
    sprite('pt110_05', 3)
    sprite('pt110_04', 3)
    sprite('pt110_03', 3)
    sprite('pt110_02', 3)
    sprite('pt111_06', 3)
    sprite('pt111_07', 3)
    sprite('pt111_08', 200)
    sprite('pt111_09', 6)


@State
def CmnActUkemiLandN():
    sprite('pt112_00', 2)
    sprite('pt112_01', 2)
    sprite('pt112_02', 2)
    sprite('pt112_03', 2)
    sprite('pt112_04', 2)
    sprite('pt112_05', 2)
    sprite('pt112_06', 2)
    sprite('pt112_07', 2)
    sprite('pt112_08', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('pt024_00', 3)
    sprite('pt024_01', 3)
    sprite('pt024_02', 3)
    sprite('pt024_03', 3)
    sprite('pt024_04', 3)
    sprite('pt024_05', 3)


@State
def CmnActMidGuardPre():
    sprite('pt041_00', 3)
    sprite('pt041_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('pt041_01', 3)
    sprite('pt041_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('pt040_03', 3)
    label(0)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('pt040_01', 3)
    sprite('pt040_00', 3)
    sprite('pt041_01', 3)
    sprite('pt041_00', 3)


@State
def CmnActHighGuardPre():
    sprite('pt041_00', 3)
    sprite('pt041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('pt041_02', 5)
    sprite('pt041_03', 5)
    sprite('pt041_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('pt041_01', 3)
    sprite('pt041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('pt041_05', 5)
    label(0)
    sprite('pt041_02', 5)
    sprite('pt041_03', 5)
    sprite('pt041_04', 5)
    loopRest()
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('pt041_01', 3)
    sprite('pt041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('pt043_00', 3)
    sprite('pt043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('pt043_02', 3)
    sprite('pt043_03', 3)
    sprite('pt043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('pt043_01', 3)
    sprite('pt043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('pt043_05', 3)
    label(0)
    sprite('pt043_02', 3)
    sprite('pt043_03', 3)
    sprite('pt043_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('pt043_01', 3)
    sprite('pt043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('pt045_00', 3)
    sprite('pt045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('pt045_02', 3)
    sprite('pt045_03', 3)
    sprite('pt045_04', 3)
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('pt045_01', 3)
    sprite('pt045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('pt045_05', 3)
    label(0)
    sprite('pt045_02', 3)
    sprite('pt045_03', 3)
    sprite('pt045_04', 3)
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('pt045_01', 3)
    sprite('pt045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('pt090_00', 2)
    sprite('pt090_01', 2)
    sprite('pt090_02', 1)
    SetCommonActionMark(1)
    sprite('pt090_03', 6)
    sprite('pt090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('pt091_00', 2)
    sprite('pt091_01', 2)
    sprite('pt091_02', 1)
    SetCommonActionMark(1)
    sprite('pt091_03', 6)
    sprite('pt091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('pt092_00', 2)
    sprite('pt092_01', 2)
    sprite('pt092_02', 1)
    SetCommonActionMark(1)
    sprite('pt092_03', 6)
    sprite('pt092_04', 6)


@State
def CmnActAirTurn():
    sprite('pt025_00', 4)
    sprite('pt025_01', 4)
    sprite('pt025_02', 4)


@State
def CmnActLockWait():
    sprite('pt040_02', 1)
    sprite('pt040_01', 3)
    sprite('pt040_00', 3)


@State
def CmnActLockReject():
    sprite('pt312_00', 2)
    sprite('pt312_01', 4)
    sprite('pt312_02', 8)
    sprite('pt312_03', 6)
    sprite('pt312_04', 5)
    sprite('pt312_05', 5)


@State
def CmnActAirLockWait():
    sprite('pt045_02', 1)
    sprite('pt045_01', 3)
    sprite('pt045_00', 3)


@State
def CmnActAirLockReject():
    sprite('pt000_00', 2)
    sprite('pt322_01', 2)
    sprite('pt322_02', 8)
    sprite('pt322_03', 2)
    sprite('pt322_04', 3)
    sprite('pt322_05', 3)


@State
def CmnActLandSpin():
    sprite('pt071_00', 4)
    sprite('pt071_01', 4)
    label(0)
    sprite('pt071_02', 2)
    sprite('pt071_03', 2)
    sprite('pt071_04', 2)
    sprite('pt071_05', 2)
    sprite('pt071_06', 2)
    sprite('pt071_07', 2)
    sprite('pt071_08', 2)
    sprite('pt071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('pt071_10', 6)
    sprite('pt071_11', 5)
    sprite('pt071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('pt071_02', 2)
    sprite('pt071_03', 2)
    sprite('pt071_04', 2)
    sprite('pt071_05', 2)
    sprite('pt071_06', 2)
    sprite('pt071_07', 2)
    sprite('pt071_08', 2)
    sprite('pt071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('pt077_00', 2)
    sprite('pt077_01', 2)
    sprite('pt077_00ex00', 2)
    sprite('pt077_01ex00', 2)
    sprite('pt077_00ex01', 2)
    sprite('pt077_01ex01', 2)
    sprite('pt077_00ex02', 2)
    sprite('pt077_01ex02', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('pt077_02', 4)
    label(0)
    sprite('pt077_03', 3)
    sprite('pt077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('pt077_05', 5)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('pt060_07', 3)
    sprite('pt060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('pt060_11', 4)
    sprite('pt060_13', 5)


@State
def CmnActBurstBegin():
    sprite('pt331_00', 2)
    sprite('pt331_01', 2)
    label(0)
    sprite('pt331_02', 3)
    sprite('pt331_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('pt331_04', 2)
    sprite('pt331_05', 2)
    label(0)
    sprite('pt331_06', 3)
    sprite('pt331_07', 3)
    sprite('pt331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('pt331_09', 3)
    sprite('pt331_10', 3)


@State
def CmnActAirBurstBegin():
    sprite('pt331_11', 2)
    sprite('pt331_12', 2)
    label(0)
    sprite('pt331_02', 3)
    sprite('pt331_03', 2)
    sprite('pt331_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('pt331_05', 2)
    label(0)
    sprite('pt331_06', 2)
    sprite('pt331_07', 2)
    sprite('pt331_08', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('pt331_13', 4)
    sprite('pt331_14', 3)
    label(0)
    sprite('pt020_07', 4)
    sprite('pt020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('pt333_00', 3)
    sprite('pt333_01', 3)
    sprite('pt333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('pt333_03', 32767)
    CreateObject('EMB_PT_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('pt333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('pt333_05', 3)
    sprite('pt333_06', 3)
    sprite('pt333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('pt333_08', 4)
    sprite('pt333_09', 4)
    sprite('pt333_10', 4)


@State
def CmnActAirOverDriveBegin():
    sprite('pt333_11', 3)
    sprite('pt333_12', 3)
    sprite('pt333_13', 3)
    CharacterFlash(16639, 20, 1)
    sprite('pt333_14', 32767)
    CreateObject('EMB_PT_OD', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('pt333_15', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    label(0)
    sprite('pt333_05', 3)
    sprite('pt333_06', 3)
    sprite('pt333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('pt333_16', 4)
    sprite('pt333_17', 4)
    sprite('pt333_18', 4)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        Damage(300)
        DamageEffect(6, 'ptef_hit_low')
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('ChainLandDrive')
        HitOrBlockJumpCancel(1)

        def upon_EVERY_FRAME():
            if SLOT_54:
                InvincibilityDuration(7)
                clearUponHandler(EVERY_FRAME)
    sprite('pt200_00', 2)
    PerInertia(60)
    if random_(2, 0, 34):
        conditionalSendToLabel(0)
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('pt200_01', 3)
    CommonSE('003_swing_grap_0_0')
    SLOT_51 = 1
    if CharacterIDCheck('pt'):
        if CharacterIDCheck('pt'):
            CopyFromRightToLeft(23, 2, 54, 22, 2, 52)
    sprite('pt200_02ex01', 2)
    RandomCommonVoiceline(0)
    sprite('pt200_03ex01', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    gotoLabel(2)
    label(0)
    sprite('pt200_01', 3)
    CommonSE('003_swing_grap_0_0')
    SLOT_52 = 1
    if CharacterIDCheck('pt'):
        if CharacterIDCheck('pt'):
            CopyFromRightToLeft(23, 2, 54, 22, 2, 53)
    sprite('pt200_02', 2)
    RandomCommonVoiceline(0)
    sprite('pt200_03', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    gotoLabel(2)
    label(1)
    sprite('pt200_01', 3)
    CommonSE('003_swing_grap_0_0')
    SLOT_53 = 1
    if CharacterIDCheck('pt'):
        if CharacterIDCheck('pt'):
            CopyFromRightToLeft(23, 2, 54, 22, 2, 51)
    sprite('pt200_02ex00', 2)
    RandomCommonVoiceline(0)
    sprite('pt200_03ex00', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    gotoLabel(2)
    label(2)
    sprite('pt200_04', 4)
    SLOT_51 = 0
    SLOT_52 = 0
    SLOT_53 = 0
    sprite('pt200_05', 4)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(580)
        AirPushbackY(20000)
        DamageEffect(6, 'ptef_hit_middle')
        StayAfterMovement(1, 0)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('ChainLandDrive')
    sprite('pt201_00', 3)
    sprite('pt201_01', 4)
    sprite('pt201_02', 2)
    physicsXImpulse(8000)
    sprite('pt201_03', 1)
    CommonSE('008_swing_pole_2')
    sprite('pt201_04', 4)
    RandomCommonVoiceline(1)
    sprite('pt201_05', 2)
    XImpulseAcceleration(20)
    sprite('pt201_06', 3)
    Recovery()
    Unknown2063()
    sprite('pt201_07', 3)
    physicsXImpulse(0)
    sprite('pt201_08', 3)
    sprite('pt201_09', 2)
    LandingEffects(100, 1, 1)
    sprite('pt201_10', 2)
    sprite('pt201_11', 2)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(810)
        DamageEffect(6, 'ptef_hit_high')
        AirUntechableTime(19)
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('ChainLandDrive')
        HitOrBlockJumpCancel(1)
    sprite('pt202_00', 2)
    sprite('pt202_01', 3)
    sprite('pt202_03', 3)
    CommonSE('003_swing_grap_0_1')
    sprite('pt202_04', 6)
    RandomCommonVoiceline(2)
    sprite('pt202_05', 4)
    CommonSE('014_electric_m')
    Recovery()
    Unknown2063()
    sprite('pt202_06', 4)
    sprite('pt202_07', 4)
    sprite('pt202_08', 1)
    sprite('pt202_09', 2)
    sprite('pt202_10', 4)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(300)
        PushbackX(12000)
        AttackP1(80)
        HitLow(2)
        DamageEffect(6, 'ptef_hit_low')
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('ChainLandDrive')
    sprite('pt230_00', 4)
    PerInertia(60)
    sprite('pt230_01', 3)
    sprite('pt230_02', 3)
    CommonSE('007_swing_knife_0')
    RandomCommonVoiceline(0)
    sprite('pt230_03', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('pt230_04', 4)
    sprite('pt230_05', 3)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(560)
        DamageEffect(6, 'ptef_hit_middle')
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3C')
        callSubroutine('ChainLandDrive')
    sprite('pt231_00', 2)
    sprite('pt231_01', 4)
    sprite('pt231_02', 2)
    sprite('pt231_03', 1)
    RandomCommonVoiceline(1)
    CommonSE('008_swing_pole_2')
    sprite('pt231_04', 3)
    sprite('pt231_05', 5)
    Recovery()
    Unknown2063()
    sprite('pt231_06', 6)
    sprite('pt231_07', 5)
    sprite('pt231_08', 5)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(870)
        DamageEffect(6, 'ptef_hit_high')
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        CHGroundedHitstunAnimation(18)
        CHAirHitstunAnimation(18)
        AirPushbackX(2000)
        AirPushbackY(39000)
        CHAirPushbackY(45000)
        EnemyHitstopAddition(0, 0, 20)
        AirUntechableTime(44)
        AttackP1(90)
        AttackP2(82)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        callSubroutine('ChainLandDrive')
    sprite('pt232_00', 3)
    sprite('pt232_01', 2)
    sprite('pt232_02', 1)
    sprite('pt232_02', 2)
    sprite('pt232_03', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('pt232_04', 3)
    CreateParticle('ptef_232attack', 0)
    sprite('pt232_05', 8)
    RandomCommonVoiceline(2)
    CommonSE('009_swing_rapier_2')
    sprite('pt232_06', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('pt232_07', 4)
    sprite('pt232_08', 4)
    sprite('pt232_09', 4)
    sprite('pt232_10', 3)
    sprite('pt232_11', 3)
    sprite('pt232_12', 3)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(850)
        AttackP1(90)
        CHHardKnockdown(1)
        EnableEmergencyTechAirHit(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HitLow(2)
        AirPushbackX(3000)
        AirPushbackY(17000)
        AirUntechableTime(30)
        callSubroutine('ChainLandDrive')

        def upon_STATE_END():
            ExtendCollisionX(0)
    sprite('pt234_00', 3)
    sprite('pt234_01', 4)
    sprite('pt234_02', 2)
    ExtendCollisionX(50)
    sprite('pt234_03', 2)
    CommonSE('009_swing_rapier_2')
    RandomCommonVoiceline(2)
    ExtendCollisionX(100)
    sprite('pt234_04', 3)
    ExtendCollisionX(200)
    sprite('pt234_05', 3)
    Recovery()
    Unknown2063()
    sprite('pt234_06', 2)
    ExtendCollisionX(100)
    sprite('pt234_07', 2)
    ExtendCollisionX(50)
    sprite('pt234_08', 3)
    ExtendCollisionX(0)
    sprite('pt234_09', 3)
    sprite('pt234_10', 3)
    sprite('pt234_11', 3)
    sprite('pt234_12', 3)
    sprite('pt234_13', 2)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        DamageEffect(6, 'ptef_hit_low')
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAirThrow')
        callSubroutine('ChainAirDrive')
        HitOrBlockJumpCancel(1)
    sprite('pt250_00', 3)
    sprite('pt250_01', 3)
    sprite('pt250_02', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    sprite('pt250_03', 3)
    Recovery()
    Unknown2063()
    sprite('pt250_04', 3)
    sprite('pt250_05', 3)


@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        DamageEffect(6, 'ptef_hit_low')
        HitOrBlockCancel('NmlAtkAIR5A3rd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAirThrow')
        callSubroutine('ChainAirDrive')
        HitOrBlockJumpCancel(1)
    sprite('pt250_01', 3)
    sprite('pt250_02ex00', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    StartMultihit()
    sprite('pt250_02ex00', 2)
    sprite('pt250_03ex00', 3)
    Recovery()
    Unknown2063()
    sprite('pt250_04', 3)
    sprite('pt250_05', 3)


@State
def NmlAtkAIR5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        DamageEffect(6, 'ptef_hit_low')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        HitOrBlockCancel('NmlAtkAirThrow')
        callSubroutine('ChainAirDrive')
        HitOrBlockJumpCancel(1)
    sprite('pt250_01', 3)
    sprite('pt250_02ex01', 2)
    RandomCommonVoiceline(0)
    CommonSE('003_swing_grap_0_0')
    StartMultihit()
    sprite('pt250_02ex01', 2)
    sprite('pt250_03ex01', 3)
    Recovery()
    Unknown2063()
    sprite('pt250_04', 3)
    sprite('pt250_05', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(540)
        DamageEffect(6, 'ptef_hit_middle')
        AttackP1(80)
        AirUntechableTime(17)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2C')
        callSubroutine('ChainAirDrive')
        HitOrBlockJumpCancel(1)
    sprite('pt251_00', 1)
    sprite('pt251_01', 2)
    sprite('pt251_02', 2)
    sprite('pt251_03', 2)
    RandomCommonVoiceline(1)
    CommonSE('019_cloth_a')
    CommonSE('019_cloth_a')
    sprite('pt251_04', 3)
    sprite('pt251_05', 3)
    sprite('pt251_06', 3)
    Recovery()
    Unknown2063()
    sprite('pt251_07', 3)
    sprite('pt251_08', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(830)
        DamageEffect(6, 'ptef_hit_high')
        AttackP1(80)
        AirUntechableTime(23)
        Hitstun(19)
        HitOrBlockCancel('NmlAtkAIR2C')
        callSubroutine('ChainAirDrive')
        HitOrBlockJumpCancel(1)
        ForcedLandingRecovery(5, 1)
    sprite('pt252_00', 1)
    sprite('pt252_01', 2)
    sprite('pt252_02', 3)
    sprite('pt252_03', 2)
    sprite('pt252_04', 3)
    RandomCommonVoiceline(2)
    sprite('pt252_05', 3)
    CommonSE('008_swing_pole_2')
    sprite('pt252_06', 1)
    sprite('pt252_06', 2)
    StartMultihit()
    sprite('pt252_07', 4)
    Recovery()
    Unknown2063()
    sprite('pt252_08', 4)
    sprite('pt252_09', 3)


@State
def NmlAtkAIR2C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        Damage(450)
        PushbackX(12000)
        Hitstop(3)
        SingleProration(1)
        AttackP1(80)
        DamageEffect(6, 'ptef_hit_low')
        HitOrBlockJumpCancel(1)
    sprite('pt253_00', 2)
    sprite('pt253_01', 3)
    sprite('pt253_02', 3)
    sprite('pt253_03', 3)
    sprite('pt253_04', 2)
    RefreshMultihit()
    ForcedLandingRecovery(3, 1)
    RandomCommonVoiceline(2)
    CommonSE('004_swing_grap_1_0')
    PrivateSE('ptse_23')
    sprite('pt253_05', 2)
    sprite('pt253_04', 2)
    RefreshMultihit()
    sprite('pt253_05', 2)
    sprite('pt253_04', 2)
    RefreshMultihit()
    sprite('pt253_05', 2)
    sprite('pt253_06', 3)
    Recovery()
    Unknown2063()
    sprite('pt253_07', 3)
    sprite('pt253_08', 3)
    sprite('pt253_09', 3)
    sprite('pt253_10', 3)
    sprite('pt253_11', 3)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(630)
        AttackP1(90)
        CHGroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(26)
        AirPushbackY(22000)
        HitAirUnblockable(3)
        DamageEffect(6, 'ptef_hit_low')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        callSubroutine('ChainLandDrive')
        HitOrBlockJumpCancel(1)
    sprite('pt210_00', 3)
    sprite('pt210_01', 2)
    sprite('pt210_01', 3)
    setInvincible(1)
    SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('pt210_02', 3)
    sprite('pt210_03', 4)
    RandomCommonVoiceline(0)
    CommonSE('009_swing_rapier_0')
    sprite('pt210_04', 3)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('pt210_05', 3)
    sprite('pt210_06', 3)
    sprite('pt210_07', 3)
    sprite('pt210_08', 3)
    sprite('pt210_09', 3)
    sprite('pt210_10', 2)
    sprite('pt210_11', 2)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(640)
        DamageEffect(6, 'ptef_hit_low')
        AttackP1(90)
        AttackP2(79)
        BonusProration(110)
        HitOverhead(2)
        HitAirUnblockable(0)
        MoveAttributes(1, 0, 0, 0, 0)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirUntechableTime(33)
        Hitstun(20)
        PushbackX(19800)
        StarterRating(2)
        SpecialCancel(0)
        uponSendToLabel(LANDING, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SetActionMark(1)
    sprite('pt211_00', 3)
    sprite('pt211_01', 3)
    sprite('pt211_02', 3)
    sprite('pt211_03', 3)
    sprite('pt211_04', 3)
    sprite('pt211_05', 4)
    sprite('pt211_06', 4)
    physicsYImpulse(8000)
    physicsXImpulse(12000)
    SetAcceleration(200)
    setGravity(1600)
    CommonSE('003_swing_grap_0_1')
    RandomCommonVoiceline(1)
    sprite('pt211_07', 4)
    sprite('pt211_08', 32767)
    label(0)
    sprite('pt211_09', 3)
    EndMomentum(1)
    LandingEffects(104, 1, 1)
    Recovery()
    Unknown2063()
    if SLOT_2:
        conditionalSendToLabel(1)
    sprite('pt211_10', 4)
    sprite('pt211_11', 4)
    sprite('pt211_12', 4)
    sprite('pt211_13', 4)
    label(1)
    sprite('pt211_14', 2)
    sprite('pt211_15', 2)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(950)
        DamageEffect(6, 'ptef_hit_high')
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(40)
        AttackP1(90)
        AttackP2(84)
        FatalCounter(1)
        HitAirUnblockable(0)
        FatalCounter(1)
        StayAfterMovement(1, 0)
        ForcedLandingRecovery(5, 1)
        WhiffCancel('NmlAtkAIR5B')
        WhiffCancel('NmlAtkAIR5C')
        WhiffCancel('NmlAtkAIR2C')
        callSubroutine('ChainAirDrive')
        ChainCancel(0)
        SpecialCancel(0)
    sprite('pt212_00', 2)
    sprite('pt212_01', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 0)
    sprite('pt212_02', 3)
    sprite('pt212_03', 3)
    sprite('pt212_04', 2)
    sprite('pt212_05', 2)
    AddX(20000)
    uponSendToLabel(LANDING, 0)
    RandomCommonVoiceline(2)
    sprite('pt212_06', 3)
    sprite('pt212_07', 5)
    physicsYImpulse(26000)
    physicsXImpulse(6000)
    EndYPhysicsImpulse()
    AddX(30000)
    CommonSE('009_swing_rapier_2')
    sprite('pt212_08', 3)
    CreateObject('Atk6CZanzo', -1)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    SpecialCancel(1)
    HitOrBlockJumpCancel(1)
    sprite('pt212_09', 4)
    setInvincible(0)
    sprite('pt212_10', 6)
    sprite('pt212_11', 9)
    sprite('pt212_12', 32767)
    label(0)
    sprite('pt024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('pt024_01', 2)
    sprite('pt024_02', 1)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        PreventBlocking(1)
    sprite('pt203_00', 1)
    sprite('pt203_01', 2)
    sprite('pt203_02', 2)
    CreateObject('pt203_mahojin', -1)
    CreateObject('pt203_mahojinsub', -1)
    CreateObject('pt203_aura1', -1)
    CreateObject('pt203_aura2', -1)
    CreateObject('pt203_aura3', -1)
    sprite('pt203_02', 2)
    if random_(2, 0, 50):
        SmartVoiceline('pt106')
    else:
        SmartVoiceline('pt107')
    sprite('pt203_03', 1)
    CreateObject('pt203_stick', 0)
    sprite('pt203_04', 2)
    callSubroutine('ItemShuffle')
    PrivateSE('ptse_13')
    sprite('pt203_05', 8)
    sprite('pt203_06', 2)
    sprite('pt203_07', 2)
    sprite('pt203_08', 2)
    sprite('pt203_09', 2)
    sprite('pt203_10', 2)
    sprite('pt203_11', 1)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PreventBlocking(1)
    sprite('pt203_12', 2)
    sprite('pt203_13', 1)
    sprite('pt203_13', 1)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    CreateObject('pt203_airmahojin', -1)
    CreateObject('pt203_mahojinsub', -1)
    CreateObject('pt203_airaura1', -1)
    CreateObject('pt203_airaura2', -1)
    CreateObject('pt203_airaura3', -1)
    sprite('pt203_14', 2)
    sprite('pt203_03', 2)
    sprite('pt203_04', 1)
    CreateObject('pt203_stick', 0)
    callSubroutine('ItemShuffle')
    PrivateSE('ptse_13')
    sprite('pt203_05', 8)
    EndMomentum(1)
    if random_(2, 0, 50):
        SmartVoiceline('pt106')
    else:
        SmartVoiceline('pt107')
    sprite('pt203_06', 2)
    sprite('pt203_07', 2)
    sprite('pt203_08', 2)
    sprite('pt203_09', 2)
    sprite('pt203_15', 2)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    if SLOT_YVelocity < -10000:
        physicsYImpulse(-10000)
    XImpulseAcceleration(75)
    sprite('pt203_16', 1)


@State
def NmlAtk5D_Hanmmer():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackY(-42000)
        CHGroundBounce(1)
        BouncePercentage(50)
        AirUntechableTime(28)
        PushbackX(19800)
        HardKnockdown(1)
        GuardCrush(100, 1)
        SetActionMark(481)
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtk5D_Hanmmer')
    sprite('pt204_00', 2)
    sprite('pt204_01', 2)
    sprite('pt204_02', 1)
    if SLOT_4 == 2:
        sendToLabel(100)
    sprite('pt204_02', 1)
    AttackLevel_(4)
    AttackP2(82)
    Damage(1200)
    Blockstun(22)
    EnemyHitstopAddition(4, 4, 12)
    GuardCrushHitstun(37)
    DamageEffect(6, 'ptef_hit_middle')
    sprite('pt204_03', 4)
    callSubroutine('ItemConsume')
    sprite('pt204_04', 4)
    sprite('pt204_05', 1)
    SmartVoiceline('pt301')
    sprite('pt204_06', 5)
    CreateParticle('ptef_hammerDwave', 0)
    ScreenShake(0, 2500)
    PrivateSE('ptse_02')
    CommonSE('003_swing_grap_0_2')
    sprite('pt204_07', 3)
    CreateParticle('ptef_204dellight00', 0)
    CreateParticle('ptef_204dellight00', 1)
    CreateParticle('ptef_204dellight00', 2)
    CreateParticle('ptef_204dellight00', 3)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    CreateParticle('ptef_lightrod00', 3)
    sprite('pt204_08', 2)
    CreateParticle('ptef_204dellight', 0)
    CreateParticle('ptef_204dellight', 1)
    CreateParticle('ptef_204dellight', 2)
    sprite('pt204_08ex00', 2)
    sprite('pt204_09', 2)
    sprite('pt204_10', 2)
    sprite('pt204_11', 2)
    sprite('pt204_12', 2)
    sprite('pt204_13', 2)
    ExitState()
    label(100)
    sprite('pt204_02', 1)
    AttackLevel_(5)
    AttackP2(84)
    BonusProration(110)
    Damage(1500)
    Blockstun(25)
    EnemyHitstopAddition(4, 4, 12)
    GuardCrushHitstun(48)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SLOT_53 = 1
    sprite('pt204_14', 4)
    callSubroutine('ItemConsume')
    sprite('pt204_15', 4)
    sprite('pt204_16', 1)
    SmartVoiceline('pt303')
    sprite('pt204_17', 5)
    CreateParticle('ptef_hammerDshock', 0)
    CommonSE('005_swing_grap_2_1')
    ScreenShake(0, 12000)
    sprite('pt204_18', 3)
    if not SLOT_53:
        CreateObject('Atk5DHiquake', 100)
    CreateParticle('ptef_204dellight00', 0)
    CreateParticle('ptef_204dellight00', 1)
    CreateParticle('ptef_204dellight00', 2)
    CreateParticle('ptef_204dellight00', 3)
    CreateParticle('ptef_204dellight00', 4)
    CreateParticle('ptef_204dellight00', 5)
    CreateParticle('ptef_lightrod00', 2)
    CreateParticle('ptef_lightrod00', 3)
    CreateParticle('ptef_lightrod00', 4)
    CreateParticle('ptef_lightrod00', 6)
    sprite('pt204_19', 3)
    CreateParticle('ptef_204dellight', 0)
    CreateParticle('ptef_204dellight', 1)
    CreateParticle('ptef_204dellight', 2)
    CreateParticle('ptef_204dellight', 3)
    CreateParticle('ptef_204dellight', 4)
    CreateParticle('ptef_204dellight', 5)
    sprite('pt204_19ex00', 2)
    sprite('pt204_09', 2)
    sprite('pt204_10', 2)
    sprite('pt204_11', 2)
    sprite('pt204_12', 2)
    sprite('pt204_13', 2)
    ExitState()


@State
def NmlAtkAIR5D_Hanmmer():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        PushSpeedX()
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtk5D_Hanmmer')
            HitOrBlockCancel('NmlAtkAIR5D_Hanmmer')
    sprite('pt255_00', 2)
    sprite('keep', 1)
    if SLOT_4 == 2:
        sendToLabel(100)
    sprite('pt255_01', 2)
    AttackLevel_(4)
    Damage(700)
    AttackP2(82)
    AttackP1(80)
    PushbackX(0)
    AirPushbackX(-1000)
    AirPushbackY(-30000)
    AirUntechableTime(30)
    HardKnockdown(10)
    CHHardKnockdown(20)
    HitOverhead(0)
    DamageEffect(6, 'ptef_hit_middle')
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)
    XImpulseAcceleration(0)
    PerInertia(10)
    physicsYImpulse(1000)
    setGravity(10)
    sprite('pt255_02', 3)
    callSubroutine('ItemConsume')
    sprite('pt255_03', 3)
    SmartVoiceline('pt302')
    EndMomentum(1)
    PopSpeedX()
    XImpulseAcceleration(10)
    sprite('pt255_04', 3)
    setGravity(2000)

    def upon_EVERY_FRAME():
        if SLOT_YVelocity < -40000:
            SLOT_51 = 1
        if SLOT_YVelocity < -52000:
            SLOT_51 = 2
    label(0)
    sprite('pt255_05', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('pt255_06', 3)
    sprite('pt255_07', 3)
    sprite('pt255_08', 3)
    CommonSE('003_swing_grap_0_2')
    sprite('pt255_09', 3)
    sprite('pt255_04', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt255_10', 3)
    ForceFaceSprite()
    RefreshMultihit()
    GuardCrush(100, 1)
    SetActionMark(481)
    GuardCrushHitstun(37)
    GroundedHitstunAnimation(9)
    PushbackX(39900)
    ResetPushback()
    if SLOT_51 == 0:
        Damage(800)
        ScreenShake(0, 7500)
        EnemyHitstopAddition(5, 5, 10)
    if SLOT_51 == 1:
        Damage(900)
        ScreenShake(0, 50000)
        EnemyHitstopAddition(7, 7, 12)
    if SLOT_51 == 2:
        Damage(1000)
        AirPushbackX(0)
        AirPushbackY(-55000)
        AirUntechableTime(40)
        GroundBounce(1)
        BouncePercentage(30)
        HardKnockdownReset()
        ScreenShake(0, 100000)
        EnemyHitstopAddition(9, 9, 14)
    EndMomentum(1)
    PrivateSE('ptse_02')
    LandingEffects(100, 1, 1)
    CreateParticle('ptef_airhammerDwave', -1)
    sprite('pt255_11', 3)
    StartMultihit()
    CreateParticle('ptef_204dellight00', 0)
    CreateParticle('ptef_204dellight00', 1)
    CreateParticle('ptef_204dellight00', 2)
    sprite('pt255_12', 4)
    CreateParticle('ptef_204dellight', 0)
    CreateParticle('ptef_204dellight', 1)
    CreateParticle('ptef_204dellight', 2)
    Recovery()
    sprite('pt255_13', 4)
    sprite('pt255_14', 4)
    sprite('pt255_15', 5)
    ExitState()
    label(100)
    sprite('pt255_01', 2)
    AttackLevel_(5)
    AttackP2(84)
    BonusProration(110)
    Damage(900)
    AttackP1(80)
    PushbackX(4000)
    AirPushbackX(-1000)
    AirPushbackY(-60000)
    AirUntechableTime(30)
    HardKnockdown(20)
    HitOverhead(0)
    clearUponHandler(LANDING)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SLOT_53 = 1
    uponSendToLabel(LANDING, 102)
    XImpulseAcceleration(0)
    PerInertia(10)
    physicsYImpulse(1000)
    setGravity(10)
    sprite('pt255_02', 3)
    callSubroutine('ItemConsume')
    sprite('pt255_16', 3)
    SmartVoiceline('pt304')
    EndMomentum(1)
    PopSpeedX()
    XImpulseAcceleration(25)
    sprite('pt255_17', 3)
    setGravity(2000)

    def upon_EVERY_FRAME():
        if SLOT_YVelocity < -40000:
            SLOT_51 = 1
        if SLOT_YVelocity < -52000:
            SLOT_51 = 2
    label(101)
    sprite('pt255_18', 3)
    CommonSE('005_swing_grap_2_1')
    sprite('pt255_19', 3)
    sprite('pt255_20', 3)
    sprite('pt255_21', 3)
    CommonSE('005_swing_grap_2_1')
    sprite('pt255_22', 3)
    sprite('pt255_17', 3)
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('pt255_23', 3)
    ForceFaceSprite()
    RefreshMultihit()
    GuardCrush(100, 1)
    SetActionMark(481)
    GuardCrushHitstun(47)
    GroundedHitstunAnimation(9)
    PushbackX(39900)
    ResetPushback()
    if SLOT_51 == 0:
        Damage(1300)
        ScreenShake(0, 50000)
        EnemyHitstopAddition(5, 5, 10)
    if SLOT_51 == 1:
        Damage(1500)
        ScreenShake(0, 80000)
        EnemyHitstopAddition(7, 7, 12)
    if SLOT_51 == 2:
        Damage(1700)
        AirPushbackX(0)
        AirPushbackY(-52500)
        AirUntechableTime(40)
        GroundBounce(1)
        BouncePercentage(50)
        HardKnockdownReset()
        ScreenShake(0, 100000)
        EnemyHitstopAddition(9, 9, 14)
    EndMomentum(1)
    CommonSE('100_hit_grap_2')
    LandingEffects(100, 1, 1)
    CreateParticle('ptef_hammerDshock', 0)
    sprite('pt255_24', 3)
    if not SLOT_53:
        CreateObject('Atk5DHiquake', -1)
    StartMultihit()
    CreateParticle('ptef_204dellight00', 0)
    CreateParticle('ptef_204dellight00', 1)
    CreateParticle('ptef_204dellight00', 2)
    CreateParticle('ptef_204dellight00', 3)
    Recovery()
    sprite('pt255_12', 4)
    sprite('pt255_13', 4)
    CreateParticle('ptef_204dellight', 0)
    CreateParticle('ptef_204dellight', 1)
    CreateParticle('ptef_204dellight', 2)
    CreateParticle('ptef_204dellight', 3)
    CreateParticle('ptef_204dellight', 4)
    sprite('pt255_14', 4)
    sprite('pt255_15', 5)
    ExitState()


@Subroutine
def ThrowItemSelect():
    if SLOT_4 == 1:
        CreateObject('Hummer', 0)
    if SLOT_4 == 2:
        CreateObject('16t_Hummer', 0)
    if SLOT_4 == 3:
        CreateObject('Cat_Hummer', 0)
    if SLOT_4 == 4:
        CreateObject('Lion_Hummer', 0)
    if SLOT_4 == 5:
        CreateObject('Frying-pan', 0)
    if SLOT_4 == 6:
        CreateObject('Harisen', 0)
    if SLOT_4 == 7:
        CreateObject('Bat', 0)
    if SLOT_4 == 8:
        CreateObject('Kanabou', 0)
    if SLOT_4 == 15:
        CreateObject('Boomerang', 0)
    if SLOT_4 == 16:
        CreateObject('SPBoomerang', 0)


@State
def WeaponThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_58 = SLOT_OverdriveTimer
    sprite('pt208_00', 3)
    EndMomentum(1)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 2)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_04', 1)
    SLOT_4 % 2
    if not SLOT_0 == 0:
        CreateParticle('ptef_throwsmokeshort', 2)
    else:
        CreateParticle('ptef_throwsmoke', 2)
    CommonSE('016_explode_0')
    PrivateSE('ptse_01')
    sprite('pt405_05', 1)
    physicsXImpulse(-20000)
    callSubroutine('ThrowItemSelect')
    callSubroutine('ItemDiscard')
    sprite('pt405_05', 4)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(70)
    sprite('pt405_05', 5)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(30)
    sprite('pt405_06', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('pt208_08', 3)
    SpriteIfNot0(2, 2, 58)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    SpriteIfNot0(2, 2, 58)
    sprite('pt208_10', 3)
    SpriteIfNot0(2, 2, 58)


@State
def NmlAtk5D_Cat():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtk5D_Cat')
    sprite('pt204_00', 1)
    sprite('pt204_01', 1)
    sprite('pt204_02', 1)
    if SLOT_4 == 4:
        sendToLabel(100)
    sprite('pt206_00', 3)
    AttackLevel_(3)
    Damage(950)
    AttackP1(80)
    AttackP2(79)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(8000)
    AirPushbackY(-50000)
    AirUntechableTime(40)
    GroundBounce(1)
    BouncePercentage(25)
    CHHardKnockdown(1)
    DamageEffect(6, 'ptef_hit_middle')
    HitAirUnblockable(0)
    callSubroutine('ItemConsume')
    sprite('pt206_01', 3)
    sprite('pt206_02', 1)
    SmartVoiceline('pt305')
    sprite('pt206_03', 8)
    CreateParticle('ptef_hammerDwave02', 0)
    CommonSE('005_swing_grap_2_2')
    PrivateSE('ptse_24')
    sprite('pt206_04', 5)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_206dellight00', 1)
    CreateParticle('ptef_206dellight00', 2)
    CreateParticle('ptef_lightrod00', 2)
    CreateParticle('ptef_lightrod00', 3)
    CreateParticle('ptef_206dellight00', 4)
    Recovery()
    sprite('pt206_05', 3)
    CreateParticle('ptef_206dellight', 0)
    CreateParticle('ptef_206dellight', 1)
    CreateParticle('ptef_206dellight', 2)
    sprite('pt206_05ex00', 2)
    sprite('pt204_09', 2)
    sprite('pt204_10', 2)
    sprite('pt204_11', 2)
    sprite('pt204_12', 2)
    sprite('pt204_13', 2)
    ExitState()
    label(100)
    sprite('pt206_06', 3)
    AttackLevel_(4)
    Damage(1200)
    AttackP1(80)
    AttackP2(82)
    BonusProration(110)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(8000)
    AirPushbackY(-50000)
    AirUntechableTime(50)
    GroundBounce(1)
    BouncePercentage(25)
    CHHardKnockdown(1)
    DamageEffect(6, 'ptef_hit_middle')
    HitAirUnblockable(0)
    callSubroutine('ItemConsume')
    sprite('pt206_07', 3)
    sprite('pt206_08', 1)
    SmartVoiceline('pt307')
    sprite('pt206_09', 8)
    CommonSE('005_swing_grap_2_2')
    PrivateSE('ptse_07')
    sprite('pt206_10', 5)
    CreateParticle('ptef_206dellight00', 0)
    CreateParticle('ptef_206dellight00', 1)
    CreateParticle('ptef_206dellight00', 3)
    CreateParticle('ptef_206dellight00', 5)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 4)
    CreateParticle('ptef_lightrod00', 5)
    Recovery()
    sprite('pt206_11', 3)
    CreateParticle('ptef_206dellight', 0)
    CreateParticle('ptef_206dellight', 1)
    CreateParticle('ptef_206dellight', 2)
    CreateParticle('ptef_206dellight', 3)
    CreateParticle('ptef_206dellight', 4)
    CreateParticle('ptef_206dellight', 5)
    sprite('pt206_11', 3)
    sprite('pt204_09', 2)
    sprite('pt204_10', 2)
    sprite('pt204_11', 2)
    sprite('pt204_12', 2)
    sprite('pt204_13', 2)
    ExitState()


@State
def NmlAtkAIR5D_Cat():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtkAIR5D_Cat')
    sprite('pt257_00', 2)
    sprite('keep', 1)
    if SLOT_4 == 4:
        sendToLabel(100)
    sprite('pt257_01', 4)
    AttackLevel_(3)
    Damage(950)
    AttackP1(80)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-50000)
    AirUntechableTime(40)
    CHGroundBounce(1)
    CHBouncePercentage(35)
    HardKnockdown(1)
    DamageEffect(6, 'ptef_hit_middle')
    HitOverhead(0)
    EndMomentum(1)
    physicsYImpulse(20000)
    physicsXImpulse(2000)
    EndYPhysicsImpulse()
    ForcedLandingRecovery(5, 1)
    sprite('pt257_02', 4)
    sprite('pt257_03', 4)
    callSubroutine('ItemConsume')
    SmartVoiceline('pt306')
    sprite('pt257_04', 4)
    PrivateSE('ptse_24')
    CommonSE('005_swing_grap_2_2')
    sprite('pt257_05', 1)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_206dellight00', 1)
    CreateParticle('ptef_lightrod00', 2)
    CreateParticle('ptef_lightrod00', 3)
    sprite('pt257_05', 2)
    StartMultihit()
    Recovery()
    sprite('pt257_06', 3)
    CreateParticle('ptef_206dellight', 0)
    CreateParticle('ptef_206dellight', 1)
    CreateParticle('ptef_206dellight', 2)
    sprite('pt257_07', 2)
    sprite('pt257_08', 2)
    sprite('pt257_09', 3)
    sprite('pt257_10', 2)
    sprite('pt257_11', 2)
    sprite('pt257_12', 4)
    ExitState()
    label(100)
    sprite('pt257_13', 3)
    AttackLevel_(4)
    Damage(1200)
    AttackP1(80)
    BonusProration(110)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-50000)
    AirUntechableTime(40)
    CHGroundBounce(1)
    CHBouncePercentage(35)
    HardKnockdown(1)
    DamageEffect(6, 'ptef_hit_middle')
    HitOverhead(0)
    EndMomentum(1)
    physicsYImpulse(20000)
    physicsXImpulse(2000)
    EndYPhysicsImpulse()
    ForcedLandingRecovery(5, 1)
    sprite('pt257_14', 3)
    sprite('pt257_15', 4)
    SmartVoiceline('pt308')
    callSubroutine('ItemConsume')
    sprite('pt257_16', 4)
    PrivateSE('ptse_07')
    CommonSE('005_swing_grap_2_2')
    sprite('pt257_17', 1)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_206dellight00', 1)
    CreateParticle('ptef_lightrod00', 2)
    CreateParticle('ptef_206dellight00', 3)
    CreateParticle('ptef_lightrod00', 4)
    sprite('pt257_17', 2)
    StartMultihit()
    Recovery()
    sprite('pt257_18', 3)
    CreateParticle('ptef_206dellight', 0)
    CreateParticle('ptef_206dellight', 1)
    CreateParticle('ptef_206dellight', 2)
    CreateParticle('ptef_206dellight', 3)
    sprite('pt257_07', 2)
    sprite('pt257_08', 2)
    sprite('pt257_09', 3)
    sprite('pt257_10', 2)
    sprite('pt257_11', 2)
    sprite('pt257_12', 4)
    ExitState()


@State
def NmlAtk5D_Harisen():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtk5D_Harisen')
    sprite('pt205_00', 2)
    sprite('keep', 1)
    if SLOT_4 == 6:
        sendToLabel(100)
    sprite('pt205_01', 3)
    AttackLevel_(3)
    Damage(850)
    AttackP2(79)
    GroundedHitstunAnimation(6)
    AirHitstunAnimation(10)
    AirPushbackX(4000)
    AirPushbackY(30000)
    Hitstun(30)
    AirUntechableTime(40)
    Hitstop(15)
    PushbackX(30400)
    DamageEffect(6, 'ptef_hit_fripan')
    sprite('pt207_00', 3)
    sprite('pt207_01', 2)
    SmartVoiceline('pt309')
    callSubroutine('ItemConsume')
    CommonSE('004_swing_grap_1_1')
    CommonSE('003_swing_grap_0_2')
    sprite('pt207_02', 2)
    sprite('pt207_03', 2)
    CreateParticle('ptef_207dellight00', 0)
    CreateParticle('ptef_207dellight00', 1)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    sprite('pt207_04', 5)
    CreateParticle('ptef_207dellight', 0)
    CreateParticle('ptef_207dellight', 1)
    Recovery()
    sprite('pt205_07', 3)
    sprite('pt205_08', 4)
    sprite('pt205_09', 3)
    sprite('pt205_10', 3)
    ExitState()
    label(100)
    sprite('pt205_01', 3)
    AttackLevel_(4)
    Damage(1300)
    AttackP2(82)
    BonusProration(110)
    GroundedHitstunAnimation(6)
    AirHitstunAnimation(10)
    AirPushbackX(4000)
    AirPushbackY(36000)
    Hitstun(40)
    AirUntechableTime(60)
    Hitstop(20)
    FatalCounter(1)
    DamageEffect(2, 'ptef_hit_harisen')
    GotoState('NmlAtk5D_HarisenSP')
    sprite('pt207_05', 3)
    sprite('pt207_06', 2)
    SmartVoiceline('pt311')
    callSubroutine('ItemConsume')
    CommonSE('004_swing_grap_1_1')
    CommonSE('003_swing_grap_0_2')
    sprite('pt207_07', 2)
    sprite('pt207_08', 2)
    CreateParticle('ptef_207dellight00', 1)
    CreateParticle('ptef_207dellight00', 2)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    sprite('pt207_09', 5)
    CreateParticle('ptef_207dellight', 0)
    CreateParticle('ptef_207dellight', 1)
    Recovery()
    sprite('pt205_07', 3)
    sprite('pt205_08', 4)
    sprite('pt205_09', 3)
    sprite('pt205_10', 3)
    ExitState()


@State
def NmlAtkAIR5D_Harisen():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtkAIR5D_Harisen')
    sprite('pt257_00', 2)
    sprite('keep', 1)
    if SLOT_4 == 6:
        sendToLabel(100)
    sprite('pt258_00', 1)
    AttackLevel_(3)
    Damage(850)
    AttackP1(80)
    AttackP2(79)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-48000)
    YImpulseBeforeWallbounce(0)
    AirUntechableTime(50)
    GroundBounce(1)
    BouncePercentage(50)
    Hitstop(15)
    DamageEffect(6, 'ptef_hit_fripan')
    StarterRating(2)
    EndMomentum(1)
    sprite('pt258_00', 3)
    physicsYImpulse(20000)
    physicsXImpulse(2000)
    EndYPhysicsImpulse()
    sprite('pt258_01', 4)
    sprite('pt258_02', 3)
    SmartVoiceline('pt310')
    callSubroutine('ItemConsume')
    CommonSE('004_swing_grap_1_1')
    CommonSE('003_swing_grap_0_2')
    sprite('pt258_03', 2)
    sprite('pt258_04', 2)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    sprite('pt258_05', 2)
    CreateParticle('ptef_207dellight', 0)
    CreateParticle('ptef_207dellight', 1)
    Recovery()
    sprite('pt257_07', 3)
    sprite('pt257_08', 3)
    sprite('pt257_09', 3)
    sprite('pt257_10', 3)
    sprite('pt257_11', 3)
    sprite('pt257_12', 3)
    ExitState()
    label(100)
    sprite('pt258_06', 1)
    AttackLevel_(4)
    Damage(1300)
    AttackP1(80)
    AttackP2(82)
    BonusProration(110)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-48000)
    YImpulseBeforeWallbounce(0)
    AirUntechableTime(65)
    GroundBounce(1)
    BouncePercentage(50)
    Hitstop(20)
    FatalCounter(1)
    DamageEffect(2, 'ptef_hit_harisen')
    StarterRating(2)
    EndMomentum(1)
    sprite('pt258_06', 2)
    physicsYImpulse(20000)
    physicsXImpulse(2000)
    EndYPhysicsImpulse()
    sprite('pt258_07', 3)
    sprite('pt258_08', 3)
    SmartVoiceline('pt312')
    callSubroutine('ItemConsume')
    CommonSE('004_swing_grap_1_1')
    CommonSE('003_swing_grap_0_2')
    sprite('pt258_09', 2)
    sprite('pt258_10', 2)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    CreateParticle('ptef_lightrod00', 3)
    CreateParticle('ptef_207dellight', 4)
    sprite('pt258_11', 2)
    CreateParticle('ptef_207dellight', 0)
    CreateParticle('ptef_207dellight', 1)
    CreateParticle('ptef_207dellight', 2)
    Recovery()
    sprite('pt257_07', 3)
    sprite('pt257_08', 3)
    sprite('pt257_09', 3)
    sprite('pt257_10', 3)
    sprite('pt257_11', 3)
    sprite('pt257_12', 3)
    ExitState()


@State
def NmlAtk5D_Bat():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtk5D_Bat')
    sprite('pt205_00', 2)
    setInvincible(1)
    sprite('keep', 1)
    if SLOT_4 == 8:
        sendToLabel(100)
    sprite('pt205_01', 4)
    AttackLevel_(2)
    Damage(900)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(13000)
    AirPushbackY(34000)
    CHGroundedHitstunAnimation(19)
    CHAirHitstunAnimation(19)
    CHAirPushbackX(36000)
    CHAirPushbackY(30000)
    AttackP1(60)
    AttackP2(75)
    AirUntechableTime(30)
    Wallbounce(1)
    NonCornerWallbounce(1)
    NonCornerCHWallbounce(0)
    WallbounceReboundTime(10)
    AirHitstunAfterWallbounce(40)
    Wallstick(1)
    WallstickDuration(25)
    Hitstop(22)
    DamageEffect(6, 'ptef_hit_bat')
    StarterRating(0)
    sprite('pt205_02', 3)
    SmartVoiceline('pt313')
    sprite('pt205_03', 1)
    callSubroutine('ItemConsume')
    CommonSE('005_swing_grap_2_2')
    sprite('pt205_04', 2)
    setInvincible(0)
    sprite('pt205_05', 1)
    CreateParticle('ptef_205dellight00', 0)
    CreateParticle('ptef_205dellight00', 1)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    sprite('pt205_06', 6)
    CreateParticle('ptef_205dellight', 0)
    CreateParticle('ptef_205dellight', 1)
    CreateParticle('ptef_205dellight', 2)
    sprite('pt205_07', 5)
    sprite('pt205_08', 5)
    sprite('pt205_09', 5)
    sprite('pt205_10', 5)
    ExitState()
    label(100)
    sprite('pt205_01', 4)
    AttackLevel_(4)
    Damage(1200)
    AttackP1(60)
    AttackP2(82)
    BonusProration(110)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(38000)
    CHGroundedHitstunAnimation(19)
    CHAirHitstunAnimation(19)
    CHAirPushbackX(38000)
    CHAirPushbackY(30000)
    Hitstop(26)
    AirUntechableTime(30)
    Wallbounce(1)
    NonCornerWallbounce(1)
    NonCornerCHWallbounce(0)
    WallbounceReboundTime(10)
    AirHitstunAfterWallbounce(40)
    Wallstick(1)
    WallstickDuration(30)
    DamageEffect(6, 'ptef_hit_kanabou')
    StarterRating(0)
    sprite('pt205_11', 3)
    SmartVoiceline('pt315')
    sprite('pt205_12', 1)
    callSubroutine('ItemConsume')
    CommonSE('005_swing_grap_2_2')
    sprite('pt205_13', 2)
    sprite('pt205_14', 2)
    CreateParticle('ptef_205dellight00', 0)
    CreateParticle('ptef_205dellight00', 1)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    sprite('pt205_15', 5)
    setInvincible(0)
    CreateParticle('ptef_205dellight', 0)
    CreateParticle('ptef_205dellight', 1)
    CreateParticle('ptef_205dellight', 2)
    sprite('pt205_07', 5)
    sprite('pt205_08', 5)
    sprite('pt205_09', 5)
    sprite('pt205_10', 4)
    ExitState()


@State
def NmlAtkAIR5D_Bat():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        SpecialCancel(0)
        SpecialCancelOnHit(1)
        if SLOT_OverdriveTimer:
            HitOrBlockCancel('NmlAtkAIR5D_Bat')
    sprite('pt256_00', 2)
    setInvincible(1)
    sprite('keep', 1)
    if SLOT_4 == 8:
        sendToLabel(100)
    sprite('pt256_01', 1)
    AttackLevel_(2)
    Damage(900)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(13000)
    AirPushbackY(30000)
    CHGroundedHitstunAnimation(19)
    CHAirHitstunAnimation(19)
    CHAirPushbackX(36000)
    CHAirPushbackY(30000)
    AirUntechableTime(30)
    AttackP1(60)
    AttackP2(75)
    Wallbounce(1)
    NonCornerWallbounce(1)
    NonCornerCHWallbounce(0)
    WallbounceReboundTime(10)
    AirHitstunAfterWallbounce(40)
    Wallstick(1)
    WallstickDuration(20)
    Hitstop(22)
    DamageEffect(6, 'ptef_hit_bat')
    StarterRating(0)
    EndMomentum(1)
    sprite('pt256_01', 3)
    physicsYImpulse(16000)
    physicsXImpulse(2000)
    setGravity(1850)
    ForcedLandingRecovery(7, 1)
    sprite('pt256_02', 3)
    SmartVoiceline('pt314')
    sprite('pt256_03', 1)
    callSubroutine('ItemConsume')
    CommonSE('005_swing_grap_2_2')
    sprite('pt256_03', 2)
    setInvincible(0)
    sprite('pt256_04', 1)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    sprite('pt256_04', 4)
    sprite('pt256_05', 2)
    EndYPhysicsImpulse()
    sprite('pt256_06', 4)
    CreateParticle('ptef_205dellight', 0)
    CreateParticle('ptef_205dellight', 1)
    CreateParticle('ptef_205dellight', 2)
    sprite('pt256_07', 3)
    sprite('pt256_08', 3)
    sprite('pt256_09', 4)
    sprite('pt256_10', 3)
    sprite('pt256_11', 3)
    ExitState()
    label(100)
    sprite('pt256_01', 1)
    AttackLevel_(4)
    Damage(1200)
    AttackP1(60)
    AttackP2(82)
    BonusProration(110)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(13000)
    AirPushbackY(29000)
    CHAirPushbackX(38000)
    CHAirPushbackY(27000)
    AirUntechableTime(30)
    Hitstop(26)
    Wallbounce(1)
    NonCornerWallbounce(1)
    NonCornerCHWallbounce(0)
    WallbounceReboundTime(10)
    AirHitstunAfterWallbounce(40)
    Wallstick(1)
    WallstickDuration(25)
    DamageEffect(6, 'ptef_hit_kanabou')
    StarterRating(0)
    EndMomentum(1)
    sprite('pt256_01', 3)
    physicsYImpulse(16000)
    physicsXImpulse(2000)
    setGravity(1850)
    ForcedLandingRecovery(7, 1)
    sprite('pt256_12', 3)
    SmartVoiceline('pt316')
    sprite('pt256_13', 1)
    callSubroutine('ItemConsume')
    CommonSE('005_swing_grap_2_2')
    sprite('pt256_13', 4)
    setInvincible(0)
    sprite('pt256_14', 5)
    CreateParticle('ptef_lightrod00', 0)
    CreateParticle('ptef_lightrod00', 1)
    CreateParticle('ptef_lightrod00', 2)
    sprite('pt256_15', 1)
    EndYPhysicsImpulse()
    sprite('pt256_16', 4)
    CreateParticle('ptef_205dellight00', 0)
    CreateParticle('ptef_205dellight00', 1)
    CreateParticle('ptef_205dellight00', 2)
    sprite('pt256_07', 3)
    sprite('pt256_08', 3)
    sprite('pt256_09', 4)
    sprite('pt256_10', 3)
    sprite('pt256_11', 3)
    ExitState()


@State
def NmlAtk5D_Bomb():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtk5D_Bomb')
    sprite('pt208_00', 2)
    EndMomentum(1)
    sprite('pt208_01', 1)
    if SLOT_4 == 10:
        sendToLabel(100)
    sprite('pt208_02', 4)
    sprite('pt208_03', 4)
    sprite('pt208_04', 4)
    sprite('pt208_05', 2)
    sprite('pt208_06', 1)
    SmartVoiceline('pt317')
    physicsXImpulse(-15000)
    sprite('pt208_06', 6)
    XImpulseAcceleration(70)
    CreateObject('Bomb', 0)
    RegisterObject(4, 1)
    callSubroutine('BombThrowCtrl')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    sprite('pt208_06', 6)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 2)
    sprite('pt208_08', 2)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt208_02', 4)
    sprite('pt208_03', 4)
    sprite('pt208_04', 4)
    sprite('pt208_05', 2)
    sprite('pt208_06', 1)
    SmartVoiceline('pt319')
    physicsXImpulse(-15000)
    sprite('pt208_06', 6)
    XImpulseAcceleration(70)
    CreateObject('SpBomb', 0)
    RegisterObject(4, 1)
    callSubroutine('BombThrowCtrl')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    sprite('pt208_06', 6)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 2)
    sprite('pt208_08', 2)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def NmlAtkAIR5D_Bomb():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtkAIR5D_Bomb')
    sprite('pt208_00', 2)
    sprite('keep', 1)
    if SLOT_4 == 10:
        sendToLabel(100)
    sprite('pt208_01', 3)
    EndMomentum(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    XImpulseAcceleration(20)
    setGravity(1500)
    sprite('pt208_02', 3)
    sprite('pt208_03', 3)
    sprite('pt208_04', 3)
    sprite('pt208_05', 3)
    SmartVoiceline('pt318')
    sprite('pt208_06', 1)
    physicsXImpulse(-10000)
    CreateObject('Bomb', 0)
    RegisterObject(4, 1)
    callSubroutine('BombThrowCtrl')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    sprite('pt208_06', 4)
    XImpulseAcceleration(70)
    sprite('pt208_06', 5)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)
    GravityDefault()
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt208_01', 3)
    EndMomentum(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    XImpulseAcceleration(20)
    setGravity(1500)
    sprite('pt208_02', 3)
    sprite('pt208_03', 3)
    sprite('pt208_04', 3)
    sprite('pt208_05', 3)
    SmartVoiceline('pt320')
    sprite('pt208_06', 1)
    physicsXImpulse(-10000)
    CreateObject('SpBomb', 0)
    RegisterObject(4, 1)
    callSubroutine('BombThrowCtrl')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    sprite('pt208_06', 4)
    XImpulseAcceleration(70)
    sprite('pt208_06', 5)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)
    GravityDefault()
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def WeaponThrow_Bomb():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('pt208_00', 2)
    EndMomentum(1)
    sprite('keep', 1)
    if SLOT_4 == 10:
        sendToLabel(100)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 3)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_05', 3)
    CreateObject('Bomb', 0)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 32)
    CreateParticle('ptef_throwsmokeshort', 0)
    callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)
    if SLOT_31 >= 1:
        CreateObject('Bomb', 0)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 33)
        ObjectUpon(STATE_END, 33)
        CreateParticle('ptef_throwsmokeshort', 1)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 4)
    if SLOT_31 >= 1:
        CreateObject('Bomb', 0)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 34)
        CreateParticle('ptef_throwsmokeshort', 2)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_06', 3)
    sprite('pt208_08', 3)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 2)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_04', 1)
    CreateParticle('ptef_throwsmoke', 2)
    CommonSE('016_explode_0')
    PrivateSE('ptse_01')
    sprite('pt405_05', 3)
    CreateObject('SpBomb', 0)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 32)
    callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)
    if SLOT_31 >= 1:
        CreateObject('SpBomb', 0)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 33)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 4)
    if SLOT_31 >= 1:
        CreateObject('SpBomb', 0)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 34)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_06', 3)
    sprite('pt208_08', 3)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def NmlAtk5D_Missaile():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtk5D_Missaile')
    sprite('pt208_00', 2)
    EndMomentum(1)
    sprite('keep', 1)
    if SLOT_4 == 12:
        sendToLabel(100)
    sprite('pt208_01', 3)
    sprite('pt208_02', 3)
    sprite('pt208_03', 3)
    sprite('pt208_04', 3)
    sprite('pt208_05', 3)
    SmartVoiceline('pt321')
    sprite('pt208_06', 1)
    physicsXImpulse(-20000)
    CreateObject('Missile', 1)
    CreateParticle('ptef_drivethrow', 1)
    callSubroutine('ItemConsume')
    sprite('pt208_06', 4)
    XImpulseAcceleration(70)
    sprite('pt208_06', 5)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt208_01', 3)
    sprite('pt208_02', 3)
    sprite('pt208_03', 3)
    sprite('pt208_04', 3)
    sprite('pt208_05', 3)
    SmartVoiceline('pt323')
    sprite('pt208_06', 1)
    physicsXImpulse(-20000)
    CreateObject('SpMissile', 1)
    CreateParticle('ptef_drivethrow', 1)
    callSubroutine('ItemConsume')
    sprite('pt208_06', 4)
    XImpulseAcceleration(70)
    sprite('pt208_06', 5)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)
    XImpulseAcceleration(0)
    sprite('pt208_08', 3)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def NmlAtkAIR5D_Missaile():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtkAIR5D_Missaile')
    sprite('pt208_00', 2)
    sprite('keep', 1)
    if SLOT_4 == 12:
        sendToLabel(100)
    sprite('pt208_01', 3)
    EndMomentum(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    XImpulseAcceleration(20)
    setGravity(1500)
    sprite('pt208_02', 3)
    sprite('pt208_03', 3)
    sprite('pt208_04', 3)
    sprite('pt208_05', 3)
    SmartVoiceline('pt322')
    sprite('pt208_06', 1)
    physicsXImpulse(-15000)
    CreateObject('Missile', 1)
    CreateParticle('ptef_drivethrow', 1)
    callSubroutine('ItemConsume')
    setGravity(1000)
    sprite('pt208_06', 4)
    XImpulseAcceleration(70)
    sprite('pt208_06', 5)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)
    GravityDefault()
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt208_01', 3)
    EndMomentum(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    XImpulseAcceleration(20)
    setGravity(1500)
    sprite('pt208_02', 3)
    sprite('pt208_03', 3)
    sprite('pt208_04', 3)
    sprite('pt208_05', 3)
    SmartVoiceline('pt324')
    sprite('pt208_06', 1)
    physicsXImpulse(-15000)
    CreateObject('SpMissile', 1)
    CreateParticle('ptef_drivethrow', 1)
    callSubroutine('ItemConsume')
    setGravity(1000)
    sprite('pt208_06', 4)
    XImpulseAcceleration(70)
    sprite('pt208_06', 5)
    XImpulseAcceleration(30)
    WhiffCancelEnable(1)
    sprite('pt208_07', 3)
    GravityDefault()
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def WeaponThrow_Missaile():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('pt208_00', 2)
    EndMomentum(1)
    sprite('keep', 1)
    if SLOT_4 == 12:
        sendToLabel(100)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 3)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_05', 1)
    physicsXImpulse(-30000)
    CreateObject('Missile', 1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 32)
    CreateParticle('ptef_throwsmokeshort', 1)
    callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)
    XImpulseAcceleration(70)
    sprite('pt405_05', 4)
    XImpulseAcceleration(50)
    if SLOT_31 >= 1:
        CreateObject('Missile', 0)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 33)
        CreateParticle('ptef_throwsmokeshort', 0)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 4)
    XImpulseAcceleration(30)
    if SLOT_31 >= 1:
        CreateObject('Missile', 2)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 34)
        CreateParticle('ptef_throwsmokeshort', 2)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_06', 3)
    XImpulseAcceleration(10)
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 3)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_05', 1)
    physicsXImpulse(-30000)
    if SLOT_31 >= 2:
        CreateObject('SpMissile', 1)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 32)
        CreateParticle('ptef_throwsmoke', 0)
        callSubroutine('ItemConsume_Throw')
    else:
        CreateObject('SpMissile', 1)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 34)
        CreateParticle('ptef_throwsmoke', 0)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)
    XImpulseAcceleration(70)
    sprite('pt405_05', 4)
    XImpulseAcceleration(50)
    sprite('pt405_05', 4)
    XImpulseAcceleration(30)
    sprite('pt405_06', 3)
    XImpulseAcceleration(10)
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    if SLOT_31 >= 1:
        gotoLabel(10)
    ExitState()
    label(10)
    sprite('pt208_00', 3)
    EndMomentum(1)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 3)
    sprite('pt405_05', 1)
    physicsXImpulse(-30000)
    if SLOT_31 >= 2:
        CreateObject('SpMissile', 1)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 33)
        CreateParticle('ptef_throwsmoke', 0)
        callSubroutine('ItemConsume_Throw')
    else:
        CreateObject('SpMissile', 1)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 34)
        CreateParticle('ptef_throwsmoke', 0)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)
    XImpulseAcceleration(70)
    sprite('pt405_05', 4)
    XImpulseAcceleration(50)
    sprite('pt405_05', 4)
    XImpulseAcceleration(30)
    sprite('pt405_06', 3)
    XImpulseAcceleration(10)
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    if SLOT_31 >= 1:
        gotoLabel(20)
    ExitState()
    label(20)
    sprite('pt208_00', 3)
    EndMomentum(1)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 3)
    sprite('pt405_05', 1)
    physicsXImpulse(-30000)
    if SLOT_31 >= 1:
        CreateObject('SpMissile', 1)
        RegisterObject(4, 1)
        ObjectUpon(FALLING, 34)
        CreateParticle('ptef_throwsmoke', 0)
        callSubroutine('ItemConsume_Throw')
    sprite('pt405_05', 3)
    XImpulseAcceleration(70)
    sprite('pt405_05', 4)
    XImpulseAcceleration(50)
    sprite('pt405_05', 4)
    XImpulseAcceleration(30)
    sprite('pt405_06', 3)
    XImpulseAcceleration(10)
    sprite('pt208_08', 3)
    XImpulseAcceleration(0)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def NmlAtk5D_Box():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtk5D_Box')
    sprite('pt209_00', 3)
    EndMomentum(1)
    sprite('keep', 1)
    if SLOT_4 == 14:
        sendToLabel(100)
    sprite('pt209_01', 4)
    sprite('pt209_00', 4)
    sprite('pt209_01', 4)
    sprite('pt209_02', 3)
    SmartVoiceline('pt325')
    sprite('pt209_03', 4)
    callSubroutine('TrapUpDate')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    RegisterObject(5, 1)
    ObjectUpon(5, 33)
    sprite('pt209_04', 5)
    WhiffCancelEnable(1)
    sprite('pt209_05', 5)
    ExitState()
    label(100)
    sprite('pt209_01', 4)
    sprite('pt209_00', 4)
    sprite('pt209_01', 4)
    sprite('pt209_02', 3)
    sprite('pt209_03', 4)
    SmartVoiceline('pt327')
    sprite('pt209_04', 5)
    callSubroutine('SpTrapUpDate')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    RegisterObject(5, 1)
    ObjectUpon(5, 33)
    sprite('pt209_05', 5)
    WhiffCancelEnable(1)
    ExitState()


@State
def NmlAtkAIR5D_Box():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtkAIR5D_Box')
    sprite('pt209_00', 4)
    sprite('keep', 1)
    if SLOT_4 == 14:
        sendToLabel(100)
    sprite('pt209_01', 5)
    CreateObject('pt203_airmahojin', -1)
    CreateObject('pt203_mahojinsub', -1)
    CreateObject('pt203_airaura1', -1)
    CreateObject('pt203_airaura2', -1)
    CreateObject('pt203_airaura3', -1)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    sprite('pt209_00', 4)
    sprite('pt209_01', 4)
    sprite('pt209_02', 3)
    SmartVoiceline('pt326')
    sprite('pt209_03', 5)
    callSubroutine('TrapUpDate')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    RegisterObject(5, 1)
    ObjectUpon(5, 33)
    sprite('pt209_04', 6)
    sprite('pt209_05', 3)
    sprite('pt209_06', 3)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    if SLOT_YVelocity < -10000:
        physicsYImpulse(-10000)
    XImpulseAcceleration(75)
    WhiffCancelEnable(1)
    sprite('pt209_07', 3)
    sprite('pt209_08', 3)
    sprite('pt209_09', 3)
    ExitState()
    label(100)
    sprite('pt209_01', 5)
    CreateObject('pt203_airmahojin', -1)
    CreateObject('pt203_mahojinsub', -1)
    CreateObject('pt203_airaura1', -1)
    CreateObject('pt203_airaura2', -1)
    CreateObject('pt203_airaura3', -1)
    PushSpeedX()
    PushSpeedY()
    PushGravity()
    EndMomentum(1)
    sprite('pt209_00', 4)
    sprite('pt209_01', 4)
    sprite('pt209_02', 3)
    sprite('pt209_03', 5)
    SmartVoiceline('pt328')
    sprite('pt209_04', 6)
    callSubroutine('SpTrapUpDate')
    CreateParticle('ptef_drivethrow', 0)
    callSubroutine('ItemConsume')
    RegisterObject(5, 1)
    ObjectUpon(5, 33)
    sprite('pt209_05', 3)
    sprite('pt209_06', 3)
    PopSpeedX()
    PopSpeedY()
    PopGravity()
    if SLOT_YVelocity < -10000:
        physicsYImpulse(-10000)
    XImpulseAcceleration(75)
    WhiffCancelEnable(1)
    sprite('pt209_07', 3)
    sprite('pt209_08', 3)
    sprite('pt209_09', 3)
    ExitState()


@State
def WeaponThrow_Box():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('pt208_00', 2)
    EndMomentum(1)
    sprite('keep', 1)
    if SLOT_4 == 14:
        sendToLabel(100)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 2)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_04', 1)
    CreateParticle('ptef_throwsmokeshort', 2)
    CommonSE('016_explode_0')
    sprite('pt405_05', 3)
    callSubroutine('TrapUpDate')
    callSubroutine('ItemConsume_Throw')
    RegisterObject(5, 1)
    ObjectUpon(5, 34)
    sprite('pt405_05', 3)
    if SLOT_31 >= 1:
        callSubroutine('TrapUpDate')
        callSubroutine('ItemConsume_Throw')
        RegisterObject(5, 1)
        ObjectUpon(5, 35)
    sprite('pt405_05', 4)
    sprite('pt405_06', 3)
    sprite('pt208_08', 3)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()
    label(100)
    sprite('pt405_00', 3)
    sprite('pt405_01', 3)
    sprite('pt405_02', 3)
    sprite('pt405_03', 3)
    sprite('pt405_04', 2)
    if random_(2, 0, 50):
        SmartVoiceline('pt207')
    else:
        SmartVoiceline('pt208')
    sprite('pt405_04', 1)
    CreateParticle('ptef_throwsmoke', 2)
    CommonSE('016_explode_0')
    sprite('pt405_05', 3)
    callSubroutine('SpTrapUpDate')
    callSubroutine('ItemConsume_Throw')
    RegisterObject(5, 1)
    ObjectUpon(5, 34)
    sprite('pt405_05', 3)
    if SLOT_31 >= 1:
        callSubroutine('SpTrapUpDate')
        callSubroutine('ItemConsume_Throw')
        RegisterObject(5, 1)
        ObjectUpon(5, 35)
    sprite('pt405_05', 4)
    sprite('pt405_06', 3)
    sprite('pt208_08', 3)
    sprite('pt208_09', 3)
    sprite('pt208_10', 3)
    ExitState()


@State
def NmlAtk5D_Boomerang():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        SpecialCancel(0)
        StayAfterMovement(1, 0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtk5D_Boomerang')
    sprite('pt409_00', 3)
    EndMomentum(1)
    sprite('pt409_01', 2)
    CreateObject('ptef_409_ring', -1)
    sprite('keep', 1)
    if SLOT_4 == 16:
        sendToLabel(100)
    sprite('pt409_02', 5)
    sprite('pt409_03', 5)
    sprite('pt409_04', 2)
    Voiceline('pt329')
    SetXCollisionFromOrigin(175)
    sprite('pt409_05', 2)
    SetXCollisionFromOrigin(200)
    CommonSE('009_swing_rapier_2')
    sprite('pt409_06', 3)
    CreateParticle('ptef409_feather', 1)
    ObjectUpon(CORNERED, 32)
    CreateObject('BoomerangAtk', 0)
    RegisterObject(7, 1)
    callSubroutine('ItemConsume')
    sprite('pt409_07', 3)
    sprite('pt409_08', 3)
    SetXCollisionFromOrigin(175)
    WhiffCancelEnable(1)
    sprite('pt409_09', 3)
    SetXCollisionFromOrigin(-1)
    sprite('pt409_10', 4)
    sprite('pt409_11', 3)
    sprite('pt409_12', 3)
    ExitState()
    label(100)
    sprite('pt409_02', 5)
    sprite('pt409_03', 5)
    sprite('pt409_04', 2)
    Voiceline('pt331')
    sprite('pt409_05', 2)
    CommonSE('009_swing_rapier_2')
    sprite('pt409_06', 3)
    CreateParticle('ptef409_feather', 1)
    ObjectUpon(CORNERED, 32)
    CreateObject('SPBoomerangAtk', 0)
    RegisterObject(7, 1)
    callSubroutine('ItemConsume')
    sprite('pt409_07', 3)
    sprite('pt409_08', 3)
    SetXCollisionFromOrigin(175)
    WhiffCancelEnable(1)
    sprite('pt409_09', 3)
    SetXCollisionFromOrigin(-1)
    sprite('pt409_10', 4)
    sprite('pt409_11', 3)
    sprite('pt409_12', 3)
    ExitState()


@State
def NmlAtkAIR5D_Boomerang():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        SpecialCancel(0)
        if SLOT_OverdriveTimer:
            WhiffCancel('NmlAtkAIR5D_Boomerang')
    sprite('pt409_00', 3)
    sprite('pt409_01', 2)
    CreateObject('ptef_409_ring_air', -1)
    sprite('keep', 1)
    if SLOT_4 == 16:
        sendToLabel(100)
    sprite('pt409_02ex01', 5)
    EndMomentum(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    XImpulseAcceleration(20)
    setGravity(1500)
    sprite('pt409_15', 5)
    sprite('pt409_16', 2)
    Voiceline('pt330')
    sprite('pt409_17', 2)
    CommonSE('009_swing_rapier_2')
    sprite('pt409_06ex01', 4)
    CreateParticle('ptef409_feather', 1)
    ObjectUpon(CORNERED, 32)
    CreateObject('BoomerangAtk', 0)
    RegisterObject(7, 1)
    callSubroutine('ItemConsume')
    sprite('pt409_07ex01', 3)
    sprite('pt409_08ex01', 3)
    WhiffCancelEnable(1)
    sprite('pt409_18', 3)
    sprite('pt409_19', 3)
    sprite('pt409_20', 3)
    sprite('pt409_21', 3)
    ExitState()
    label(100)
    sprite('pt409_02ex01', 5)
    EndMomentum(1)
    physicsYImpulse(16000)
    physicsXImpulse(-10000)
    XImpulseAcceleration(20)
    setGravity(1500)
    sprite('pt409_15', 5)
    sprite('pt409_16', 2)
    Voiceline('pt332')
    sprite('pt409_17', 2)
    CommonSE('009_swing_rapier_2')
    sprite('pt409_06ex01', 4)
    CreateParticle('ptef409_feather', 1)
    ObjectUpon(CORNERED, 32)
    CreateObject('SPBoomerangAtk', 0)
    RegisterObject(7, 1)
    callSubroutine('ItemConsume')
    sprite('pt409_07ex01', 3)
    sprite('pt409_08ex01', 3)
    WhiffCancelEnable(1)
    sprite('pt409_18', 3)
    sprite('pt409_19', 3)
    sprite('pt409_20', 3)
    sprite('pt409_21', 3)
    ExitState()


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('pt300_00', 4)
    sprite('pt300_01', 4)
    sprite('pt300_02', 4)
    sprite('pt300_03', 6)
    if random_(2, 0, 50):
        conditionalSendToLabel(0)
    sprite('pt300_04', 6)
    SmartVoiceline('pt404')
    sprite('pt300_05', 7)
    sprite('pt300_06', 6)
    sprite('pt300_07', 7)
    PrivateSE('ptse_00')
    gotoLabel(1)
    label(0)
    sprite('pt300_10', 6)
    SmartVoiceline('pt405')
    sprite('pt300_11', 7)
    sprite('pt300_12', 6)
    sprite('pt300_13', 7)
    PrivateSE('ptse_00')
    label(1)
    sprite('pt300_08', 9)
    sprite('pt300_09', 6)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        DamageEffect(6, 'ptef_hit_middle')
        StayAfterMovement(1, 0)
    sprite('pt201_00', 3)
    sprite('pt201_01', 3)
    sprite('pt201_02', 3)
    physicsXImpulse(8000)
    sprite('pt201_03', 3)
    CommonSE('008_swing_pole_2')
    sprite('pt201_04', 2)
    sprite('pt201_05', 2)
    XImpulseAcceleration(20)
    sprite('pt201_06', 3)
    sprite('pt201_07', 3)
    physicsXImpulse(0)
    sprite('pt201_08', 3)
    sprite('pt201_09', 3)
    LandingEffects(100, 1, 1)
    sprite('pt201_10', 9)
    sprite('pt201_09', 4)
    sprite('pt201_11', 4)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(12)
        AirPushbackX(45000)
        AirPushbackY(18000)
        AirUntechableTime(60)
        Floorslide(15)
        Wallbounce(1)
        WallbounceReboundTime(30)
        Wallstick(1)
        WallstickDuration(35)
        AirHitstunAfterWallbounce(60)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
        StayAfterMovement(1, 0)
        StarterRating(2)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 10:
                SetActionMark(481)
                GuardCrushHitstun(32)
                AttackP2(60)
                if CheckInput(0x5):
                    sendToLabel(0)
                elif CheckInput(0xe):
                    sendToLabel(0)
            if SLOT_StateDuration >= 20:
                clearUponHandler(OPPONENT_BLOCKS)
                SetActionMark(0)
                GuardCrushHitstun(60)
                AttackP2(100)
                StarterRating(3)
                if CheckInput(0x5):
                    sendToLabel(0)
                elif CheckInput(0xe):
                    sendToLabel(0)
                EnableAfterimage(1)
                AfterimageBlendMode(2)
                AfterimageColor_1(160, 0, 0, 0)
                AfterimageColor_2(96, 0, 0, 0)
                AfterimageMask_1(0, 8, 48, 192)
                AfterimageMask_2(0, 8, 48, 255)
                AfterimageSize_1(1010)
                AfterimageSize_2(900)
            if SLOT_StateDuration >= 50:
                sendToLabel(0)
    sprite('pt407_00', 3)
    sprite('pt407_01', 1)
    E0EAEffect('GuardCrushWind', 65535)
    CharacterFlash(16750300, 8, 2)
    Voiceline('pt159')
    HeatChange(-2500)
    sprite('pt407_01', 2)
    CharacterFlash(16763080, 8, 2)
    sprite('pt407_02', 3)
    label(100)
    sprite('pt407_03', 3)
    sprite('pt407_04', 3)
    sprite('pt407_05', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('keep', 1)
    clearUponHandler(EVERY_FRAME)
    sprite('pt407_03', 2)
    sprite('pt407_04', 2)
    sprite('pt407_05', 2)
    sprite('pt407_03', 2)
    sprite('pt407_06', 1)
    PrivateSE('ptse_08')
    PrivateSE('ptse_02')
    ParticleRotationAngle(90000)
    CallCustomizableParticle('ptef_guardcrushptc', 0)
    sprite('pt407_06', 3)
    StartMultihit()
    EnableAfterimage(0)
    sprite('pt407_07', 4)
    physicsXImpulse(-5000)
    sprite('pt407_08', 4)
    XImpulseAcceleration(70)
    sprite('pt407_09', 4)
    XImpulseAcceleration(40)
    sprite('pt407_10', 4)
    physicsXImpulse(0)
    sprite('pt407_11', 3)
    sprite('pt407_12', 3)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('pt310_00', 3)
    sprite('pt310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('pt310_02', 3)
    sprite('pt310_03', 3)
    SmartVoiceline('pt155')
    sprite('pt310_04', 3)
    sprite('pt310_05', 3)
    sprite('pt310_04', 3)
    sprite('pt310_05', 3)
    sprite('pt310_06', 3)
    sprite('pt310_07', 3)
    sprite('pt310_08', 2)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        Hitstop(20)
        PushbackX(10133)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(48)
        Crumple(38)
        DamageEffect(6, 'ptef_hit_throw')
        StarterRating(2)
        NoAttackDuringAction(1)

        def upon_OPPONENT_HIT():
            ObjectUpon(8, 35)
    sprite('pt310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('pt310_08', 3)
    CreateObject('ThrowKousoku', 0)
    RegisterObject(4, 1)
    Voiceline('pt153')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt311_00', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_00ex01', 4)
    CommonSE('022_magiccircle_b')
    PrivateSE('ptse_17')
    SFX_FOOTSTEP_(100, 1, 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_01ex01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_02ex01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_03ex01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('Kemuri', 0)
    sprite('pt203_04ex01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('MagicIron', 0)
    RegisterObject(8, 1)
    ObjectUpon(8, 32)
    DeleteObject(4)
    sprite('pt203_05ex01', 15)
    sprite('pt203_05ex01', 1)
    NoAttackDuringAction(0)
    sprite('pt203_06ex01', 4)
    sprite('pt203_07ex01', 4)
    sprite('pt203_08ex01', 4)
    sprite('pt203_09ex01', 4)
    sprite('pt203_10ex01', 4)
    sprite('pt203_11ex01', 3)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('pt310_00', 3)
    sprite('pt310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('pt310_02', 3)
    sprite('pt310_03', 3)
    SmartVoiceline('pt155')
    sprite('pt310_04', 3)
    sprite('pt310_05', 3)
    sprite('pt310_04', 3)
    sprite('pt310_05', 3)
    sprite('pt310_06', 3)
    sprite('pt310_07', 3)
    sprite('pt310_08', 2)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(18000)
        AirPushbackY(27000)
        AirUntechableTime(100)
        NonCornerWallbounce(1)
        Wallbounce(1)
        WallbounceReboundTime(1)
        DamageEffect(5, '')
        DamageFromStateOnly('BackThrowExeAdd')
        StarterRating(2)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        AttackOff()
        EnableRapidCancel(0)
        SpecialCancel(0)
    sprite('pt310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('pt310_02', 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('ThrowKousoku', 0)
    RegisterObject(4, 1)
    CommonSE('022_magiccircle_b')
    PrivateSE('ptse_17')
    NoAttackOffset(0)
    sprite('pt310_02', 1)
    RefreshMultihit()
    Hitstop(0)
    NoAttackOffset(1)
    EnemyHitstopAddition(100, 100, 100)
    sprite('pt203_07ex01', 3)
    SetXCollisionFromOrigin(50)
    EnableCollision(0)
    physicsXImpulse(60000)
    sprite('pt203_08ex01', 5)
    XImpulseAcceleration(33)
    sprite('pt203_09ex01', 5)
    XImpulseAcceleration(50)
    sprite('pt203_10ex01', 5)
    XImpulseAcceleration(50)
    sprite('keep', 5)
    enterState('BackThrowExeAdd')


@State
def BackThrowExeAdd():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AttackDirection(3)
        Hitstop(20)
        PushbackX(15200)
        EnemyHitstopAddition(0, 0, 5)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(48)
        Crumple(38)
        DamageEffect(6, 'ptef_hit_throw')
        StarterRating(2)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
        AttackOff()

        def upon_OPPONENT_HIT():
            ObjectUpon(8, 35)
    sprite('pt203_00ex01', 3)
    ForceFaceSprite()
    SetXCollisionFromOrigin(100)
    EnableCollision(1)
    XImpulseAcceleration(0)
    Voiceline('pt153')
    sprite('pt203_01ex01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_02ex01', 4)
    SFX_FOOTSTEP_(100, 1, 1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('Kemuri', 0)
    sprite('pt203_03ex01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('MagicIron', 0)
    RegisterObject(8, 1)
    ObjectUpon(8, 32)
    sprite('pt203_04ex01', 5)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_05ex01', 8)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    DeleteObject(4)
    sprite('pt203_05ex01', 1)
    RefreshMultihit()
    sprite('pt203_06ex01', 4)
    sprite('pt203_07ex01', 4)
    sprite('pt203_08ex01', 4)
    sprite('pt203_09ex01', 4)
    sprite('pt203_10ex01', 4)
    sprite('pt203_11ex01', 3)
    SFX_FOOTSTEP_(100, 1, 1)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('pt320_00', 3)
    sprite('pt320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('pt320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('pt320_03', 3)
    SmartVoiceline('pt155')
    sprite('pt320_04', 3)
    sprite('pt320_05', 3)
    sprite('pt320_04', 3)
    sprite('pt320_05', 3)
    sprite('pt320_06', 3)
    sprite('pt320_07', 3)
    sprite('pt320_08', 2)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(4)
        Damage(1500)
        AttackP2(50)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-35000)
        AirPushbackX(0)
        AirUntechableTime(100)
        HardKnockdown(1)
        BouncePercentage(40)
        GroundBounce(1)
        DamageEffect(6, 'ptef_hit_throw')
        StarterRating(2)
        ForcedLandingRecovery(0, 0)
        NoAttackDuringAction(1)

        def upon_OPPONENT_HIT():
            ObjectUpon(8, 37)
    sprite('pt320_02', 3)
    OppThrowAnimation(9, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    ThrowLock(1)
    sprite('pt203_12ex01', 4)
    Voiceline('pt154')
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('ThrowKousoku', 0)
    CommonSE('022_magiccircle_b')
    PrivateSE('ptse_17')
    RegisterObject(4, 1)
    sprite('pt203_13ex01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    sprite('pt203_14ex01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('Kemuri3', 0)
    sprite('pt203_03ex01', 4)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 1, 1, 0, 0)
    CreateObject('MagicIron', 0)
    RegisterObject(8, 1)
    ObjectUpon(8, 34)
    sprite('pt203_04ex01', 4)
    sprite('pt203_05ex01', 1)
    DeleteObject(4)
    NoAttackDuringAction(0)
    sprite('pt203_06ex01', 3)
    sprite('pt203_07ex01', 3)
    sprite('pt203_08ex01', 3)
    sprite('pt203_09ex01', 3)
    sprite('pt203_15ex01', 3)
    EndYPhysicsImpulse()
    sprite('pt203_16ex01', 3)


@State
def Oiuchi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(800)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(-19000)
        AirPushbackX(10000)
        GroundBounce(1)
        AirUntechableTime(33)
        YImpulseBeforeWallbounce(0)
        DamageEffect(6, 'ptef_hit_middle')
        RangeCheck(170000)
        uponSendToLabel(LANDING, 1)
        AttackOff()
        EnableAfterimage(1)
        AfterimageColor_1(255, 60, 60, 60)
        AfterimageColor_2(100, 60, 60, 60)
        AfterimageBlendMode(2)
    sprite('pt403_07ex', 1)
    if SLOT_IsAirborne:
        SLOT_67 = SLOT_19
        if SLOT_67 > 500000:
            SLOT_67 = 500000
        SLOT_XVelocity = SLOT_67
        XImpulseAcceleration(4)
        GotoState('OiuchiAIR')
    else:
        SLOT_67 = SLOT_19
        if SLOT_67 > 750000:
            SLOT_67 = 750000
        SLOT_XVelocity = SLOT_67
        XImpulseAcceleration(8)
    physicsYImpulse(19000)
    setGravity(4400)
    Voiceline('pt206')
    sprite('pt403_08ex', 2)
    sprite('pt403_09ex', 2)
    sprite('pt403_10ex', 2)
    sprite('pt403_17ex', 2)
    sprite('pt403_18ex', 32767)
    label(1)
    sprite('pt403_19ex', 1)
    PushSpeedX()
    EndMomentum(1)
    LandingEffects(104, 1, 1)
    sprite('pt403_20ex', 2)
    PrivateSE('ptse_08')
    RefreshMultihit()
    sprite('pt403_21ex', 2)
    sprite('pt403_20ex', 2)
    sprite('pt403_21ex', 2)
    PopSpeedX()
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    physicsXImpulse(-3000)
    physicsYImpulse(30000)
    setGravity(3700)
    sprite('pt403_22ex', 7)
    Recovery()
    sprite('pt403_29ex', 3)
    sprite('pt403_30ex', 3)
    sprite('pt403_06ex', 3)
    sprite('pt403_07ex', 32767)


@State
def Shabon_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('pt400_00', 2)
    sprite('pt400_01', 3)
    Voiceline('pt200')
    sprite('pt400_02', 3)
    sprite('pt400_03', 3)
    sprite('pt400_04', 4)
    sprite('pt400_05', 4)
    sprite('pt400_06', 5)
    CreateParticle('ptef_specialmc', -1)
    CreateObject('Shabon1', 1)
    sprite('pt400_07', 3)
    CommonSE('022_magiccircle_a')
    sprite('pt400_07', 2)
    CreateObject('Shabon2', 0)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 32)
    sprite('pt400_08', 5)
    sprite('pt400_09', 4)
    sprite('pt400_10', 4)
    sprite('pt400_11', 3)
    sprite('pt400_12', 3)


@State
def Shabon_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('pt400_00', 2)
    sprite('pt400_01', 3)
    Voiceline('pt200')
    sprite('pt400_02', 3)
    sprite('pt400_03', 3)
    sprite('pt400_04', 4)
    sprite('pt400_05', 4)
    sprite('pt400_06', 5)
    CreateParticle('ptef_specialmc', -1)
    CreateObject('Shabon1', 1)
    sprite('pt400_07', 3)
    CommonSE('022_magiccircle_a')
    sprite('pt400_07', 2)
    CreateObject('Shabon2', 0)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 33)
    sprite('pt400_08', 5)
    sprite('pt400_09', 4)
    sprite('pt400_10', 4)
    sprite('pt400_11', 3)
    sprite('pt400_12', 3)


@State
def Shabon_C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('pt400_00', 2)
    sprite('pt400_01', 3)
    Voiceline('pt200')
    sprite('pt400_02', 3)
    sprite('pt400_03', 3)
    sprite('pt400_04', 4)
    sprite('pt400_05', 4)
    sprite('pt400_06', 5)
    CreateParticle('ptef_specialmc', -1)
    CreateObject('Shabon1', 1)
    sprite('pt400_07', 3)
    CommonSE('022_magiccircle_a')
    sprite('pt400_07', 2)
    CreateObject('Shabon2', 0)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 34)
    sprite('pt400_08', 5)
    sprite('pt400_09', 4)
    sprite('pt400_10', 4)
    sprite('pt400_11', 3)
    sprite('pt400_12', 3)


@State
def Hopping():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        uponSendToLabel(LANDING, 0)
        Unknown2061(1)
        WhiffCancel('HoppingPlus_A')
        WhiffCancel('HoppingPlus_B')
        WhiffCancel('HoppingPlus_C')
    sprite('pt403_00', 2)
    CreateParticle('ptef_specialmc', -1)
    Voiceline('pt204')
    sprite('pt403_01', 2)
    sprite('pt403_02', 1)
    physicsXImpulse(16000)
    physicsYImpulse(26000)
    setGravity(2200)
    SLOT_60 = 0
    JumpEffects(1, 100)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('pt403_08', 2)
    sprite('pt403_09', 2)
    sprite('pt403_10', 2)
    sprite('pt403_17', 32767)
    WhiffCancelEnable(1)
    label(0)
    sprite('pt403_29', 2)
    setInvincible(0)
    EndMomentum(1)
    clearUponHandler(LANDING)
    sprite('pt403_30', 2)
    sprite('pt024_02', 2)


@Subroutine
def Hopping_Default():
    AttackLevel_(2)
    Damage(450)
    AttackP1(90)
    AttackP2(94)
    SameMoveProration(-1)
    GroundedHitstunAnimation(4)
    AirPushbackY(16000)
    Hitstun(20)
    AirUntechableTime(20)
    PushbackX(8000)
    AttackDirection(0)
    DamageEffect(6, 'ptef_hit_middle')
    if SLOT_60 >= 4:
        AirPushbackY(12000)
    Unknown2061(1)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 1)

    def upon_LANDING():
        EndMomentum(1)
    HitOrBlockCancel('HoppingPlus_A')
    HitOrBlockCancel('HoppingPlus_B')
    HitOrBlockCancel('HoppingPlus_C')


@State
def HoppingPlus_A():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Hopping_Default')

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_60 >= 4:
                XImpulseAcceleration(80)
                SetAcceleration(200)
            else:
                XImpulseAcceleration(50)
                SetAcceleration(400)
            XSpeed(-6000)
            physicsYImpulse(15000)
            setGravity(3000)
            if SLOT_60 == 7:
                Damage(1000)
                AttackP2(84)
                SameMoveProration(80)
                AirPushbackX(30000)
                AirPushbackY(-50000)
                AirUntechableTime(30)
                XSpeed(-500)
            if SLOT_60 == 3:
                Damage(500)
                AttackP2(84)
                SameMoveProration(80)
                GroundedHitstunAnimation(2)
                Crumple(22)
                AirPushbackX(36000)
                AirPushbackY(-30000)
                Floorslide(10)
                XSpeed(-6000)
    sprite('pt403_17', 1)
    if SLOT_60 == 2:
        ChainCancel(0)
    if SLOT_60 == 6:
        ChainCancel(0)
    sprite('pt403_18', 2)
    sprite('pt403_19', 2)
    sprite('pt403_20', 3)
    SLOT_60 = SLOT_60 + 1
    CreateObject('AssaultBwave', 0)
    PrivateSE('ptse_08')
    sprite('pt403_21', 3)
    sprite('pt403_22', 3)
    Recovery()
    sprite('pt403_10', 1)
    if SLOT_60 == 3:
        gotoLabel(0)
    if SLOT_60 == 7:
        gotoLabel(0)
    sprite('pt403_10', 32767)
    label(1)
    sprite('pt024_01', 4)
    EndMomentum(1)
    clearUponHandler(LANDING)
    WhiffCancelEnable(0)
    ChainCancel(0)
    sprite('pt024_02', 3)
    ExitState()
    label(0)
    sprite('pt403_29', 3)
    clearUponHandler(LANDING)

    def upon_LANDING():
        physicsXImpulse(0)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('pt403_30', 3)
    sprite('pt403_06', 3)
    sprite('pt403_07', 3)
    label(2)
    sprite('pt020_07', 3)
    sprite('pt020_08', 3)
    gotoLabel(2)


@State
def HoppingPlus_B():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Hopping_Default')

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_60 >= 4:
                XImpulseAcceleration(80)
                SetAcceleration(200)
            else:
                XImpulseAcceleration(50)
                SetAcceleration(400)
            XSpeed(2000)
            YAccel(30)
            YSpeed(25000)
            setGravity(3000)
            if SLOT_60 == 7:
                Damage(500)
                AttackP2(84)
                SameMoveProration(80)
                GroundedHitstunAnimation(9)
                AirPushbackY(-60000)
                YImpulseBeforeWallbounce(0)
                AirUntechableTime(45)
                GroundBounce(1)
                BouncePercentage(50)
            if SLOT_60 == 3:
                Damage(500)
                AttackP2(84)
                SameMoveProration(80)
                AirHitstunAnimation(17)
                GroundedHitstunAnimation(9)
                AirPushbackY(-60000)
                YImpulseBeforeWallbounce(0)
                AirUntechableTime(40)
                GroundBounce(1)
                BouncePercentage(55)
    sprite('pt403_11', 1)
    if SLOT_60 == 2:
        ChainCancel(0)
    if SLOT_60 == 6:
        ChainCancel(0)
    sprite('pt403_12', 2)
    sprite('pt403_13', 2)
    sprite('pt403_14', 3)
    SLOT_60 = SLOT_60 + 1
    PrivateSE('ptse_08')
    sprite('pt403_15', 3)
    CreateObject('AssaultAwave', 0)
    sprite('pt403_16', 3)
    Recovery()
    sprite('pt403_10', 1)
    if SLOT_60 == 3:
        gotoLabel(0)
    if SLOT_60 == 7:
        gotoLabel(0)
    sprite('pt403_10', 30)
    label(1)
    sprite('pt024_01', 4)
    EndMomentum(1)
    clearUponHandler(LANDING)
    WhiffCancelEnable(0)
    ChainCancel(0)
    sprite('pt024_02', 3)
    ExitState()
    label(0)
    sprite('pt403_29', 3)
    clearUponHandler(LANDING)

    def upon_LANDING():
        physicsXImpulse(0)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('pt403_30', 3)
    sprite('pt403_06', 3)
    sprite('pt403_07', 3)
    label(2)
    sprite('pt020_07', 3)
    sprite('pt020_08', 3)
    gotoLabel(2)


@State
def HoppingPlus_C():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('Hopping_Default')

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_60 >= 4:
                XImpulseAcceleration(80)
                SetAcceleration(200)
            else:
                XImpulseAcceleration(40)
                SetAcceleration(100)
            XSpeed(8000)
            physicsYImpulse(15000)
            setGravity(3000)
            if SLOT_60 == 7:
                Damage(1000)
                AttackP2(84)
                SameMoveProration(80)
                AirPushbackX(-30000)
                AirPushbackY(-50000)
                AirUntechableTime(30)
                XSpeed(4000)
            if SLOT_60 == 3:
                Damage(500)
                AirUntechableTime(30)
                AttackP2(84)
                SameMoveProration(80)
                GroundedHitstunAnimation(2)
                Crumple(22)
                AirHitstunAnimation(19)
                AirPushbackX(-36000)
                AirPushbackY(-30000)
                Floorslide(15)
                XSpeed(4000)
    sprite('pt403_23', 1)
    if SLOT_60 == 2:
        ChainCancel(0)
    if SLOT_60 == 6:
        ChainCancel(0)
    sprite('pt403_24', 2)
    sprite('pt403_25', 2)
    sprite('pt403_26', 3)
    SLOT_60 = SLOT_60 + 1
    CreateObject('AssaultCwave', 0)
    PrivateSE('ptse_08')
    sprite('pt403_27', 3)
    sprite('pt403_28', 3)
    Recovery()
    sprite('pt403_10', 1)
    if SLOT_60 == 3:
        gotoLabel(0)
    if SLOT_60 == 7:
        gotoLabel(0)
    sprite('pt403_10', 32767)
    label(1)
    sprite('pt024_01', 4)
    EndMomentum(1)
    clearUponHandler(LANDING)
    WhiffCancelEnable(0)
    ChainCancel(0)
    sprite('pt024_02', 3)
    ExitState()
    label(0)
    sprite('pt403_29', 3)
    clearUponHandler(LANDING)

    def upon_LANDING():
        physicsXImpulse(0)
    EnterStateIfEventID(2, 'CmnActJumpLanding')
    sprite('pt403_30', 3)
    sprite('pt403_06', 3)
    sprite('pt403_07', 3)
    label(2)
    sprite('pt020_07', 3)
    sprite('pt020_08', 3)
    gotoLabel(2)


@State
def AirHopping():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 0)
        WhiffCancel('HoppingPlus_A')
        WhiffCancel('HoppingPlus_B')
        WhiffCancel('HoppingPlus_C')

        def upon_STATE_END():
            XImpulseAcceleration(50)
    sprite('pt403_08', 2)
    Voiceline('pt204')
    physicsXImpulse(12000)
    physicsYImpulse(35000)
    setGravity(2400)
    SLOT_60 = 0
    AirDashEffects(1)
    sprite('pt403_09', 2)
    sprite('pt403_10', 2)
    sprite('pt403_17', 32767)
    SLOT_60 = SLOT_60 + 4
    WhiffCancelEnable(1)
    label(0)
    sprite('pt403_29', 2)
    EndMomentum(1)
    clearUponHandler(LANDING)
    sprite('pt403_30', 2)
    sprite('pt024_02', 2)


@State
def SurfingU():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(90)
        GroundedHitstunAnimation(9)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        AirPushbackX(32000)
        AirPushbackY(14000)
        YImpulseBeforeWallbounce(3000)
        AirUntechableTime(40)
        Floorslide(9)
        DamageEffect(6, 'ptef_hit_high')
        FatalCounter(1)
        SetYCollisionFromOrigin(120)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            physicsXImpulse(45000)
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            sendToLabel(0)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('pt408_00', 3)
    sprite('pt408_01', 3)
    CreateParticle('ptef_specialmc', -1)
    physicsXImpulse(10000)
    physicsYImpulse(7500)
    EndYPhysicsImpulse()
    JumpEffects(1, 100)
    sprite('pt408_02', 2)
    Voiceline('pt203')
    sprite('pt408_03', 2)
    PrivateSE('ptse_21')
    sprite('pt408_04', 2)
    XImpulseAcceleration(150)
    sprite('pt408_05', 3)
    XImpulseAcceleration(200)
    CreateObject('ptef_408_splash', -1)
    sprite('pt408_06', 3)
    XImpulseAcceleration(150)
    sprite('pt408_07', 3)
    sprite('pt408_05', 3)
    sprite('pt408_06', 3)
    label(0)
    sprite('pt408_08', 3)
    XImpulseAcceleration(50)
    Recovery()
    DespawnEAEffect('ptef_408_splash')
    sprite('pt408_09', 3)
    XImpulseAcceleration(50)
    sprite('pt402_09ex01', 3)
    XImpulseAcceleration(50)
    physicsYImpulse(10000)
    uponSendToLabel(LANDING, 1)
    sprite('pt402_10ex01', 3)
    sprite('pt402_11ex01', 32767)
    label(1)
    sprite('pt408_10', 2)
    EndMomentum(1)
    LandingEffects(104, 1, 1)
    sprite('pt402_13ex01', 2)
    sprite('pt402_14ex01', 2)
    sprite('pt402_15ex01', 2)


@State
def SurfingV():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(90)
        AirUntechableTime(60)
        GroundedHitstunAnimation(9)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
        AirPushbackY(-45000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(50)
        HardKnockdown(10)
        EnableEmergencyTechAirHit(1)
        FatalCounter(1)
        StarterRating(2)
        DamageEffect(6, 'ptef_hit_high')
        PushCollisionHeightLow(120000)
        uponSendToLabel(LANDING, 1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('pt402_00', 2)
    setInvincible(1)
    SpecificInvincibility(0, 1, 0, 0, 0)
    sprite('pt402_01', 2)
    sprite('pt402_02', 2)
    CreateParticle('ptef_specialmc', -1)
    physicsXImpulse(-12000)
    physicsYImpulse(18000)
    JumpEffects(1, 100)
    sprite('pt402_03', 3)
    XImpulseAcceleration(50)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    PrivateSE('ptse_21')
    sprite('pt402_03', 2)
    setInvincible(0)
    Voiceline('pt202')
    physicsXImpulse(20000)
    physicsYImpulse(30000)
    AddY(75000)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_03', 3)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_04', 3)
    XImpulseAcceleration(150)
    AddY(40000)
    setGravity(4000)
    YAccel(50)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    StartMultihit()
    sprite('pt402_05', 2)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    StartMultihit()
    sprite('pt402_05', 2)
    XImpulseAcceleration(75)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_06', 2)
    AddY(-40000)
    XImpulseAcceleration(80)
    YAccel(40)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_06', 2)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_06', 2)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_06', 2)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt402_06', 32767)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    label(1)
    sprite('pt402_07', 3)
    setGravity(-100)
    physicsXImpulse(0)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    Recovery()
    sprite('pt402_08', 3)
    physicsYImpulse(15000)
    setGravity(3500)
    CreateParticle('ptef_402light', 0)
    sprite('pt402_09', 3)
    CreateParticle('ptef_402light', 0)
    sprite('pt402_10', 3)
    sprite('pt402_11', 3)
    sprite('pt402_12', 32767)
    uponSendToLabel(LANDING, 2)
    label(2)
    sprite('pt402_13', 2)
    EndMomentum(1)
    LandingEffects(104, 1, 1)
    sprite('pt402_14', 2)
    sprite('pt402_15', 3)


@State
def CommandThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('CommandThrow2', 2, 0, 0)
        RangeCheck(100000)

        def upon_EVERY_FRAME():
            SLOT_19 < 160000
            if not SLOT_0 and not SLOT_52:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(0)
    sprite('pt404_00', 5)
    physicsXImpulse(-8000)
    sprite('pt404_00', 6)
    physicsXImpulse(0)
    sprite('pt404_01', 3)
    sprite('pt404_02', 2)
    DashEffects(100, 1, 1)
    physicsXImpulse(34000)
    CommonSE('000_airdash_0')
    PrivateSE('ptse_23')
    sprite('pt404_03', 2)
    SLOT_52 = 1
    sprite('pt404_04', 2)
    sprite('pt404_02', 2)
    sprite('pt404_03', 2)
    sprite('pt404_04', 2)
    sprite('pt404_02', 2)
    sprite('pt404_03', 2)
    sprite('pt404_04', 2)
    sprite('pt404_02', 2)
    sprite('pt404_03', 2)
    sprite('pt404_04', 2)
    label(0)
    sprite('pt404_05', 2)
    clearUponHandler(EVERY_FRAME)
    physicsXImpulse(0)
    SkidEffects(100, 1, 1)
    sprite('pt404_06', 2)
    sprite('pt404_07', 1)
    sprite('pt310_01', 1)
    CommonSE('010_swing_sword_0')
    sprite('pt310_02', 3)
    sprite('pt310_03', 3)
    sprite('pt310_04', 3)
    sprite('pt310_05', 3)
    sprite('pt310_04', 3)
    sprite('pt310_05', 3)
    sprite('pt310_06', 3)
    sprite('pt310_07', 3)
    sprite('pt310_08', 4)


@State
def CommandThrow2():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        EnableRapidCancel(0)
    sprite('pt310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(1, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('pt404_08', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    CommonSE('022_magiccircle_b')
    PrivateSE('ptse_17')
    sprite('pt404_09', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('pt404_10', 8)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 32)
    CreateObject('CommandThrowHeart', 0)
    CreateObject('CommandThrowMcircle', 1)
    Voiceline('pt205')
    sprite('pt404_11', 4)
    AddX(-50000)
    sprite('pt404_12', 3)
    sprite('pt404_13', 4)
    sprite('pt404_14', 4)
    sprite('pt404_15', 4)
    sprite('pt404_16', 3)
    AddX(-34000)
    sprite('pt404_17', 10)
    CreateParticle('ptef_specialmc', -1)
    sprite('pt404_18', 5)
    sprite('pt404_19', 3)
    sprite('pt404_20', 6)
    CreateParticle('ptef_404kiss', 1)
    PrivateSE('ptse_15')
    sprite('pt404_21', 4)
    sprite('pt404_22', 2)
    sprite('pt404_22', 2)
    RefreshMultihit()
    AttackLevel_(3)
    StarterRating(2)
    AttackP2(60)
    Damage(1500)
    AirUntechableTime(100)
    AirPushbackX(2000)
    AirPushbackY(49000)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    CommonSE('016_explode_2')
    CreateParticle('ptef_bomber_heart', 0)
    TriggerUponForState('CommandThrowMcircle', 32)
    if SLOT_137:
        DamageMultiplier(80)
    sprite('pt404_23', 3)
    EnableRapidCancel(1)
    sprite('pt404_24', 3)
    sprite('pt404_25', 3)
    sprite('pt404_26', 5)
    CreateObject('CommandThrowRod', 0)
    sprite('pt404_27', 3)
    sprite('pt404_28', 3)
    sprite('pt404_29', 3)
    sprite('pt203_03', 1)
    CreateObject('pt203_stick', 0)
    sprite('pt203_04', 2)
    if SLOT_4:
        SLOT_31 = 9999
    else:
        callSubroutine('ItemShuffle')
    PrivateSE('ptse_13')
    sprite('pt203_05', 8)
    sprite('pt203_06', 3)
    sprite('pt203_07', 3)
    sprite('pt203_08', 3)
    sprite('pt203_09', 3)
    sprite('pt203_10', 2)
    sprite('pt203_11', 1)


@State
def AirSlide():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        SLOT_6 = 0
        SetActionMark(0)

        def upon_STATE_END():
            EndYPhysicsImpulse()
            CommonSE('100_hit_grap_0')
            CreateObject('AirSlideBalloon', -1)

        def upon_EVERY_FRAME():
            ForceFaceSprite()
            if SLOT_2:
                if CheckInput(0x5f):
                    physicsXImpulse(-3000)
                    physicsYImpulse(10)
                if CheckInput(0x79):
                    physicsXImpulse(3000)
                    physicsYImpulse(10)
                if CheckInput(0x45):
                    physicsYImpulse(-4000)
                if CheckInput(0x93):
                    physicsYImpulse(2500)

        def upon_LANDING():
            CommonSE('100_hit_grap_1')
            CreateObject('AirSlideBalloon', -1)
    sprite('pt401_00', 2)
    Voiceline('pt201')
    CreateObject('AirSlideMcirle', -1)
    XImpulseAcceleration(70)
    YAccel(0)
    setGravity(10)
    SetInertia(0)
    sprite('pt401_01', 1)
    XImpulseAcceleration(40)
    IgnoreInertia(1)
    sprite('pt401_02', 5)
    SetActionMark(1)
    sprite('pt401_08', 5)
    PrivateSE('ptse_00')
    sprite('pt401_07', 4)
    WhiffNormalCancel(1)
    WhiffSpecialCancel(1)
    WhiffBarrierCancel2(1)
    sprite('pt401_08', 6)
    sprite('pt401_02', 6)
    sprite('pt401_09', 6)
    sprite('pt401_10', 6)
    sprite('pt401_09', 6)
    sprite('pt401_02', 6)
    sprite('pt401_08', 6)
    PrivateSE('ptse_00')
    sprite('pt401_07', 6)
    sprite('pt401_08', 6)
    sprite('pt401_02', 7)
    sprite('pt401_03', 3)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(STATE_END)
    CommonSE('100_hit_grap_0')
    CreateObject('AirSlideBalloon', -1)
    physicsYImpulse(32000)
    EndYPhysicsImpulse()
    sprite('pt401_04', 3)
    YAccel(40)
    sprite('pt401_05', 3)
    YAccel(30)
    sprite('pt401_06', 2)
    YAccel(10)
    label(0)
    sprite('pt401_06', 1)
    EndMomentum(1)
    EndYPhysicsImpulse()


@State
def Atemi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)
        GuardpointHitstop(0, 8)
        PreventBlocking(1)
        GuardpointBlockUnblockable(0)

        def upon_GUARDPOINT_ACTIVATION():
            enterState('AtemiExe')
            NoDamageAction(1)
    sprite('pt406_00', 3)
    sprite('pt406_01', 3)
    sprite('pt406_02', 3)
    SmartVoiceline('pt209')
    sprite('pt406_03', 8)
    PrivateSE('ptse_00')
    sprite('pt406_04', 8)
    sprite('pt406_05', 8)
    sprite('pt406_06', 8)
    sprite('pt406_03', 8)
    PrivateSE('ptse_00')
    sprite('pt406_04', 8)
    sprite('pt406_05', 8)
    sprite('pt406_06', 8)
    sprite('pt406_03', 8)
    PrivateSE('ptse_00')
    sprite('pt406_04', 8)
    sprite('pt406_05', 8)
    sprite('pt406_06', 8)
    sprite('pt406_07', 5)
    setInvincible(0)
    sprite('pt406_08', 5)
    sprite('pt406_09', 5)
    sprite('pt406_10', 5)
    sprite('pt406_11', 5)
    sprite('pt406_12', 5)


@State
def AtemiExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        setInvincible(1)
        PreventBlocking(1)
    sprite('null', 10)
    SmartVoiceline('pt010')
    CreateObject('FakeDoll', -1)
    CommonSE('016_explode_0')
    CommonSE('016_explode_0')
    sprite('pt401_00', 1)
    AddX(-150000)
    CreateObject('Atemi_Smoke', -1)
    sprite('pt300_00', 4)
    sprite('pt300_01', 4)
    sprite('pt300_02', 4)
    sprite('pt300_03', 6)
    if random_(2, 0, 50):
        conditionalSendToLabel(30)
    sprite('pt300_04', 6)
    setInvincible(0)
    SmartVoiceline('pt404')
    sprite('pt300_05', 7)
    sprite('pt300_06', 6)
    sprite('pt300_07', 7)
    gotoLabel(40)
    label(30)
    sprite('pt300_10', 6)
    setInvincible(0)
    SmartVoiceline('pt405')
    sprite('pt300_11', 7)
    sprite('pt300_12', 6)
    sprite('pt300_13', 7)
    label(40)
    sprite('pt300_08', 9)
    sprite('pt300_09', 6)


@State
def HiWeapon():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        PreventBlocking(1)
    sprite('pt430_00', 3)
    sprite('pt430_01', 3)
    sprite('pt430_02', 3)
    setInvincible(1)
    DistortionSettings(128, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    StopClock(1)
    Voiceline('pt250')
    sprite('pt430_03', 3)
    sprite('pt430_04', 3)
    sprite('pt430_05', 3)
    sprite('pt430_06', 3)
    sprite('pt430_07', 3)
    CreateObject('pt430_mahojin', 0)
    CreateObject('pt203_mahojinsub', 0)
    CreateObject('pt430_circle1', 1)
    CreateObject('pt430_circle2', 1)
    sprite('pt430_08', 3)
    sprite('pt430_09', 3)
    sprite('pt430_10', 3)
    sprite('pt430_11', 3)
    CreateObject('ptef_430power', 0)
    sprite('pt430_12', 3)
    sprite('pt430_13', 3)
    sprite('pt203_02', 40)
    CreateObject('pt430_mahojinsub', 0)
    CreateObject('pt430_aura1', 0)
    CreateObject('pt430_aura2', 0)
    CreateObject('pt430_aura3', 0)
    sprite('pt203_03', 3)
    CreateObject('pt430_stick', 0)
    callSubroutine('ItemShufflePowerUP')
    TriggerUponForState('SphereLight_Model', 32)
    PrivateSE('ptse_13')
    sprite('pt203_04', 3)
    sprite('pt203_05', 30)
    sprite('pt203_06', 3)
    sprite('pt203_07', 3)
    sprite('pt203_08', 3)
    sprite('pt203_09', 3)
    setInvincible(0)
    sprite('pt203_10', 3)
    sprite('pt203_11', 3)


@State
def HiWeapon_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        SLOT_58 = SLOT_OverdriveTimer
    sprite('pt430_00', 3)
    sprite('pt430_01', 3)
    sprite('pt430_02', 3)
    setInvincible(1)
    DistortionSettings(128, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    StopClock(1)
    Voiceline('pt250')
    sprite('pt430_03', 3)
    sprite('pt430_04', 3)
    sprite('pt430_05', 3)
    sprite('pt430_06', 3)
    sprite('pt430_07', 3)
    CreateObject('pt430_mahojin', 0)
    CreateObject('pt203_mahojinsub', 0)
    CreateObject('pt430_circle1', 1)
    CreateObject('pt430_circle2', 1)
    sprite('pt430_08', 3)
    sprite('pt430_09', 3)
    sprite('pt430_10', 3)
    sprite('pt430_11', 3)
    CreateObject('ptef_430power', 0)
    sprite('pt430_12', 3)
    sprite('pt430_13', 3)
    sprite('pt203_02', 40)
    CreateObject('pt430_mahojinsub', 0)
    CreateObject('pt430_aura1', 0)
    CreateObject('pt430_aura2', 0)
    CreateObject('pt430_aura3', 0)
    sprite('pt203_03', 3)
    CreateObject('pt430_stick', 0)
    callSubroutine('ItemShufflePowerUP')
    TriggerUponForState('SphereLight_Model', 32)
    PrivateSE('ptse_13')
    sprite('pt203_04', 3)
    sprite('pt203_05', 30)
    sprite('pt203_06', 3)
    sprite('pt203_07', 3)
    sprite('pt203_08', 3)
    sprite('pt203_09', 3)
    setInvincible(0)
    sprite('pt203_10', 3)
    sprite('pt203_11', 3)


@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(440)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        DamageEffect(6, 'ptef_hit_middle')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        AirUntechableTime(100)
        Hitstun(100)
        StarterRating(2)
        EndMomentum(1)
        if SLOT_IsGrounded:
            sendToLabel(100)
        if SLOT_IsAirborne:
            sendToLabel(101)
            GotoState('UltimateAssaultAir')
        setInvincible(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('keep', 1)
    StartMultihit()
    label(101)
    sprite('pt431_03', 2)
    sprite('pt431_03', 1)
    Voiceline('pt251')
    DistortionSettings(70, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('pt431_03', 1)
    gotoLabel(102)
    label(100)
    sprite('pt431_00', 3)
    sprite('pt431_00', 3)
    Voiceline('pt251')
    DistortionSettings(70, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('pt431_01', 3)
    sprite('pt431_02', 3)
    label(102)
    sprite('pt431_03', 3)
    sprite('pt431_04', 3)
    CreateObject('pt431_aura3', -1)
    CreateObject('pt431_aura3', -1)
    sprite('pt431_05', 40)
    CreateObject('pt431_startcircle', 0)
    CreateObject('ptef_431aura', 0)
    CreateObject('pt431_floorcircle', -1)
    sprite('pt431_05', 10)
    CreateObject('pt431_aura1', -1)
    CreateObject('pt431_aura2', -1)
    sprite('pt431_06', 3)
    CreateObject('pt431_tornado', -1)
    sprite('pt431_07', 3)

    def upon_16():
        if CheckInput(0x5f):
            XSpeed(-500)
        if CheckInput(0x79):
            XSpeed(500)
        if SLOT_113:
            XSpeed(500)
        XImpulseAcceleration(95)
        YAccel(95)
    sprite('pt431_08', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_09', 3)
    sprite('pt431_10', 1)
    sprite('pt431_10', 3)
    setInvincible(0)
    sprite('pt431_11', 3)
    sprite('pt431_12', 3)
    sprite('pt431_13', 3)
    sprite('pt431_09', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_10', 4)
    RefreshMultihit()
    sprite('pt431_11', 3)
    sprite('pt431_12', 3)
    sprite('pt431_13', 3)
    AirPushbackX(-5000)
    AirPushbackY(8000)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)

    def upon_16():
        if CheckInput(0x5f):
            XSpeed(-700)
        if CheckInput(0x79):
            XSpeed(700)
        if CheckInput(0x93):
            YSpeed(1200)
        if CheckInput(0x45):
            YSpeed(-200)
        if SLOT_113:
            XSpeed(500)
        XImpulseAcceleration(95)
        YAccel(95)
        setGravity(700)
    CreateObject('pt431_ranbucircle', -1)
    CreateObject('pt431_tornado', -1)
    CreateObject('pt431_aura1', -1)
    CreateObject('pt431_aura2', -1)
    CreateObject('pt431_smoke', -1)
    Voiceline('pt252')
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    Hitstop(0)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)

    def upon_OPPONENT_HIT():
        AddActionMark(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(30000)
    AirPushbackY(24000)
    YImpulseBeforeWallbounce(1000)
    AirUntechableTime(150)
    HardKnockdown(36)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_16', 2)
    label(5)
    sprite('pt431_14', 3)
    setGravity(1200)
    AttackOff()
    clearUponHandler(16)

    def upon_EVERY_FRAME():
        if SLOT_IsGrounded:
            sendToLabel(10)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    gotoLabel(5)
    label(10)
    sprite('pt431_17', 5)
    clearUponHandler(EVERY_FRAME)
    sprite('pt431_18', 5)

    def upon_16():
        XImpulseAcceleration(90)
    sprite('pt431_19', 5)
    sprite('pt431_20', 5)
    sprite('pt431_21', 5)
    sprite('pt431_22', 5)
    loopRest()
    if SLOT_2:
        gotoLabel(0)
    sprite('pt431_31', 7)
    sprite('pt431_32', 7)
    ExitState()
    label(0)
    sprite('pt431_23', 6)
    Voiceline('pt253')
    CreateObject('pt203_mahojin', -1)
    CreateObject('pt203_mahojinsub', -1)
    CreateObject('pt203_aura1', -1)
    CreateObject('pt203_aura2', -1)
    CreateObject('pt203_aura3', -1)
    sprite('pt431_24', 6)
    sprite('pt431_25', 6)
    sprite('pt431_26', 6)
    sprite('pt431_27', 8)
    CreateObject('pt203_stick', 0)
    if SLOT_4:
        SLOT_31 = 9999
    else:
        callSubroutine('ItemShuffle')
    PrivateSE('ptse_13')
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_28', 6)
    sprite('pt431_29', 6)
    sprite('pt431_30', 6)
    ExitState()


@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(440)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        DamageEffect(6, 'ptef_hit_middle')
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-6000)
        AirPushbackY(18000)
        AirUntechableTime(100)
        Hitstun(100)
        StarterRating(2)
        AttackType(4)
        EndMomentum(1)
        if SLOT_IsGrounded:
            sendToLabel(100)
        if SLOT_IsAirborne:
            sendToLabel(101)
        setInvincible(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('keep', 1)
    StartMultihit()
    label(101)
    sprite('pt431_03', 2)
    sprite('pt431_03', 1)
    Voiceline('pt251')
    DistortionSettings(70, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('pt431_03', 1)
    gotoLabel(102)
    label(100)
    sprite('pt431_00', 3)
    sprite('pt431_00', 3)
    Voiceline('pt251')
    DistortionSettings(70, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB', -1)
    sprite('pt431_01', 3)
    sprite('pt431_02', 3)
    label(102)
    sprite('pt431_03', 3)
    sprite('pt431_04', 3)
    CreateObject('pt431_aura3', -1)
    CreateObject('pt431_aura3', -1)
    sprite('pt431_05', 40)
    CreateObject('pt431_startcircle', 0)
    CreateObject('ptef_431aura', 0)
    CreateObject('pt431_floorcircle', -1)
    sprite('pt431_05', 10)
    CreateObject('pt431_aura1', -1)
    CreateObject('pt431_aura2', -1)
    sprite('pt431_06', 3)
    CreateObject('pt431_tornado', -1)
    sprite('pt431_07', 3)

    def upon_16():
        if CheckInput(0x5f):
            XSpeed(-500)
        if CheckInput(0x79):
            XSpeed(500)
        if SLOT_113:
            XSpeed(500)
        XImpulseAcceleration(95)
        YAccel(95)
    sprite('pt431_08', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_09', 3)
    sprite('pt431_10', 1)
    sprite('pt431_10', 3)
    setInvincible(0)
    sprite('pt431_11', 3)
    sprite('pt431_12', 3)
    sprite('pt431_13', 3)
    sprite('pt431_09', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_10', 4)
    RefreshMultihit()
    sprite('pt431_11', 3)
    sprite('pt431_12', 3)
    sprite('pt431_13', 3)
    AirPushbackX(-5000)
    AirPushbackY(8000)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)

    def upon_16():
        if CheckInput(0x5f):
            XSpeed(-700)
        if CheckInput(0x79):
            XSpeed(700)
        if CheckInput(0x93):
            YSpeed(1200)
        if CheckInput(0x45):
            YSpeed(-200)
        if SLOT_113:
            XSpeed(500)
        XImpulseAcceleration(95)
        YAccel(95)
        setGravity(700)
    CreateObject('pt431_ranbucircle', -1)
    CreateObject('pt431_tornado', -1)
    CreateObject('pt431_aura1', -1)
    CreateObject('pt431_aura2', -1)
    CreateObject('pt431_smoke', -1)
    Voiceline('pt252')
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    Hitstop(0)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)

    def upon_OPPONENT_HIT():
        AddActionMark(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(30000)
    AirPushbackY(24000)
    YImpulseBeforeWallbounce(1000)
    AirUntechableTime(150)
    HardKnockdown(80)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_16', 2)
    label(5)
    sprite('pt431_14', 3)
    setGravity(1200)
    AttackOff()
    clearUponHandler(16)

    def upon_EVERY_FRAME():
        if SLOT_IsGrounded:
            sendToLabel(10)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    gotoLabel(5)
    label(10)
    sprite('pt431_17', 5)
    clearUponHandler(EVERY_FRAME)
    sprite('pt431_18', 5)

    def upon_16():
        XImpulseAcceleration(90)
    sprite('pt431_19', 5)
    sprite('pt431_20', 5)
    sprite('pt431_21', 5)
    sprite('pt431_22', 5)
    loopRest()
    if SLOT_2:
        gotoLabel(0)
    sprite('pt431_31', 7)
    sprite('pt431_32', 7)
    ExitState()
    label(0)
    sprite('pt431_23', 6)
    Voiceline('pt253')
    CreateObject('pt203_mahojin', -1)
    CreateObject('pt203_mahojinsub', -1)
    CreateObject('pt203_aura1', -1)
    CreateObject('pt203_aura2', -1)
    CreateObject('pt203_aura3', -1)
    sprite('pt431_24', 6)
    sprite('pt431_25', 6)
    sprite('pt431_26', 6)
    sprite('pt431_27', 8)
    CreateObject('pt203_stick', 0)
    if SLOT_4:
        SLOT_31 = 9999
    else:
        callSubroutine('ItemShuffle')
    PrivateSE('ptse_13')
    CreateObject('DollMaker', -1)

    def upon_STATE_END():
        TriggerUponForState('DollMaker', 32)
    sprite('pt431_27', 7)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    loopRest()
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_27', 8)
    sprite('pt431_28', 6)
    sprite('pt431_29', 6)
    sprite('pt431_30', 6)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        DefeatOpponentBehavior(1)
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        StrikeProjectileLevel(0)
        ProjectileLevel(3)
        MoveAttributes(0, 0, 0, 1, 0)
        MinimumDamage(100)
        setInvincible(1)
        EndMomentum(1)
        EnemyHitstopAddition(0, 525, 525)
        OppPositionOnHit(3, 128000, 0)

        def upon_OPPONENT_HIT():
            SetActionMark(1)
            AstralHeatCleanup(1, 1)
            PlayPlayAstralBGM(1)
            SetBackground(3)
            HUDVisibillity(1)
            setInvincible(1)
    if SLOT_IsGrounded:
        gotoLabel(0)
    if SLOT_IsAirborne:
        gotoLabel(1)
    label(0)
    sprite('pt450_00', 4)
    Voiceline('pt290')
    gotoLabel(3)
    label(1)
    sprite('pt450_21', 4)
    Voiceline('pt290')
    gotoLabel(3)
    label(3)
    sprite('pt450_01', 1)
    sprite('pt450_01', 3)
    DistortionSettings(53, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_PT_AH', -1)
    physicsYImpulse(900)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(6)
    AfterimageMask_1(0, 255, 150, 150)
    AfterimageMask_2(0, 0, 0, 0)
    AfterimageSize_1(1010)
    AfterimageSize_2(1010)
    sprite('pt450_02', 7)
    CreateParticle('ptef_specialmc', -1)
    sprite('pt450_03', 7)
    sprite('pt450_04', 7)
    sprite('pt450_05', 7)
    sprite('pt450_06', 7)
    sprite('pt450_07', 7)
    sprite('pt450_08', 5)
    physicsYImpulse(0)
    sprite('pt450_09', 4)
    CreateObject('Astral1stBeam', 0)
    PrivateSE('ptse_12')
    sprite('pt450_10', 3)
    PrivateSE('ptse_09')
    PrivateSE('ptse_09')
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    ScreenShake(20000, 0)
    loopRest()
    if SLOT_2:
        gotoLabel(4)
    sprite('pt450_09', 3)
    setInvincible(0)
    TriggerUponForState('Astral1stBeam', 32)
    EnableAfterimage(0)
    sprite('pt450_22', 3)
    sprite('pt450_23', 3)
    EndYPhysicsImpulse()
    loopRest()
    ExitState()
    label(4)
    clearUponHandler(OPPONENT_HIT)
    sprite('pt450_09', 3)
    CreateObject('AstralAura', -1)
    CreateObject('AstralAura02', -1)
    CreateObject('AstralMcircle', -1)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    CharacterFlash2(16777215, 9)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    StopCharacterFlash2()
    CreateObject('Fade1', -1)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    Voiceline('pt291')
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    CreateObject('pt450cutin_hand', -1)
    CreateObject('pt450cutin_handbg', -1)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    CreateObject('pt450cutin_leg', -1)
    CreateObject('pt450cutin_legbg', -1)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    CreateObject('pt450cutin_bustupbg', -1)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    CreateObject('pt450cutin_bustup', -1)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    Voiceline('pt292')
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    sprite('pt450_09', 3)
    sprite('pt450_10', 3)
    sprite('pt450_11', 3)
    StartMultihit()
    CreateParticle('ptef_450change2nd', 1)
    sprite('pt450_12', 3)
    StartMultihit()
    CreateObject('pt450_mahojin1', -1)
    TriggerUponForState('AstralAura', 32)
    TriggerUponForState('Astral1stBeam', 32)
    sprite('pt450_13', 3)
    CharacterFlash2(0, 9)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    PrivateSE('ptse_22')
    StartMultihit()
    sprite('pt450_13', 3)
    StopCharacterFlash2()
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    CreateObject('pt450_mahojin2', -1)
    CreateObject('pt450_mahojin3', -1)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    Voiceline('pt293')
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    CreateParticle('ptef_450second', 0)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    CreateObject('pt450Beam', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 3)
    ScreenShake(0, 90000)
    StartMultihit()
    sprite('pt450_13', 3)
    sprite('pt450_14', 3)
    sprite('pt450_12', 5)
    RefreshMultihit()
    Damage(9999)
    DefeatOpponentBehavior(3)
    HitAnywhere(1)
    Hitstop(0)
    YImpulseBeforeWallbounce(0)
    OppPositionOnHit(3, 0, 0)
    EnemyHitstopAddition(0, 2000, 2000)
    GroundedHitstunAnimation(4)
    sprite('pt450_12', 15)
    StartMultihit()
    sprite('pt450_12', 15)
    StartMultihit()
    CreateObject('FadeWhite', -1)
    sprite('pt450_13', 45)
    SetBackground(0)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    AbsoluteY(70000)
    XPositionRelativeFacing(0)
    TriggerUponForState('AstralAura02', 32)
    EnableAfterimage(0)
    setInvincible(0)

    def RunOnObject_22():
        Visibility(1)
        AbsoluteY(4000000)
        XPositionRelativeFacing(1865000)
    sprite('pt450_13', 15)
    CreateObject('AstralAuraWin', -1)
    sprite('pt450_14', 6)
    sprite('pt450_15', 6)
    sprite('pt450_16', 6)
    sprite('pt450_17', 6)
    sprite('pt450_18', 6)
    sprite('pt450_19', 6)
    sprite('pt450_20', 6)
    WinAction()
    if SLOT_43:
        DemoTimer(240)
    else:
        DemoTimer(290)
    sprite('pt450_18', 6)
    CallCustomizableParticle('ptef_450win', 0)
    PrivateSE('ptse_16')
    sprite('pt450_19', 6)
    sprite('pt450_20', 6)
    sprite('pt450_18', 6)
    sprite('pt450_19', 6)
    Voiceline('pt407')
    sprite('pt450_20', 6)
    sprite('pt450_18', 6)
    sprite('pt450_19', 6)
    sprite('pt450_20', 6)
    label(5)
    sprite('pt450_18', 6)
    CallCustomizableParticle('ptef_450win', 0)
    PrivateSE('ptse_16')
    sprite('pt450_19', 6)
    sprite('pt450_20', 6)
    sprite('pt450_18', 6)
    sprite('pt450_19', 6)
    sprite('pt450_20', 6)
    sprite('pt450_18', 6)
    sprite('pt450_19', 6)
    sprite('pt450_20', 6)
    gotoLabel(5)


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('pt054')
    sprite('pt900_00', 6)
    EnableCollision(0)
    WallCollisionDetection(0)
    ScreenCollision(0)
    CameraFast(1)
    CameraControlEnable(1)
    CameraControlInfinity(1)
    FaceLeft()
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    EndMomentum(1)
    sprite('pt900_01', 6)
    sprite('pt900_02', 6)
    label(0)
    sprite('pt900_00', 6)
    sprite('pt900_01', 6)
    sprite('pt900_02', 6)
    gotoLabel(0)
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(250000)
    sprite('pt901_00', 50)
    physicsYImpulse(-150)
    sprite('pt901_00', 50)
    physicsYImpulse(150)
    Voiceline('pt055')
    label(0)
    sprite('pt901_00', 50)
    physicsYImpulse(-150)
    sprite('pt901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        PushbackX(12000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            EnableCollision(0)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('pt204_00ex01', 2)
    E0EAEffect('BurstDDeff', 103)
    sprite('pt204_01ex01', 2)
    sprite('pt204_02ex01', 3)
    sprite('pt440_00', 5)
    Voiceline('pt280')
    sprite('pt440_01', 5)
    sprite('pt440_02', 2)
    CommonSE('009_swing_rapier_2')
    CommonSE('006_swing_blade_2')
    sprite('pt440_03', 3)
    sprite('pt440_04', 5)
    setInvincible(0)
    sprite('pt204_08ex01', 5)
    sprite('pt204_09ex01', 5)
    sprite('pt204_10ex01', 5)
    sprite('pt204_11ex01', 5)
    sprite('pt204_12ex01', 5)
    sprite('pt204_13ex01', 4)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(100)
        Crumple(80)
        PushbackX(12000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 300000, 0)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)
            EnableCollision(0)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('pt204_00ex01', 1)
    E0EAEffect('BurstDDeff', 103)
    sprite('pt204_01ex01', 1)
    sprite('pt204_02ex01', 2)
    sprite('pt440_00', 2)
    Voiceline('pt280')
    sprite('pt440_01', 2)
    sprite('pt440_02', 1)
    CommonSE('009_swing_rapier_2')
    CommonSE('006_swing_blade_2')
    sprite('pt440_03', 3)
    sprite('pt440_04', 5)
    setInvincible(0)
    sprite('pt204_08ex01', 5)
    sprite('pt204_09ex01', 5)
    sprite('pt204_10ex01', 5)
    sprite('pt204_11ex01', 5)
    sprite('pt204_12ex01', 5)
    sprite('pt204_13ex01', 4)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(3)
        Damage(800)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(50000)
        AirUntechableTime(60)
        Wallbounce(1)
        WallbounceReboundTime(5)
        HardKnockdown(10)
        DamageFromStateOnly('BurstDDAdd')
        MinimumDamage(10)
        AttackOff()
        SetBackground(1)
    sprite('pt440_03', 3)
    StartMultihit()
    sprite('pt440_04', 5)
    sprite('pt204_08ex01', 5)
    sprite('pt204_09ex01', 4)
    sprite('pt204_10ex01', 4)
    sprite('pt204_11ex01', 4)
    CreateObject('ThrowMcircle', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddY(200000)
    sprite('pt204_12ex01', 4)
    sprite('pt204_13ex01', 4)
    Voiceline('pt281')
    CreateObject('BurstDDCamera', -1)
    sprite('pt610_00ex01', 3)
    sprite('pt610_01ex01', 3)
    sprite('pt440_05', 5)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    EndYPhysicsImpulse()
    sprite('pt440_06', 5)
    CreateObject('pt440kira', -1)
    XImpulseAcceleration(50)
    sprite('pt440_07', 3)
    XImpulseAcceleration(50)
    sprite('pt440_26', 3)
    sprite('pt440_08', 3)
    EnableCollision(0)
    WallCollisionDetection(0)
    ScreenCollision(0)
    physicsXImpulse(5000)
    sprite('pt440_09', 3)
    XImpulseAcceleration(300)
    PrivateSE('ptse_21')
    sprite('pt440_10', 3)
    RefreshMultihit()
    XImpulseAcceleration(500)
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('null', 18)
    physicsXImpulse(0)
    sprite('pt440_08', 3)
    ForceFaceSprite()
    physicsXImpulse(75000)
    RefreshMultihit()
    if not SLOT_51:
        AirPushbackY(85000)
        AirUntechableTime(120)
    else:
        AirHitstunAnimation(13)
        AirPushbackY(35000)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    PrivateSE('ptse_21')
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 2)
    sprite('keep', 1)
    if SLOT_51:
        sendToLabel(100)
    sprite('null', 15)
    physicsXImpulse(0)
    sprite('pt440_08', 3)
    ForceFaceSprite()
    physicsXImpulse(80000)
    CommonSE('000_airdash_0')
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_11', 3)
    XImpulseAcceleration(50)
    sprite('pt440_12', 5)
    XImpulseAcceleration(75)
    DespawnEAEffect('pt440kira')
    sprite('pt440_13', 5)
    XImpulseAcceleration(75)
    sprite('pt440_13', 5)
    XImpulseAcceleration(50)
    sprite('pt440_13', 5)
    XImpulseAcceleration(50)
    sprite('pt440_13', 5)
    XImpulseAcceleration(50)
    sprite('pt440_14', 3)
    XImpulseAcceleration(50)
    sprite('pt440_15', 3)
    XImpulseAcceleration(50)
    Voiceline('pt282')
    sprite('pt440_16', 3)
    XImpulseAcceleration(50)
    sprite('pt440_17', 5)
    RefreshMultihit()
    AttackLevel_(4)
    AirPushbackY(35000)
    HardKnockdownReset()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    DefeatOpponentBehavior(0)
    physicsXImpulse(30000)
    physicsYImpulse(30000)
    WallCollisionDetection(1)
    ScreenCollision(1)
    DamageEffect(4, 'ptef_hit_high')
    HitsparkSize(2500)
    sprite('pt440_18', 5)
    EnableCollision(1)
    XImpulseAcceleration(50)
    sprite('pt440_19', 3)
    XImpulseAcceleration(50)
    gotoLabel(200)
    label(100)
    sprite('null', 3)
    physicsXImpulse(0)
    sprite('pt440_08', 3)
    ForceFaceSprite()
    physicsXImpulse(100000)
    RefreshMultihit()
    AirHitstunAnimation(17)
    AirPushbackY(25000)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    PrivateSE('ptse_21')
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('null', 3)
    physicsXImpulse(0)
    sprite('pt440_08', 3)
    ForceFaceSprite()
    physicsXImpulse(100000)
    RefreshMultihit()
    AirHitstunAnimation(18)
    AirPushbackY(80000)
    AirUntechableTime(120)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    PrivateSE('ptse_21')
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('null', 15)
    physicsXImpulse(0)
    sprite('pt440_08', 3)
    ForceFaceSprite()
    physicsXImpulse(80000)
    CommonSE('000_airdash_0')
    sprite('pt440_09', 3)
    sprite('pt440_10', 3)
    sprite('pt440_08', 3)
    sprite('pt440_11', 3)
    XImpulseAcceleration(50)
    sprite('pt440_12', 5)
    XImpulseAcceleration(75)
    DespawnEAEffect('pt440kira')
    sprite('pt440_13', 5)
    XImpulseAcceleration(75)
    sprite('pt440_13', 5)
    XImpulseAcceleration(50)
    sprite('pt440_13', 5)
    XImpulseAcceleration(50)
    sprite('pt440_13', 5)
    XImpulseAcceleration(50)
    sprite('pt440_14', 3)
    XImpulseAcceleration(50)
    sprite('pt440_15', 3)
    XImpulseAcceleration(50)
    Voiceline('pt282')
    sprite('pt440_16', 3)
    XImpulseAcceleration(50)
    sprite('pt440_23', 5)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1950)
    AirPushbackY(35000)
    HardKnockdownReset()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    DefeatOpponentBehavior(0)
    physicsXImpulse(30000)
    physicsYImpulse(30000)
    WallCollisionDetection(1)
    ScreenCollision(1)
    DamageEffect(2, 'pt440HitEx')
    HitsparkSize(2500)
    Hitstop(30)
    ScreenShake(0, 100000)
    CommonSE('025_cleanhit_grap')
    sprite('pt440_24', 5)
    EnableCollision(1)
    XImpulseAcceleration(50)
    sprite('pt440_25', 3)
    XImpulseAcceleration(50)
    gotoLabel(200)
    label(200)
    sprite('pt440_20', 3)
    ForceFaceSprite()
    Flip()
    sprite('pt440_21', 3)
    sprite('pt440_22', 3)
    sprite('pt256_09ex01', 3)
    sprite('pt256_10ex01', 3)
    sprite('pt256_11ex01', 3)
    sprite('pt020_04', 3)
    ForceFaceSprite()
    uponSendToLabel(LANDING, 1)
    sprite('pt020_05', 3)
    sprite('pt020_06', 3)
    label(0)
    sprite('pt020_07', 4)
    sprite('pt020_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt024_00', 3)
    EndMomentum(1)
    sprite('pt024_01', 3)
    sprite('pt024_02', 3)
    loopRest()


@Subroutine
def MouthTableInit():
    Unknown18011('pt000', 14689, 14179, 14433, 14179, 14177, 14179, 14177, 
        14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt055', 12641, 25394, 12337, 12897, 25392, 12342, 14433, 
        14435, 14433, 14435, 12641, 25400, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt292', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt400', 14433, 14435, 13153, 25392, 56, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt401', 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt404', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('pt405', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('pt406', 14433, 14179, 14433, 13667, 14433, 14179, 14433, 
        14179, 14433, 14179, 14433, 14179, 14433, 14179, 14433, 14179, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt407', 12641, 25392, 24888, 25400, 24888, 12337, 14435, 
        14433, 14435, 14689, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt408', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('pt411', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('pt412', 14177, 13667, 14177, 13667, 14177, 13667, 14177, 
        13667, 14177, 13411, 14177, 12643, 24885, 25398, 24886, 25398, 
        24886, 25398, 24886, 25398, 24886, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt413', 14433, 13667, 14433, 13667, 14433, 12899, 48, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt414', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 12641, 25397, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt415', 12643, 24881, 25398, 24886, 25399, 13617, 14433, 
        14435, 14433, 14435, 12641, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pt416', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    Unknown18011('pt417', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0)
    if SLOT_44:
        Unknown18011('pt000', 14689, 14435, 14177, 14179, 14177, 14435, 
            12641, 25395, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt292', 14433, 14435, 14433, 14435, 14433, 13411, 
            24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('pt400', 14433, 14435, 14433, 14435, 12641, 25398, 56,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt401', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt404', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt405', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt406', 13153, 25397, 12341, 14433, 14435, 14433, 
            14435, 14433, 14435, 14433, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt407', 14433, 14435, 14433, 14435, 12641, 25397, 
            24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt408', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt411', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt412', 12641, 25392, 12337, 12641, 25392, 12337, 
            12641, 25392, 12337, 12641, 25392, 12337, 12641, 48, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0)
        Unknown18011('pt413', 14435, 14433, 14435, 14433, 14435, 14433, 
            14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt414', 14433, 14435, 14433, 14435, 14433, 14435, 
            12641, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt415', 14433, 14435, 14433, 14435, 14433, 14435, 
            14433, 14435, 14433, 14435, 14433, 12643, 50, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('pt416', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pt417', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('tm'):
            Unknown18011('pt000', 12641, 25392, 24888, 12337, 14435, 12641,
                25392, 24888, 12337, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
            Unknown18011('pt400', 14433, 12899, 24880, 25400, 24888, 25400,
                24888, 25400, 24888, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('pt401', 14177, 14179, 14177, 14179, 14177, 14179,
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            if SLOT_44:
                Unknown18011('pt000', 12641, 25392, 24888, 12337, 14435, 
                    12641, 25392, 24888, 12337, 14435, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt400', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641,
                    25396, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt401', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('pt502', 13411, 24885, 25399, 24887, 25399, 12340,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt5030', 14177, 14179, 14177, 14179, 14177, 13155,
                24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0)
            Unknown18011('pt5031', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_44:
                Unknown18011('pt502', 14177, 13923, 24880, 25399, 24887, 
                    25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kg'):
            Unknown18011('pt546', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 
                24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt547', 12897, 25392, 24888, 25400, 24888, 25400,
                24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_44:
                Unknown18011('pt546', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt547', 14177, 14179, 13153, 25392, 13617, 
                    12641, 25392, 24887, 25399, 24887, 12337, 14179, 14177,
                    14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0)
        if CharacterIDCheck('tm'):
            Unknown18011('pt550', 14177, 14179, 14177, 14177, 14179, 14177,
                14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt551', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_44:
                Unknown18011('pt550', 12897, 25392, 12342, 14177, 14179, 
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0)
                Unknown18011('pt551', 14177, 14179, 14177, 13411, 24885, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            if SLOT_138:
                Unknown18011('pt552', 13921, 13923, 13921, 13923, 13921, 
                    13155, 24880, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt553', 12641, 25394, 12339, 13921, 13411, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411,
                    24880, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_44:
                    Unknown18011('pt552', 14433, 14435, 14433, 14435, 14433,
                        13155, 24880, 25400, 12339, 13921, 13923, 13921, 
                        13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0)
                    Unknown18011('pt553', 14689, 13923, 14689, 13923, 14689,
                        13923, 14689, 13923, 14689, 13923, 13921, 13923, 
                        13921, 13923, 13921, 13923, 24880, 25398, 24886, 
                        12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('pt5520', 13665, 13667, 13665, 13667, 13665, 
                    13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
                Unknown18011('pt5521', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 14433, 13923, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt553', 12641, 25394, 12339, 13921, 13411, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411,
                    24880, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_44:
                    Unknown18011('pt5520', 14177, 14179, 14177, 14179, 
                        14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    Unknown18011('pt5521', 14177, 14179, 14177, 14179, 
                        14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                        14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                        12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    Unknown18011('pt553', 14689, 13923, 14689, 13923, 14689,
                        13923, 14689, 13923, 14689, 13923, 13921, 13923, 
                        13921, 13923, 13921, 13923, 24880, 25398, 24886, 
                        12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('pt558', 13921, 13923, 13921, 13923, 13921, 13155,
                24880, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0)
            Unknown18011('pt559', 14433, 14435, 14433, 14435, 14433, 14435,
                14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 
                14433, 14435, 14433, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('pt558', 12641, 25392, 12339, 13921, 13923, 
                    13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923,
                    13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt559', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_44:
                Unknown18011('pt558', 14433, 14435, 14433, 14435, 14433, 
                    14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433,
                    14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt559', 14433, 14435, 14433, 13923, 24880, 
                    25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888,
                    25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_140:
                    Unknown18011('pt558', 14689, 14691, 14689, 14691, 14689,
                        13667, 24880, 25398, 24886, 25398, 24886, 25398, 
                        24886, 25398, 12339, 14433, 14435, 14433, 14435, 
                        14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    Unknown18011('pt559', 14433, 14435, 14433, 14435, 14433,
                        14435, 14433, 14435, 14433, 13667, 24880, 25400, 
                        24888, 25400, 24888, 25400, 24888, 25400, 24888, 
                        25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jb'):
            Unknown18011('pt000', 14177, 14179, 14177, 14179, 14177, 12899,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 
                14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt400', 14433, 14435, 14433, 14435, 12897, 25392,
                12339, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 
                14435, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt401', 14177, 13667, 14177, 13667, 14177, 12899,
                24880, 25400, 24888, 25400, 24888, 12338, 14435, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt570', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('pt571', 14177, 12899, 24880, 25399, 12340, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 
                25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_44:
                Unknown18011('pt000', 14689, 14435, 14177, 14179, 14177, 
                    14435, 12641, 25395, 12339, 14177, 14179, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397,
                    55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0)
                Unknown18011('pt400', 14433, 14435, 14433, 14435, 12897, 
                    25392, 12852, 14433, 14435, 14433, 14435, 14433, 14435,
                    14433, 14435, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt401', 14433, 14435, 14433, 14435, 14433, 
                    12899, 24880, 25400, 24888, 25400, 24888, 12338, 14435,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt570', 12899, 12341, 12897, 25392, 55, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('pt571', 14433, 14435, 14433, 14435, 14433, 
                    14435, 13153, 25392, 12342, 14433, 14435, 14433, 14435,
                    14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435,
                    12897, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jn'):
        SyncEntry()
        gotoLabel(110)
    if CharacterIDCheck('kg'):
        SyncEntry()
        gotoLabel(330)
    if CharacterIDCheck('tm'):
        SyncEntry()
        gotoLabel(350)
    if CharacterIDCheck('ce'):
        SyncEntry()
        if SLOT_138:
            gotoLabel(360)
        else:
            gotoLabel(1360)
    if CharacterIDCheck('ph'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2390)
        else:
            gotoLabel(390)
    if CharacterIDCheck('jb'):
        SyncEntry()
        gotoLabel(440)
    label(482)
    if random_(2, 0, 34):
        conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('pt600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('pt600_00', 39)
    Voiceline('pt412')
    label(1)
    sprite('pt600_00', 6)
    if SLOT_97:
        conditionalSendToLabel(1)
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('008_swing_pole_2')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    CommonSE('008_swing_pole_2')
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 15)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CommonSE('019_cloth_c')
    PrivateSE('ptse_13')
    Voiceline('pt413')
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(10)
    sprite('pt601_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(10)
    sprite('pt601_00', 30)
    Voiceline('pt414')
    label(11)
    sprite('pt601_00', 5)
    if SLOT_97:
        conditionalSendToLabel(11)
    sprite('pt601_00', 15)
    CreateParticle('ptef_entryheartA', 0)
    PrivateSE('ptse_15')
    sprite('pt601_01', 6)
    sprite('pt601_02', 6)
    CreateObject('EntryHeart', 0)
    PrivateSE('ptse_21')
    sprite('pt601_03', 6)
    sprite('pt601_04', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    sprite('pt601_07', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    sprite('pt601_07', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    sprite('pt601_07', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    CreateObject('EntryRod', -1)
    sprite('pt601_07', 6)
    sprite('pt601_08', 6)
    sprite('pt601_09', 6)
    sprite('pt601_10', 5)
    CreateParticle('ptef_450light01', 0)
    CommonSE('003_swing_grap_0_1')
    CommonSE('100_hit_grap_0')
    sprite('pt601_11', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CommonSE('008_swing_pole_0')
    sprite('pt601_12', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CreateParticle('ptef_450light01', 2)
    sprite('pt601_13', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CreateParticle('ptef_450light01', 2)
    sprite('pt601_14', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CommonSE('008_swing_pole_0')
    sprite('pt601_15', 4)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    sprite('pt601_16', 3)
    CreateParticle('ptef_450light01', 0)
    sprite('pt601_17', 7)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CreateParticle('ptef_450light01', 0)
    PrivateSE('ptse_13')
    sprite('pt601_18', 6)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    Voiceline('pt415')
    sprite('pt601_19', 6)
    label(12)
    sprite('pt601_20', 9)
    if SLOT_97:
        conditionalSendToLabel(12)
    sprite('pt601_21', 6)
    sprite('pt601_22', 5)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(20)
    sprite('null', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(20)
    sprite('pt331_05', 100)
    CreateObject('FusenEntry', -1)
    XPositionRelativeFacing(-521000)
    AbsoluteY(350000)
    physicsXImpulse(1500)
    setGravity(7)
    Visibility(1)
    Voiceline('pt416')
    sprite('pt331_05', 74)
    sprite('pt331_06', 3)
    CreateParticle('ptef_entrysmoke', 0)
    EndMomentum(1)
    physicsYImpulse(24000)
    Visibility(0)
    Voiceline('pt417')
    sprite('pt331_07', 4)
    YAccel(40)
    sprite('pt331_08', 6)
    setGravity(1300)
    sprite('pt331_06', 6)
    sprite('pt331_07', 6)
    sprite('pt331_08', 6)
    sprite('pt331_13', 6)
    physicsXImpulse(0)
    uponSendToLabel(LANDING, 22)
    sprite('pt331_14', 6)
    label(21)
    sprite('pt020_07', 6)
    sprite('pt020_08', 6)
    loopRest()
    gotoLabel(21)
    label(22)
    sprite('pt024_00', 3)
    XPositionRelativeFacing(-260000)
    clearUponHandler(LANDING)
    LandingEffects(100, 1, 1)
    sprite('pt024_01', 9)
    sprite('pt024_02', 5)
    sprite('pt024_03', 5)
    sprite('pt024_04', 5)
    sprite('pt024_05', 5)
    sprite('pt000_00', 3)
    DemoTimer(60)
    loopRest()
    ExitState()
    label(110)
    uponSendToLabel(32, 112)
    label(111)
    sprite('pt600_00', 6)
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('pt600_00', 120)
    clearUponHandler(32)
    Voiceline('pt502')
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('008_swing_pole_2')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    CommonSE('008_swing_pole_2')
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 15)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CommonSE('019_cloth_c')
    PrivateSE('ptse_13')
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    loopRest()
    ExitState()
    label(330)
    uponSendToLabel(32, 331)
    sprite('pt001_00', 180)
    loopRest()
    gotoLabel(330)
    label(331)
    uponSendToLabel(33, 332)
    sprite('pt001_00', 180)
    loopRest()
    gotoLabel(331)
    label(332)
    sprite('pt001_00', 5)
    Voiceline('pt546')
    label(333)
    sprite('pt001_00', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(333)
    sprite('pt001_00', 20)
    ObjectUpon(22, 32)
    sprite('pt001_01', 5)
    sprite('pt001_02', 8)
    sprite('pt001_03', 8)
    sprite('pt001_04', 8)
    sprite('pt001_05', 8)
    sprite('pt001_06', 5)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(350)
    sprite('pt600_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(350)
    sprite('pt600_00', 220)
    Voiceline('pt550')
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('008_swing_pole_2')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    CommonSE('008_swing_pole_2')
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 15)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CommonSE('019_cloth_c')
    PrivateSE('ptse_13')
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(360)
    uponSendToLabel(32, 362)
    label(361)
    sprite('pt600_00', 6)
    loopRest()
    gotoLabel(361)
    label(362)
    sprite('pt600_00', 150)
    clearUponHandler(32)
    Voiceline('pt552')
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('008_swing_pole_2')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    CommonSE('008_swing_pole_2')
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 15)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CommonSE('019_cloth_c')
    PrivateSE('ptse_13')
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    loopRest()
    ExitState()
    label(1360)
    sprite('pt601_00', 1)
    uponSendToLabel(32, 1361)
    sprite('pt601_00', 32767)
    loopRest()
    label(1361)
    sprite('pt601_00', 2)
    SpriteIfNot0(30, 2, 44)
    Voiceline('pt5520')
    sprite('pt601_00', 30)
    CreateParticle('ptef_entryheartA', 0)
    PrivateSE('ptse_15')
    sprite('pt601_01', 6)
    sprite('pt601_02', 6)
    CreateObject('EntryHeart', 0)
    PrivateSE('ptse_21')
    sprite('pt601_03', 6)
    sprite('pt601_04', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    sprite('pt601_07', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    sprite('pt601_07', 6)
    sprite('pt601_05', 6)
    sprite('pt601_06', 6)
    CreateObject('EntryRod', -1)
    sprite('pt601_07', 6)
    sprite('pt601_08', 6)
    sprite('pt601_09', 6)
    sprite('pt601_10', 5)
    CreateParticle('ptef_450light01', 0)
    CommonSE('003_swing_grap_0_1')
    CommonSE('100_hit_grap_0')
    sprite('pt601_11', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CommonSE('008_swing_pole_0')
    sprite('pt601_12', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CreateParticle('ptef_450light01', 2)
    sprite('pt601_13', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CreateParticle('ptef_450light01', 2)
    sprite('pt601_14', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    CommonSE('008_swing_pole_0')
    sprite('pt601_15', 4)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    sprite('pt601_16', 3)
    CreateParticle('ptef_450light01', 0)
    sprite('pt601_17', 5)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CreateParticle('ptef_450light01', 0)
    PrivateSE('ptse_13')
    sprite('pt601_18', 5)
    CreateParticle('ptef_450light01', 0)
    CreateParticle('ptef_450light01', 1)
    sprite('pt601_19', 5)
    sprite('pt601_20', 6)
    Voiceline('pt5521')
    label(1362)
    sprite('pt601_20', 10)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(1362)
    sprite('pt601_20', 20)
    sprite('pt601_21', 6)
    ObjectUpon(22, 32)
    sprite('pt601_22', 5)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(390)
    uponSendToLabel(32, 392)
    label(391)
    sprite('pt600_00', 6)
    loopRest()
    gotoLabel(391)
    label(392)
    if SLOT_44:
        gotoLabel(393)
    sprite('pt600_00', 90)
    Voiceline('pt558')
    clearUponHandler(32)
    loopRest()
    gotoLabel(394)
    label(393)
    sprite('pt600_00', 120)
    Voiceline('pt558')
    clearUponHandler(32)
    loopRest()
    label(394)
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('008_swing_pole_2')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    CommonSE('008_swing_pole_2')
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 15)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CommonSE('019_cloth_c')
    PrivateSE('ptse_13')
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    loopRest()
    ExitState()
    label(2390)
    uponSendToLabel(32, 2392)
    label(2391)
    sprite('pt600_00', 6)
    loopRest()
    gotoLabel(2391)
    label(2392)
    if SLOT_44:
        gotoLabel(2393)
    sprite('pt600_00', 90)
    Voiceline('pt558')
    clearUponHandler(32)
    loopRest()
    gotoLabel(2394)
    label(2393)
    sprite('pt600_00', 120)
    Voiceline('pt558')
    clearUponHandler(32)
    loopRest()
    label(2394)
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('008_swing_pole_2')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    CommonSE('008_swing_pole_2')
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 15)
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    CommonSE('019_cloth_c')
    PrivateSE('ptse_13')
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(440)
    sprite('null', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(440)
    sprite('pt331_05', 100)
    CreateObject('FusenEntry', -1)
    XPositionRelativeFacing(-521000)
    AbsoluteY(350000)
    physicsXImpulse(1500)
    setGravity(7)
    Visibility(1)
    Voiceline('pt570')
    sprite('pt331_05', 74)
    sprite('pt331_06', 3)
    CreateParticle('ptef_entrysmoke', 0)
    EndMomentum(1)
    physicsYImpulse(24000)
    Visibility(0)
    sprite('pt331_07', 4)
    YAccel(40)
    sprite('pt331_08', 6)
    setGravity(1300)
    sprite('pt331_06', 6)
    sprite('pt331_07', 6)
    sprite('pt331_08', 6)
    sprite('pt331_13', 6)
    physicsXImpulse(0)
    uponSendToLabel(LANDING, 442)
    sprite('pt331_14', 6)
    label(441)
    sprite('pt020_07', 6)
    sprite('pt020_08', 6)
    loopRest()
    gotoLabel(441)
    label(442)
    sprite('pt024_00', 3)
    XPositionRelativeFacing(-260000)
    clearUponHandler(LANDING)
    LandingEffects(100, 1, 1)
    sprite('pt024_01', 9)
    sprite('pt024_02', 5)
    sprite('pt024_03', 5)
    sprite('pt024_04', 5)
    sprite('pt024_05', 5)
    ObjectUpon(22, 32)
    sprite('pt000_00', 3)
    DemoTimer(60)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    label(0)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 5)
    if random_(2, 0, 50):
        Voiceline('pt400')
        DemoEndOnVoiceEnd(1)
    else:
        Voiceline('pt401')
        DemoEndOnVoiceEnd(1)
    sprite('pt615_07', 5)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    label(2)
    sprite('pt615_09', 5)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('pt615_06', 32767)
    loopRest()


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jn'):
        conditionalSendToLabel(110)
    if CharacterIDCheck('kg'):
        conditionalSendToLabel(330)
    if CharacterIDCheck('tm'):
        conditionalSendToLabel(350)
    if CharacterIDCheck('ce'):
        if SLOT_138:
            gotoLabel(360)
        else:
            gotoLabel(1360)
    if CharacterIDCheck('ph'):
        if SLOT_140:
            gotoLabel(2390)
        else:
            gotoLabel(390)
    if CharacterIDCheck('jb'):
        conditionalSendToLabel(440)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    label(0)
    SetZLine(1, 100)
    SetActionMark(1)
    WallCollisionDetection(0)
    ScreenCollision(0)
    CameraControlEnable(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 200000:
                SetActionMark(0)
                sendToLabel(2)
        if not SLOT_2:

            def RunOnObject_22():
                WallCollisionDetection(0)
                ScreenCollision(0)
            if SLOT_29 >= 1600000:
                sendToLabel(4)
    sprite('pt610_00', 3)
    physicsXImpulse(5000)
    SpecialSE('ptse_14')
    sprite('pt610_01', 3)
    sprite('pt610_02', 3)
    sprite('pt610_03', 3)
    sprite('pt610_04', 3)
    sprite('pt610_05', 3)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    label(1)
    sprite('pt610_06', 6)
    sprite('pt610_07', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_08', 6)
    sprite('pt610_06', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_07', 6)
    sprite('pt610_08', 6)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('pt610_06', 6)
    physicsXImpulse(5000)
    if random_(2, 0, 50):
        Voiceline('pt406')
        if SLOT_43:
            DemoTimer(160)
        else:
            DemoTimer(210)
    else:
        Voiceline('pt407')
        if SLOT_43:
            DemoTimer(150)
        else:
            DemoTimer(120)
    sprite('pt610_07', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_08', 6)
    sprite('pt610_06', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_07', 6)
    sprite('pt610_08', 6)
    sprite('pt610_06', 6)
    sprite('pt610_07', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_08', 6)
    sprite('pt610_09', 3)
    sprite('pt610_10', 3)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_11', 3)
    physicsXImpulse(0)
    SetZLine(0, 100)
    CameraControlEnable(0)
    CameraLookAtEnemy(1)
    sprite('pt610_10ex01', 3)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_09ex01', 3)
    physicsXImpulse(-5000)
    physicsYImpulse(700)
    label(3)
    sprite('pt610_06ex01', 6)
    sprite('pt610_07ex01', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_08ex01', 6)
    sprite('pt610_06ex01', 6)
    CreateParticle('ptef_402light', 0)
    CreateParticle('ptef_402light', 1)
    sprite('pt610_07ex01', 6)
    sprite('pt610_08ex01', 6)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('pt610_07ex01', 32767)
    EndMomentum(1)
    label(10)
    sprite('pt611_00', 3)
    sprite('pt611_01', 4)
    sprite('pt611_02', 4)
    CreateParticle('ptef_drivethrow', 0)
    CreateParticle('ptef_winsmoke', 1)
    CreateParticle('ptef_winsmoke', 2)
    CommonSE('016_explode_0')
    Voiceline('pt408')
    sprite('pt611_03', 6)
    sprite('pt611_04', 8)
    sprite('pt611_05', 4)
    sprite('pt611_06', 4)
    sprite('pt611_07', 5)
    PrivateSE('ptse_03')
    sprite('pt611_08', 5)
    sprite('pt611_09', 4)
    sprite('pt611_10', 4)
    sprite('pt611_11', 4)
    sprite('pt611_12', 4)
    sprite('pt611_13', 6)
    sprite('pt611_14', 6)
    sprite('pt611_15', 6)
    sprite('pt611_14ex00', 6)
    DemoTimer(120)
    label(11)
    sprite('pt611_16', 7)
    CreateParticle('ptef_winheart', 0)
    PrivateSE('ptse_15')
    sprite('pt611_17', 7)
    sprite('pt611_18', 7)
    sprite('pt611_17', 7)
    sprite('pt611_16', 7)
    sprite('pt611_17', 7)
    sprite('pt611_18', 7)
    sprite('pt611_17', 7)
    sprite('pt611_16', 7)
    sprite('pt611_17', 7)
    sprite('pt611_18', 7)
    sprite('pt611_17', 7)
    gotoLabel(11)
    label(110)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 5)
    sprite('pt615_06', 150)
    Voiceline('pt5030')
    sprite('pt615_06', 32767)
    Voiceline('pt5031')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(330)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(332)
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    label(331)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(331)
    label(332)
    physicsXImpulse(0)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 32767)
    Voiceline('pt547')
    DemoEndOnVoiceEnd(1)
    loopRest()
    gotoLabel(332)
    label(350)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(352)
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    label(351)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(351)
    label(352)
    physicsXImpulse(0)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 5)
    Voiceline('pt551')
    DemoEndOnVoiceEnd(1)
    sprite('pt615_07', 5)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    label(353)
    sprite('pt615_09', 5)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    loopRest()
    gotoLabel(353)
    label(360)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(362)
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    label(361)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(361)
    label(362)
    physicsXImpulse(0)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 32767)
    Voiceline('pt553')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(1360)
    CameraControlEnable(1)
    sprite('pt430_00', 6)
    sprite('pt430_01', 6)
    sprite('pt430_02', 6)
    sprite('pt430_03', 3)
    sprite('pt430_04', 3)
    sprite('pt430_05', 3)
    Voiceline('pt553')
    DemoEndOnVoiceEnd(1)
    loopRest()
    sprite('pt430_06', 3)
    CommonSE('008_swing_pole_2')
    sprite('pt430_07', 3)
    sprite('pt430_08', 3)
    sprite('pt430_09', 3)
    sprite('pt430_10', 3)
    sprite('pt430_12', 3)
    sprite('pt430_06', 2)
    CommonSE('008_swing_pole_2')
    sprite('pt430_07', 2)
    sprite('pt430_08', 2)
    sprite('pt430_09', 2)
    sprite('pt430_10', 2)
    sprite('pt430_12', 2)
    sprite('pt430_06', 2)
    CommonSE('008_swing_pole_2')
    sprite('pt430_07', 2)
    sprite('pt430_08', 2)
    sprite('pt430_09', 2)
    sprite('pt430_10', 2)
    sprite('pt430_12', 2)
    sprite('pt430_06', 3)
    CommonSE('008_swing_pole_2')
    sprite('pt430_07', 3)
    CreateObject('pt430_circle1', 1)
    CreateObject('pt430_circle2', 1)
    sprite('pt430_08', 3)
    sprite('pt430_09', 3)
    sprite('pt430_10', 3)
    sprite('pt430_11', 3)
    CreateObject('ptef_430power', 0)
    PrivateSE('ptse_09')
    sprite('pt430_12', 3)
    sprite('pt430_13', 3)
    sprite('pt203_02', 40)
    sprite('pt203_03', 1)
    TriggerUponForState('SphereLight_Model', 32)
    PrivateSE('ptse_13')
    label(1361)
    sprite('pt203_03', 7)
    CreateObject('pt430_stick', 0)
    PrivateSE('ptse_16')
    sprite('pt203_04', 7)
    sprite('pt203_05', 8)
    sprite('pt203_04', 7)
    sprite('pt203_03', 7)
    sprite('pt203_04', 7)
    sprite('pt203_05', 8)
    sprite('pt203_04', 7)
    loopRest()
    gotoLabel(1361)
    label(390)
    CameraControlEnable(1)
    physicsXImpulse(5000)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(392)
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    label(391)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(391)
    label(392)
    physicsXImpulse(0)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 32767)
    Voiceline('pt559')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(2390)
    sprite('keep', 1)
    CameraControlEnable(1)

    def upon_EVERY_FRAME():
        if SLOT_29 < 280000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            sendToLabel(2392)
    sprite('pt030_00', 5)
    physicsXImpulse(5000)
    sprite('pt030_01', 5)
    label(2391)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(2391)
    label(2392)
    sprite('pt615_00', 5)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 32767)
    Voiceline('pt559')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(440)
    sprite('keep', 1)
    CameraControlEnable(1)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_29 < 280000:
                SetActionMark(0)
                sendToLabel(442)
    sprite('pt030_00', 5)
    physicsXImpulse(5000)
    sprite('pt030_01', 5)
    label(441)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(441)
    label(442)
    sprite('pt615_00', 5)
    EndMomentum(1)
    sprite('pt615_01', 5)
    sprite('pt615_02', 5)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 5)
    sprite('pt615_04', 5)
    sprite('pt615_05', 5)
    sprite('pt615_06', 32767)
    Voiceline('pt571')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(666)
    sprite('pt611_00', 3)
    sprite('pt611_01', 4)
    sprite('pt611_02', 4)
    CreateParticle('ptef_drivethrow', 0)
    CreateParticle('ptef_winsmoke', 1)
    CreateParticle('ptef_winsmoke', 2)
    CommonSE('016_explode_0')
    if random_(2, 0, 50):
        Voiceline('pt406')
    else:
        Voiceline('pt408')
    DemoEndOnVoiceEnd(1)
    sprite('pt611_03', 6)
    sprite('pt611_04', 8)
    sprite('pt611_05', 4)
    sprite('pt611_06', 4)
    sprite('pt611_07', 5)
    PrivateSE('ptse_03')
    sprite('pt611_08', 5)
    sprite('pt611_09', 4)
    sprite('pt611_10', 4)
    sprite('pt611_11', 4)
    sprite('pt611_12', 4)
    sprite('pt611_13', 6)
    sprite('pt611_14', 6)
    sprite('pt611_15', 6)
    sprite('pt611_14ex00', 6)
    label(667)
    sprite('pt611_16', 7)
    CreateParticle('ptef_winheart', 0)
    PrivateSE('ptse_15')
    sprite('pt611_17', 7)
    sprite('pt611_18', 7)
    sprite('pt611_17', 7)
    sprite('pt611_16', 7)
    sprite('pt611_17', 7)
    sprite('pt611_18', 7)
    sprite('pt611_17', 7)
    sprite('pt611_16', 7)
    sprite('pt611_17', 7)
    sprite('pt611_18', 7)
    sprite('pt611_17', 7)
    gotoLabel(667)
    loopRest()


@State
def CmnActLose():
    sprite('pt620_00', 6)
    Voiceline('pt411')
    sprite('pt620_01', 6)
    sprite('pt620_02', 6)
    sprite('pt620_03', 6)
    CommonSE('019_cloth_b')
    sprite('pt620_04', 6)
    sprite('pt620_05', 6)
    sprite('pt620_06', 6)
    sprite('pt620_07', 6)
    sprite('pt620_08', 6)
    SpecialSE('ptse_05')
    sprite('pt620_09', 6)
    sprite('pt620_10', 6)
    sprite('pt620_09', 6)
    sprite('pt620_08', 6)
    sprite('pt620_09', 6)
    sprite('pt620_10', 6)
    sprite('pt620_11', 6)
    EndSE()
    sprite('pt620_12', 12)
    sprite('pt620_11', 6)
    DemoTimer(90)
    sprite('pt620_10', 6)
    PrivateSE('ptse_29')
    sprite('pt620_09', 6)
    sprite('pt620_08', 6)
    sprite('pt620_09', 6)
    label(0)
    sprite('pt620_10', 6)
    sprite('pt620_09', 6)
    sprite('pt620_08', 6)
    sprite('pt620_09', 6)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryWait():
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def EventDefEntryStand():
    sprite('keep', 2)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefWin():
    sprite('keep', 2)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefLose():
    label(0)
    sprite('pt620_10', 6)
    sprite('pt620_09', 6)
    sprite('pt620_08', 6)
    sprite('pt620_09', 6)
    gotoLabel(0)


@State
def EventDefLose2():
    sprite('pt063_11', 32767)


@State
def EventNoDisp():
    sprite('keep', 32767)
    Visibility(1)


@State
def EventChouhatsu():
    sprite('pt300_00', 4)
    sprite('pt300_01', 4)
    sprite('pt300_02', 4)
    sprite('pt300_03', 6)
    sprite('pt300_04', 6)
    sprite('pt300_05', 7)
    sprite('pt300_06', 30)
    sprite('pt300_07', 7)
    PrivateSE('ptse_00')
    sprite('pt300_08', 9)
    sprite('pt300_09', 6)
    sprite('pt000_00', 1)
    enterState('CmnActStand')


@State
def EventDownFaceUp():
    sprite('pt060_14', 32767)
    loopRest()


@State
def EventDownFaceUpToStand():
    sprite('pt061_00', 3)
    sprite('pt061_01', 3)
    sprite('pt061_02', 3)
    sprite('pt061_03', 3)
    sprite('pt061_04', 3)
    sprite('pt061_05', 3)
    sprite('pt061_06', 2)
    sprite('pt061_07', 2)
    sprite('pt061_08', 2)
    sprite('pt061_09', 2)
    loopRest()
    enterState('CmnActStand')


@State
def EventDashLeaveOpposite():
    sprite('pt003_00', 3)
    ForceFaceSprite()
    Flip()
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)
    sprite('pt032_00', 2)
    physicsXImpulse(25000)
    PreDashEffects(100, 1, 1)
    EnableCollision(0)
    ScreenCollision(0)
    sprite('pt032_01', 2)
    label(0)
    sprite('pt032_02', 4)
    sprite('pt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_04', 4)
    sprite('pt032_05', 4)
    sprite('pt032_06', 4)
    sprite('pt032_07', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_08', 4)
    loopRest()
    gotoLabel(0)


@State
def EventDefLose3():
    sprite('pt620_05', 32767)


@State
def EventSitting():
    sprite('pt064_02', 32767)


@State
def EventSittingEnd():
    sprite('pt064_02', 7)
    sprite('pt064_03', 7)
    sprite('pt064_04', 7)
    sprite('pt064_05', 7)
    sprite('pt064_06', 7)
    sprite('pt064_07', 7)
    sprite('pt064_08', 7)
    sprite('pt064_09', 7)
    sprite('pt064_10', 7)
    sprite('pt000_00', 1)
    enterState('CmnActStand')


@State
def EventVSAR1():
    ScreenCollision(0)
    XPositionRelativeFacing(-2400000)
    sprite('null', 32767)


@State
def EventVSAR2():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('pt030_00', 7)
    CameraControlEnable(1)
    sprite('pt030_01', 6)
    physicsXImpulse(1650)
    label(0)
    sprite('pt030_02', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 6)
    sprite('pt030_04', 6)
    sprite('pt030_05', 6)
    sprite('pt030_06', 6)
    sprite('pt030_07', 6)
    sprite('pt030_08', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 6)
    sprite('pt030_10', 6)
    sprite('pt030_11', 6)
    sprite('pt030_12', 6)
    sprite('pt030_13', 6)
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    CameraControlEnable(0)
    enterState('CmnActStand')


@State
def EventVSHA1():
    sprite('pt070_13', 8)
    sprite('pt070_12', 8)
    sprite('pt070_11', 8)
    sprite('pt070_10', 32767)


@State
def EventPhantom():
    sprite('pt000_00', 7)
    CreateObject('ptPhantom_2', 0)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-20000)
        SetZVal(-500)
    CommonSE('022_magiccircle_b')
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventPhantomDelete():
    sprite('keep', 2)
    ObjectUpon(FALLING, 32)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSHA2():
    sprite('pt070_10', 8)
    sprite('pt070_11', 8)
    sprite('pt070_12', 8)
    sprite('pt070_13', 8)
    loopRest()
    enterState('EventPhantom')


@State
def EventTKVsPT_StompTao():
    ForceFaceSprite()
    XPositionRelativeFacing(-1100000)
    ScreenCollision(0)
    EnableCollision(0)
    SetZLine(1, 50)

    def upon_EVERY_FRAME():
        if SLOT_19 < 100000:
            sendToLabel(1)
    sprite('pt030_00', 7)
    sprite('pt030_01', 5)
    CameraControlEnable(1)
    physicsXImpulse(8000)
    loopRest()
    label(0)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    gotoLabel(0)
    label(1)
    clearUponHandler(EVERY_FRAME)
    CameraControlEnable(0)
    EndMomentum(1)
    sprite('keep', 32767)
    PrivateSE('ptse_00')
    CommonSE('021_bonecleak_0')
    ScreenShake(0, 8000)
    CreateParticle('ef_hits', -1)
    CreateParticle('ef_jumpsmoke00', -1)
    loopRest()


@State
def EventTKVsPT_Surprised():
    EnableCollision(0)
    SetZLine(1, 50)
    sprite('pt000_00', 4)
    sprite('pt050_00', 4)
    sprite('pt050_00', 2)
    physicsXImpulse(-40000)
    sprite('pt050_01', 2)
    sprite('pt050_01', 2)
    physicsXImpulse(0)
    Unknown1004()
    AddX(1000)
    loopRest()
    SLOT_51 = 0
    label(0)
    sprite('pt050_01', 2)
    AddX(-2000)
    sprite('pt050_01', 2)
    AddX(2000)
    SLOT_51 = SLOT_51 + 1
    loopRest()
    if SLOT_51 < 8:
        conditionalSendToLabel(0)
    sprite('pt050_01', 4)
    Unknown1005()
    sprite('pt050_00', 4)
    sprite('pt615_00', 4)
    sprite('pt615_01', 4)
    sprite('pt615_02', 4)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 4)
    sprite('pt615_04', 4)
    sprite('pt615_05', 4)
    sprite('pt615_06', 4)
    sprite('pt615_07', 4)
    loopRest()
    SLOT_51 = 0
    label(1)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    sprite('pt615_09', 5)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    sprite('pt615_09', 90)
    SLOT_51 = SLOT_51 + 1
    loopRest()
    if SLOT_51 < 3:
        conditionalSendToLabel(1)
    sprite('pt615_09', 32767)
    loopRest()


@State
def EventTKVsPT_JumpAway():
    EnableCollision(0)
    SetZLine(1, 50)
    sprite('pt615_03', 2)
    sprite('pt615_02', 2)
    sprite('pt052_01', 2)
    sprite('pt052_02', 2)
    sprite('pt052_03', 2)
    Unknown1004()
    AddX(2000)
    loopRest()
    SLOT_51 = 0
    label(0)
    sprite('pt052_03', 2)
    AddX(-4000)
    sprite('pt052_03', 2)
    AddX(4000)
    SLOT_51 = SLOT_51 + 1
    loopRest()
    if SLOT_51 < 8:
        conditionalSendToLabel(0)
    sprite('pt052_02', 2)
    Unknown1005()
    loopRest()
    uponSendToLabel(LANDING, 2)
    sprite('pt033_01', 1)
    physicsXImpulse(-32000)
    physicsYImpulse(2000)
    setGravity(1500)
    JumpSoundEffects()
    sprite('pt033_02', 1)
    sprite('pt033_03', 1)
    loopRest()
    label(1)
    sprite('pt033_02', 3)
    sprite('pt033_03', 3)
    loopRest()
    gotoLabel(1)
    label(2)
    clearUponHandler(LANDING)
    sprite('pt033_04', 2)
    sprite('pt033_05', 2)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    LandingEffects(100, 1, 1)
    sprite('pt033_06', 2)
    loopRest()
    enterState('CmnActStand')


@State
def EventPTHood():
    sprite('pt600_00', 32767)


@State
def EventPTHoodEnd():
    sprite('pt600_01', 6)
    sprite('pt600_02', 6)
    CommonSE('019_cloth_c')
    sprite('pt600_03', 6)
    sprite('pt600_04', 6)
    sprite('pt600_05', 7)
    sprite('pt600_06', 5)
    CreateParticle('ptef_entrylightA', 0)
    sprite('pt600_07', 5)
    CharacterFlash(13145800, 16, 2)
    sprite('pt600_08', 4)
    sprite('pt600_08', 3)
    CreateParticle('ptef_entrylightB', 0)
    sprite('pt600_08', 3)
    sprite('pt600_09', 6)
    sprite('pt600_10', 8)
    PrivateSE('ptse_13')
    CreateObject('yugami_ring', 0)
    CreateParticle('ptef_entrymc', 0)
    sprite('pt600_11', 6)
    sprite('pt600_12', 5)
    sprite('pt600_10ex00', 5)
    sprite('pt600_11ex00', 5)
    sprite('pt600_12ex00', 5)
    sprite('pt600_13', 6)
    sprite('pt600_14', 6)
    sprite('pt600_15', 6)
    sprite('pt600_16', 6)
    enterState('CmnActStand')


@State
def EventPTWalkaway():
    EnableCollision(0)
    ScreenCollision(0)
    physicsXImpulse(6200)
    sprite('pt030_00', 5)
    sprite('pt030_01', 5)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)


@State
def EventYorokeStart():
    sprite('pt070_00', 5)
    sprite('pt070_01', 5)
    label(0)
    sprite('pt070_02', 5)
    loopRest()
    gotoLabel(0)


@State
def EventYorokeEnd():
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_01', 5)
    sprite('pt070_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def EventWarp():

    def upon_IMMEDIATE():
        SetZVal(-500)
        ScreenCollision(0)
        BlendMode_Normal()
    sprite('pt071_00', 4)
    sprite('pt071_01', 4)
    sprite('pt071_02', 2)
    sprite('pt071_03', 2)
    sprite('pt071_04', 2)
    sprite('pt071_05', 2)
    sprite('pt071_06', 2)
    sprite('pt071_07', 2)
    sprite('pt071_08', 2)
    sprite('pt071_09', 2)
    sprite('pt071_02', 2)
    CreateParticle('haef_event_lose', 103)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('pt071_03', 2)
    sprite('pt071_04', 2)
    sprite('pt071_05', 2)
    sprite('pt071_06', 2)
    sprite('pt071_07', 2)
    sprite('pt071_08', 2)
    sprite('pt071_09', 2)
    sprite('pt071_02', 2)
    sprite('pt071_03', 2)
    sprite('pt071_04', 2)
    sprite('pt071_05', 2)
    sprite('pt071_06', 2)
    sprite('pt071_07', 2)
    CreateParticle('haef_event_lose_end', 103)
    XPositionRelativeFacing(-500000)
    sprite('pt071_08', 2)
    sprite('pt071_09', 2)
    sprite('null', 32767)
    loopRest()


@State
def EventPTFrameOut():
    ScreenCollision(0)
    XPositionRelativeFacing(-900000)
    sprite('null', 32767)


@State
def EventPTWalkFrameIn():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('pt030_00', 7)
    sprite('pt030_01', 5)
    physicsXImpulse(4650)
    label(0)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventPTSuwari():
    sprite('pt620_00', 6)
    sprite('pt620_01', 6)
    sprite('pt620_02', 6)
    LandingEffects(100, 1, 1)
    sprite('pt620_03', 6)
    sprite('pt620_04', 6)
    sprite('pt620_05', 32767)


@State
def EventPTFSitDown():
    sprite('pt064_10', 5)
    sprite('pt064_09', 5)
    sprite('pt064_08', 5)
    sprite('pt064_07', 5)
    sprite('pt064_06', 5)
    sprite('pt064_05', 5)
    sprite('pt064_04', 5)
    LandingEffects(100, 1, 1)
    sprite('pt064_03', 32767)


@State
def EventPTFSitDown02():
    sprite('pt064_02', 5)
    sprite('pt064_01', 5)
    sprite('pt064_00', 5)
    sprite('pt063_11', 32767)
    KnockdownEffects(100, 1, 1)


@State
def EventPTFDownLoop():
    sprite('pt063_11', 32767)


@State
def EventPTFDown2Stand01():
    sprite('pt064_00', 5)
    sprite('pt064_01', 5)
    sprite('pt064_02', 5)
    sprite('pt064_03', 32767)


@State
def EventPTFDown2Stand02():
    sprite('pt064_04', 5)
    sprite('pt064_05', 5)
    sprite('pt064_06', 5)
    sprite('pt064_07', 5)
    sprite('pt064_08', 5)
    sprite('pt064_09', 5)
    sprite('pt064_10', 5)
    sprite('pt000_00', 1)
    enterState('CmnActStand')


@State
def EventPTExcite():
    sprite('pt300_00', 4)
    sprite('pt300_01', 4)
    sprite('pt300_02', 4)
    sprite('pt300_03', 6)
    sprite('pt300_04', 6)
    sprite('pt300_05', 7)
    sprite('pt300_06', 30)
    sprite('pt300_07', 7)
    PrivateSE('ptse_00')
    sprite('pt300_08', 9)
    sprite('pt300_09', 6)
    sprite('pt000_00', 1)
    enterState('CmnActStand')


@State
def EventStartWithBN():
    SetZLine(1, 100)
    DeleteObject(7)
    CreateObject('EventPT01_ibbn', -1)
    RegisterObject(7, 1)
    sprite('pt063_11', 32767)
    loopRest()


@State
def EventWorpOutBN():
    sprite('keep', 100)
    ObjectUpon(CORNERED, 32)
    sprite('keep', 32767)
    DeleteObject(7)
    loopRest()


@State
def EventHZVsPT_Yoroke():
    sprite('pt043_00', 32767)
    loopRest()


@State
def EventHZVsPT_YorokeToWarp():
    sprite('pt010_01', 6)
    sprite('pt010_00', 6)
    loopRest()
    enterState('EventWarp')


@State
def EventVSHAWalk():
    ScreenCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('pt030_00', 7)
    CameraControlEnable(1)
    CreateObject('ptPhantom_2', 0)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-40000)
        physicsXImpulse(3250)
        SetZVal(-500)
    physicsXImpulse(3250)
    sprite('pt030_01_ex', 6)
    label(0)
    sprite('pt030_02_ex', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 6)
    sprite('pt030_04_ex', 6)
    sprite('pt030_05_ex', 6)
    sprite('pt030_06_ex', 6)
    sprite('pt030_07_ex', 6)
    sprite('pt030_08_ex', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 6)
    sprite('pt030_10_ex', 6)
    sprite('pt030_11_ex', 6)
    sprite('pt030_12_ex', 6)
    sprite('pt030_13_ex', 6)
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    CameraControlEnable(0)

    def RunOnObject_4():
        physicsXImpulse(0)
    enterState('CmnActStand')


@State
def EventPHTeni():

    def upon_IMMEDIATE():
        SetZVal(-500)
        ScreenCollision(0)
        BlendMode_Normal()
    label(0)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    ConstantAlphaModifier(-5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    CreateParticle('haef_event_lose_end', 103)
    XPositionRelativeFacing(-500000)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    sprite('null', 32767)
    loopRest()


@State
def EventNoAtk5C():
    sprite('pt202_00', 2)
    sprite('pt202_01', 3)
    sprite('pt202_03', 4)
    CommonSE('003_swing_grap_0_1')
    sprite('pt202_04', 6)
    sprite('pt202_05', 4)
    CommonSE('014_electric_m')
    sprite('pt202_06', 4)
    sprite('pt202_07', 4)
    sprite('pt202_08', 1)
    sprite('pt202_09', 2)
    sprite('pt202_10', 4)
    loopRest()
    enterState('CmnActStand')


@State
def EventVSTKTunTUn():
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 200000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('pt030_00', 7)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(-40000)
        physicsXImpulse(3250)
        SetZVal(-1000)
    physicsXImpulse(3250)
    sprite('pt030_01', 6)
    label(0)
    sprite('pt030_02_ex', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 6)
    sprite('pt030_04_ex', 6)
    sprite('pt030_05_ex', 6)
    sprite('pt030_06_ex', 6)
    sprite('pt030_07_ex', 6)
    sprite('pt030_08_ex', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 6)
    sprite('pt030_10_ex', 6)
    sprite('pt030_11_ex', 6)
    sprite('pt030_12_ex', 6)
    sprite('pt030_13_ex', 6)
    gotoLabel(0)
    label(1)
    sprite('pt615_00', 4)
    physicsXImpulse(0)
    sprite('pt615_01', 4)
    sprite('pt615_02', 4)
    CommonSE('019_cloth_b')
    sprite('pt615_03', 4)
    sprite('pt615_04', 4)
    sprite('pt615_05', 4)
    sprite('pt615_06', 4)
    sprite('pt615_07', 4)
    loopRest()
    label(2)
    sprite('pt615_09', 5)
    sprite('pt615_08', 5)
    sprite('pt615_09', 5)
    PrivateSE('ptse_25')
    sprite('pt615_10', 5)
    loopRest()
    gotoLabel(2)


@State
def EventVSBLWalk():
    ScreenCollision(0)
    SetActionMark(1)
    XPositionRelativeFacing(-900000)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 120000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('pt030_00', 7)
    physicsXImpulse(5300)
    sprite('pt030_01', 6)
    label(0)
    sprite('pt030_02', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 6)
    sprite('pt030_04', 6)
    sprite('pt030_05', 6)
    sprite('pt030_06', 6)
    sprite('pt030_07', 6)
    sprite('pt030_08', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 6)
    sprite('pt030_10', 6)
    sprite('pt030_11', 6)
    sprite('pt030_12', 6)
    sprite('pt030_13', 6)
    gotoLabel(0)
    label(1)
    sprite('pt033_00', 1)
    sprite('pt033_01', 2)
    physicsXImpulse(-18500)
    physicsYImpulse(12800)
    setGravity(1550)
    JumpSoundEffects()
    sprite('pt033_02', 3)
    uponSendToLabel(LANDING, 3)
    label(2)
    sprite('pt033_03', 3)
    sprite('pt033_02', 3)
    gotoLabel(2)
    label(3)
    clearUponHandler(LANDING)
    sprite('pt033_04', 2)
    sprite('pt033_05', 2)
    physicsXImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('pt033_06', 2)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventDefEntryReverseWait():
    sprite('pt000_00', 7)
    Flip()
    label(0)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    sprite('pt000_00', 7)
    loopRest()
    gotoLabel(0)


@State
def EventStandTurn():
    sprite('pt003_00', 3)
    Flip()
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)
    loopRest()
    enterState('CmnActStand')


@State
def EventUltimateLoop():

    def upon_IMMEDIATE():
        EndMomentum(1)
    sprite('pt431_00', 3)
    sprite('pt431_00', 3)
    sprite('pt431_01', 3)
    sprite('pt431_02', 3)
    sprite('pt431_03', 3)
    sprite('pt431_04', 3)
    sprite('pt431_05', 10)
    sprite('pt431_06', 3)
    CreateObject('pt431_tornado', -1)
    sprite('pt431_07', 3)
    sprite('pt431_08', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_09', 3)
    sprite('pt431_10', 3)
    sprite('pt431_11', 3)
    sprite('pt431_12', 3)
    sprite('pt431_13', 3)
    loopRest()
    sprite('pt431_09', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_10', 4)
    sprite('pt431_11', 3)
    sprite('pt431_12', 3)
    sprite('pt431_13', 3)
    CommonSE('005_swing_grap_2_0')
    sprite('pt431_14', 3)
    CreateObject('pt431_smoke', -1)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    CommonSE('005_swing_grap_2_0')
    label(0)
    sprite('pt431_14', 3)
    CreateObject('pt431_smoke', -1)
    sprite('pt431_15', 3)
    sprite('pt431_16', 3)
    CommonSE('005_swing_grap_2_0')
    loopRest()
    gotoLabel(0)


@State
def EventUltimateLoopToStop():
    sprite('pt431_17', 5)
    sprite('pt431_18', 5)
    sprite('pt431_19', 5)
    sprite('pt431_20', 5)
    sprite('pt431_21', 5)
    sprite('pt431_22', 5)
    loopRest()
    sprite('pt431_23', 6)
    sprite('pt431_24', 6)
    sprite('pt431_25', 6)
    sprite('pt431_26', 6)
    sprite('pt431_27', 32767)
    loopRest()


@State
def EventUltimateLoopEnd():
    sprite('pt431_28', 6)
    sprite('pt431_29', 6)
    sprite('pt431_30', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Evetn_Down():
    sprite('pt063_11', 32767)
    loopRest()


@State
def Act2Event_tmvspt_00():
    sprite('keep', 1)
    XPositionRelativeFacing(-360000)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_tmvspt_01():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 260000:
                    EndMomentum(1)
                    XPositionRelativeFacing(-260000)
                    sendToLabel(0)
                    clearUponHandler(EVERY_FRAME)
            elif SLOT_XDistanceFromCenterOfStage > -260000:
                EndMomentum(1)
                XPositionRelativeFacing(-260000)
                sendToLabel(0)
                clearUponHandler(EVERY_FRAME)
    sprite('pt030_00', 7)
    physicsXImpulse(1000)
    sprite('pt030_01_ex', 8)
    label(9)
    sprite('pt030_02_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)
    sprite('pt030_04_ex', 8)
    sprite('pt030_05_ex', 8)
    sprite('pt030_06_ex', 8)
    sprite('pt030_07_ex', 8)
    sprite('pt030_08_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 8)
    sprite('pt030_10_ex', 8)
    sprite('pt030_11_ex', 8)
    sprite('pt030_12_ex', 8)
    sprite('pt030_13_ex', 8)
    gotoLabel(9)
    label(0)
    sprite('keep', 2)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_tmvspt_02():
    sprite('pt063_11', 32767)
    XPositionRelativeFacing(-160000)
    loopRest()


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_WalkIn():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        XPositionRelativeFacing(-720000)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 260000:
                    clearUponHandler(EVERY_FRAME)
                    XPositionRelativeFacing(-260000)
                    EndMomentum(1)
                    sendToLabel(0)
            elif SLOT_XDistanceFromCenterOfStage > -260000:
                clearUponHandler(EVERY_FRAME)
                XPositionRelativeFacing(-260000)
                EndMomentum(1)
                sendToLabel(0)
    sprite('pt030_00', 5)
    physicsXImpulse(4650)
    sprite('pt030_01', 5)
    label(9)
    sprite('pt030_02', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03', 5)
    sprite('pt030_04', 5)
    sprite('pt030_05', 5)
    sprite('pt030_06', 5)
    sprite('pt030_07', 5)
    sprite('pt030_08', 5)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09', 5)
    sprite('pt030_10', 5)
    sprite('pt030_11', 5)
    sprite('pt030_12', 5)
    sprite('pt030_13', 5)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Muchorin():
    sprite('pt203_00', 4)
    sprite('pt203_01', 4)
    sprite('pt203_02', 4)
    sprite('pt203_02', 4)
    sprite('pt203_03', 4)
    CreateObject('pt203_stick', 0)
    sprite('pt203_04', 4)
    PrivateSE('ptse_13')
    sprite('pt203_05', 32767)
    loopRest()


@State
def Act2Event_MuchorinEnd():
    sprite('pt203_06', 4)
    sprite('pt203_07', 4)
    sprite('pt203_08', 4)
    sprite('pt203_09', 4)
    sprite('pt203_10', 4)
    sprite('pt203_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yoin():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
        XPositionRelativeFacing(-290000)
    sprite('pt201_05', 10)
    PrivateSE('ptse_16')
    sprite('pt201_06', 5)
    sprite('pt201_07', 5)
    sprite('pt201_08', 5)
    sprite('pt201_09', 4)
    LandingEffects(100, 1, 1)
    sprite('pt201_10', 5)
    sprite('pt201_11', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Chouhatsu():
    sprite('pt300_00', 4)
    sprite('pt300_01', 4)
    sprite('pt300_02', 4)
    sprite('pt300_03', 6)
    sprite('pt300_04', 6)
    sprite('pt300_05', 7)
    sprite('pt300_06', 30)
    sprite('pt300_07', 7)
    PrivateSE('ptse_00')
    sprite('pt300_08', 9)
    sprite('pt300_09', 6)
    sprite('pt000_00', 1)
    enterState('CmnActStand')


@State
def Act2Event_Magica():
    sprite('pt406_00', 5)
    sprite('pt406_01', 5)
    sprite('pt406_02', 5)
    label(0)
    sprite('pt406_03', 8)
    PrivateSE('ptse_00')
    sprite('pt406_04', 7)
    sprite('pt406_05', 7)
    sprite('pt406_06', 8)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_MagicaEnd():
    sprite('keep', 2)
    sprite('pt406_07', 5)
    sprite('pt406_08', 5)
    sprite('pt406_09', 5)
    sprite('pt406_10', 5)
    sprite('pt406_11', 5)
    sprite('pt406_12', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_RunOut():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        EnableCollision(0)
    sprite('pt032_00', 3)
    physicsXImpulse(24000)
    sprite('pt032_01', 3)
    SetActionMark(4)
    label(0)
    sprite('pt032_02', 4)
    AddActionMark(-1)
    sprite('pt032_03', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_04', 4)
    sprite('pt032_05', 4)
    sprite('pt032_06', 4)
    sprite('pt032_07', 4)
    DashEffects(100, 1, 1)
    sprite('pt032_08', 4)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('null', 32767)
    EndMomentum(1)
    Visibility(1)
    loopRest()


@State
def Act2Event_cevspt_00():
    sprite('pt203_00', 4)
    sprite('pt203_01', 4)
    sprite('pt203_02', 4)
    sprite('pt203_02', 4)
    sprite('pt203_03', 4)
    CreateObject('pt203_stick', 0)
    sprite('pt203_04', 4)
    PrivateSE('ptse_13')
    sprite('pt203_05', 32767)
    loopRest()


@State
def Act2Event_cevspt_01():
    sprite('pt203_06', 4)
    sprite('pt203_07', 4)
    sprite('pt203_08', 4)
    sprite('pt203_09', 4)
    sprite('pt203_10', 4)
    sprite('pt203_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_cevspt_02():
    sprite('pt030_00', 7)
    physicsXImpulse(1000)
    sprite('pt030_01_ex', 8)
    sprite('pt030_02_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)
    sprite('pt030_04_ex', 8)
    sprite('pt030_05_ex', 8)
    sprite('pt030_06_ex', 8)
    sprite('pt030_07_ex', 8)
    sprite('pt030_08_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 8)
    sprite('pt030_10_ex', 8)
    sprite('pt030_11_ex', 8)
    sprite('pt030_12_ex', 8)
    sprite('pt030_13_ex', 8)
    sprite('pt063_00', 3)
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    sprite('pt063_01', 3)
    sprite('pt063_02', 3)
    sprite('pt063_03', 3)
    sprite('pt063_04', 3)
    sprite('pt063_05', 3)
    sprite('pt063_06', 2)
    physicsXImpulse(0)
    physicsYImpulse(3000)
    EndYPhysicsImpulse()
    CommonSE('209_down_normal_0')
    sprite('pt063_07', 2)
    sprite('pt063_08', 3)
    sprite('pt063_09', 3)
    sprite('pt063_10', 3)
    sprite('pt063_11', 32767)
    loopRest()


@State
def Act2Event_ptvsmi_00():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        XPositionRelativeFacing(-920000)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    CameraControlEnable(0)
    CreateObject('Act2Event_Camera', -1)
    RegisterObject(11, 1)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_ptvsmi_01():
    sprite('keep', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 32)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ptvsmi_02():
    sprite('keep', 1)
    ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 41)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ptvsmi_03():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage < 260000:
                    EndMomentum(1)
                    XPositionRelativeFacing(-260000)
                    sendToLabel(0)
                    clearUponHandler(EVERY_FRAME)
            elif SLOT_XDistanceFromCenterOfStage > -260000:
                EndMomentum(1)
                XPositionRelativeFacing(-260000)
                sendToLabel(0)
                clearUponHandler(EVERY_FRAME)
    sprite('pt030_00', 7)
    physicsXImpulse(3000)
    sprite('pt030_01_ex', 6)
    label(9)
    sprite('pt030_02_ex', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 6)
    sprite('pt030_04_ex', 6)
    sprite('pt030_05_ex', 6)
    sprite('pt030_06_ex', 6)
    sprite('pt030_07_ex', 6)
    sprite('pt030_08_ex', 6)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 6)
    sprite('pt030_10_ex', 6)
    sprite('pt030_11_ex', 6)
    sprite('pt030_12_ex', 6)
    sprite('pt030_13_ex', 6)
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ptvsmi_04():
    sprite('pt041_00', 4)
    sprite('pt041_01', 4)
    label(0)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_ptvsmi_05():
    sprite('keep', 2)
    CreateObject('Act2Event_Fade', -1)
    CommonSE('022_magiccircle_c')
    ConstantAlphaModifier(-4)

    def RunOnObject_22():
        ConstantAlphaModifier(-4)
        ObjectUpon(OPPONENT_CHAR_HIT_OR_BLOCK, 39)
    label(0)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_ptvsaz_00():
    sprite('pt030_00', 7)
    physicsXImpulse(1000)
    sprite('pt030_01_ex', 8)
    sprite('pt030_02_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)
    sprite('pt030_04_ex', 8)
    sprite('pt030_05_ex', 8)
    sprite('pt030_06_ex', 8)
    sprite('pt030_07_ex', 8)
    sprite('pt030_08_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_09_ex', 8)
    sprite('pt030_10_ex', 8)
    sprite('pt030_11_ex', 8)
    sprite('pt030_12_ex', 8)
    sprite('pt030_13_ex', 8)
    sprite('pt030_02_ex', 8)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('pt030_03_ex', 8)
    sprite('pt030_04_ex', 8)
    sprite('pt030_05_ex', 8)
    sprite('pt063_00', 3)
    physicsXImpulse(2000)
    physicsYImpulse(12000)
    EndYPhysicsImpulse()
    sprite('pt063_01', 3)
    sprite('pt063_02', 3)
    sprite('pt063_03', 3)
    sprite('pt063_04', 3)
    sprite('pt063_05', 3)
    sprite('pt063_06', 2)
    physicsXImpulse(0)
    physicsYImpulse(3000)
    EndYPhysicsImpulse()
    CommonSE('209_down_normal_0')
    sprite('pt063_07', 2)
    sprite('pt063_08', 3)
    sprite('pt063_09', 3)
    sprite('pt063_10', 3)
    sprite('pt063_11', 32767)
    loopRest()


@State
def Act2Event_ptvsaz_01():
    sprite('pt064_00', 4)
    sprite('pt064_01', 4)
    sprite('pt064_02', 4)
    sprite('pt064_03', 4)
    sprite('pt064_04', 4)
    sprite('pt064_05', 4)
    sprite('pt064_06', 4)
    sprite('pt064_07', 4)
    sprite('pt064_08', 4)
    sprite('pt064_09', 4)
    sprite('pt064_10', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_ptvsaz_02():
    sprite('pt310_02', 4)
    sprite('pt310_06', 4)
    label(0)
    sprite('pt310_04', 4)
    sprite('pt310_05', 4)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_Guard():
    sprite('pt041_00', 4)
    sprite('pt041_01', 4)
    sprite('pt041_02', 4)
    sprite('pt041_03', 4)
    sprite('pt041_04', 15)
    sprite('pt041_03', 4)
    sprite('pt041_02', 4)
    sprite('pt041_01', 4)
    sprite('pt041_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_GuardStop():
    sprite('pt041_00', 4)
    sprite('pt041_01', 4)
    label(0)
    sprite('pt041_02', 4)
    sprite('pt041_03', 4)
    sprite('pt041_04', 4)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_GuardEnd():
    sprite('pt041_01', 4)
    sprite('pt041_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvsph_00():

    def upon_IMMEDIATE():
        SetActionMark(0)
        uponSendToLabel(33, 1)

        def upon_32():
            CreateObject('Act3Event_FadeWhite', -1)
            PrivateSE('ptse_12')
            AddActionMark(1)
    sprite('pt064_02', 3)
    sprite('pt064_03', 3)
    sprite('pt064_04', 3)
    sprite('pt064_05', 3)
    sprite('pt064_06', 3)
    sprite('pt064_07', 3)
    sprite('pt064_08', 3)
    sprite('pt064_09', 3)
    sprite('pt064_10', 3)
    sprite('pt000_00', 5)
    CreateObject('AstralAura02', -1)
    label(0)
    sprite('pt040_01', 5)
    CharacterFlash2(16777215, 30)
    if SLOT_2 == 0:
        CommonSE('022_magiccircle_d')
    sprite('pt040_02', 5)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    CharacterFlash2(0, 30)
    sprite('pt040_02', 5)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    sprite('pt040_00', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    clearUponHandler(EVERY_FRAME)
    TriggerUponForState('Act3Event_FadeWhite', 32)
    TriggerUponForState('AstralAura02', 32)
    Visibility(1)


@State
def Act3Event_ptvsph_01():
    sprite('pt001_00', 7)
    sprite('pt001_01', 5)
    sprite('pt001_02', 8)
    sprite('pt001_03', 8)
    sprite('pt001_04', 8)
    sprite('pt001_05', 8)
    sprite('pt001_06', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvstm_00():
    sprite('pt003_00', 3)
    Flip()
    CameraControlEnable(1)
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)
    loopRest()
    sprite('pt001_00', 7)
    sprite('pt001_01', 5)
    sprite('pt001_02', 8)
    sprite('pt001_03', 8)
    sprite('pt001_04', 8)
    sprite('pt001_05', 8)
    sprite('pt001_06', 5)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvstm_01_Loop():
    sprite('pt620_00', 5)
    CameraControlEnable(1)
    sprite('pt620_01', 5)
    sprite('pt620_02', 32767)


@State
def Act3Event_ptvstm_01_LoopEnd():
    sprite('pt620_01', 5)
    CameraControlEnable(1)
    sprite('pt620_00', 5)
    loopRest()
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvstm_02():
    sprite('pt003_00', 3)
    Flip()
    CameraControlEnable(0)
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)
    loopRest()
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvstm_03():
    label(0)
    sprite('pt010_02', 6)
    sprite('pt010_03', 6)
    sprite('pt010_04', 6)
    sprite('pt010_05', 6)
    sprite('pt010_06', 6)
    sprite('pt010_07', 6)
    sprite('pt010_08', 6)
    sprite('pt010_09', 6)
    sprite('pt010_10', 6)
    sprite('pt010_11', 6)
    sprite('pt010_12', 6)
    sprite('pt010_13', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvstm_04():
    sprite('pt010_01', 6)
    sprite('pt010_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvsrl_00():

    def upon_IMMEDIATE():
        SetActionMark(1)

        def upon_EVERY_FRAME():
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 >= 36:
                ConstantAlphaModifier(5)
            else:
                ConstantAlphaModifier(-5)
                if SLOT_2:
                    SetActionMark(0)
                    CommonSE('022_magiccircle_d')
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvsrl_01():
    sprite('pt620_00', 5)
    sprite('pt620_01', 5)
    sprite('pt620_02', 32767)


@State
def Act3Event_ptvsrl_02():
    sprite('pt620_01', 5)
    sprite('pt620_00', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvsrl_03():
    sprite('pt041_00', 3)
    sprite('pt041_01', 3)
    label(0)
    sprite('pt040_00', 5)
    sprite('pt040_01', 5)
    sprite('pt040_02', 5)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvsrl_04():
    sprite('pt064_00', 5)
    sprite('pt064_01', 5)
    sprite('pt064_02', 5)
    sprite('pt064_03', 32767)


@State
def Act3Event_ptvsrl_05():

    def upon_IMMEDIATE():
        SetActionMark(1)

        def upon_EVERY_FRAME():
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 >= 36:
                ConstantAlphaModifier(5)
                if SLOT_51 >= 84:
                    SLOT_51 = 0
                    SetActionMark(1)
            else:
                ConstantAlphaModifier(-5)
                if SLOT_2:
                    SetActionMark(0)
                    CommonSE('022_magiccircle_d')
    sprite('pt064_03', 32767)


@State
def Act3Event_ptvsrl_06():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 240)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    loopRest()
    enterState('EventChouhatsu')


@State
def Act3Event_ptvsjn_00():

    def upon_IMMEDIATE():
        SetActionMark(1)

        def upon_EVERY_FRAME():
            SLOT_51 = SLOT_51 + 1
            if SLOT_51 >= 36:
                ConstantAlphaModifier(5)
                if SLOT_51 >= 84:
                    SLOT_51 = 0
                    SetActionMark(1)
            else:
                ConstantAlphaModifier(-5)
                if SLOT_2:
                    SetActionMark(0)
                    CommonSE('022_magiccircle_d')
    sprite('pt070_13', 4)
    sprite('pt070_12', 4)
    sprite('pt070_11', 4)
    sprite('pt070_10', 32767)
    loopRest()


@State
def Act3Event_ptvsjn_01():
    sprite('pt070_11', 4)
    ConstantAlphaModifier(255)
    sprite('pt070_12', 4)
    sprite('pt070_13', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvsjn_02():
    sprite('pt620_00', 6)
    sprite('pt620_01', 6)
    sprite('pt620_02', 6)
    sprite('pt620_03', 6)
    CommonSE('019_cloth_b')
    sprite('pt620_04', 6)
    sprite('pt620_05', 6)
    sprite('pt620_06', 6)
    sprite('pt620_07', 6)
    label(0)
    sprite('pt620_08', 6)
    PrivateSE('ptse_05')
    sprite('pt620_09', 6)
    sprite('pt620_10', 6)
    sprite('pt620_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptvsjn_03():
    sprite('pt620_07', 4)
    sprite('pt620_06', 4)
    sprite('pt620_05', 4)
    sprite('pt620_03', 4)
    sprite('pt620_02', 4)
    sprite('pt620_01', 4)
    sprite('pt620_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_ptvsjn_04():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        XPositionRelativeFacing(-60000)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt070_00', 2)
    CallCustomizableParticle('ef_girdbreak', 103)
    CommonSE('104_guard_grap_1')
    CommonSE('106_guard_crush')
    ScreenShake(3000, 18000)
    SetInertia(-20000)
    sprite('pt070_01', 2)
    SetActionMark(6)
    label(2)
    sprite('pt070_02', 5)
    sprite('pt070_03', 5)
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2)
    sprite('pt070_04', 4)
    sprite('pt070_05', 4)
    sprite('pt070_06', 4)
    sprite('pt070_07', 6)
    sprite('pt070_08', 6)
    sprite('pt070_09', 5)
    sprite('pt063_11', 32767)
    KnockdownEffects(100, 1, 1)
    AddX(80000)


@State
def Act3Event_ptvsjn_05():
    sprite('pt064_00', 7)
    sprite('pt064_01', 7)
    sprite('pt064_02', 32767)


@State
def Act3Event_ptvsjn_06():
    sprite('pt064_03', 4)
    sprite('pt064_04', 4)
    sprite('pt064_05', 4)
    sprite('pt064_06', 4)
    sprite('pt064_07', 4)
    sprite('pt064_08', 4)
    sprite('pt064_09', 4)
    sprite('pt064_10', 4)
    sprite('pt000_00', 1)
    enterState('Act3Event_ptvsph_01')


@State
def Act3Event_ptvsjn_07():
    sprite('pt430_00', 3)
    sprite('pt430_01', 3)
    sprite('pt430_02', 3)
    CommonSE('008_swing_pole_2')
    sprite('pt430_03', 3)
    sprite('pt430_04', 3)
    sprite('pt430_05', 3)
    sprite('pt430_06', 3)
    sprite('pt430_07', 3)
    CreateObject('pt430_mahojin', 0)
    CreateObject('pt203_mahojinsub', 0)
    CreateObject('pt430_circle1', 1)
    CreateObject('pt430_circle2', 1)
    sprite('pt430_08', 3)
    sprite('pt430_09', 3)
    sprite('pt430_10', 3)
    sprite('pt430_11', 3)
    CreateObject('ptef_430power', 0)
    CommonSE('022_magiccircle_b')
    sprite('pt430_12', 3)
    sprite('pt203_02', 32767)
    CreateObject('pt430_mahojinsub', 0)
    CreateObject('pt430_aura1', 0)
    CreateObject('pt430_aura2', 0)
    CreateObject('pt430_aura3', 0)


@State
def Act3Event_mavspt_00():

    def upon_IMMEDIATE():
        Flip()
        CameraControlEnable(1)

        def upon_32():
            CameraControlEnable(0)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_01():
    sprite('pt003_00', 4)
    Flip()
    CameraControlEnable(0)
    sprite('pt003_01', 4)
    sprite('pt003_02', 4)
    loopRest()
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-200000)
    sprite('pt070_00', 3)
    sprite('pt070_01', 3)
    label(0)
    sprite('pt070_02', 4)
    sprite('pt070_03', 4)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_03():
    sprite('pt070_10', 5)
    sprite('pt070_11', 5)
    sprite('pt070_12', 5)
    sprite('pt070_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavspt_04():
    sprite('pt620_00', 6)
    sprite('pt620_01', 6)
    sprite('pt620_02', 6)
    sprite('pt620_03', 6)
    CommonSE('019_cloth_b')
    sprite('pt620_04', 6)
    sprite('pt620_05', 32767)
    loopRest()


@State
def Act3Event_mavspt_05():
    sprite('pt620_06', 6)
    sprite('pt620_07', 6)
    label(0)
    sprite('pt620_08', 6)
    sprite('pt620_09', 6)
    sprite('pt620_10', 6)
    sprite('pt620_09', 6)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mavspt_06():
    sprite('keep', 2)
    sprite('pt620_11', 6)
    sprite('pt620_12', 32767)
    loopRest()


@State
def Act3Event_mavspt_07():
    sprite('pt620_11', 6)
    label(0)
    sprite('pt620_08', 6)
    sprite('pt620_09', 6)
    sprite('pt620_10', 6)
    sprite('pt620_09', 6)
    loopRest()
    gotoLabel(0)
    loopRest()


@State
def Act3Event_mavspt_08():
    sprite('pt064_03', 4)
    sprite('pt064_04', 4)
    sprite('pt064_05', 4)
    sprite('pt064_06', 4)
    sprite('pt064_07', 4)
    sprite('pt064_08', 4)
    sprite('pt064_09', 4)
    sprite('pt064_10', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mavspt_09():
    sprite('pt033_00', 3)
    sprite('pt033_01', 3)
    physicsXImpulse(-10000)
    physicsYImpulse(5000)
    setGravity(1550)
    uponSendToLabel(LANDING, 1)
    sprite('pt033_02', 3)
    sprite('pt033_03', 3)
    loopRest()
    label(0)
    sprite('pt033_02', 3)
    sprite('pt033_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt033_04', 4)
    EndMomentum(1)
    sprite('pt033_05', 4)
    LandingEffects(100, 1, 1)
    sprite('pt033_06', 4)
    loopRest()
    enterState('CmnActStand')
