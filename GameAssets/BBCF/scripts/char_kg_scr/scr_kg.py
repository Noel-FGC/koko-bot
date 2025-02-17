@Subroutine
def PreInit():
    CharacterID('kg')
    EnableDashBuffer(1)


@Subroutine
def InitializeStandByLand():
    DeleteObject(5)
    PreventBlocking(1)
    AttackOff()
    RunLoopUpon(17, 60)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    if SLOT_OverdriveTimer:
        SLOT_60 = 1
        SLOT_61 = 1
        SLOT_62 = 1
    WhiffCancel('UltimateStandByLand')
    WhiffCancel('UltimateStandByLandOD')


@Subroutine
def InitializeStandByStart():
    AddActionMark(0)
    SLOT_60 = 1
    SLOT_61 = 1
    SLOT_62 = 1


@Subroutine
def InitializeStandByFlexChange():
    AddActionMark(0)
    if SLOT_60:
        WhiffCancel('Change_NmlAtk5D')
        WhiffCancel('Change_NmlAtk4D')
        WhiffCancel('Change_NmlAtkAIR5D')
    if SLOT_61:
        WhiffCancel('Change_NmlAtk2D')
        WhiffCancel('Change_NmlAtkAIR2D')
    if SLOT_62:
        WhiffCancel('Change_NmlAtk6D')
        WhiffCancel('Change_NmlAtkAIR6D')


@Subroutine
def InitializeStandByChange():
    AddActionMark(0)

    def upon_OPPONENT_HIT_OR_BLOCK():
        if SLOT_51:
            SpecialCancelOnHit(1)
            if SLOT_60:
                HitOrBlockCancel('Change_NmlAtk5D')
                HitOrBlockCancel('Change_NmlAtk4D')
            if SLOT_61:
                HitOrBlockCancel('Change_NmlAtk2D')
            if SLOT_62:
                HitOrBlockCancel('Change_NmlAtk6D')
            if SLOT_55:
                SpecialCancel(1)
                HitOrBlockCancel('StandByFDash')
                HitOrBlockCancel('StandByBDash')


@Subroutine
def InitializeStandByChangeNoCheck():
    if SLOT_51:
        if SLOT_60:
            HitOrBlockCancel('Change_NmlAtk5D')
            HitOrBlockCancel('Change_NmlAtk4D')
        if SLOT_61:
            HitOrBlockCancel('Change_NmlAtk2D')
        if SLOT_62:
            HitOrBlockCancel('Change_NmlAtk6D')
        if SLOT_55:
            SpecialCancel(1)
            HitOrBlockCancel('StandByFDash')
            HitOrBlockCancel('StandByBDash')


@Subroutine
def InitializeStandByChangeAir():
    AddActionMark(0)

    def upon_OPPONENT_HIT_OR_BLOCK():
        if SLOT_51:
            SpecialCancelOnHit(1)
            if SLOT_60:
                HitOrBlockCancel('Change_NmlAtk5D')
                HitOrBlockCancel('Change_NmlAtk4D')
                HitOrBlockCancel('Change_NmlAtkAIR5D')
                HitOrBlockCancel('Change_NmlAtkAIR4D')
            if SLOT_61:
                HitOrBlockCancel('Change_NmlAtk2D')
                HitOrBlockCancel('Change_NmlAtkAIR2D')
            if SLOT_62:
                HitOrBlockCancel('Change_NmlAtk6D')
                HitOrBlockCancel('Change_NmlAtkAIR6D')
            if SLOT_55:
                if not SLOT_52:
                    SLOT_60 = 1
                if not SLOT_53:
                    SLOT_61 = 1
                if not SLOT_54:
                    SLOT_62 = 1
                SpecialCancel(1)
                HitOrBlockCancel('StandByFDash')
                HitOrBlockCancel('StandByBDash')


@Subroutine
def InitializeStandByAir():
    AttackDefaults_AirNormal()
    DeleteObject(5)
    PreventBlocking(1)
    AttackOff()
    PushSpeedX()
    PushSpeedY()
    RunLoopUpon(17, 60)

    def upon_17():
        clearUponHandler(17)
        clearUponHandler(EVERY_FRAME)
        sendToLabel(1)
    SetActionMark(0)

    def upon_EVERY_FRAME():
        if SLOT_94:
            SetActionMark(0)
            if CurrentStateCheck('Change_NmlAtkAIR5D'):
                SetActionMark(1)
            if CurrentStateCheck('Change_NmlAtkAIR2D'):
                SetActionMark(1)
            if CurrentStateCheck('Change_NmlAtkAIR6D'):
                SetActionMark(1)
            if SLOT_StateDuration >= 8:
                SetActionMark(1)
        if SLOT_2:
            if CheckInput(INPUT_HOLD_A):
                clearUponHandler(17)
                clearUponHandler(EVERY_FRAME)
                SLOT_59 = 1
                SLOT_51 = 1
            if CheckInput(INPUT_HOLD_B):
                clearUponHandler(17)
                clearUponHandler(EVERY_FRAME)
                SLOT_59 = 2
                SLOT_51 = 1
            if CheckInput(INPUT_HOLD_C):
                clearUponHandler(17)
                clearUponHandler(EVERY_FRAME)
                SLOT_59 = 3
                SLOT_51 = 1
            if SLOT_113:
                clearUponHandler(17)
                clearUponHandler(EVERY_FRAME)
                Unknown61(0, 1, 0, 3, 0, 0, 0, 9999, 0, 9999, 0, 9999)
                SLOT_59 = SLOT_0
                SLOT_51 = 1
        if SLOT_51:
            sendToLabel(2)
    WhiffCancel('UltimateStandByAir')
    WhiffCancel('UltimateStandByAirOD')


@Subroutine
def DeleteStandByEffect():
    AddActionMark(0)
    DeleteObject(5)


@Subroutine
def InitializeStandByChainAttack():
    AddActionMark(0)
    HitsparkSize(750)
    SLOT_4 = 1
    ForceFaceSprite()
    if SLOT_OverdriveTimer:
        SLOT_55 = 1


@Subroutine
def InitializeCAttackChainAttack():
    UseSlashHitspark(1)
    Hitstop(15)
    AddActionMark(0)
    if SLOT_OverdriveTimer:
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('StandByFDash')
        HitOrBlockCancel('StandByBDash')
    else:
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')


@Subroutine
def DiveDirectionSet():
    CommonSE('000_airdash_2')
    SetXCollisionFromOrigin(50)
    physicsYImpulse(-50000)
    if CheckInput(0x78):
        physicsXImpulse(50000)
        sendToLabel(1)
    if CheckInput(0x51):
        physicsXImpulse(20000)
        sendToLabel(1)
    if CheckInput(0x9f):
        physicsXImpulse(20000)
        sendToLabel(1)
    if CheckInput(0x44):
        pass
    if CheckInput(0x37):
        physicsXImpulse(-20000)
        sendToLabel(2)
    if CheckInput(0x85):
        physicsXImpulse(-20000)
        sendToLabel(2)
    if CheckInput(0x5e):
        physicsXImpulse(-20000)
        sendToLabel(2)
    if SLOT_113:
        physicsXImpulse(50000)
        sendToLabel(1)


@Subroutine
def MatchInit():
    Health(11500)
    WalkFSpeed(4500)
    WalkBSpeed(3500)
    DashFInitialVelocity(12000)
    DashFAccel(250)
    DashFMaxVelocity(25000)
    JumpYVelocity(34000)
    SuperJumpYVelocity(40000)
    AirDashFSpeed(25000)
    AirDashBSpeed(20000)
    AirFDashDuration(23)
    HeatGainFactor(20)
    ComboRate(60)
    NegativePenaltyResistance(5)
    Unknown12054(3, 2)
    OverdriveDuration(240, 270, 300, 330, 360, 390, 420, 480, 480, 480)
    FootstepType(2)
    FootstepSE(0)
    CreateDecalOn(1)
    CPUJumpPriority(100)
    Move_Register('NmlAtkExcite', 0x602)
    Move_EndRegister()
    Move_Register('NmlAtk5A', INPUT_5A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6A', INPUT_6A)
    MoveMid()
    AirborneOpponentPriority(1)
    GuardStunPriority(3000)
    SkillEstimateRange(0, 320000, -200000, 250000, 400, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', INPUT_2A)
    MoveMaxChainRepeat(3)
    SkillEstimateRange(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', INPUT_5B)
    MoveMaxChainRepeat(2)
    MoveLow()
    DamageStunPriority(1500)
    SkillEstimateRange(0, 300000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6B', INPUT_6B)
    SkillEstimateRange(0, 400000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('Atk6B_Input5', 0x1)
    StateCall('NmlAtk6B')
    FollowupOnly(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Condition(0x2000)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', INPUT_2B)
    SharedGatling('NmlAtk5B')
    MoveLow()
    SkillEstimateRange(0, 300000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5C', INPUT_5C)
    AirborneOpponentPriority(2000)
    GuardStunPriority(2000)
    SkillEstimateRange(200000, 750000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('NmlAtk6C', INPUT_6C)
    AirborneOpponentPriority(6000)
    DamageStunPriority(0)
    MoveCancellableFrames(100, 100)
    SkillEstimateRange(300000, 700000, 250000, 500000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2C', INPUT_2C)
    AirborneOpponentPriority(1)
    SkillEstimateRange(200000, 750000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk3C', INPUT_3C)
    MoveLow()
    AirborneOpponentPriority(1)
    GuardStunPriority(500)
    SkillEstimateRange(100000, 500000, -200000, 200000, 400, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5D', INPUT_5D)
    OpponentAttackPriority(1)
    GuardStunPriority(1500)
    DamageStunPriority(1500)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 300000, 250, 10)
    Move_EndRegister()
    Move_Register('Change_NmlAtk5D', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    AirborneOpponentPriority(2000)
    SkillEstimateRange(0, 450000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('Change_NmlAtk4D', 0x1)
    StateCall('Change_NmlAtk5D')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtk6D', INPUT_6D)
    OpponentAttackPriority(1)
    DamageStunPriority(1500)
    Unknown15027(2000)
    SkillEstimateRange(0, 600000, -200000, 300000, 400, 10)
    Move_EndRegister()
    Move_Register('Change_NmlAtk6D', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(600000, 1000000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2D', INPUT_2D)
    OpponentAttackPriority(1)
    GuardStunPriority(1500)
    DamageStunPriority(1500)
    SkillEstimateRange(0, 450000, -200000, 300000, 400, 10)
    Move_EndRegister()
    Move_Register('Change_NmlAtk2D', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_D)
    OpponentAttackPriority(1)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 450000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', INPUT_J5A)
    SkillEstimateRange(0, 300000, -100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', INPUT_J5B)
    SkillEstimateRange(-250000, 250000, -300000, 0, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', INPUT_J5C)
    DamageStunPriority(4000)
    SkillEstimateRange(0, 500000, -600000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5D', INPUT_J5D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Change_NmlAtkAIR5D', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x6b)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 450000, -350000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('Change_NmlAtkAIR4D', 0x1)
    StateCall('Change_NmlAtkAIR5D')
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR6D', INPUT_J6D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Change_NmlAtkAIR6D', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 450000, -350000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2D', INPUT_J2D)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('Change_NmlAtkAIR2D', 0x1)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_D)
    SkillEstimateRange(0, 450000, -350000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkDeadAngle', 0x603)
    Move_EndRegister()
    Move_Register('NmlAtkGuardCrush', 0x605)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(4000)
    SkillEstimateRange(0, 250000, -200000, 200000, 250, 0)
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
    SkillEstimateRange(0, 250000, 0, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('StandByFDash', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_66)
    Move_EndRegister()
    Move_Register('StandByBDash', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_44)
    Move_EndRegister()
    Move_Register('StandBy5DD', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckUsed5D')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(10)
    Move_EndRegister()
    Move_Register('StandBy5DA', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy5DB', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_B)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy5DC', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_C)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy2DD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(10)
    Move_EndRegister()
    Move_Register('StandBy2DA', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy2DB', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_B)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy2DC', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_C)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy6DD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    MovePriority(10)
    Move_EndRegister()
    Move_Register('StandBy6DA', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_A)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy6DB', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_B)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandBy6DC', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_HOLD_C)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('StandByAIR5DD', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckUsed5D')
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    Move_EndRegister()
    Move_Register('StandByAIR2DD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    Move_EndRegister()
    Move_Register('StandByAIR6DD', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_D)
    Move_EndRegister()
    Move_Register('StandBy5DA_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy5DA')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    PlayerUsable(0)
    AirborneOpponentPriority(1)
    OpponentAttackPriority(5000)
    GuardStunPriority(2000)
    SkillEstimateRange(0, 650000, -200000, 300000, 10000, 50)
    Move_EndRegister()
    Move_Register('StandBy5DB_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy5DB')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_B)
    PlayerUsable(0)
    AirborneOpponentPriority(1)
    DamageStunPriority(1)
    GuardStunPriority(5000)
    SkillEstimateRange(-100000, 200000, -200000, 300000, 20000, 0)
    Move_EndRegister()
    Move_Register('StandBy5DC_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy5DC')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_C)
    PlayerUsable(0)
    DamageStunPriority(2000)
    AirborneOpponentPriority(5000)
    SkillEstimateRange(0, 400000, 150000, 450000, 20000, 50)
    Move_EndRegister()
    Move_Register('StandBy2DA_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy2DA')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    PlayerUsable(0)
    MoveMid()
    SkillEstimateRange(0, 500000, -200000, 300000, 20000, 50)
    Move_EndRegister()
    Move_Register('StandBy2DB_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy2DB')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_B)
    PlayerUsable(0)
    MoveLow()
    DamageStunPriority(2500)
    SkillEstimateRange(250000, 1300000, -200000, 400000, 20000, 50)
    Move_EndRegister()
    Move_Register('StandBy2DC_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy2DC')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_C)
    PlayerUsable(0)
    AirborneOpponentPriority(4000)
    SkillEstimateRange(0, 400000, -200000, 450000, 10000, 50)
    Move_EndRegister()
    Move_Register('StandBy6DA_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy6DA')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_A)
    PlayerUsable(0)
    MoveCancellableFrames(100, 100)
    SkillEstimateRange(0, 850000, -200000, 300000, 10000, 50)
    Move_EndRegister()
    Move_Register('StandBy6DB_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy6DB')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_B)
    PlayerUsable(0)
    GuardStunPriority(1500)
    SkillEstimateRange(0, 850000, -200000, 300000, 10000, 50)
    Move_EndRegister()
    Move_Register('StandBy6DC_CPU', INPUT_SPECIALMOVE)
    StateCall('StandBy6DC')
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Input_(INPUT_PRESS_C)
    PlayerUsable(0)
    DamageStunPriority(5000)
    SkillEstimateRange(0, 1200000, -200000, 600000, 10000, 50)
    Move_EndRegister()
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckShotAvailable')
    Move_Condition(0x2000)
    Move_Input_(INPUT_4HOLDLONG6)
    Move_Input_(INPUT_PRESS_A)
    DamageStunPriority(1)
    GuardStunPriority(1500)
    OpponentAttackPriority(1)
    JumpAvoidPriority(10000)
    SkillEstimateRange(200000, 800000, -100000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckShotAvailable')
    Move_Condition(0x2000)
    Move_Input_(INPUT_4HOLDLONG6)
    Move_Input_(INPUT_PRESS_B)
    OpponentAttackPriority(1)
    DamageStunPriority(1)
    Unknown15027(0)
    JumpAvoidPriority(10000)
    SkillEstimateRange(400000, 800000, -100000, 200000, 10, 400)
    Move_EndRegister()
    Move_Register('ShotC', INPUT_SPECIALMOVE)
    CallSkillConditions('CheckShotAvailable')
    Move_Condition(0x2000)
    Move_Input_(INPUT_4HOLDLONG6)
    Move_Input_(INPUT_PRESS_C)
    Unknown15027(0)
    JumpAvoidPriority(10000)
    SkillEstimateRange(400000, 800000, -100000, 200000, 100, 400)
    PlayerUsable(0)
    CPUUsable(0)
    Move_EndRegister()
    Move_Register('AntiAirB', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_4HOLDLONG8)
    Move_Input_(INPUT_PRESS_B)
    AirborneOpponentPriority(4000)
    GuardStunPriority(1)
    DamageStunPriority(1)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-350000, 400000, 100000, 500000, 500, 5)
    Move_EndRegister()
    Move_Register('AntiAirC', INPUT_SPECIALMOVE)
    Move_Condition(0x2000)
    Move_Input_(INPUT_4HOLDLONG8)
    Move_Input_(INPUT_PRESS_C)
    OpponentAttackPriority(3000)
    GuardStunPriority(1)
    DamageStunPriority(1)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-50000, 300000, -200000, 500000, 500, 5)
    Move_EndRegister()
    Move_Register('AirAssault', INPUT_SPECIALMOVE)
    Move_Condition(0x2001)
    Move_Input_(INPUT_8HOLD2)
    Move_Input_(INPUT_PRESS_C)
    MoveMid()
    GuardStunPriority(3000)
    SkillEstimateRange(-50000, 400000, -400000, 200000, 500, 5)
    Move_EndRegister()
    Move_Register('AirAssaultChain', INPUT_SPECIALMOVE)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Input_(INPUT_82)
    Move_Input_(INPUT_PRESS_C)
    SkillEstimateRange(-50000, 400000, -250000, 250000, 3000, 5)
    Move_EndRegister()
    Move_Register('UltimateShot', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_4HOLD1236)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(2000)
    SkillEstimateRange(250000, 600000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShotOD', INPUT_DISTORTION)
    Move_Condition(0x3081)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_4HOLD1236)
    Move_Input_(INPUT_PRESS_C)
    DamageStunPriority(2000)
    SkillEstimateRange(250000, 600000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateStandByLand', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_28)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    SkillEstimateRange(0, 400000, -200000, 500000, 400, 0)
    Move_EndRegister()
    Move_Register('UltimateStandByAir', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_28)
    Move_Input_(INPUT_PRESS_D)
    DamageStunPriority(5000)
    SkillEstimateRange(0, 400000, -400000, 300000, 400, 0)
    Move_EndRegister()
    Move_Register('UltimateStandByLandOD', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Condition(0x3081)
    Move_Condition(0x2000)
    Move_Condition(0x2002)
    Move_Input_(INPUT_28)
    Move_Input_(INPUT_PRESS_D)
    Move_EndRegister()
    Move_Register('UltimateStandByAirOD', INPUT_DISTORTION)
    FollowupOnly(1)
    Move_Condition(0x3081)
    Move_Condition(0x2001)
    Move_Condition(0x2002)
    Move_Input_(INPUT_28)
    Move_Input_(INPUT_PRESS_D)
    Move_EndRegister()
    Move_Register('UltimateAntiAir', INPUT_DISTORTION)
    Move_Condition(0x2000)
    Move_Input_(INPUT_2HOLD8)
    Move_Input_(INPUT_PRESS_D)
    PlayerUsable(0)
    CPUUsable(0)
    GuardStunPriority(1)
    OpponentAttackPriority(4000)
    DamageStunPriority(100)
    MoveCPULevel(500, 1000, 10, 1000)
    SkillEstimateRange(-50000, 500000, -100000, 500000, 500, 10)
    Move_EndRegister()
    Move_Register('AstralHeat', INPUT_ASTRAL)
    Move_Condition(0x304a)
    Move_Condition(0x2000)
    Move_Input_(INPUT_236236)
    Move_Input_(INPUT_PRESS_C)
    MoveComboPriority(0)
    OpponentAttackPriority(2000)
    SkillEstimateRange(0, 350000, -200000, 200000, 500, 0)
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
    SkillEstimateRange(0, 450000, -200000, 300000, 500, 10)
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
    SkillEstimateRange(0, 450000, -200000, 300000, 500, 10)
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
    SkillEstimateRange(0, 450000, -200000, 300000, 500, 10)
    Move_EndRegister()
    TempPriorityMultiplier('NmlAtk5B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk6B', 10000000)
    TempPriorityMultiplier('NmlAtk2B', 'NmlAtk3C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk5C', 10000000)
    TempPriorityMultiplier('NmlAtk6B', 'NmlAtk2C', 10000000)
    TempPriorityMultiplier('NmlAtk5C', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtk2C', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk2D', 10000000)
    TempPriorityMultiplier('NmlAtk3C', 'NmlAtk6D', 10000000)
    TempPriorityMultiplier('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    TempPriorityMultiplier('StandBy5DA_CPU', 'StandByFDash', 10000000)
    TempPriorityMultiplier('StandBy5DC_CPU', 'AntiAirC', 10000000)
    TempPriorityMultiplier('StandBy6DA_CPU', 'Change_NmlAtk5D', 10000000)
    TempPriorityMultiplier('StandBy6DB_CPU', 'Change_NmlAtk2D', 10000000)
    TempPriorityMultiplier('StandBy6DC_CPU', 'Change_NmlAtk2D', 10000000)
    TempPriorityMultiplier('StandBy2DA_CPU', 'Change_NmlAtkAIR6D', 10000000)
    TempPriorityMultiplier('StandBy2DB_CPU', 'ShotA', 10000000)
    TempPriorityMultiplier('StandBy2DB_CPU', 'ShotB', 10000000)
    TempPriorityMultiplier('StandBy2DB_CPU', 'UltimateShot', 10000000)
    TempPriorityMultiplier('StandBy2DB_CPU', 'UltimateShotOD', 10000000)
    TempPriorityMultiplier('StandBy2DC_CPU', 'ShotA', 10000000)
    TempPriorityMultiplier('StandBy2DC_CPU', 'ShotB', 10000000)
    TempPriorityMultiplier('StandBy2DC_CPU', 'AntiAirC', 10000000)
    StylishModeSpecialButton('AntiAirB', 0x4, 0xea)
    StylishModeSpecialButton('ShotA', 0x4, 0x79)
    StylishModeSpecialButton('UltimateShot', 0x4, 0x5f)
    StylishModeSpecialButton('UltimateShotOD', 0x4, 0x5f)
    StylishModeSpecialButton('ShotB', 0x4, 0x45)
    StylishModeSpecialButton('AirAssault', 0x4, 0xea)
    StylishModeSpecialButton('AirAssaultChain', 0x4, 0xea)
    StylishModeSpecialButton('UltimateStandByLand', 0x4, 0xea)
    StylishModeSpecialButton('UltimateStandByLandOD', 0x4, 0xea)
    StylishModeSpecialButton('UltimateStandByAir', 0x4, 0xea)
    StylishModeSpecialButton('UltimateStandByAirOD', 0x4, 0xea)
    StylishModeCancels('NmlAtk5A', 'NmlAtk5B', 0, 0)
    StylishModeCancels('NmlAtk5A', 'NmlAtk6B', 12, 0)
    StylishModeCancels('NmlAtk5B', 'NmlAtk6B', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2D', 0, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6D', 1, 250000)
    StylishModeCancels('NmlAtk5C', 'NmlAtk2D', 8, 0)
    StylishModeCancels('NmlAtk5C', 'NmlAtk6D', 12, 0)
    StylishModeCancels('NmlAtk5C', 'ShotA', 13, 0)
    StylishModeCancels('NmlAtk6A', 'AntiAirB', 6, 0)
    StylishModeCancels('NmlAtk6A', 'UltimateShot', 6, 0)
    StylishModeCancels('NmlAtk6A', 'UltimateShotOD', 6, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk2C', 0, 0)
    StylishModeCancels('NmlAtk6B', 'FJump', 12, 0)
    StylishModeCancels('NmlAtk6B', 'NmlAtk5C', 8, 0)
    StylishModeCancels('NmlAtk6C', 'ShotB', 0, 0)
    StylishModeCancels('NmlAtk6C', 'AntiAirC', 1, 250000)
    StylishModeCancels('NmlAtk6C', 'ShotA', 13, 0)
    StylishModeCancels('NmlAtk2A', 'NmlAtk6B', 0, 0)
    StylishModeCancels('NmlAtk2B', 'NmlAtk6B', 0, 0)
    StylishModeCancels('NmlAtk2C', 'NmlAtk2D', 0, 0)
    StylishModeCancels('NmlAtk2C', 'AstralHeat', 10, 400000)
    StylishModeCancels('NmlAtk2C', 'ShotA', 13, 0)
    StylishModeCancels('NmlAtk3C', 'ShotB', 0, 0)
    StylishModeCancels('NmlAtk3C', 'AntiAirC', 1, 250000)
    StylishModeCancels('NmlAtk3C', 'ShotA', 13, 0)
    StylishModeCancels('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    StylishModeCancels('NmlAtkAIR5B', 'AirAssault', 3, 0)
    StylishModeCancels('NmlAtkAIR5B', 'NmlAtkAIR5C', 13, 0)
    StylishModeCancels('NmlAtk5D', 'StandBy5DC', 3, 0)
    StylishModeCancels('NmlAtk5D', 'StandBy5DA', 6, 0)
    StylishModeCancels('NmlAtk5D', 'StandBy5DA', 10, 500000)
    StylishModeCancels('Change_NmlAtk5D', 'StandBy5DA', 6, 0)
    StylishModeCancels('Change_NmlAtk5D', 'UltimateStandByLand', 6, 0)
    StylishModeCancels('Change_NmlAtk5D', 'UltimateStandByLandOD', 6, 0)
    StylishModeCancels('Change_NmlAtk5D', 'StandBy5DA', 10, 600000)
    StylishModeCancels('Change_NmlAtk5D', 'StandBy5DA', 13, 0)
    StylishModeCancels('NmlAtk6D', 'StandBy6DC', 6, 0)
    StylishModeCancels('NmlAtk6D', 'StandBy6DC', 12, 0)
    StylishModeCancels('Change_NmlAtk6D', 'StandBy6DC', 6, 0)
    StylishModeCancels('Change_NmlAtk6D', 'UltimateStandByLand', 10, 600000)
    StylishModeCancels('Change_NmlAtk6D', 'UltimateStandByLandOD', 10, 600000)
    StylishModeCancels('NmlAtk2D', 'StandBy2DB', 6, 0)
    StylishModeCancels('NmlAtk2D', 'StandBy2DC', 8, 0)
    StylishModeCancels('NmlAtk2D', 'StandBy2DC', 10, 500000)
    StylishModeCancels('Change_NmlAtk2D', 'StandBy2DB', 6, 0)
    StylishModeCancels('Change_NmlAtk2D', 'StandBy2DA', 10, 500000)
    StylishModeCancels('Change_NmlAtk2D', 'StandBy2DB', 13, 0)
    StylishModeCancels('NmlAtkAIR5D', 'UltimateStandByAir', 6, 0)
    StylishModeCancels('NmlAtkAIR5D', 'UltimateStandByAirOD', 7, 0)
    StylishModeCancels('NmlAtkAIR2D', 'UltimateStandByAir', 6, 0)
    StylishModeCancels('NmlAtkAIR2D', 'UltimateStandByAirOD', 7, 0)
    StylishModeCancels('NmlAtkAIR6D', 'UltimateStandByAir', 6, 0)
    StylishModeCancels('NmlAtkAIR6D', 'UltimateStandByAirOD', 7, 0)
    StylishModeCancels('StandBy5DA', 'Change_NmlAtk6D', 0, 0)
    StylishModeCancels('StandBy5DA', 'AntiAirC', 10, 500000)
    StylishModeCancels('StandBy5DA', 'StandByBDash', 13, 0)
    StylishModeCancels('StandBy5DBExe', 'Change_NmlAtkAIR2D', 0, 0)
    StylishModeCancels('StandBy5DC', 'AntiAirB', 0, 0)
    StylishModeCancels('StandBy5DC', 'Change_NmlAtk2D', 13, 0)
    StylishModeCancels('StandBy2DA', 'Change_NmlAtkAIR6D', 0, 0)
    StylishModeCancels('StandBy2DA', 'AirAssault', 1, 250000)
    StylishModeCancels('StandBy2DA', 'Change_NmlAtkAIR6D', 10, 500000)
    StylishModeCancels('StandBy2DB', 'ShotB', 0, 0)
    StylishModeCancels('StandBy2DB', 'UltimateShot', 3, 20000)
    StylishModeCancels('StandBy2DB', 'UltimateShotOD', 3, 20000)
    StylishModeCancels('StandBy2DB', 'Change_NmlAtk5D', 13, 0)
    StylishModeCancels('StandBy2DC', 'Change_NmlAtk6D', 0, 0)
    StylishModeCancels('StandBy2DC', 'Change_NmlAtk5D', 1, 250000)
    StylishModeCancels('StandBy2DC', 'Change_NmlAtk6D', 10, 500000)
    StylishModeCancels('StandBy2DC', 'Change_NmlAtk6D', 3, 0)
    StylishModeCancels('StandBy6DA', 'Change_NmlAtk2D', 0, 0)
    StylishModeCancels('StandBy6DA', 'Change_NmlAtk5D', 13, 0)
    StylishModeCancels('StandBy6DB', 'Change_NmlAtk2D', 0, 0)
    StylishModeCancels('StandBy6DC', 'Change_NmlAtk2D', 6, 0)
    StylishModeCancels('StandBy6DC', 'Change_NmlAtk5D', 10, 500000)
    StylishModeCancels('StandBy6DC', 'Change_NmlAtk5D', 13, 0)
    StylishModeCancels('AntiAirB', 'AirAssaultChain', 0, 0)
    StylishModeCancels('AntiAirC', 'AirAssaultChain', 0, 0)
    StylishModeCancels('ThrowExe', 'ShotA', 0, 0)
    StylishModeCancels('BackThrowExe', 'ShotA', 0, 0)
    StylishModeCancels('AirThrowExe', 'AntiAirC', 0, 0)
    HitSprites(0, 'kg062_01')
    HitSprites(1, 'kg062_03')
    HitSprites(2, 'kg062_04')
    HitSprites(3, 'kg062_05')
    HitSprites(4, 'kg062_05')
    HitSprites(5, 'kg062_06')
    HitSprites(6, 'kg062_07')
    HitSprites(7, 'kg041_02')
    HitSprites(8, 'kg040_02')
    HitSprites(9, 'kg045_02')
    HitSprites(10, 'kg060_00')
    HitSprites(11, 'kg060_01')
    HitSprites(12, 'kg060_03')
    HitSprites(13, 'kg060_05')
    HitSprites(14, 'kg060_07')
    HitSprites(15, 'kg060_14')
    HitSprites(16, 'kg050_00')
    HitSprites(17, 'kg052_00')
    HitSprites(18, 'kg054_00')
    HitSprites(19, 'kg000_00')
    HitSprites(20, 'kg000_00')
    HitSprites(25, 'kg063_00')
    HitSprites(26, 'kg063_01')
    HitSprites(27, 'kg063_02')
    HitSprites(28, 'kg063_04')
    HitSprites(29, 'kg063_10')
    HitSprites(30, 'kg077_00')
    HitSprites(31, 'kg077_01')
    HitSprites(32, 'kg077_00ex01')
    HitSprites(33, 'kg077_01ex01')
    HitSprites(34, 'kg077_00ex02')
    HitSprites(35, 'kg077_01ex02')
    HitSprites(36, 'kg077_00ex03')
    HitSprites(37, 'kg077_01ex03')
    HitSprites(24, 'kg073_01')
    CommonVoicelines(0, 'kg000')
    CommonVoicelines(1, 'kg001')
    CommonVoicelines(2, 'kg002')
    CommonVoicelines(3, 'kg003')
    CommonVoicelines(4, 'kg004')
    CommonVoicelines(5, 'kg005')
    CommonVoicelines(6, 'kg006')
    CommonVoicelines(7, 'kg007')
    CommonVoicelines(8, 'kg008')
    CommonVoicelines(9, 'kg009')
    CommonVoicelines(10, 'kg010')
    CommonVoicelines(11, 'kg011')
    CommonVoicelines(12, 'kg012')
    CommonVoicelines(13, 'kg013')
    CommonVoicelines(14, 'kg014')
    CommonVoicelines(15, 'kg015')
    CommonVoicelines(16, 'kg016')
    CommonVoicelines(17, 'kg017')
    CommonVoicelines(18, 'kg018')
    CommonVoicelines(19, 'kg019')
    CommonVoicelines(20, 'kg020')
    CommonVoicelines(21, 'kg021')
    CommonVoicelines(22, 'kg022')
    CommonVoicelines(23, 'kg023')
    CommonVoicelines(24, 'kg024')
    CommonVoicelines(25, 'kg025')
    CommonVoicelines(26, 'kg026')
    CommonVoicelines(27, 'kg027')
    CommonVoicelines(28, 'kg028')
    CommonVoicelines(29, 'kg029')
    CommonVoicelines(30, 'kg030')
    CommonVoicelines(31, 'kg031')
    CommonVoicelines(32, 'kg032')
    CommonVoicelines(33, 'kg033')
    CommonVoicelines(34, 'kg034')
    CommonVoicelines(35, 'kg035')
    CommonVoicelines(36, 'kg036')
    CommonVoicelines(37, 'kg037')
    CommonVoicelines(38, 'kg038')
    CommonVoicelines(39, 'kg039')
    CommonVoicelines(40, 'kg040')
    CommonVoicelines(41, 'kg041')
    CommonVoicelines(42, 'kg042')
    CommonVoicelines(43, 'kg043')
    CommonVoicelines(44, 'kg044')
    CommonVoicelines(45, 'kg045')
    CommonVoicelines(46, 'kg046')
    CommonVoicelines(47, 'kg047')
    CommonVoicelines(48, 'kg048')
    CommonVoicelines(49, 'kg049')
    CommonVoicelines(50, 'kg050')
    CommonVoicelines(51, 'kg051')
    CommonVoicelines(52, 'kg052')
    CommonVoicelines(53, 'kg053')
    CommonVoicelines(54, 'kg100')
    CommonVoicelines(55, 'kg101')
    CommonVoicelines(56, 'kg102')
    CommonVoicelines(57, 'kg103')
    CommonVoicelines(58, 'kg104')
    CommonVoicelines(59, 'kg105')
    CommonVoicelines(60, 'kg106')
    CommonVoicelines(61, 'kg107')
    CommonVoicelines(62, 'kg108')
    CommonVoicelines(63, 'kg109')
    CommonVoicelines(64, 'kg150')
    CommonVoicelines(65, 'kg151')
    CommonVoicelines(66, 'kg152')
    CommonVoicelines(67, 'kg153')
    CommonVoicelines(68, 'kg154')
    CommonVoicelines(69, 'kg155')
    CommonVoicelines(70, 'kg156')
    CommonVoicelines(71, 'kg157')
    CommonVoicelines(72, 'kg158')
    CommonVoicelines(75, 'kg160')
    CommonVoicelines(73, 'kg402')
    CommonVoicelines(74, 'kg403')


@Subroutine
def OnFrameStep():
    if not SLOT_21:
        if SLOT_121 >= 1:
            if not SLOT_66:
                if not SLOT_CurrentHealth:
                    if CurrentStateCheck('CmnActFDownLoop'):
                        SLOT_51 = 1
                    if CurrentStateCheck('CmnActBDownLoop'):
                        SLOT_51 = 1
                    if SLOT_51:
                        if CurrentStateCheck('CmnActBDownLoop'):
                            if not CheckObjectPresence(11):
                                enterState('LoseAction')
                                CreateObject('LoseKaguraGirl', -1)
                                RegisterObject(11, 1)
                                if SLOT_121 == 1:
                                    ObjectUpon(STATE_END, 32)
                                if SLOT_121 == 2:
                                    ObjectUpon(STATE_END, 33)
                                if SLOT_121 == 3:
                                    ObjectUpon(STATE_END, 34)
                                if SLOT_121 == 4:
                                    ObjectUpon(STATE_END, 35)


@Subroutine
def OnFinalize():
    if SLOT_4:
        SLOT_4 = 0


@Subroutine
def CheckUsed5D():
    SLOT_47 = 0
    if not SLOT_60:
        SLOT_47 = 1


@Subroutine
def CheckShotAvailable():
    if CheckObjectPresence(4):
        SLOT_47 = 0
    else:
        SLOT_47 = 1


@Subroutine
def Func_BurstDD_Easy():
    SLOT_47 = 0
    if PreviousStateCheck('CmnActOverDriveEnd'):
        SLOT_47 = 1


@State
def CmnActStand():
    label(0)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if random_(1, 2, 87):
        conditionalSendToLabel(0)
    if random_(2, 0, 90):
        conditionalSendToLabel(0)
    sprite('kg001_00', 6)
    SLOT_88 = 960
    Voiceline('kg000')
    sprite('kg001_01', 6)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 7)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 7)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 7)
    sprite('kg001_03', 7)
    sprite('kg001_01', 6)
    sprite('kg001_00', 6)
    loopRest()
    gotoLabel(0)


@State
def CmnActStandTurn():
    sprite('kg003_00ex', 3)
    SmartVoiceline('kg001')
    sprite('kg003_01', 3)
    sprite('kg003_00', 3)


@State
def CmnActStand2Crouch():
    sprite('kg010_00', 4)
    sprite('kg010_01', 4)


@State
def CmnActCrouch():
    label(0)
    sprite('kg010_02', 7)
    sprite('kg010_03', 7)
    sprite('kg010_04', 7)
    sprite('kg010_05', 7)
    sprite('kg010_06', 7)
    sprite('kg010_07', 7)
    sprite('kg010_08', 7)
    sprite('kg010_09', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActCrouchTurn():
    sprite('kg013_00ex', 3)
    sprite('kg013_01', 3)
    sprite('kg013_00', 3)


@State
def CmnActCrouch2Stand():
    sprite('kg010_01', 4)
    sprite('kg010_00', 4)


@State
def CmnActJumpPre():
    sprite('kg023_00', 2)
    sprite('kg023_01', 2)
    if SLOT_IsMovingForward:
        RandomVoiceline('kg003', 75, '', 100, '', 100, '', 100)
    else:
        RandomVoiceline('kg002', 75, '', 100, '', 100, '', 100)


@State
def CmnActJumpUpper():
    label(0)
    sprite('kg020_00', 4)
    sprite('kg020_01', 4)
    SmartVoiceline('rg002')
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpUpperEnd():
    sprite('kg020_02', 3)
    sprite('kg020_03', 3)
    sprite('kg020_04', 3)


@State
def CmnActJumpDown():
    sprite('kg020_05', 3)
    sprite('kg020_06', 3)
    label(0)
    sprite('kg020_07', 4)
    sprite('kg020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActJumpLanding():
    sprite('kg024_00', 3)
    sprite('kg024_01', 3)
    sprite('kg024_02', 3)
    sprite('kg024_03', 3)
    sprite('kg024_04', 3)


@State
def CmnActLandingStiffLoop():
    sprite('kg024_00', 2)
    sprite('kg024_01', 2)
    sprite('kg024_02', 32767)


@State
def CmnActLandingStiffEnd():
    sprite('kg024_03', 3)
    sprite('kg024_04', 3)


@State
def CmnActFWalk():
    sprite('kg030_00', 7)
    sprite('kg030_01', 7)
    label(0)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)


@State
def CmnActBWalk():
    sprite('kg031_00', 7)
    sprite('kg031_01', 7)
    label(0)
    sprite('kg031_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg031_03', 7)
    sprite('kg031_04', 7)
    sprite('kg031_05', 7)
    sprite('kg031_06', 7)
    sprite('kg031_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg031_08', 7)
    sprite('kg031_09', 7)
    sprite('kg031_10', 7)
    sprite('kg031_11', 7)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDash():
    sprite('kg032_00', 2)
    sprite('kg032_01', 2)
    label(0)
    sprite('kg032_02', 4)
    sprite('kg032_03', 4)
    DashEffects(100, 1, 1)
    sprite('kg032_04', 4)
    sprite('kg032_05', 4)
    sprite('kg032_06', 4)
    sprite('kg032_07', 4)
    DashEffects(100, 1, 1)
    sprite('kg032_08', 4)
    sprite('kg032_09', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDashStop():
    sprite('kg032_10', 3)
    sprite('kg032_11', 3)
    sprite('kg032_12', 3)
    sprite('kg032_13', 3)


@State
def CmnActBDash():

    def upon_IMMEDIATE():
        SetCommonActionMark(1)
        EnterStateIfEventID(8, '_NEUTRAL')
        ExternalForcesRate(100, 0)
        NegativeForBackDash()
        setInvincible(1)
        EndMomentum(1)
    sprite('kg033_00', 2)
    sprite('kg033_01', 2)
    SmartVoiceline('kg005')
    sprite('kg033_02', 1)
    AddX(-20000)
    physicsXImpulse(-6000)
    sprite('kg033_02', 2)
    XImpulseAcceleration(400)
    sprite('kg033_03', 3)
    setInvincible(0)
    XImpulseAcceleration(150)
    sprite('kg033_04', 3)
    XImpulseAcceleration(30)
    LandingEffects(100, 1, 1)
    sprite('kg033_05', 3)
    sprite('kg033_06', 3)
    XImpulseAcceleration(50)
    sprite('kg033_07', 3)
    XImpulseAcceleration(50)
    sprite('kg033_08', 3)
    physicsXImpulse(0)


@State
def CmnActBDashLanding():
    pass


@State
def CmnActAirFDash():
    sprite('kg035_00', 3)
    label(0)
    sprite('kg035_01', 3)
    sprite('kg035_02', 3)
    sprite('kg035_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBDash():
    sprite('kg036_00', 3)
    label(0)
    sprite('kg036_01', 3)
    sprite('kg036_02', 3)
    sprite('kg036_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActHitStandLv1():
    sprite('kg050_00', 1)
    sprite('kg050_01', 1)
    sprite('kg050_00', 2)


@State
def CmnActHitStandLv2():
    sprite('kg050_01', 1)
    sprite('kg050_02', 1)
    sprite('kg050_01', 2)
    sprite('kg050_00', 2)


@State
def CmnActHitStandLv3():
    sprite('kg050_02', 1)
    sprite('kg050_03', 1)
    sprite('kg050_02', 2)
    sprite('kg050_01', 2)
    sprite('kg050_00', 2)


@State
def CmnActHitStandLv4():
    sprite('kg050_03', 1)
    sprite('kg050_04', 1)
    sprite('kg050_03', 2)
    sprite('kg050_02', 2)
    sprite('kg050_01', 2)
    sprite('kg050_00', 2)


@State
def CmnActHitStandLv5():
    sprite('kg050_04', 1)
    sprite('kg050_04', 1)
    sprite('kg050_04', 2)
    sprite('kg050_03', 2)
    sprite('kg050_02', 2)
    sprite('kg050_01', 2)
    sprite('kg050_00', 2)


@State
def CmnActHitStandLowLv1():
    sprite('kg052_00', 1)
    sprite('kg052_01', 1)
    sprite('kg052_00', 2)


@State
def CmnActHitStandLowLv2():
    sprite('kg052_01', 1)
    sprite('kg052_02', 1)
    sprite('kg052_01', 2)
    sprite('kg052_00', 2)


@State
def CmnActHitStandLowLv3():
    sprite('kg052_02', 1)
    sprite('kg052_03', 1)
    sprite('kg052_02', 2)
    sprite('kg052_01', 2)
    sprite('kg052_00', 2)


@State
def CmnActHitStandLowLv4():
    sprite('kg052_03', 1)
    sprite('kg052_04', 1)
    sprite('kg052_03', 2)
    sprite('kg052_02', 2)
    sprite('kg052_01', 2)
    sprite('kg052_00', 2)


@State
def CmnActHitStandLowLv5():
    sprite('kg052_04', 1)
    sprite('kg052_04', 1)
    sprite('kg052_04', 2)
    sprite('kg052_03', 2)
    sprite('kg052_02', 2)
    sprite('kg052_01', 2)
    sprite('kg052_00', 2)


@State
def CmnActHitCrouchLv1():
    sprite('kg054_00', 1)
    sprite('kg054_01', 1)
    sprite('kg054_00', 2)


@State
def CmnActHitCrouchLv2():
    sprite('kg054_01', 1)
    sprite('kg054_02', 1)
    sprite('kg054_01', 2)
    sprite('kg054_00', 2)


@State
def CmnActHitCrouchLv3():
    sprite('kg054_02', 1)
    sprite('kg054_03', 1)
    sprite('kg054_02', 2)
    sprite('kg054_01', 2)
    sprite('kg054_00', 2)


@State
def CmnActHitCrouchLv4():
    sprite('kg054_03', 1)
    sprite('kg054_04', 1)
    sprite('kg054_03', 2)
    sprite('kg054_02', 2)
    sprite('kg054_01', 2)
    sprite('kg054_00', 2)


@State
def CmnActHitCrouchLv5():
    sprite('kg054_04', 1)
    sprite('kg054_04', 1)
    sprite('kg054_04', 2)
    sprite('kg054_03', 2)
    sprite('kg054_02', 2)
    sprite('kg054_01', 2)
    sprite('kg054_00', 2)


@State
def CmnActBDownUpper():
    sprite('kg060_00', 4)
    label(0)
    sprite('kg060_01', 4)
    sprite('kg060_02', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownUpperEnd():
    sprite('kg060_03', 4)


@State
def CmnActBDownDown():
    sprite('kg060_04', 4)
    label(0)
    sprite('kg060_05', 4)
    sprite('kg060_06', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActBDownCrash():
    sprite('kg060_07', 2)
    sprite('kg060_08', 2)


@State
def CmnActBDownBound():
    sprite('kg060_09', 3)
    sprite('kg060_10', 3)
    sprite('kg060_11', 3)
    sprite('kg060_12', 3)
    sprite('kg060_13', 3)


@State
def CmnActBDownLoop():
    sprite('kg060_14', 1)


@State
def CmnActBDown2Stand():
    sprite('kg061_00', 3)
    sprite('kg061_01', 3)
    sprite('kg061_02', 3)
    sprite('kg061_03', 3)
    sprite('kg061_04', 3)
    sprite('kg061_05', 3)
    sprite('kg061_06', 2)
    sprite('kg061_07', 2)
    sprite('kg061_08', 3)
    sprite('kg061_09', 3)


@State
def CmnActFDownUpper():
    sprite('kg063_00', 3)


@State
def CmnActFDownUpperEnd():
    sprite('kg063_01', 3)


@State
def CmnActFDownDown():
    label(0)
    sprite('kg063_02', 3)
    sprite('kg063_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActFDownCrash():
    sprite('kg063_04', 3)
    sprite('kg063_05', 3)


@State
def CmnActFDownBound():
    sprite('kg063_06', 2)
    sprite('kg063_07', 2)
    sprite('kg063_08', 3)
    sprite('kg063_09', 3)
    sprite('kg063_10', 3)


@State
def CmnActFDownLoop():
    sprite('kg063_11', 3)


@State
def CmnActFDown2Stand():
    sprite('kg064_00', 1)
    sprite('kg064_01', 1)
    sprite('kg064_02', 2)
    sprite('kg064_03', 2)
    sprite('kg064_04', 1)
    sprite('kg064_05', 3)
    sprite('kg064_06', 2)
    sprite('kg064_07', 3)
    sprite('kg064_08', 3)
    sprite('kg064_09', 2)
    sprite('kg064_10', 2)


@State
def CmnActVDownUpper():
    sprite('kg062_00', 3)
    label(0)
    sprite('kg062_01', 3)
    sprite('kg062_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownUpperEnd():
    sprite('kg062_03', 3)
    sprite('kg062_04', 3)


@State
def CmnActVDownDown():
    sprite('kg062_05', 3)
    sprite('kg062_06', 3)
    label(0)
    sprite('kg062_07', 3)
    sprite('kg062_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActVDownCrash():
    sprite('kg062_09', 2)
    sprite('kg062_10', 2)


@State
def CmnActZSpinCrash():
    sprite('kg062_09', 2)
    sprite('kg062_10', 2)


@State
def CmnActBlowoff():
    sprite('kg072_00', 3)
    sprite('kg072_01', 3)
    sprite('kg072_02', 3)
    label(0)
    sprite('kg072_01', 3)
    sprite('kg072_02', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActKirimomiUpper():
    label(0)
    sprite('kg074_00', 3)
    sprite('kg074_01', 3)
    sprite('kg074_02', 3)
    sprite('kg074_03', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSkeleton():
    label(0)
    sprite('kg082_00', 2)
    sprite('kg082_01', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActFreeze():
    sprite('kg071_06', 1)


@State
def CmnActWallBound():
    sprite('kg073_00', 3)
    sprite('kg073_01', 3)


@State
def CmnActWallBoundDown():
    sprite('kg073_02', 3)
    label(0)
    sprite('kg073_03', 3)
    sprite('kg073_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActStaggerLoop():
    sprite('kg070_00', 3)
    sprite('kg070_01', 3)
    sprite('kg070_02', 4)
    sprite('kg070_03', 4)


@State
def CmnActStaggerDown():
    sprite('kg070_04', 4)
    sprite('kg070_05', 4)
    sprite('kg070_06', 4)
    sprite('kg070_07', 4)
    sprite('kg070_08', 4)
    sprite('kg070_09', 4)


@State
def CmnActUkemiStagger():
    sprite('kg070_10', 2)
    sprite('kg070_11', 2)
    sprite('kg070_12', 2)
    sprite('kg070_13', 2)


@State
def CmnActUkemiAirF():
    sprite('kg113_00', 3)
    sprite('kg113_01', 3)
    sprite('kg113_02', 3)


@State
def CmnActUkemiAirB():
    sprite('kg113_00', 3)
    sprite('kg113_01', 3)
    sprite('kg113_02', 3)


@State
def CmnActUkemiAirN():
    sprite('kg113_00', 3)
    sprite('kg113_01', 3)
    sprite('kg113_02', 3)


@State
def CmnActUkemiLandF():
    sprite('kg110_00', 2)
    sprite('kg110_01', 2)
    sprite('kg110_02', 2)
    sprite('kg110_03', 2)
    sprite('kg110_04', 2)
    sprite('kg110_06', 2)
    sprite('kg110_07', 2)
    sprite('kg110_08', 200)
    sprite('kg110_09', 3)
    sprite('kg110_10', 3)


@State
def CmnActUkemiLandB():
    sprite('kg111_00', 3)
    sprite('kg111_01', 3)
    sprite('kg111_02', 3)
    sprite('kg111_03', 3)
    sprite('kg111_04', 3)
    sprite('kg111_06', 3)
    sprite('kg111_07', 200)
    sprite('kg111_08', 3)
    sprite('kg111_09', 3)


@State
def CmnActUkemiLandN():
    sprite('kg112_00', 2)
    sprite('kg112_01', 2)
    sprite('kg112_02', 2)
    sprite('kg112_03', 2)
    sprite('kg112_04', 2)
    sprite('kg112_05', 2)
    sprite('kg112_06', 2)
    sprite('kg112_07', 2)
    sprite('kg112_08', 2)
    sprite('kg112_09', 2)


@State
def CmnActUkemiLandNLanding():
    sprite('kg024_00', 3)
    sprite('kg024_01', 3)
    sprite('kg024_02', 3)
    sprite('kg024_03', 3)
    sprite('kg024_04', 3)


@State
def CmnActMidGuardPre():
    sprite('kg040_00', 3)
    sprite('kg040_01', 3)


@State
def CmnActMidGuardLoop():
    label(0)
    sprite('kg040_02', 3)
    sprite('kg040_03', 3)
    sprite('kg040_04', 3)
    gotoLabel(0)


@State
def CmnActMidGuardEnd():
    sprite('kg040_01', 3)
    sprite('kg040_00', 3)


@State
def CmnActMidHeavyGuardLoop():
    sprite('kg040_05', 3)
    label(0)
    sprite('kg040_02', 3)
    sprite('kg040_03', 3)
    sprite('kg040_04', 3)
    gotoLabel(0)


@State
def CmnActMidHeavyGuardEnd():
    sprite('kg040_01', 3)
    sprite('kg040_00', 3)


@State
def CmnActHighGuardPre():
    sprite('kg041_00', 3)
    sprite('kg041_01', 3)


@State
def CmnActHighGuardLoop():
    label(0)
    sprite('kg041_02', 3)
    sprite('kg041_03', 3)
    sprite('kg041_04', 3)
    gotoLabel(0)


@State
def CmnActHighGuardEnd():
    sprite('kg041_01', 3)
    sprite('kg041_00', 3)


@State
def CmnActHighHeavyGuardLoop():
    sprite('kg041_05', 3)
    label(0)
    sprite('kg041_02', 3)
    sprite('kg041_03', 3)
    sprite('kg041_04', 3)
    gotoLabel(0)


@State
def CmnActHighHeavyGuardEnd():
    sprite('kg041_01', 3)
    sprite('kg041_00', 3)


@State
def CmnActCrouchGuardPre():
    sprite('kg043_00', 3)
    sprite('kg043_01', 3)


@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('kg043_02', 3)
    sprite('kg043_03', 3)
    sprite('kg043_04', 3)
    gotoLabel(0)


@State
def CmnActCrouchGuardEnd():
    sprite('kg043_01', 3)
    sprite('kg043_00', 3)


@State
def CmnActCrouchHeavyGuardLoop():
    sprite('kg043_05', 3)
    label(0)
    sprite('kg043_02', 3)
    sprite('kg043_03', 3)
    sprite('kg043_04', 3)
    gotoLabel(0)


@State
def CmnActCrouchHeavyGuardEnd():
    sprite('kg043_01', 3)
    sprite('kg043_00', 3)


@State
def CmnActAirGuardPre():
    sprite('kg045_00', 3)
    sprite('kg045_01', 3)


@State
def CmnActAirGuardLoop():
    label(0)
    sprite('kg045_02', 3)
    sprite('kg045_03', 3)
    sprite('kg045_04', 3)
    gotoLabel(0)


@State
def CmnActAirGuardEnd():
    sprite('kg045_01', 3)
    sprite('kg045_00', 3)


@State
def CmnActAirHeavyGuardLoop():
    sprite('kg045_05', 3)
    label(0)
    sprite('kg045_02', 3)
    sprite('kg045_03', 3)
    sprite('kg045_04', 3)
    gotoLabel(0)


@State
def CmnActAirHeavyGuardEnd():
    sprite('kg045_01', 3)
    sprite('kg045_00', 3)


@State
def CmnActGuardBreakStand():
    sprite('kg090_00', 2)
    sprite('kg090_01', 2)
    sprite('kg090_02', 1)
    SetCommonActionMark(1)
    sprite('kg090_03', 6)
    sprite('kg090_04', 6)


@State
def CmnActGuardBreakCrouch():
    sprite('kg091_00', 2)
    sprite('kg091_01', 2)
    sprite('kg091_02', 1)
    SetCommonActionMark(1)
    sprite('kg091_03', 6)
    sprite('kg091_04', 6)


@State
def CmnActGuardBreakAir():
    sprite('kg092_00', 2)
    sprite('kg092_01', 2)
    sprite('kg092_02', 1)
    SetCommonActionMark(1)
    sprite('kg092_03', 6)
    sprite('kg092_04', 6)


@State
def CmnActAirTurn():
    sprite('kg025_00ex', 4)
    sprite('kg025_01', 4)
    sprite('kg025_00', 4)


@State
def CmnActLockWait():
    sprite('kg040_02', 1)
    sprite('kg040_01', 3)
    sprite('kg040_00', 3)


@State
def CmnActLockReject():
    sprite('kg312_00', 2)
    sprite('kg312_01', 2)
    sprite('kg312_02', 2)
    sprite('kg312_03', 3)
    sprite('kg312_04', 2)
    sprite('kg312_05', 4)
    sprite('kg312_06', 4)
    sprite('kg312_07', 3)
    sprite('kg312_08', 3)


@State
def CmnActAirLockWait():
    sprite('kg045_02', 1)
    sprite('kg045_01', 3)
    sprite('kg045_00', 3)


@State
def CmnActAirLockReject():
    sprite('kg322_00', 2)
    sprite('kg322_01', 2)
    sprite('kg322_02', 8)
    sprite('kg322_03', 2)
    sprite('kg322_04', 2)
    sprite('kg322_05', 3)
    sprite('kg322_06', 3)
    sprite('kg322_07', 3)
    sprite('kg322_08', 3)


@State
def CmnActLandSpin():
    sprite('kg071_00', 4)
    sprite('kg071_01', 4)
    label(0)
    sprite('kg071_02', 2)
    sprite('kg071_03', 2)
    sprite('kg071_04', 2)
    sprite('kg071_05', 2)
    sprite('kg071_06', 2)
    sprite('kg071_07', 2)
    sprite('kg071_08', 2)
    sprite('kg071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActLandSpinDown():
    sprite('kg071_10', 6)
    sprite('kg071_11', 5)
    sprite('kg071_12', 5)


@State
def CmnActVertSpin():
    label(0)
    sprite('kg071_02', 2)
    sprite('kg071_03', 2)
    sprite('kg071_04', 2)
    sprite('kg071_05', 2)
    sprite('kg071_06', 2)
    sprite('kg071_07', 2)
    sprite('kg071_08', 2)
    sprite('kg071_09', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideAir():
    label(0)
    sprite('kg077_00', 2)
    sprite('kg077_01', 2)
    sprite('kg077_00ex01', 2)
    sprite('kg077_01ex01', 2)
    sprite('kg077_00ex02', 2)
    sprite('kg077_01ex02', 2)
    sprite('kg077_00ex03', 2)
    sprite('kg077_01ex03', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideKeep():
    sprite('kg077_02', 4)
    label(0)
    sprite('kg077_03', 3)
    sprite('kg077_04', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActSlideEnd():
    sprite('kg077_05', 5)
    sprite('kg077_06', 4)


@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('kg060_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAomukeSlideEnd():
    sprite('kg060_11', 4)
    sprite('kg060_13', 5)


@State
def CmnActBurstBegin():
    sprite('kg331_00', 2)
    sprite('kg331_01', 2)
    label(0)
    sprite('kg331_02', 2)
    sprite('kg331_03', 2)
    sprite('kg331_04', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstLoop():
    sprite('kg331_05', 2)
    label(0)
    sprite('kg331_06', 3)
    sprite('kg331_07', 3)
    sprite('kg331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActBurstEnd():
    sprite('kg331_09', 1)
    sprite('kg331_10', 1)
    sprite('kg331_11', 2)
    sprite('kg331_12', 2)


@State
def CmnActAirBurstBegin():
    sprite('kg331_13', 2)
    sprite('kg331_14', 2)
    label(0)
    sprite('kg331_15', 2)
    sprite('kg331_16', 2)
    sprite('kg331_17', 2)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstLoop():
    sprite('kg331_18', 2)
    label(0)
    sprite('kg331_06', 3)
    sprite('kg331_07', 3)
    sprite('kg331_08', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirBurstEnd():
    sprite('kg331_09', 2)
    sprite('kg331_19', 2)
    sprite('kg331_20', 2)
    label(0)
    sprite('kg020_07', 4)
    sprite('kg020_08', 4)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveBegin():
    sprite('kg333_00', 3)
    sprite('kg333_01', 3)
    sprite('kg333_02', 3)
    CharacterFlash(16639, 20, 1)
    sprite('kg333_03', 32767)
    CreateObject('EMB_KG_OD', -1)
    loopRest()


@State
def CmnActOverDriveLoop():
    sprite('kg333_04', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('kg333_05', 3)
    sprite('kg333_06', 3)
    sprite('kg333_07', 3)
    label(0)
    sprite('kg333_05', 3)
    sprite('kg333_06', 3)
    sprite('kg333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActOverDriveEnd():
    sprite('kg333_08', 6)
    sprite('kg333_09', 6)


@State
def CmnActAirOverDriveBegin():
    sprite('kg333_10', 3)
    sprite('kg333_11', 3)
    sprite('kg333_12', 3)
    CharacterFlash(16639, 20, 1)
    sprite('kg333_13', 32767)
    CreateObject('EMB_KG', -1)
    loopRest()


@State
def CmnActAirOverDriveLoop():
    sprite('kg333_14', 3)
    StopCharacterFlash1(16639)
    CharacterFlash(0, 20, 1)
    sprite('kg333_05', 3)
    sprite('kg333_06', 3)
    sprite('kg333_07', 3)
    label(0)
    sprite('kg333_05', 3)
    sprite('kg333_06', 3)
    sprite('kg333_07', 3)
    loopRest()
    gotoLabel(0)


@State
def CmnActAirOverDriveEnd():
    sprite('kg333_15', 6)
    sprite('kg333_16', 6)


@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        AirPushbackY(19000)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('kg200_00', 1)
    PerInertia(60)
    sprite('kg200_01', 1)
    CommonSE('004_swing_grap_1_0')
    sprite('kg200_02', 2)
    RandomCommonVoiceline(0)
    sprite('kg200_03', 3)
    sprite('kg200_04', 3)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('kg200_02', 2)
    sprite('kg200_01', 2)
    sprite('kg200_00', 2)


@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(480)
        AttackP1(90)
        HitLow(2)
        AirUntechableTime(17)
        AirPushbackY(-15000)
        GroundBounce(1)
        BouncePercentage(65)
        PushbackX(13000)
        MoveAttributes(0, 0, 1, 0, 0)
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('Atk6B_Input5')
    sprite('kg201_00', 2)
    sprite('kg201_01', 2)
    sprite('kg201_02', 3)
    CommonSE('004_swing_grap_1_2')
    RandomCommonVoiceline(1)
    sprite('kg201_03', 3)
    sprite('kg201_04', 3)
    Recovery()
    Unknown2063()
    sprite('kg201_05', 4)
    sprite('kg201_06', 2)
    sprite('kg201_07', 2)


@State
def NmlAtk5C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('InitializeCAttackChainAttack')
        AttackLevel_(4)
        Damage(1100)
        Hitstun(28)
        Blockstun(22)
        PushbackX(42000)

        def upon_OPPONENT_HIT():
            PushbackX(37000)
        AirPushbackX(30000)
        AirPushbackY(30000)
        AirUntechableTime(36)
        CHAirPushbackY(20000)
        CHWallbounce(1)
        CHWallbounceReboundTime(1)
        StayAfterMovement(1, 0)
    sprite('kg202_00', 3)
    sprite('kg202_01', 2)
    sprite('kg202_02', 2)
    RandomCommonVoiceline(2)
    sprite('kg202_03', 2)
    sprite('kg202_04', 3)
    sprite('kg202_05', 3)
    physicsXImpulse(5000)
    sprite('kg202_06', 3)
    PrivateSE('kgse_01')
    sprite('kg202_07', 2)
    XImpulseAcceleration(25)
    AltKnockdownEffects(100, 1, 0)
    CreateObject('efkg_202', -1)
    sprite('kg202_08', 2)
    sprite('kg202_09', 2)
    Recovery()
    Unknown2063()
    physicsXImpulse(0)
    sprite('kg202_10', 3)
    sprite('kg202_11', 3)
    sprite('kg202_12', 3)
    sprite('kg202_13', 3)
    sprite('kg202_14', 3)
    sprite('kg202_15', 3)
    sprite('kg202_16', 3)


@State
def NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('InitializeStandByLand')
        callSubroutine('InitializeStandByStart')
        SLOT_60 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandBy5DA_CPU')
        WhiffCancel('StandBy5DB_CPU')
        WhiffCancel('StandBy5DC_CPU')
    sprite('kg203_00', 3)
    sprite('kg203_01', 3)
    sprite('kg203_02', 3)
    CreateObject('efkg_203', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    SetActionMark(1)
    BeginBuffer('StandBy5DA')
    BeginBuffer('StandBy5DB')
    BeginBuffer('StandBy5DC')
    BeginBuffer('StandBy5DD')
    sprite('kg203_02', 2)
    WhiffCancelEnable(1)
    BufferedOrPressedGoto('StandBy5DA')
    BufferedOrPressedGoto('StandBy5DB')
    BufferedOrPressedGoto('StandBy5DC')
    BufferedOrPressedGoto('StandBy5DD')
    sprite('kg203_03', 5)
    sprite('kg203_04', 5)
    label(0)
    sprite('kg203_05', 5)
    sprite('kg203_06', 5)
    sprite('kg203_02', 5)
    sprite('kg203_03', 5)
    sprite('kg203_04', 5)
    gotoLabel(0)
    label(1)
    sprite('kg203_01', 6)
    WhiffCancelEnable(0)
    DisallowGoto('StandBy5DA')
    DisallowGoto('StandBy5DB')
    DisallowGoto('StandBy5DC')
    DisallowGoto('StandBy5DD')
    Recovery()
    sprite('kg203_00', 6)


@State
def Change_NmlAtk5D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('InitializeStandByLand')
        SLOT_60 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandBy5DA')
        WhiffCancel('StandBy5DB')
        WhiffCancel('StandBy5DC')
        WhiffCancel('StandBy5DD')
        WhiffCancel('StandBy5DA_CPU')
        WhiffCancel('StandBy5DB_CPU')
        WhiffCancel('StandBy5DC_CPU')
    sprite('kg203_00', 3)
    sprite('kg203_01', 3)
    sprite('kg203_02', 1)
    CreateObject('efkg_203', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    SetActionMark(1)
    sprite('kg203_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg203_05', 5)
    sprite('kg203_06', 5)
    sprite('kg203_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg203_01', 6)
    WhiffCancelEnable(0)
    Recovery()
    sprite('kg203_00', 6)


@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(12000)
        HitAirUnblockable(0)
        StarterRating(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk6A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('kg230_00', 2)
    PerInertia(60)
    sprite('kg230_01', 2)
    CommonSE('004_swing_grap_1_0')
    sprite('kg230_02', 2)
    RandomCommonVoiceline(0)
    sprite('kg230_03', 3)
    sprite('kg230_04', 2)
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('kg230_02', 3)
    sprite('kg230_01', 3)
    sprite('kg230_00', 2)


@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
    sprite('kg231_00', 3)
    sprite('kg231_01', 3)
    sprite('kg231_02', 3)
    CommonSE('004_swing_grap_1_2')
    RandomCommonVoiceline(1)
    sprite('kg231_03', 3)
    sprite('kg231_04', 2)
    Recovery()
    Unknown2063()
    sprite('kg231_05', 2)
    sprite('kg231_06', 4)
    sprite('kg231_07', 3)
    sprite('kg231_08', 3)


@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        callSubroutine('InitializeCAttackChainAttack')
        AttackLevel_(4)
        Damage(1000)
        AttackP2(82)
        GroundedHitstunAnimation(11)
        Blockstun(20)
        PushbackX(40000)
        AirPushbackX(19000)
        AirPushbackY(1000)
        AirUntechableTime(35)
        CHAirUntechableTime(40)
        Floorslide(40)
        CHFloorslide(45)
        StayAfterMovement(1, 0)
        SetActionMark(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            SetActionMark(1)
    sprite('kg232_00', 3)
    sprite('kg232_01', 3)
    RandomCommonVoiceline(2)
    sprite('kg232_02', 2)
    sprite('kg232_03', 2)
    sprite('kg232_04', 2)
    sprite('kg232_05', 3)
    PrivateSE('kgse_01')
    sprite('kg232_06ex01', 2)
    CreateObject('efkg_232', -1)
    sprite('kg232_06', 2)
    sprite('kg232_07', 3)
    sprite('kg232_08', 2)
    Recovery()
    Unknown2063()
    sprite('kg232_09', 2)
    sprite('kg232_10', 3)
    BeginBuffer('NmlAtk5C')
    sprite('kg232_11', 4)
    if SLOT_2:
        BufferedOrPressedGoto('NmlAtk5C')
    sprite('kg232_12', 4)
    DisallowGoto('NmlAtk5C')
    sprite('kg232_13', 4)
    sprite('kg232_14', 4)


@State
def NmlAtk3C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(900)
        AttackP1(90)
        AttackP2(79)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(12000)
        CHAirPushbackX(8000)
        AirPushbackY(22000)
        PushbackX(40000)
        AirUntechableTime(40)
        CHHardKnockdown(10)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        StayAfterMovement(1, 0)
    sprite('kg235_00', 3)
    sprite('kg235_01', 3)
    sprite('kg235_02', 3)
    if random_(2, 0, 50):
        Voiceline('kg108')
    else:
        Voiceline('kg109')
    sprite('kg235_03', 2)
    sprite('kg235_04', 2)
    PrivateSE('kgse_01')
    sprite('kg235_05', 3)
    CreateObject('efkg_235', -1)
    sprite('kg235_06', 2)
    Recovery()
    Unknown2063()
    sprite('kg235_07', 3)
    sprite('kg235_08', 3)
    sprite('kg235_09', 3)
    sprite('kg235_10', 3)
    sprite('kg235_11', 3)
    sprite('kg235_12', 3)
    sprite('kg235_13', 3)


@State
def NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        callSubroutine('InitializeStandByLand')
        callSubroutine('InitializeStandByStart')
        SLOT_61 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandBy2DA_CPU')
        WhiffCancel('StandBy2DB_CPU')
        WhiffCancel('StandBy2DC_CPU')
    sprite('kg233_00', 3)
    sprite('kg233_01', 3)
    sprite('kg233_02', 3)
    CreateObject('efkg_233', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    SetActionMark(1)
    BeginBuffer('StandBy2DA')
    BeginBuffer('StandBy2DB')
    BeginBuffer('StandBy2DC')
    BeginBuffer('StandBy2DD')
    sprite('kg233_02', 2)
    WhiffCancelEnable(1)
    BufferedOrPressedGoto('StandBy2DA')
    BufferedOrPressedGoto('StandBy2DB')
    BufferedOrPressedGoto('StandBy2DC')
    BufferedOrPressedGoto('StandBy2DD')
    sprite('kg233_03', 5)
    sprite('kg233_04', 5)
    label(0)
    sprite('kg233_05', 5)
    sprite('kg233_06', 5)
    sprite('kg233_02', 5)
    sprite('kg233_03', 5)
    sprite('kg233_04', 5)
    gotoLabel(0)
    label(1)
    sprite('kg233_01', 6)
    WhiffCancelEnable(0)
    DisallowGoto('StandBy2DA')
    DisallowGoto('StandBy2DB')
    DisallowGoto('StandBy2DC')
    DisallowGoto('StandBy2DD')
    Recovery()
    sprite('kg233_00', 6)


@State
def Change_NmlAtk2D():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        callSubroutine('InitializeStandByLand')
        SLOT_61 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandBy2DA')
        WhiffCancel('StandBy2DB')
        WhiffCancel('StandBy2DC')
        WhiffCancel('StandBy2DD')
        WhiffCancel('StandBy2DA_CPU')
        WhiffCancel('StandBy2DB_CPU')
        WhiffCancel('StandBy2DC_CPU')
    sprite('kg233_00', 3)
    sprite('kg233_01', 3)
    sprite('kg233_02', 1)
    CreateObject('efkg_233', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    SetActionMark(1)
    sprite('kg233_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg233_03', 5)
    sprite('kg233_04', 5)
    sprite('kg233_05', 5)
    sprite('kg233_06', 5)
    sprite('kg233_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg233_01', 6)
    WhiffCancelEnable(0)
    Recovery()
    sprite('kg233_00', 6)


@State
def NmlAtk6A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        BonusProration(110)
        HitOverhead(2)
        GroundedHitstunAnimation(3)
        AirPushbackX(2000)
        AirPushbackY(-40000)
        AirUntechableTime(33)
        GroundBounce(1)
        BouncePercentage(45)
        Hitstun(25)
        PushbackX(15000)
        StarterRating(2)
        SpecialCancel(0)
        HitOrBlockCancel('ShotA')
        HitOrBlockCancel('ShotB')
        HitOrBlockCancel('AntiAirB')
        HitOrBlockCancel('AntiAirC')
        HitOrBlockCancel('UltimateShot')
        HitOrBlockCancel('UltimateShotOD')
    sprite('kg210_00', 3)
    sprite('kg210_01', 3)
    sprite('kg210_02', 3)
    sprite('kg210_03', 5)
    sprite('kg210_04', 5)
    sprite('kg210_05', 2)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_1')
    sprite('kg210_06', 3)
    sprite('kg210_07', 3)
    Recovery()
    sprite('kg210_08', 3)
    sprite('kg210_09', 3)
    sprite('kg210_10', 3)
    sprite('kg210_11', 3)
    sprite('kg210_12', 2)
    sprite('kg210_13', 2)


@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(600)
        AirUntechableTime(21)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk3C')
        HitOrBlockCancel('NmlAtk5D')
        HitOrBlockCancel('NmlAtk2D')
        HitOrBlockCancel('NmlAtk6D')
        HitOrBlockJumpCancel(1)
        StayAfterMovement(1, 0)
    sprite('kg211_00', 2)
    sprite('kg211_01', 2)
    sprite('kg211_02', 2)
    sprite('kg211_03', 2)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_2')
    sprite('kg211_04', 4)
    sprite('kg211_05', 3)
    Recovery()
    Unknown2063()
    sprite('kg211_06', 3)
    sprite('kg211_07', 3)
    sprite('kg211_08', 3)
    sprite('kg211_09', 3)
    sprite('kg211_10', 3)
    sprite('kg211_11', 3)


@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('InitializeCAttackChainAttack')
        AttackLevel_(5)
        Damage(1300)
        AttackP1(90)
        AttackP2(84)
        BonusProration(110)
        Blockstun(24)
        AirHitstunAnimation(10)
        CHAirHitstunAnimation(9)
        GroundedHitstunAnimation(10)
        CHGroundedHitstunAnimation(9)
        AirPushbackX(14000)
        AirPushbackY(38000)
        AirUntechableTime(55)
        PushbackX(60000)
        CHAirPushbackX(50000)
        CHAirPushbackY(20000)
        CHWallbounce(1)
        CHWallbounceReboundTime(0)
        CHHardKnockdown(1)
        StayAfterMovement(1, 0)
    sprite('kg212_00', 3)
    sprite('kg212_01', 2)
    AddX(400000)
    physicsXImpulse(5000)
    SetXCollisionFromOrigin(200)
    sprite('kg212_02', 2)
    RandomCommonVoiceline(2)
    sprite('kg212_03', 4)
    physicsXImpulse(0)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg212_04', 3)
    sprite('kg212_05', 3)
    sprite('kg212_06', 2)
    PrivateSE('kgse_01')
    sprite('kg212_07', 2)
    CreateObject('efkg_212', -1)
    StartMultihit()
    sprite('kg212_07', 3)
    sprite('kg212_08', 3)
    sprite('kg212_09', 3)
    Recovery()
    Unknown2063()
    sprite('kg212_10', 3)
    sprite('kg212_11', 3)
    sprite('kg212_12', 5)
    sprite('kg212_13', 5)
    sprite('kg212_14', 5)
    sprite('kg212_15', 5)
    AltKnockdownEffects(100, 1, 1)


@State
def NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('InitializeStandByLand')
        callSubroutine('InitializeStandByStart')
        SLOT_62 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandBy6DA_CPU')
        WhiffCancel('StandBy6DB_CPU')
        WhiffCancel('StandBy6DC_CPU')
    sprite('kg213_00', 3)
    sprite('kg213_01', 3)
    sprite('kg213_02', 3)
    CreateObject('efkg_213', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    SetActionMark(1)
    BeginBuffer('StandBy6DA')
    BeginBuffer('StandBy6DB')
    BeginBuffer('StandBy6DC')
    BeginBuffer('StandBy6DD')
    sprite('kg213_02', 2)
    WhiffCancelEnable(1)
    BufferedOrPressedGoto('StandBy6DA')
    BufferedOrPressedGoto('StandBy6DB')
    BufferedOrPressedGoto('StandBy6DC')
    BufferedOrPressedGoto('StandBy6DD')
    sprite('kg213_03', 5)
    sprite('kg213_04', 5)
    label(0)
    sprite('kg213_05', 5)
    sprite('kg213_06', 5)
    sprite('kg213_02', 5)
    sprite('kg213_03', 5)
    sprite('kg213_04', 5)
    gotoLabel(0)
    label(1)
    sprite('kg213_01', 6)
    WhiffCancelEnable(0)
    DisallowGoto('StandBy6DA')
    DisallowGoto('StandBy6DB')
    DisallowGoto('StandBy6DC')
    DisallowGoto('StandBy6DD')
    Recovery()
    sprite('kg213_00', 6)


@State
def Change_NmlAtk6D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('InitializeStandByLand')
        SLOT_62 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandBy6DA')
        WhiffCancel('StandBy6DB')
        WhiffCancel('StandBy6DC')
        WhiffCancel('StandBy6DD')
        WhiffCancel('StandBy6DA_CPU')
        WhiffCancel('StandBy6DB_CPU')
        WhiffCancel('StandBy6DC_CPU')
    sprite('kg213_00', 3)
    sprite('kg213_01', 3)
    sprite('kg213_02', 1)
    CreateObject('efkg_213', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    SetActionMark(1)
    sprite('kg213_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg213_03', 5)
    sprite('kg213_04', 5)
    sprite('kg213_05', 5)
    sprite('kg213_06', 5)
    sprite('kg213_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg213_01', 6)
    WhiffCancelEnable(0)
    Recovery()
    sprite('kg213_00', 6)


@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(300)
        AttackP1(80)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockCancel('NmlAtkAirThrow')
        HitOrBlockJumpCancel(1)
    sprite('kg250_00', 3)
    sprite('kg250_01', 3)
    RandomCommonVoiceline(0)
    CommonSE('005_swing_grap_2_0')
    sprite('kg250_02', 3)
    sprite('kg250_03', 3)
    Recovery()
    Unknown2063()
    sprite('kg250_01', 3)
    sprite('kg250_00', 3)


@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(550)
        AirHitstunAnimation(10)
        AirUntechableTime(19)
        AttackP1(80)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
        HitOrBlockJumpCancel(1)
    sprite('kg251_00', 3)
    sprite('kg251_01', 3)
    sprite('kg251_02', 3)
    RandomCommonVoiceline(1)
    CommonSE('004_swing_grap_1_2')
    sprite('kg251_03', 2)
    sprite('kg251_04', 2)
    sprite('kg251_05', 3)
    Recovery()
    Unknown2063()
    sprite('kg251_06', 3)
    sprite('kg251_07', 3)
    sprite('kg251_08', 3)
    sprite('kg251_09', 3)


@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        AirUntechableTime(29)
        AirPushbackX(15000)
        AirPushbackY(-25000)
        UseSlashHitspark(1)
        HitOrBlockCancel('NmlAtkAIR5D')
        HitOrBlockCancel('NmlAtkAIR2D')
        HitOrBlockCancel('NmlAtkAIR6D')
    sprite('kg252_00', 2)
    sprite('kg252_00', 2)
    sprite('kg252_01', 2)
    sprite('kg252_02', 2)
    sprite('kg252_03', 2)
    if random_(2, 0, 50):
        Voiceline('kg108')
    else:
        Voiceline('kg109')
    sprite('kg252_04', 2)
    PrivateSE('kgse_01')
    sprite('kg252_05', 5)
    CreateObject('efkg_252', -1)
    sprite('kg252_06', 3)
    Recovery()
    Unknown2063()
    sprite('kg252_07', 3)
    sprite('kg252_08', 3)
    sprite('kg252_09', 3)
    sprite('kg252_10', 3)
    sprite('kg252_11', 3)
    sprite('kg252_12', 3)
    sprite('kg252_13', 3)


@State
def NmlAtkAIR5D():

    def upon_IMMEDIATE():
        callSubroutine('InitializeStandByAir')
        callSubroutine('InitializeStandByStart')
        SLOT_60 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandByAIR5DD')
    sprite('kg253_00', 3)
    sprite('kg253_01', 3)
    RandomCommonVoiceline(3)
    EndMomentum(1)
    sprite('kg253_02', 1)
    CreateObject('efkg_253', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(25)
    YAccel(10)
    setGravity(50)
    SetActionMark(1)
    sprite('kg253_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg253_03', 5)
    sprite('kg253_04', 5)
    sprite('kg253_05', 5)
    sprite('kg253_06', 5)
    sprite('kg253_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg253_01', 6)
    EndYPhysicsImpulse()
    Recovery()
    sprite('kg253_00', 6)
    loopRest()
    ExitState()
    label(2)
    sprite('keep', 3)
    enterState('AIR5DDive')


@State
def Change_NmlAtkAIR5D():

    def upon_IMMEDIATE():
        callSubroutine('InitializeStandByAir')
        SLOT_60 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandByAIR5DD')
    sprite('kg253_00', 3)
    sprite('kg253_01', 3)
    EndMomentum(1)
    SetActionMark(1)
    sprite('kg253_02', 1)
    CreateObject('efkg_253', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(25)
    YAccel(10)
    setGravity(50)
    sprite('kg253_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg253_03', 5)
    sprite('kg253_04', 5)
    sprite('kg253_05', 5)
    sprite('kg253_06', 5)
    sprite('kg253_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg253_01', 6)
    EndYPhysicsImpulse()
    Recovery()
    sprite('kg253_00', 6)
    loopRest()
    ExitState()
    label(2)
    sprite('keep', 3)
    enterState('AIR5DDive')


@State
def StandByAIR5DD():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        Recovery()
    sprite('kg253_02', 4)
    sprite('kg253_03', 4)
    sprite('kg253_04', 4)
    sprite('kg253_05', 4)
    sprite('kg253_02', 6)
    EndYPhysicsImpulse()
    WhiffBlockCancel(1)
    sprite('kg253_01', 6)
    sprite('kg253_00', 6)


@State
def AIR5DDive():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 3)
        EnableCollision(0)

        def upon_STATE_END():
            SLOT_59 = 0
            if SLOT_OverdriveTimer:
                SLOT_61 = 1
                SLOT_62 = 1
    sprite('kg409_00', 2)
    sprite('kg409_01', 2)
    sprite('kg409_06', 1)
    sprite('keep', 1)
    callSubroutine('DiveDirectionSet')
    label(0)
    sprite('kg409_09', 2)
    sprite('kg409_10', 2)
    gotoLabel(0)
    label(1)
    sprite('kg409_07', 2)
    sprite('kg409_08', 2)
    gotoLabel(1)
    label(2)
    sprite('kg409_11', 2)
    sprite('kg409_12', 2)
    gotoLabel(2)
    label(3)
    sprite('kg409_13', 2)
    ForceFaceSprite()
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('kg409_14', 2)
    sprite('kg409_15', 2)
    sprite('kg409_16', 2)
    sprite('kg409_17', 2)
    sprite('kg203_02', 1)
    if SLOT_59 == 1:
        enterState('StandBy5DA')
    if SLOT_59 == 2:
        enterState('StandBy5DB')
    if SLOT_59 == 3:
        enterState('StandBy5DC')


@State
def NmlAtkAIR2D():

    def upon_IMMEDIATE():
        callSubroutine('InitializeStandByAir')
        callSubroutine('InitializeStandByStart')
        SLOT_61 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandByAIR2DD')
    sprite('kg254_00', 3)
    sprite('kg254_01', 3)
    RandomCommonVoiceline(3)
    EndMomentum(1)
    sprite('kg254_02', 1)
    CreateObject('efkg_254', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(25)
    YAccel(10)
    setGravity(50)
    SetActionMark(1)
    sprite('kg254_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg254_03', 5)
    sprite('kg254_04', 5)
    sprite('kg254_05', 5)
    sprite('kg254_06', 5)
    sprite('kg254_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg254_01', 6)
    EndYPhysicsImpulse()
    Recovery()
    sprite('kg254_00', 6)
    loopRest()
    ExitState()
    label(2)
    sprite('keep', 3)
    enterState('AIR2DDive')


@State
def Change_NmlAtkAIR2D():

    def upon_IMMEDIATE():
        callSubroutine('InitializeStandByAir')
        SLOT_61 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandByAIR2DD')
    sprite('kg254_00', 3)
    sprite('kg254_01', 3)
    EndMomentum(1)
    SetActionMark(1)
    sprite('kg254_02', 1)
    CreateObject('efkg_254', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(25)
    YAccel(10)
    setGravity(50)
    sprite('kg254_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg254_03', 5)
    sprite('kg254_04', 5)
    sprite('kg254_05', 5)
    sprite('kg254_06', 5)
    sprite('kg254_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg254_01', 6)
    EndYPhysicsImpulse()
    Recovery()
    sprite('kg254_00', 6)
    loopRest()
    ExitState()
    label(2)
    sprite('keep', 3)
    enterState('AIR2DDive')


@State
def StandByAIR2DD():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        Recovery()
    sprite('kg254_02', 4)
    sprite('kg254_03', 4)
    sprite('kg254_04', 4)
    sprite('kg254_05', 4)
    sprite('kg254_02', 6)
    EndYPhysicsImpulse()
    WhiffBlockCancel(1)
    sprite('kg254_01', 6)
    sprite('kg254_00', 6)


@State
def AIR2DDive():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 3)
        EnableCollision(0)

        def upon_STATE_END():
            SLOT_59 = 0
            if SLOT_OverdriveTimer:
                SLOT_60 = 1
                SLOT_62 = 1
    sprite('kg409_02', 2)
    sprite('kg409_03', 2)
    sprite('kg409_06', 1)
    sprite('keep', 1)
    callSubroutine('DiveDirectionSet')
    label(0)
    sprite('kg409_09', 2)
    sprite('kg409_10', 2)
    gotoLabel(0)
    label(1)
    sprite('kg409_07', 2)
    sprite('kg409_08', 2)
    gotoLabel(1)
    label(2)
    sprite('kg409_11', 2)
    sprite('kg409_12', 2)
    gotoLabel(2)
    label(3)
    sprite('kg409_13', 2)
    ForceFaceSprite()
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('kg409_14', 2)
    sprite('kg409_18', 2)
    sprite('kg409_19', 2)
    sprite('kg409_20', 2)
    sprite('kg233_02', 1)
    if SLOT_59 == 1:
        enterState('StandBy2DA')
    if SLOT_59 == 2:
        enterState('StandBy2DB')
    if SLOT_59 == 3:
        enterState('StandBy2DC')


@State
def NmlAtkAIR6D():

    def upon_IMMEDIATE():
        callSubroutine('InitializeStandByAir')
        callSubroutine('InitializeStandByStart')
        SLOT_62 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandByAIR6DD')
    sprite('kg255_00', 3)
    sprite('kg255_01', 3)
    RandomCommonVoiceline(3)
    EndMomentum(1)
    sprite('kg255_02', 1)
    CreateObject('efkg_255', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(25)
    YAccel(10)
    setGravity(50)
    SetActionMark(1)
    sprite('kg255_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg255_03', 5)
    sprite('kg255_04', 5)
    sprite('kg255_05', 5)
    sprite('kg255_06', 5)
    sprite('kg255_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg255_01', 6)
    EndYPhysicsImpulse()
    Recovery()
    sprite('kg255_00', 6)
    loopRest()
    ExitState()
    label(2)
    sprite('keep', 3)
    enterState('AIR6DDive')


@State
def Change_NmlAtkAIR6D():

    def upon_IMMEDIATE():
        callSubroutine('InitializeStandByAir')
        SLOT_62 = 0
        callSubroutine('InitializeStandByFlexChange')
        WhiffCancel('StandByAIR6DD')
    sprite('kg255_00', 3)
    sprite('kg255_01', 3)
    EndMomentum(1)
    SetActionMark(1)
    sprite('kg255_02', 1)
    CreateObject('efkg_255', -1)
    RegisterObject(5, 1)
    CreateParticle('kgef_kamaekira_kira03', 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(25)
    YAccel(10)
    setGravity(50)
    sprite('kg255_02', 4)
    WhiffCancelEnable(1)
    label(0)
    sprite('kg255_03', 5)
    sprite('kg255_04', 5)
    sprite('kg255_05', 5)
    sprite('kg255_06', 5)
    sprite('kg255_02', 5)
    gotoLabel(0)
    label(1)
    sprite('kg255_01', 6)
    EndYPhysicsImpulse()
    Recovery()
    sprite('kg255_00', 6)
    loopRest()
    ExitState()
    label(2)
    sprite('keep', 3)
    enterState('AIR6DDive')


@State
def StandByAIR6DD():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        Recovery()
    sprite('kg255_02', 4)
    sprite('kg255_03', 4)
    sprite('kg255_04', 4)
    sprite('kg255_05', 4)
    sprite('kg255_02', 6)
    EndYPhysicsImpulse()
    WhiffBlockCancel(1)
    sprite('kg255_01', 6)
    sprite('kg255_00', 6)


@State
def AIR6DDive():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 3)
        EnableCollision(0)

        def upon_STATE_END():
            SLOT_59 = 0
            if SLOT_OverdriveTimer:
                SLOT_60 = 1
                SLOT_61 = 1
    sprite('kg409_04', 2)
    sprite('kg409_05', 2)
    sprite('kg409_06', 1)
    sprite('keep', 1)
    callSubroutine('DiveDirectionSet')
    label(0)
    sprite('kg409_09', 2)
    sprite('kg409_10', 2)
    gotoLabel(0)
    label(1)
    sprite('kg409_07', 2)
    sprite('kg409_08', 2)
    gotoLabel(1)
    label(2)
    sprite('kg409_11', 2)
    sprite('kg409_12', 2)
    gotoLabel(2)
    label(3)
    sprite('kg409_13', 2)
    ForceFaceSprite()
    EndMomentum(1)
    EnableCollision(1)
    LandingEffects(100, 1, 1)
    sprite('kg409_14', 2)
    sprite('kg409_21', 2)
    sprite('kg409_22', 2)
    sprite('kg409_23', 2)
    sprite('kg213_02', 1)
    if SLOT_59 == 1:
        enterState('StandBy6DA')
    if SLOT_59 == 2:
        enterState('StandBy6DB')
    if SLOT_59 == 3:
        enterState('StandBy6DC')


@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        AttackDefaults_NoAttack()
        StayAfterMovement(1, 0)
        RunLoopUpon(17, 61)

        def upon_17():
            WhiffBlockCancel(1)
            WhiffBarrierCancel2(1)
            WhiffSpecialCancel(1)
    sprite('kg300_00', 7)
    sprite('kg300_01', 7)
    sprite('kg300_02', 7)
    sprite('kg300_03', 7)
    if random_(2, 0, 50):
        Voiceline('kg404')
    else:
        Voiceline('kg405')
    sprite('kg300_04', 60)
    sprite('kg300_05', 6)
    sprite('kg300_06', 6)
    sprite('kg300_07', 6)
    sprite('kg300_08', 8)
    sprite('kg300_09', 8)


@State
def NmlAtkDeadAngle():

    def upon_IMMEDIATE():
        AttackDefaults_DeadAngle()
        StayAfterMovement(1, 0)
    sprite('kg211_00', 3)
    sprite('kg211_01', 3)
    sprite('kg211_02', 3)
    sprite('kg211_03', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('kg211_04ex01', 3)
    sprite('kg211_04', 2)
    sprite('kg211_05', 4)
    sprite('kg211_06', 4)
    sprite('kg211_07', 4)
    sprite('kg211_08', 4)
    sprite('kg211_09', 4)
    sprite('kg211_10', 4)
    sprite('kg211_11', 4)


@State
def NmlAtkGuardCrush():

    def upon_IMMEDIATE():
        ScriptSameAttackComboNoSpecialCancel()
        GroundedHitstunAnimation(2)
        Stagger(60)
        Crumple(50)
        AirHitstunAnimation(17)
        AirPushbackX(500)
        AirPushbackY(38000)
        YImpulseBeforeWallbounce(1800)
        AirUntechableTime(60)
        PushbackX(8000)
        Blockstun(24)
        HitBackReturnIgnore(1)
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
    sprite('kg340_00', 3)
    sprite('kg340_00', 1)
    Voiceline('kg159')
    E0EAEffect('GuardCrushWind', 65535)
    CharacterFlash(16750300, 8, 2)
    HeatChange(-2500)
    sprite('kg340_01', 4)
    CharacterFlash(16763080, 8, 2)
    sprite('kg340_02', 3)
    label(100)
    sprite('kg340_03', 3)
    sprite('kg340_04', 3)
    sprite('kg340_05', 3)
    loopRest()
    gotoLabel(100)
    label(0)
    sprite('kg340_03', 3)
    clearUponHandler(EVERY_FRAME)
    sprite('kg340_04', 3)
    sprite('kg340_05', 2)
    sprite('kg340_06', 1)
    PrivateSE('kgse_01')
    sprite('kg340_07', 1)
    CreateObject('efkg_340', -1)
    sprite('kg340_07', 1)
    StartMultihit()
    EnableAfterimage(0)
    sprite('kg340_08', 2)
    sprite('kg340_09', 3)
    sprite('kg340_10', 3)
    sprite('kg340_11', 4)
    sprite('kg340_12', 4)
    sprite('kg340_13', 4)
    sprite('kg340_14', 4)


@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('ThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('kg310_00', 3)
    sprite('kg310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('kg310_02', 3)
    sprite('kg310_03', 3)
    sprite('kg310_04', 3)
    SmartVoiceline('kg155')
    sprite('kg310_05', 7)
    sprite('kg310_06', 5)
    sprite('kg310_07', 5)


@State
def ThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(30000)
        StarterRating(2)
        SpecialCancel(0)
    sprite('kg310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('kg311_00', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('kg311_01', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('kg311_01', 2)
    sprite('kg311_02', 4)
    SmartVoiceline('kg153')
    sprite('kg311_03', 4)
    sprite('kg311_04', 4)
    sprite('kg311_05', 4)
    sprite('kg311_06', 4)
    sprite('kg311_07', 3)
    PrivateSE('kgse_01')
    sprite('kg311_08', 1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1400)
    AttackP2(50)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    UseSlashHitspark(1)
    AirPushbackX(50000)
    AirPushbackY(15000)
    AirHitstunAfterWallbounce(50)
    Wallbounce(1)
    WallbounceReboundTime(18)
    Hitstop(15)
    Wallstick(1)
    WallstickDuration(30)
    CreateObject('efkg_311', -1)
    sprite('kg311_08', 2)
    SpecialCancel(1)
    sprite('kg311_09', 3)
    sprite('kg311_10', 5)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg311_11', 5)
    sprite('kg311_12', 5)
    sprite('kg311_13', 5)
    sprite('kg311_14', 5)


@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('BackThrowExe', 1, 0, 0)
        DistanceCheck(200000, 1, 130000, 0)
    sprite('kg310_00', 3)
    sprite('kg310_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('kg310_02', 3)
    sprite('kg310_03', 3)
    sprite('kg310_04', 3)
    SmartVoiceline('kg155')
    sprite('kg310_05', 7)
    sprite('kg310_06', 5)
    sprite('kg310_07', 5)


@State
def BackThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 0, 0)
        AttackLevel_(0)
        Damage(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(60)
        AirPushbackX(1000)
        AirPushbackY(35000)
        StarterRating(2)
        SpecialCancel(0)
        FlipOnHit(1)
        WhiffCrouchBlockCancel(1)
        IgnoreTurn(1)
    sprite('kg310_02', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('kg313_00', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('kg313_01', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 1)
    sprite('kg313_01', 2)
    sprite('kg313_02', 4)
    sprite('kg313_03', 4)
    sprite('kg313_04', 4)
    SmartVoiceline('kg153')
    sprite('kg311_04', 4)
    Flip()
    sprite('kg311_05', 4)
    sprite('kg311_06', 4)
    sprite('kg311_07', 3)
    ForceFaceSprite()
    PrivateSE('kgse_01')
    sprite('kg311_08', 1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1400)
    AttackP2(50)
    UseSlashHitspark(1)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    UseSlashHitspark(1)
    AirPushbackX(50000)
    AirPushbackY(15000)
    AirHitstunAfterWallbounce(50)
    Wallbounce(1)
    WallbounceReboundTime(15)
    Hitstop(15)
    FlipOnHit(0)
    Wallstick(1)
    WallstickDuration(30)
    CreateObject('efkg_311', -1)
    sprite('kg311_08', 2)
    SpecialCancel(1)
    sprite('kg311_09', 3)
    sprite('kg311_10', 5)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg311_11', 5)
    sprite('kg311_12', 5)
    sprite('kg311_13', 5)
    sprite('kg311_14', 5)


@State
def NmlAtkAirThrow():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('AirThrowExe', 1, 1, 0)
        RangeCheck(120000)
    sprite('kg320_00', 3)
    sprite('kg320_01', 3)
    CommonSE('010_swing_sword_0')
    sprite('kg320_02', 3)
    ForcedLandingRecovery(4, 1)
    sprite('kg320_03', 3)
    sprite('kg320_04', 3)
    SmartVoiceline('kg155')
    sprite('kg320_05', 10)
    sprite('kg320_06', 7)


@State
def AirThrowExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(1, 1, 0)
        AttackLevel_(0)
        Damage(500)
        AttackP1(100)
        AttackP2(50)
        AirPushbackX(7500)
        AirPushbackY(25000)
        AirUntechableTime(60)
        Hitstop(0)
        StarterRating(2)
        SpecialCancel(0)
        ForcedLandingRecovery(0, 0)
        physicsXImpulse(0)
        physicsYImpulse(0)
        setGravity(0)
        SetZLine(0, 50)
        clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 1)
    sprite('kg320_02', 3)
    StartMultihit()
    OppThrowAnimation(9, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    ThrowLock(1)
    sprite('kg321_00', 3)
    sprite('kg321_01', 3)
    physicsXImpulse(2000)
    physicsYImpulse(10000)
    setGravity(500)
    OppThrowAnimation(9, 0)
    sprite('kg321_02', 3)
    SmartVoiceline('kg154')
    sprite('kg321_03', 6)
    sprite('kg321_04', 6)
    sprite('kg321_05', 2)
    sprite('kg321_06', 2)
    AttackLevel_(4)
    Damage(200)
    RefreshMultihit()
    Hitstop(6)
    AirPushbackX(0)
    AirPushbackY(-74000)
    HardKnockdown(10)
    AttackP2(100)
    physicsYImpulse(-70000)
    setGravity(2000)
    sprite('kg321_07', 2)
    label(0)
    sprite('kg321_06', 2)
    sprite('kg321_07', 2)
    gotoLabel(0)
    label(1)
    sprite('kg321_08', 2)
    StartMultihit()
    EndMomentum(1)
    sprite('kg321_08', 1)
    RefreshMultihit()
    Damage(800)
    AirPushbackY(-38000)
    Hitstop(12)
    HardKnockdownReset()
    GroundBounce(1)
    BouncePercentage(100)
    ScreenShake(0, 50000)
    MoveAttributes(0, 1, 0, 0, 0)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg321_08', 2)
    SpecialCancel(1)
    sprite('kg321_09', 3)
    sprite('kg321_10', 3)
    sprite('kg321_11', 4)
    sprite('kg321_12', 4)
    sprite('kg321_13', 4)
    sprite('kg321_14', 4)


@State
def StandBy5DA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        HitOrBlockCancel('StandByFDash')
        HitOrBlockCancel('StandByBDash')
        callSubroutine('InitializeStandByChange')
        SLOT_51 = 1
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AttackP2(89)
        HitAirUnblockable(3)
        GroundedHitstunAnimation(2)
        Stagger(34)
        Crumple(24)
        CHStagger(45)
        CHCrumple(43)
        Blockstun(19)
        AirUntechableTime(33)
        PushbackX(30000)
        FatalCounter(1)
        StarterRating(2)
        AirPushbackX(17500)
        AirPushbackY(30000)
        AirHitstunAfterWallbounce(36)
        Wallbounce(1)
        WallbounceReboundTime(1)
        StayAfterMovement(1, 0)
    sprite('kg400_00', 2)
    sprite('kg400_01', 2)
    Voiceline('kg200')
    sprite('kg400_02', 2)
    physicsXImpulse(50000)
    SetYCollisionFromOrigin(300)
    sprite('kg400_03', 6)
    SetXCollisionFromOrigin(250)
    XImpulseAcceleration(15)
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 0)
    GuardpointBlockUnblockable(0)
    BlockLow(0)
    GuardPoint_(1)
    ArmorChipDamage(50)
    ArmorHealth(3000)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg400_04', 6)
    XImpulseAcceleration(25)
    sprite('kg400_05', 3)
    physicsXImpulse(0)
    CreateParticle('kgef400impact_05', 0)
    AddX(60000)
    ScreenShake(10000, 0)
    CommonSE('213_bound_1')
    sprite('kg400_06', 4)
    setInvincible(0)
    Recovery()
    SetXCollisionFromOrigin(-1)
    sprite('kg400_07', 4)
    sprite('kg400_08', 3)
    sprite('kg400_09', 3)
    sprite('kg400_10', 3)
    sprite('kg400_11', 3)
    PrivateSE('kgse_15')
    sprite('kg400_12', 3)
    sprite('kg400_13', 2)
    sprite('kg400_14', 3)
    sprite('kg400_15', 3)


@State
def StandBy5DB():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('StandBy5DBExe', 2, 0, 0)
        RangeCheck(120000)
        DistanceCheck(250000, 1, -1, -1)
        SameMoveProration(-1)
        callSubroutine('DeleteStandByEffect')
    sprite('kg401_00', 2)
    sprite('kg401_01', 2)
    sprite('kg401_02', 2)
    CommonSE('010_swing_sword_0')
    sprite('kg401_03', 3)
    sprite('kg401_04', 8)
    SmartVoiceline('kg155')
    sprite('kg401_02', 6)
    sprite('kg401_01', 6)
    sprite('kg401_00', 6)
    sprite('kg203_01', 6)
    sprite('kg203_00', 6)


@State
def StandBy5DBExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(0)
        Damage(300)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP1(100)
        AttackP2(90)
        Hitstop(0)
        AirUntechableTime(90)
        AirPushbackX(11000)
        AirPushbackY(32000)
        StarterRating(2)
        Unknown12055(1)
        SLOT_52 = 1
        callSubroutine('InitializeStandByChangeAir')

        def upon_STATE_END():
            if SLOT_63:
                AbsoluteY(150000)
                SLOT_63 = 0
    sprite('kg401_03', 3)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    StartMultihit()
    ThrowLock(1)
    sprite('kg401_05', 1)
    StartMultihit()
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('kg401_05', 3)
    HitOrBlockCancel('ShotA')
    HitOrBlockCancel('ShotB')
    HitOrBlockCancel('AntiAirB')
    HitOrBlockCancel('AntiAirC')
    HitOrBlockCancel('UltimateShot')
    HitOrBlockCancel('UltimateShotOD')
    OppPositionOnHit(1, 100000, 100000)
    sprite('kg401_06', 6)
    Voiceline('kg201')
    sprite('kg401_07', 5)
    sprite('kg401_08', 5)
    sprite('kg401_09', 2)
    sprite('kg401_10', 2)
    sprite('kg401_11', 2)
    SLOT_63 = 1
    AbsoluteY(500)
    setGravity(0)
    sprite('kg401_12', 2)
    sprite('kg401_13', 2)
    CreateObject('401slash00', -1)
    CreateObject('401slash01', -1)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(1200)
    Hitstop(12)
    AirHitstunAnimation(13)
    AirPushbackX(8000)
    AirPushbackY(-100000)
    BouncePercentage(25)
    GroundBounce(1)
    AirUntechableTime(50)
    AttackP2(60)
    SLOT_51 = 1
    OppPositionOnHit(0, 0, 0)
    sprite('kg401_14', 3)
    sprite('kg401_15', 3)
    sprite('kg401_16', 3)
    sprite('kg401_17', 3)
    sprite('kg401_18', 3)
    SLOT_63 = 0
    EndYPhysicsImpulse()
    sprite('kg401_19', 4)
    LandingEffects(100, 1, 1)
    sprite('kg401_20', 4)
    sprite('kg401_21', 4)
    sprite('kg401_22', 4)
    sprite('kg400_10', 4)
    AddX(-120000)
    sprite('kg400_11', 4)
    PrivateSE('kgse_15')
    sprite('kg400_12', 4)
    sprite('kg400_13', 4)
    sprite('kg400_14', 4)
    sprite('kg400_15', 4)


@State
def StandBy5DC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(5)
        Damage(700)
        AttackP1(90)
        AttackP2(84)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(15000)
        PushbackX(20000)
        AirUntechableTime(30)
        UseSlashHitspark(1)
        Hitstop(7)
        HitAirUnblockable(3)
        AttackDirection(0)
        StayAfterMovement(1, 0)
        callSubroutine('InitializeStandByChange')
        setInvincible(1)
        SpecificInvincibility(1, 0, 0, 0, 0)
    sprite('kg402_00', 3)
    sprite('kg402_01', 3)
    sprite('kg402_02', 3)
    sprite('kg402_03', 3)
    Voiceline('kg202')
    sprite('kg402_04', 2)
    physicsXImpulse(20000)
    sprite('kg402_05', 2)
    XImpulseAcceleration(25)
    CreateObject('402slash00', -1)
    PrivateSE('kgse_12')
    sprite('kg402_06', 3)
    XImpulseAcceleration(25)
    sprite('kg402_07', 3)
    sprite('kg402_08', 3)
    physicsXImpulse(10000)
    physicsYImpulse(5000)
    setGravity(2000)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg402_09', 4)
    XImpulseAcceleration(75)
    sprite('kg402_10', 4)
    CreateObject('402slash01', -1)
    XImpulseAcceleration(75)
    PrivateSE('kgse_12')
    sprite('kg402_11', 3)
    SLOT_51 = 1
    physicsXImpulse(0)
    RefreshMultihit()
    Damage(1200)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(-28000)
    AirPushbackY(40000)
    CHAirPushbackX(-45000)
    CHAirPushbackY(25000)
    AirUntechableTime(37)
    ResetPushbackX()
    Hitstop(13)
    Wallstick(1)
    WallstickDuration(17)
    CHWallstickDuration(35)
    Wallbounce(1)
    WallbounceReboundTime(3)
    AirHitstunAfterWallbounce(50)
    NonCornerWallbounce(1)
    CHWallstick(1)
    CHWallbounceReboundTime(35)
    NonCornerCHWallbounce(0)
    if SLOT_55:
        Wallbounce(-1)
        AirUntechableTime(50)
        AirPushbackX(-1000)
        CHAirPushbackX(2500)
    SetYCollisionFromOrigin(100)
    sprite('kg402_12', 4)
    setInvincible(0)
    Recovery()
    callSubroutine('InitializeStandByChangeNoCheck')
    sprite('kg402_13', 4)
    SetYCollisionFromOrigin(180)
    sprite('kg402_14', 4)
    sprite('kg402_15', 4)
    sprite('kg402_16', 6)
    sprite('kg402_17', 6)
    sprite('kg402_18', 6)


@State
def StandBy5DD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        Recovery()
    sprite('keep', 5)
    sprite('kg203_01', 8)
    sprite('kg203_00', 8)


@State
def StandBy2DA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(5)
        Damage(1000)
        AttackP1(90)
        AirPushbackX(4000)
        CHAirPushbackX(3000)
        AirPushbackY(-150000)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        HitOverhead(2)
        GroundBounce(1)
        BouncePercentage(25)
        CHBouncePercentage(25)
        CHHardKnockdown(1)
        StarterRating(2)
        FatalCounter(1)
        YImpulseBeforeWallbounce(0)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        MoveAttributes(1, 0, 0, 0, 0)

        def upon_FALLING():
            clearUponHandler(FALLING)
            setGravity(5000)
            sendToLabel(1)
        uponSendToLabel(LANDING, 2)
        SLOT_51 = 1
        SLOT_53 = 1
        callSubroutine('InitializeStandByChangeAir')

        def upon_PLAYER_DAMAGED():
            if SLOT_63:
                SLOT_63 = 0

        def upon_STATE_END():
            if SLOT_63:
                AbsoluteY(150000)
                SLOT_63 = 0
                ForcedLandingRecovery(6, 1)
    sprite('kg233_02', 3)
    Voiceline('kg203')
    sprite('kg406_00', 3)
    physicsXImpulse(10000)
    physicsYImpulse(22000)
    setGravity(3000)
    JumpEffects(1, 0)
    setInvincible(1)
    SpecificInvincibility(0, 0, 1, 0, 1)
    sprite('kg406_01', 3)
    label(0)
    sprite('kg406_02', 3)
    sprite('kg406_03', 3)
    sprite('kg406_04', 3)
    gotoLabel(0)
    label(1)
    sprite('kg406_05', 3)
    sprite('kg406_06', 32767)
    PrivateSE('kgse_01')
    label(2)
    sprite('kg406_07', 3)
    CreateObject('406slash00', -1)
    EndMomentum(1)
    SetXCollisionFromOrigin(200)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    AbsoluteY(500)
    setGravity(0)
    SLOT_63 = 1
    sprite('kg406_08', 4)
    sprite('kg406_09', 4)
    setInvincible(0)
    Recovery()
    sprite('kg406_10', 4)
    sprite('kg406_11', 3)
    AbsoluteY(0)
    SLOT_63 = 0
    SetXCollisionFromOrigin(-1)
    LandingEffects(100, 1, 1)
    sprite('kg406_12', 5)
    sprite('kg406_13', 5)
    sprite('kg406_14', 5)
    sprite('kg406_15', 5)
    sprite('kg406_16', 5)
    sprite('kg406_17', 5)


@State
def StandBy2DB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-40000)
        PushbackX(10000)
        HardKnockdown(20)
        AirUntechableTime(22)
        UseSlashHitspark(1)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        StayAfterMovement(1, 0)
        EnterStateIfEventID(8, 'CmnActCrouch')
        AttackOff()
        callSubroutine('InitializeStandByChange')

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 400000:
                    XImpulseAcceleration(75)
                    SetActionMark(0)
                    clearUponHandler(EVERY_FRAME)
    sprite('kg407_00', 2)
    physicsXImpulse(12000)
    JumpEffects(1, 0)
    sprite('kg407_01', 2)
    XImpulseAcceleration(450)
    CreateObject('efkg_407', -1)
    CreateParticle('kgef407_b', -1)
    sprite('kg407_02', 2)
    Voiceline('kg204')
    sprite('kg407_03', 2)
    CreateObject('efkg_407', -1)
    sprite('kg407_04', 2)
    SetActionMark(1)
    sprite('kg407_05', 2)
    PrivateSE('kgse_01')
    CreateObject('efkg_407', -1)
    sprite('kg407_06', 3)
    RefreshMultihit()
    XImpulseAcceleration(25)
    SetXCollisionFromOrigin(200)
    sprite('kg407_07', 5)
    CreateObject('efkg_407', -1)
    CreateParticle('kgef407_brake', -1)
    sprite('kg407_09', 5)
    sprite('kg407_10', 2)
    SLOT_51 = 1
    XImpulseAcceleration(0)
    RefreshMultihit()
    Damage(1200)
    AirPushbackX(20000)
    AirPushbackY(9000)
    HitLow(0)
    PushbackX(8000)
    HardKnockdown(0)
    CHAirPushbackX(10000)
    CHHardKnockdown(1)
    if SLOT_55:
        HardKnockdown(1)
    PrivateSE('kgse_01')
    sprite('kg407_11', 2)
    SetInertia(-3000)
    Recovery()
    callSubroutine('InitializeStandByChangeNoCheck')
    sprite('kg407_12', 3)
    SetXCollisionFromOrigin(-1)
    sprite('kg407_13', 3)
    sprite('kg407_14', 3)
    sprite('kg407_15', 3)
    sprite('kg407_16', 2)
    sprite('kg407_17', 2)
    sprite('kg407_18', 2)
    sprite('kg407_19', 2)


@State
def StandBy2DC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(5)
        Damage(600)
        AttackP2(84)
        SingleProration(1)
        UseSlashHitspark(1)
        AirPushbackX(-6500)
        AirPushbackY(20000)
        CHAirPushbackY(13500)
        AirUntechableTime(35)
        Blockstun(25)
        HitAirUnblockable(3)
        StayAfterMovement(1, 0)
        EnterStateIfEventID(8, 'CmnActCrouch')
        PushbackX(-5000)
        Hitstop(7)
        SetYCollisionFromOrigin(300)
        callSubroutine('InitializeStandByChange')
    sprite('kg408_00', 4)
    sprite('kg408_01', 4)
    Voiceline('kg205')
    sprite('kg408_02', 3)
    sprite('kg408_03', 3)
    sprite('kg408_04', 3)
    PrivateSE('kgse_12')
    sprite('kg408_05', 2)
    CreateObject('408slash00', -1)
    sprite('kg408_06', 2)
    sprite('kg408_07', 5)
    sprite('kg408_08', 4)
    sprite('kg408_09', 2)
    sprite('kg408_09', 2)
    physicsXImpulse(10000)
    sprite('kg408_10', 2)
    sprite('kg408_11', 2)
    PrivateSE('kgse_01')
    sprite('kg408_12', 3)
    SLOT_51 = 1
    CreateObject('408slash01', -1)
    RefreshMultihit()
    Damage(1200)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(6)
    AirUntechableTime(40)
    Hitstun(20)
    Hitstop(13)
    PushbackX(30400)
    AttackP1(90)
    HitLow(2)
    MoveAttributes(0, 0, 1, 0, 0)
    Blockstun(20)
    AirPushbackX(8000)
    AirPushbackY(22000)
    CHAirPushbackX(10000)
    CHAirPushbackY(-30000)
    CHHardKnockdown(1)
    physicsXImpulse(0)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    if SLOT_55:
        HardKnockdown(1)
    sprite('kg408_13', 5)
    Recovery()
    callSubroutine('InitializeStandByChangeNoCheck')
    sprite('kg408_14', 5)
    sprite('kg408_15', 5)
    SetXCollisionFromOrigin(200)
    sprite('kg408_16', 5)
    sprite('kg408_17', 5)
    sprite('kg408_18', 2)


@State
def StandBy2DD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        Recovery()
        EnterStateIfEventID(8, 'CmnActCrouch')
    sprite('keep', 5)
    sprite('kg233_01', 8)
    sprite('kg233_00', 8)


@State
def StandBy6DA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(4)
        Damage(850)
        AttackP1(90)
        AttackP2(82)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(7000)
        CHAirPushbackX(9000)
        AirPushbackY(-55000)
        AirUntechableTime(45)
        GroundBounce(1)
        BouncePercentage(50)
        FatalCounter(1)
        UseSlashHitspark(1)
        AttackDirection(0)
        StayAfterMovement(1, 0)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 400000:
                    sendToLabel(0)
        callSubroutine('InitializeStandByChange')
        SLOT_51 = 1
    sprite('kg403_00', 2)
    physicsXImpulse(10000)
    AirDashEffects(1)
    setInvincible(1)
    SpecificInvincibility(0, 1, 0, 0, 0)
    sprite('kg403_01', 2)
    SetActionMark(1)
    XImpulseAcceleration(400)
    sprite('kg403_00', 2)
    DashEffects(100, 1, 1)
    sprite('kg403_01', 2)
    DashEffects(100, 1, 1)
    sprite('kg403_00', 2)
    DashEffects(100, 1, 1)
    sprite('kg403_01', 2)
    DashEffects(100, 1, 1)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('kg403_02', 4)
    XImpulseAcceleration(15)
    SetXCollisionFromOrigin(180)
    sprite('kg403_03', 3)
    sprite('kg403_04', 3)
    sprite('kg403_05', 3)
    sprite('kg403_06', 3)
    sprite('kg403_07', 3)
    sprite('kg403_08', 3)
    Voiceline('kg206')
    PrivateSE('kgse_01')
    sprite('kg403_09', 3)
    setInvincible(0)
    CreateObject('403slash00', -1)
    XImpulseAcceleration(0)
    sprite('kg403_10', 2)
    Recovery()
    sprite('kg403_11', 2)
    sprite('kg403_12', 2)
    sprite('kg403_13', 4)
    sprite('kg403_14', 4)
    sprite('kg403_15', 4)
    sprite('kg403_16', 4)


@State
def StandBy6DB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(4)
        Damage(900)
        AttackP1(90)
        AttackP2(82)
        AirPushbackX(1500)
        AirPushbackY(-40000)
        PushbackX(-15000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        UseSlashHitspark(1)
        HardKnockdown(12)
        StayAfterMovement(1, 0)
        StarterRating(2)
        CHGroundedHitstunAnimation(9)
        CHHardKnockdown(1)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 400000:
                    sendToLabel(0)
        SLOT_63 = 0

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_63 = 1

        def upon_STATE_END():
            SetInertia(0)
            AlphaValue(255)
            ConstantAlphaModifier(0)
            if SLOT_63:
                ForceFaceSprite()
                SLOT_63 = 0
            else:
                Flip()
        callSubroutine('InitializeStandByChange')
        SLOT_51 = 1
    sprite('kg403_00', 2)
    physicsXImpulse(10000)
    AirDashEffects(1)
    setInvincible(1)
    SpecificInvincibility(0, 1, 0, 0, 0)
    sprite('kg403_01', 2)
    SetActionMark(1)
    XImpulseAcceleration(400)
    sprite('kg403_00', 2)
    DashEffects(100, 1, 1)
    sprite('kg403_01', 2)
    DashEffects(100, 1, 1)
    sprite('kg403_00', 2)
    DashEffects(100, 1, 1)
    sprite('kg403_01', 2)
    DashEffects(100, 1, 1)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('kg403_02', 4)
    XImpulseAcceleration(15)
    sprite('kg403_03', 2)
    setInvincible(0)
    sprite('kg403_04', 2)
    Voiceline('kg207')
    sprite('kg403_05', 3)
    sprite('kg403_06', 3)
    sprite('kg403_07', 7)
    CreateObject('403Zanzo', -1)
    AlphaValue(255)
    ConstantAlphaModifier(-42)
    setInvincible(1)
    SpecificInvincibility(1, 1, 1, 1, 1)
    sprite('kg403_08', 1)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    EnableCollision(0)
    JumpEffects(1, 0)
    sprite('kg404_00', 3)
    ConstantAlphaModifier(42)
    XImpulseAcceleration(25)
    AddX(600000)
    SetInertia(60000)
    SetXCollisionFromOrigin(5)
    sprite('kg404_01', 2)
    sprite('kg404_02', 2)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    PrivateSE('kgse_01')
    setInvincible(0)
    sprite('kg404_03', 3)
    CreateObject('404slash00', -1)
    XImpulseAcceleration(0)
    EnableCollision(1)
    SetXCollisionFromOrigin(-1)
    sprite('kg404_04', 3)
    Recovery()
    sprite('kg404_05', 3)
    sprite('kg404_06', 3)
    sprite('kg404_07', 3)
    sprite('kg404_08', 3)
    SetInertia(0)
    sprite('kg404_09', 3)
    sprite('kg404_10', 3)
    sprite('kg404_11', 3)


@State
def StandBy6DC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        callSubroutine('InitializeStandByChainAttack')
        AttackLevel_(5)
        Damage(1200)
        AttackP1(80)
        AttackP2(84)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(35000)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Floorslide(26)
        StarterRating(2)
        UseSlashHitspark(1)
        AttackDirection(0)
        StayAfterMovement(1, 0)
        HitAirUnblockable(0)
        CHWallbounce(1)
        CHWallstick(0)
        CHAirPushbackY(25000)
        CHAirHitstunAfterWallbounce(40)
        CHWallbounceReboundTime(30)
        SLOT_58 = 0

        def upon_EVERY_FRAME():
            if SLOT_58:
                if SLOT_19 < 400000:
                    sendToLabel(0)
        if SLOT_55:
            AirUntechableTime(32)
            Floorslide(12)
        callSubroutine('InitializeStandByChange')
        SLOT_51 = 1
    sprite('kg405_00', 2)
    Voiceline('kg208')
    CreateObject('405Slash', -1)
    CommonSE('000_airdash_1')
    sprite('kg405_01', 2)
    sprite('kg405_02', 2)
    physicsXImpulse(6000)
    AddX(50000)
    sprite('kg405_03', 3)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    GuardpointBlockUnblockable(0)
    GuardPoint_(1)
    ArmorChipDamage(0)
    GuardpointHitstop(3, -1)
    XImpulseAcceleration(200)
    sprite('kg405_04', 2)
    XImpulseAcceleration(200)
    sprite('kg405_05', 2)
    SLOT_58 = 1
    sprite('kg405_04', 2)
    sprite('kg405_05', 2)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('kg405_06', 2)
    JumpEffects(1, 0)
    DashEffects(100, 1, 1)
    TriggerUponForState('405Slash', 32)
    XImpulseAcceleration(250)
    PrivateSE('kgse_12')
    sprite('kg405_07', 2)
    sprite('kg405_08', 2)
    XImpulseAcceleration(75)
    sprite('kg405_09', 4)
    setInvincible(0)
    XImpulseAcceleration(50)
    Recovery()
    sprite('kg405_10', 4)
    XImpulseAcceleration(50)
    sprite('kg405_11', 4)
    XImpulseAcceleration(50)
    sprite('kg405_12', 4)
    XImpulseAcceleration(0)
    sprite('kg405_13', 5)
    sprite('kg405_14', 5)


@State
def StandBy6DD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('DeleteStandByEffect')
        PreventBlocking(1)
        Recovery()
    sprite('keep', 5)
    sprite('kg213_01', 8)
    sprite('kg213_00', 8)


@State
def StandByFDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        WhiffCancel('NmlAtk5D')
        WhiffCancel('NmlAtk2D')
        WhiffCancel('NmlAtk6D')
    sprite('kg032_00', 2)
    sprite('kg032_01', 2)
    sprite('kg032_02', 1)
    physicsXImpulse(8000)
    sprite('kg032_02', 2)
    XImpulseAcceleration(400)
    sprite('kg032_03', 3)
    XImpulseAcceleration(150)
    sprite('kg032_10', 3)
    XImpulseAcceleration(30)
    LandingEffects(100, 1, 1)
    sprite('kg032_11', 3)
    sprite('kg032_12', 3)
    WhiffCancelEnable(1)
    XImpulseAcceleration(50)
    sprite('kg032_13', 3)
    XImpulseAcceleration(0)


@State
def StandByBDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        WhiffCancel('NmlAtk5D')
        WhiffCancel('NmlAtk2D')
        WhiffCancel('NmlAtk6D')
        setInvincible(1)
    sprite('kg033_00', 3)
    sprite('kg033_01', 3)
    sprite('kg033_02', 1)
    AddX(-20000)
    physicsXImpulse(-3000)
    sprite('kg033_02', 2)
    XImpulseAcceleration(400)
    sprite('kg033_03', 3)
    XImpulseAcceleration(150)
    setInvincible(0)
    sprite('kg033_04', 3)
    XImpulseAcceleration(30)
    LandingEffects(100, 1, 1)
    sprite('kg033_05', 3)
    sprite('kg033_06', 3)
    WhiffCancelEnable(1)
    XImpulseAcceleration(50)
    sprite('kg033_07', 2)
    XImpulseAcceleration(50)
    sprite('kg033_08', 2)
    physicsXImpulse(0)


@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Hitstop(2)
        AirPushbackX(2500)
        AirPushbackY(2500)
        PreventGroundedHit(1)
        CrouchWhiff(1)
        ForceFaceSprite()
    sprite('kg410_08', 2)
    TriggerUponForState('ChargeTameAura', 32)
    CreateObject('ChargeTameFinFast', -1)
    CommonSE('015_blaze_1')
    CommonSE('015_blaze_1')
    sprite('kg410_09', 3)
    sprite('kg410_10', 3)
    Voiceline('kg209')
    sprite('kg410_11', 2)
    sprite('kg410_12', 2)
    CreateObject('ShotObj', -1)
    RegisterObject(4, 1)
    sprite('kg410_13', 4)
    sprite('kg410_14', 4)
    sprite('kg410_15', 4)
    sprite('kg410_16', 4)
    Recovery()
    sprite('kg410_17', 4)
    sprite('kg410_18', 4)


@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Hitstop(2)
        AirPushbackX(2500)
        AirPushbackY(2500)
        PreventGroundedHit(1)
        CrouchWhiff(1)
        ForceFaceSprite()

        def upon_17():
            clearUponHandler(17)
            AltKnockdownEffects(100, 1, 0)
            sendToLabel(1)
    sprite('kg410_00', 2)
    sprite('kg410_01', 2)
    CreateObject('ChargeTameAura', -1)
    RunLoopUpon(17, 13)
    sprite('kg410_02', 3)
    AttackOff()
    label(0)
    sprite('kg410_03', 3)
    CreateObject('ChargeTameJizoku', -1)
    sprite('kg410_04', 3)
    sprite('kg410_05', 3)
    sprite('kg410_02', 3)
    gotoLabel(0)
    label(1)
    sprite('kg410_06', 2)
    TriggerUponForState('ChargeTameAura', 32)
    CreateObject('ChargeTameFin', -1)
    clearUponHandler(17)
    sprite('kg410_07', 4)
    sprite('kg410_08', 4)
    CommonSE('015_blaze_1')
    CommonSE('015_blaze_1')
    sprite('kg410_09', 3)
    Voiceline('kg210')
    sprite('kg410_10', 3)
    sprite('kg410_11', 2)
    sprite('kg410_12', 2)
    CreateObject('ChargeShotObj', -1)
    RegisterObject(4, 1)
    sprite('kg410_13', 3)
    sprite('kg410_14', 3)
    sprite('kg410_15', 3)
    sprite('kg410_16', 3)
    Recovery()
    sprite('kg410_17', 3)
    sprite('kg410_18', 3)


@State
def ShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Hitstop(2)
        AirPushbackX(2500)
        AirPushbackY(2500)
        PreventGroundedHit(1)
        CrouchWhiff(1)

        def upon_17():
            clearUponHandler(17)
            AltKnockdownEffects(100, 1, 0)
            sendToLabel(1)
    sprite('kg410_00', 2)
    sprite('kg410_01', 2)
    CreateObject('ChargeTameAura', -1)
    RunLoopUpon(17, 13)
    sprite('kg410_02', 3)
    AttackOff()
    label(0)
    sprite('kg410_03', 3)
    CreateObject('ChargeTameJizoku', -1)
    sprite('kg410_04', 3)
    sprite('kg410_05', 3)
    sprite('kg410_02', 3)
    gotoLabel(0)
    label(1)
    sprite('kg410_06', 2)
    TriggerUponForState('ChargeTameAura', 32)
    CreateObject('ChargeTameFin', -1)
    clearUponHandler(17)
    sprite('kg410_07', 4)
    sprite('kg410_08', 4)
    CommonSE('015_blaze_1')
    CommonSE('015_blaze_1')
    sprite('kg410_09', 3)
    Voiceline('kg209')
    sprite('kg410_10', 3)
    sprite('kg410_11', 2)
    sprite('kg410_12', 2)
    CreateObject('ChargeShotObj', -1)
    RegisterObject(4, 1)
    sprite('kg410_13', 4)
    sprite('kg410_14', 4)
    sprite('kg410_15', 4)
    sprite('kg410_16', 3)
    Recovery()
    sprite('kg410_17', 3)
    sprite('kg410_18', 3)


@State
def AntiAirB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        StarterRating(0)
        AirBlockstun(6)
        AirPushbackX(6000)
        AirPushbackY(39000)
        AirUntechableTime(48)
        CHAirPushbackX(5000)
        CHAirPushbackY(40000)
        CHAirUntechableTime(50)
        Hitstop(2)
        Blockstun(20)
        PushbackX(40000)
        DamageEffect(2, 'efkg_slash')
        ForcedLandingRecovery(3, 1)
        ForceFaceSprite()
        AttackDirection(0)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            Damage(700)
            if SLOT_137:
                DamageMultiplier(80)
            if SLOT_2:
                Damage(300)
                if SLOT_137:
                    DamageMultiplier(80)
            AddActionMark(1)
        setInvincible(1)
        SpecificInvincibility(1, 0, 0, 0, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1

        def upon_EVERY_FRAME():
            if SLOT_51:
                HitAirUnblockable(0)
        BeginBuffer('AirAssaultChain')
    sprite('kg411_00', 3)
    sprite('kg411_01', 3)
    Voiceline('kg211')
    sprite('kg411_02', 3)
    JumpEffects(2, 100)
    sprite('kg411_03', 3)
    StartMultihit()
    CommonSE('006_swing_blade_2')
    PrivateSE('kgse_01')
    CreateObject('efkg_411', -1)
    sprite('kg411_04', 3)
    physicsXImpulse(10000)
    physicsYImpulse(45000)
    setGravity(2100)
    PrivateSE('kgse_12')
    uponSendToLabel(LANDING, 1)
    RefreshMultihit()
    YSpeed(-20000)
    sprite('kg411_04', 2)
    RefreshMultihit()
    CrouchWhiff(1)
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_05', 3)
    setInvincible(0)
    if SLOT_2:
        BufferedOrPressedGoto('AirAssaultChain')
    sprite('kg411_06', 5)
    sprite('kg411_07', 3)
    XImpulseAcceleration(40)
    sprite('kg411_08', 3)
    sprite('kg411_09', 3)
    label(0)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('kg024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('kg024_01', 3)
    sprite('kg024_02', 3)
    sprite('kg024_03', 2)
    sprite('kg024_04', 2)


@State
def AntiAirC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        AttackP1(60)
        AttackP2(82)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        StarterRating(0)
        AirUntechableTime(35)
        AirPushbackX(-17500)
        AirPushbackY(35000)
        UseSlashHitspark(1)
        AttackDirection(0)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        EnemyHitstopAddition(0, 0, 0)
        Hitstop(15)
        PushbackX(10000)
        ForceFaceSprite()
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            Damage(900)
            if SLOT_2:
                Damage(200)
            AddActionMark(1)
        setInvincible(1)

        def upon_STATE_END():
            EndYPhysicsImpulse()
        BeginBuffer('AirAssaultChain')
    sprite('kg411_00', 2)
    sprite('kg411_01', 2)
    sprite('kg411_02', 1)
    Voiceline('kg212')
    physicsXImpulse(40000)
    DashEffects(100, 1, 1)
    sprite('kg411_02', 3)
    CreateObject('efkg_411Sub01', -1)
    XImpulseAcceleration(25)
    sprite('kg411_03', 2)
    CommonSE('006_swing_blade_2')
    PrivateSE('kgse_01')
    CreateObject('efkg_411', -1)
    JumpEffects(2, 100)
    XImpulseAcceleration(25)
    sprite('kg411_04', 1)
    StartMultihit()
    physicsYImpulse(120000)
    physicsXImpulse(4000)
    setGravity(1800)
    PrivateSE('kgse_12')
    uponSendToLabel(LANDING, 1)
    sprite('kg411_04', 2)
    CreateObject('efkg_411Sub00', -1)
    StartMultihit()
    physicsYImpulse(60000)
    sprite('kg411_04', 2)
    AttackLevel_(4)
    YSpeed(-25000)
    RefreshMultihit()
    Hitstop(1)
    AirPushbackX(4000)
    AirPushbackY(70000)
    HitsparkSize(500)
    HitAirUnblockable(0)
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_04', 2)
    RefreshMultihit()
    AirPushbackX(2500)
    AirPushbackY(32000)
    CHAirPushbackX(4500)
    CHAirPushbackY(45000)
    AirHitstunAnimation(13)
    sprite('kg411_05', 3)
    setGravity(1800)
    setInvincible(0)
    if SLOT_2:
        BufferedOrPressedGoto('AirAssaultChain')
    sprite('kg411_06', 3)
    sprite('kg411_07', 4)
    setGravity(2500)
    XImpulseAcceleration(40)
    sprite('kg411_08', 4)
    sprite('kg411_09', 4)
    label(0)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('kg024_00', 4)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('kg024_01', 4)
    sprite('kg024_02', 4)
    sprite('kg024_03', 4)
    sprite('kg024_04', 4)


@State
def AirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(1200)
        if SLOT_137:
            DamageMultiplier(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        HitOverhead(2)
        AirUntechableTime(40)
        AttackP1(90)
        AttackP2(82)
        StarterRating(2)
        AirPushbackX(15000)
        AirPushbackY(-40000)
        UseSlashHitspark(1)
        GroundBounce(1)
        BouncePercentage(14)
        HardKnockdown(10)
        ForcedLandingRecovery(9, 1)
        EndMomentum(1)
    sprite('kg412_00', 4)
    physicsYImpulse(1000)
    setGravity(50)
    sprite('kg412_01', 3)
    sprite('kg412_02', 3)
    sprite('kg412_03', 2)
    physicsXImpulse(-2500)
    physicsYImpulse(19000)
    EndYPhysicsImpulse()
    Voiceline('kg213')
    sprite('kg412_04', 3)
    CreateObject('efkg_412SlashEff', -1)
    PrivateSE('kgse_12')
    sprite('kg412_05', 3)
    Recovery()
    sprite('kg412_06', 3)
    sprite('kg412_07', 3)
    sprite('kg412_08', 3)
    sprite('kg412_09', 3)
    sprite('kg412_10', 3)
    label(0)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(0)


@State
def AirAssaultChain():

    def upon_IMMEDIATE():
        AttackDefaults_AirSpecial()
        AttackLevel_(4)
        Damage(1200)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        HitOverhead(2)
        AirUntechableTime(40)
        AttackP1(90)
        StarterRating(2)
        AirPushbackX(25000)
        AirPushbackY(-60000)
        HardKnockdown(10)
        UseSlashHitspark(1)
        ForcedLandingRecovery(9, 1)
        ForceFaceSprite()
        EndMomentum(1)
    sprite('kg412_00', 3)
    physicsYImpulse(12000)
    setGravity(100)
    sprite('kg412_01', 3)
    sprite('kg412_02', 5)
    sprite('kg412_03', 2)
    physicsYImpulse(15000)
    setGravity(3000)
    Voiceline('kg214')
    sprite('kg412_04ex00', 5)
    CreateObject('efkg_412SlashEff', -1)
    physicsXImpulse(-5000)
    PrivateSE('kgse_12')
    sprite('kg412_05', 5)
    Recovery()
    XImpulseAcceleration(50)
    sprite('kg412_06', 5)
    sprite('kg412_07', 5)
    sprite('kg412_08', 5)
    sprite('kg412_09', 5)
    sprite('kg412_10', 5)
    label(0)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(0)


@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        ForceFaceSprite()
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
    sprite('kg430_00', 3)
    Voiceline('kg250')
    DistortionSettings(62, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg430_01', 3)
    sprite('kg430_02', 3)
    sprite('kg430_03', 3)
    sprite('kg430_04', 3)
    sprite('kg430_01', 3)
    sprite('kg430_02', 3)
    sprite('kg430_03', 3)
    sprite('kg430_04', 3)
    sprite('kg430_05', 5)
    sprite('kg430_06', 5)
    sprite('kg430_07', 5)
    sprite('kg430_08', 5)
    sprite('kg430_09', 5)
    Voiceline('kg251')
    sprite('kg430_10', 5)
    setInvincible(0)
    sprite('kg430_11', 2)
    CreateObject('UltimateShotImpact', -1)
    sprite('kg430_12', 6)
    CreateObject('UltimateShotMaster', -1)
    sprite('kg430_13', 6)
    sprite('kg430_14', 8)
    sprite('kg430_15', 8)
    sprite('kg430_16', 5)
    sprite('kg430_17', 4)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 0)
    sprite('kg430_18', 4)
    sprite('kg430_19', 4)
    sprite('kg430_17', 4)
    sprite('kg430_18', 4)
    sprite('kg430_19', 4)
    sprite('kg430_20', 5)


@State
def UltimateShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        ForceFaceSprite()
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
        AttackOff()
        SetActionMark(0)

        def upon_32():
            AddActionMark(1)
    sprite('kg430_00', 3)
    DistortionSettings(62, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    Voiceline('kg250')
    sprite('kg430_01', 3)
    sprite('kg430_02', 3)
    sprite('kg430_03', 3)
    sprite('kg430_04', 3)
    sprite('kg430_01', 3)
    sprite('kg430_02', 3)
    sprite('kg430_03', 3)
    sprite('kg430_04', 3)
    sprite('kg430_05', 5)
    sprite('kg430_06', 5)
    sprite('kg430_07', 5)
    sprite('kg430_08', 5)
    sprite('kg430_09', 5)
    Voiceline('kg251')
    sprite('kg430_10', 5)
    setInvincible(0)
    sprite('kg430_11', 2)
    CreateObject('UltimateShotImpact', -1)
    sprite('kg430_12', 13)
    CreateObject('UltimateShotMasterOD', -1)
    sprite('kg430_13', 13)
    sprite('kg430_14', 8)
    sprite('kg430_15', 8)
    sprite('keep', 1)
    if SLOT_2:
        enterState('UltimateShotODAddAttack')
    sprite('kg430_16', 2)
    sprite('kg430_17', 2)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 0)
    sprite('kg430_18', 2)
    sprite('kg430_19', 2)
    sprite('kg430_17', 2)
    sprite('kg430_18', 2)
    sprite('kg430_19', 2)
    sprite('kg430_20', 5)
    ExitState()


@State
def UltimateShotODAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackOff()
        CHStateIfCHStart(3)
    sprite('kg450_00', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    DistortionSettings(51, -1, 0)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg450_01', 3)
    RandomVoiceline('kg252', 100, 'kg252', 100, 'kg253', 100, 'kg253', 100)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_04', 3)
    PrivateSE('kgse_11')
    sprite('kg450_05', 3)
    sprite('kg450_06', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('kg450_07', 4)
    Voiceline('kg254')
    CreateObject('UltimateShotObjODAdd', -1)
    PrivateSE('kgse_06')
    sprite('kg450_08', 4)
    sprite('kg450_09', 4)
    sprite('kg450_10', 4)
    PrivateSE('kgse_11')
    sprite('kg450_11', 4)
    sprite('kg450_12', 4)
    sprite('kg450_13', 4)
    CreateObject('UltimateShotObjODAdd', -1)
    PrivateSE('kgse_06')
    sprite('kg450_14', 8)
    sprite('kg450_15', 8)
    sprite('kg450_16', 8)
    sprite('kg450_17', 8)
    sprite('kg450_18', 8)
    sprite('kg400_14', 8)
    sprite('kg400_15', 8)


@State
def UltimateStandByLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        ForceFaceSprite()
    sprite('kg431_00', 5)
    Voiceline('kg255')
    DistortionSettings(52, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg431_01', 5)
    sprite('kg431_02', 5)
    sprite('kg431_03', 5)
    sprite('kg431_04', 5)
    sprite('kg431_05', 5)
    sprite('kg431_06', 3)
    CreateObject('ImpactAuraMato', -1)
    PrivateSE('kgse_07')
    sprite('kg431_07', 3)
    sprite('kg431_08', 3)
    sprite('kg431_09', 3)
    sprite('kg431_10', 3)
    sprite('kg431_06', 3)
    sprite('kg431_07', 3)
    sprite('kg431_08', 3)
    sprite('kg431_09', 3)
    sprite('kg431_10', 3)
    TriggerUponForState('ImpactAuraMato', 32)
    enterState('UltimateStandByExe')


@State
def UltimateStandByAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        ForceFaceSprite()

        def upon_LANDING():
            enterState('UltimateStandByExe')
    sprite('kg431_20', 5)
    Voiceline('kg255')
    EndMomentum(1)
    physicsXImpulse(-1000)
    physicsYImpulse(500)
    DistortionSettings(48, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg431_21', 5)
    sprite('kg431_22', 3)
    CreateObject('ImpactAuraMatoAir', -1)
    PrivateSE('kgse_07')
    sprite('kg431_23', 3)
    sprite('kg431_24', 3)
    sprite('kg431_22', 3)
    sprite('kg431_23', 3)
    sprite('kg431_24', 3)
    sprite('kg431_25', 3)
    TriggerUponForState('ImpactAuraMatoAir', 32)
    physicsXImpulse(3000)
    physicsYImpulse(20000)
    setGravity(3000)
    sprite('kg431_26', 3)
    TriggerUponForState('ImpactAuraMatoAir', 33)
    sprite('kg431_27', 3)
    sprite('kg431_28', 3)
    label(0)
    sprite('kg431_26', 3)
    sprite('kg431_27', 3)
    sprite('kg431_28', 3)
    gotoLabel(0)


@State
def UltimateStandByExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(5)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(84)
        StarterRating(2)
        DefeatOpponentBehavior(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        HitAirUnblockable(3)
        EnemyHitstopAddition(0, 30, 30)

        def upon_OPPONENT_HIT():
            enterState('UltimateStandByAddAttack')
        SLOT_4 = 1
    sprite('kg431_11', 2)
    CreateObject('406Rock', -1)

    def RunOnObject_1():
        Flip()
        AddX(-350000)
        AddScale(300)
    sprite('kg431_12', 2)
    PrivateSE('kgse_01')
    sprite('kg431_13', 3)
    CreateObject('ImpactFirstShock', -1)
    ScreenShake(0, 40000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    CreateObject('efkg_431_splash', -1)
    sprite('kg431_14', 3)
    setInvincible(0)
    AttackOff()
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_17', 6)
    sprite('kg431_18', 6)
    sprite('kg431_19', 6)
    sprite('kg400_12', 6)
    sprite('kg400_13', 6)
    sprite('kg400_14', 6)
    sprite('kg400_15', 6)


@State
def UltimateStandByAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(5)
        Damage(5000)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP2(50)
        MinimumDamage(20)
        AirUntechableTime(90)
        Hitstop(2)
        HardKnockdown(10)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(2000)
        AirPushbackY(60000)
        DamageFromStateOnly('UltimateStandByAddAttack')
        DamageEffect(4, 'kgef_431hit_02')
        CHStateIfCHStart(3)
        UseFireHitspark(1)
        EnableCollision(0)
        OnlyHitPlayer(1)
        AttackOff()
        SetZLine(0, 50)
        EnableRapidCancel(0)
        SLOT_4 = 1
        if SLOT_19 >= 500000:

            def RunOnObject_22():
                TeleportToObject(22)
                AddX(-500000)
    sprite('kg431_14', 3)
    Voiceline('kg256')
    CreateObject('UltimateImpactHibasira', -1)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    PrivateSE('kgse_08')
    CommonSE('016_explode_2')
    RefreshMultihit()
    TriggerUponForState('UltimateImpactHibasira', 32)
    EnableCollision(1)
    sprite('kg431_14', 3)
    setInvincible(0)
    AttackOff()
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_17', 6)
    sprite('kg431_18', 6)
    sprite('kg431_19', 6)
    sprite('kg400_12', 6)
    sprite('kg400_13', 6)
    sprite('kg400_14', 6)
    sprite('kg400_15', 6)


@State
def UltimateStandByLandOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        ForceFaceSprite()
    sprite('kg431_00', 5)
    Voiceline('kg255')
    DistortionSettings(52, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg431_01', 5)
    sprite('kg431_02', 5)
    sprite('kg431_03', 5)
    sprite('kg431_04', 5)
    sprite('kg431_05', 5)
    sprite('kg431_06', 3)
    CreateObject('ImpactAuraMato', -1)
    PrivateSE('kgse_07')
    sprite('kg431_07', 3)
    sprite('kg431_08', 3)
    sprite('kg431_09', 3)
    sprite('kg431_10', 3)
    sprite('kg431_06', 3)
    sprite('kg431_07', 3)
    sprite('kg431_08', 3)
    sprite('kg431_09', 3)
    sprite('kg431_10', 3)
    enterState('UltimateStandByODExe')


@State
def UltimateStandByAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        ForceFaceSprite()

        def upon_LANDING():
            enterState('UltimateStandByODExe')
    sprite('kg431_20', 5)
    Voiceline('kg255')
    EndMomentum(1)
    physicsXImpulse(-1000)
    physicsYImpulse(500)
    DistortionSettings(48, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg431_21', 5)
    sprite('kg431_22', 3)
    CreateObject('ImpactAuraMatoAir', -1)
    PrivateSE('kgse_07')
    sprite('kg431_23', 3)
    sprite('kg431_24', 3)
    sprite('kg431_22', 3)
    sprite('kg431_23', 3)
    sprite('kg431_24', 3)
    sprite('kg431_25', 3)
    TriggerUponForState('ImpactAuraMatoAir', 32)
    physicsXImpulse(3000)
    physicsYImpulse(20000)
    setGravity(3000)
    sprite('kg431_26', 3)
    TriggerUponForState('ImpactAuraMatoAir', 33)
    sprite('kg431_27', 3)
    sprite('kg431_28', 3)
    label(0)
    sprite('kg431_26', 3)
    sprite('kg431_27', 3)
    sprite('kg431_28', 3)
    gotoLabel(0)


@State
def UltimateStandByODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(5)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(84)
        StarterRating(2)
        DefeatOpponentBehavior(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        HitAirUnblockable(3)
        EnemyHitstopAddition(0, 30, 30)

        def upon_OPPONENT_HIT():
            enterState('UltimateStandByODAddAttack')
        SLOT_4 = 1
    sprite('kg431_11', 2)
    sprite('kg431_12', 2)
    PrivateSE('kgse_01')
    sprite('kg431_13', 3)
    CreateObject('ImpactFirstShock', -1)
    ScreenShake(0, 40000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    sprite('kg431_14', 3)
    setInvincible(0)
    AttackOff()
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_17', 6)
    sprite('kg431_18', 6)
    sprite('kg431_19', 6)
    sprite('kg400_12', 6)
    sprite('kg400_13', 6)
    sprite('kg400_14', 6)
    sprite('kg400_15', 6)


@State
def UltimateStandByODAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        AttackLevel_(5)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        AttackType(4)
        DefeatOpponentBehavior(1)
        AttackP2(50)
        SingleProration(1)
        MinimumDamage(10)
        Hitstop(2)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(7000)
        DamageFromStateOnly('UltimateStandByODAddAttack')
        DamageEffect(4, 'kgef_431hit_02')
        CHStateIfCHStart(3)
        UseFireHitspark(1)
        EnableCollision(0)
        OnlyHitPlayer(1)
        AttackOff()
        SetZLine(0, 50)
        EnableRapidCancel(0)
        SLOT_4 = 1
        if SLOT_19 >= 500000:

            def RunOnObject_22():
                TeleportToObject(22)
                AddX(-500000)
    sprite('kg431_14', 3)
    Voiceline('kg256')
    CreateObject('UltimateImpactHibasira', -1)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    ScreenShake(20000, 0)
    RefreshMultihit()
    PrivateSE('kgse_08')
    sprite('kg431_15', 3)
    RefreshMultihit()
    sprite('kg431_16', 3)
    RefreshMultihit()
    sprite('kg431_14', 3)
    ScreenShake(20000, 0)
    RefreshMultihit()
    sprite('kg431_15', 3)
    RefreshMultihit()
    sprite('kg431_16', 3)
    RefreshMultihit()
    sprite('kg431_14', 3)
    ScreenShake(20000, 0)
    RefreshMultihit()
    sprite('kg431_15', 3)
    RefreshMultihit()
    sprite('kg431_16', 3)
    RefreshMultihit()
    sprite('kg431_14', 3)
    ScreenShake(20000, 0)
    RefreshMultihit()
    sprite('kg431_15', 3)
    RefreshMultihit()
    sprite('kg431_16', 3)
    RefreshMultihit()
    sprite('kg431_14', 3)
    ScreenShake(20000, 0)
    RefreshMultihit()
    sprite('kg431_15', 3)
    RefreshMultihit()
    sprite('kg431_16', 3)
    RefreshMultihit()
    sprite('kg431_14', 3)
    ScreenShake(20000, 0)
    RefreshMultihit()
    sprite('kg431_15', 3)
    RefreshMultihit()
    sprite('kg431_16', 3)
    RefreshMultihit()
    sprite('kg431_14', 3)
    Voiceline('kg257')
    ScreenShake(50000, 50000)
    RefreshMultihit()
    Damage(3000)
    if SLOT_137:
        DamageMultiplier(80)
    MinimumDamage(15)
    Hitstop(40)
    DefeatOpponentBehavior(0)
    GroundedHitstunAnimation(18)
    AirHitstunAnimation(18)
    AirUntechableTime(80)
    ResetPushbackX()
    AirPushbackX(1500)
    AirPushbackY(50000)
    HardKnockdown(10)
    TriggerUponForState('UltimateImpactHibasira', 32)
    EnableCollision(1)
    sprite('kg431_14', 3)
    setInvincible(0)
    AttackOff()
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_14', 3)
    sprite('kg431_15', 3)
    sprite('kg431_16', 3)
    sprite('kg431_17', 6)
    sprite('kg431_18', 6)
    sprite('kg431_19', 6)
    sprite('kg400_12', 6)
    sprite('kg400_13', 6)
    sprite('kg400_14', 6)
    sprite('kg400_15', 6)


@State
def UltimateAntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(3)
        Damage(400)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(25000)
        AirPushbackX(7500)
        Hitstop(5)
        AirUntechableTime(50)
        Blockstun(35)
        DamageEffect(2, 'efkg_slash')
        uponSendToLabel(LANDING, 1)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        AttackDirection(0)
        setInvincible(1)
    sprite('kg411_00', 2)
    DistortionSettings(32, -1, 0)
    HeatChange(-5000)
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG', -1)
    sprite('kg411_01', 30)
    sprite('kg411_02', 2)
    JumpEffects(3, 100)
    sprite('kg411_03', 2)
    CommonSE('006_swing_blade_2')
    CommonSE('011_spin_0')
    CreateObject('efkg_411', -1)
    sprite('kg411_04', 1)
    physicsYImpulse(10000)
    physicsXImpulse(15000)
    setGravity(2100)
    sprite('kg411_04', 1)
    sprite('kg411_04', 1)
    RefreshMultihit()
    sprite('kg411_04', 1)
    sprite('kg411_04', 1)
    RefreshMultihit()
    sprite('kg411_05', 5)
    setInvincible(0)
    sprite('kg411_06', 5)
    sprite('kg411_07', 3)
    XImpulseAcceleration(50)
    sprite('kg411_08', 3)
    sprite('kg411_09', 3)
    label(0)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('kg024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 3)
    sprite('kg024_01', 2)
    sprite('kg024_02', 2)
    sprite('kg024_03', 2)
    sprite('kg411_00', 2)
    sprite('kg411_01', 2)
    sprite('kg411_02', 2)
    JumpEffects(3, 100)
    sprite('kg411_03', 2)
    CommonSE('006_swing_blade_2')
    CommonSE('011_spin_0')
    CreateObject('efkg_411', -1)
    sprite('kg411_04', 1)
    RefreshMultihit()
    physicsYImpulse(10000)
    physicsXImpulse(15000)
    setGravity(2100)
    sprite('kg411_04', 1)
    sprite('kg411_04', 1)
    RefreshMultihit()
    sprite('kg411_04', 1)
    sprite('kg411_04', 1)
    RefreshMultihit()
    sprite('kg411_05', 5)
    setInvincible(0)
    sprite('kg411_06', 5)
    sprite('kg411_07', 3)
    XImpulseAcceleration(50)
    sprite('kg411_08', 3)
    sprite('kg411_09', 3)
    label(2)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('kg024_00', 2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 5)
    sprite('kg024_01', 2)
    sprite('kg024_02', 2)
    sprite('kg024_03', 2)
    label(1)
    sprite('kg024_00', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('kg411_00', 2)
    sprite('kg411_01', 2)
    sprite('kg411_02', 2)
    JumpEffects(3, 100)
    sprite('kg411_03', 2)
    CommonSE('006_swing_blade_2')
    CommonSE('011_spin_0')
    CreateObject('efkg_411', -1)
    sprite('kg411_04', 2)
    RefreshMultihit()
    AirPushbackY(35000)
    AirPushbackX(15000)
    Hitstop(3)
    physicsYImpulse(35000)
    physicsXImpulse(20000)
    setGravity(2100)
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_04', 2)
    RefreshMultihit()
    sprite('kg411_05', 5)
    setInvincible(0)
    sprite('kg411_06', 5)
    XImpulseAcceleration(50)
    sprite('kg411_07', 3)
    XImpulseAcceleration(50)
    sprite('kg411_08', 3)
    sprite('kg411_09', 3)
    label(4)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(4)
    label(5)
    sprite('kg024_00', 3)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('kg024_01', 3)
    sprite('kg024_02', 3)
    sprite('kg024_03', 3)
    sprite('kg024_04', 3)


@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(210)
        Crumple(200)
        AirUntechableTime(200)
        UseSlashHitspark(1)
        PushbackX(30000)
        MoveAttributes(0, 1, 0, 0, 0)
        OppPositionOnHit(1, 200000, 0)
        DefeatOpponentBehavior(1)
        AttackDirection(0)
        EnterStateIfEventID(12, 'AstralHeatExe')
        IgnoreScreenfreeze(1)
        EndMomentum(1)
        setInvincible(1)
    sprite('kg450_00', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    Voiceline('kg290')
    DistortionSettings(42, -1, 2)
    EmptyHeat()
    E0EAEffect('aura', 65535)
    CreateObject('EMB_KG_AH', -1)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_01', 3)
    sprite('kg450_02', 3)
    sprite('kg450_03', 3)
    sprite('kg450_04', 8)
    sprite('kg450_05', 8)
    sprite('kg450_06', 8)
    PrivateSE('kgse_01')
    sprite('kg450_07', 5)
    CreateObject('450slash00', -1)
    sprite('kg450_08', 3)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg450_09', 3)
    sprite('kg450_28', 6)
    setInvincible(0)
    sprite('kg450_29', 7)
    sprite('kg450_30', 7)
    sprite('kg450_31', 7)
    sprite('kg450_32', 7)


@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        AttackLevel_(5)
        Damage(1000)
        MinimumDamage(100)
        DefeatOpponentBehavior(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(610)
        Crumple(600)
        Hitstop(7)
        PushbackX(0)
        PassByArmor(1)
        UseSlashHitspark(1)
        EnableCollision(0)
        HitAnywhere(1)
    sprite('kg450_09', 5)
    CreateObject('AstKousokuEff', -1)
    sprite('kg450_10', 5)
    sprite('kg450_11', 5)
    sprite('kg450_12', 5)
    sprite('kg450_13', 5)
    CreateObject('450slash01', -1)
    sprite('kg450_14', 8)
    CreateObject('AstKousokuEff2', -1)
    AstralHeatCleanup(1, 1)
    PlayPlayAstralBGM(1)
    HUDVisibillity(1)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    sprite('kg450_15', 8)
    sprite('kg450_16', 8)
    sprite('kg450_17', 6)
    sprite('kg450_18', 6)
    Voiceline('kg291')
    sprite('kg450_19', 6)
    sprite('kg450_20', 6)
    sprite('kg450_21', 6)
    sprite('null', 60)

    def RunOnObject_22():
        Visibility(1)
        AbsoluteY(40000000)
        setGravity(0)
    Visibility(1)
    CreateObject('AstBG00', -1)
    CreateObject('AstCutin00', -1)
    TriggerUponForState('AstKousokuEff', 32)
    TriggerUponForState('AstKousokuEff2', 32)
    CameraControlEnable(0)
    CreateObject('AstCamera00', -1)
    sprite('null', 40)
    Voiceline('kg292')
    sprite('null', 10)
    DespawnEAEffect('AstCamera00')
    DespawnEAEffect('AstBG00')
    DespawnEAEffect('AstCutin00')
    sprite('null', 60)
    CreateObject('AstCutin01', -1)
    sprite('null', 80)
    Voiceline('kg293')
    sprite('null', 40)
    Voiceline('kg294')
    sprite('kg450_25', 1)
    RefreshMultihit()
    HitAnywhere(1)
    Hitstop(15)
    Damage(30000)
    DefeatOpponentBehavior(3)
    AttackDirection(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackY(30000)
    AirPushbackX(100000)
    OppPositionOnHit(1, 20000, 0)
    sprite('kg450_25', 5)
    sprite('null', 80)
    sprite('kg431_14', 3)
    XPositionRelativeFacing(260000)
    AttackOff()
    DespawnEAEffect('AstCutin01')
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    CameraWinnerControlStop(1)
    Visibility(0)
    SetBackground(0)
    ScreenShake(1000, 12000)
    sprite('kg431_15', 3)
    ScreenShake(1000, 12000)
    sprite('kg431_16', 3)
    ScreenShake(1000, 10000)
    sprite('kg431_14', 3)
    ScreenShake(1000, 10000)
    sprite('kg431_15', 3)
    ScreenShake(1000, 8000)
    sprite('kg431_16', 3)
    ScreenShake(1000, 8000)
    sprite('kg431_14', 3)
    ScreenShake(1000, 6000)
    sprite('kg431_15', 3)
    ScreenShake(1000, 6000)
    sprite('kg431_16', 3)
    ScreenShake(1000, 4000)
    sprite('kg431_14', 3)
    ScreenShake(1000, 4000)
    sprite('kg431_15', 3)
    ScreenShake(1000, 3000)
    sprite('kg431_16', 3)
    ScreenShake(1000, 3000)
    sprite('kg431_14', 4)
    ScreenShake(1000, 2000)
    sprite('kg431_15', 4)
    ScreenShake(1000, 2000)
    sprite('kg431_16', 4)
    ScreenShake(1000, 2000)
    sprite('kg431_14', 6)
    ScreenShake(0, 1000)
    sprite('kg431_15', 6)
    ScreenShake(0, 1000)
    sprite('kg431_16', 6)
    ScreenShake(0, 1000)
    sprite('kg431_17', 6)
    sprite('kg431_18', 6)
    sprite('kg431_19', 6)
    sprite('kg400_12', 6)
    sprite('kg400_13', 6)
    sprite('kg400_14', 6)
    sprite('kg400_15', 6)


@State
def LoseAction():

    def upon_IMMEDIATE():
        uponSendToLabel(LANDING, 1)
        EnterStateIfEventID(8, 'CmnActFDownLoop')
        NoDamageAction(1)

        def upon_32():
            clearUponHandler(32)
            physicsYImpulse(5000)
            EndYPhysicsImpulse()
            sendToLabel(0)
    sprite('keep', 32767)
    label(0)
    sprite('kg063_02', 3)
    sprite('kg063_03', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('kg063_04', 3)
    sprite('kg063_05', 3)
    sprite('kg063_06', 2)
    sprite('kg063_07', 2)
    sprite('kg063_08', 3)
    sprite('kg063_09', 3)
    sprite('kg063_10', 3)
    if SLOT_121 == 1:
        ObjectUpon25(1, 'gs008')
    if SLOT_121 == 2:
        ObjectUpon25(1, 'gs002')
    if SLOT_121 == 3:
        ObjectUpon25(1, 'gs005')
    if SLOT_121 == 4:
        ObjectUpon25(1, 'gs011')
    loopRest()


@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)

        def upon_14():
            Voiceline('kg054')
    sprite('kg900_00', 32767)
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
    loopRest()


@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        AbsoluteY(200000)
    sprite('kg901_00', 50)
    physicsYImpulse(-150)
    sprite('kg901_00', 50)
    physicsYImpulse(150)
    Voiceline('kg055')
    label(0)
    sprite('kg901_00', 50)
    physicsYImpulse(-150)
    sprite('kg901_00', 50)
    physicsYImpulse(150)
    gotoLabel(0)


@State
def BurstDD():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 300000, 0)
        UseSlashHitspark(1)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        ForceFaceSprite()
        StayAfterMovement(1, 0)
        SetXCollisionFromOrigin(200)
        DamageFromStateOnly('BurstDDAdd')

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_FALLING():
            clearUponHandler(FALLING)
            setGravity(5000)
            sendToLabel(1)
        uponSendToLabel(LANDING, 2)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
    sprite('kg406_00ex01', 2)
    E0EAEffect('BurstDDeff', 103)
    physicsXImpulse(10000)
    physicsYImpulse(18000)
    EndYPhysicsImpulse()
    JumpEffects(1, 0)
    Voiceline('kg280')
    sprite('kg406_01ex01', 3)
    label(0)
    sprite('kg406_02ex01', 3)
    sprite('kg406_03ex01', 3)
    sprite('kg406_04ex01', 3)
    gotoLabel(0)
    label(1)
    sprite('kg440_00', 3)
    sprite('kg440_01', 32767)
    PrivateSE('kgse_01')
    label(2)
    sprite('kg440_02', 3)
    EndMomentum(1)
    SetXCollisionFromOrigin(200)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    sprite('kg406_08ex01', 4)
    setInvincible(0)
    sprite('kg406_09ex01', 4)
    sprite('kg406_10ex01', 4)
    sprite('kg406_11ex01', 3)
    SetXCollisionFromOrigin(-1)
    LandingEffects(100, 1, 1)
    sprite('kg406_12ex01', 4)
    sprite('kg406_13ex01', 4)
    sprite('kg406_14ex01', 3)
    sprite('kg406_15ex01', 3)
    sprite('kg406_16ex01', 3)
    sprite('kg406_17ex01', 2)


@State
def BurstDD_Easy():

    def upon_IMMEDIATE():
        AttackDefaults_Stage1ExceedAccel()
        GroundedHitstunAnimation(9)
        AirPushbackY(20000)
        Blockstun(26)
        Hitstop(20)
        OppPositionOnHit(1, 300000, 0)
        UseSlashHitspark(1)
        MinimumDamage(10)
        setInvincible(1)
        EndMomentum(1)
        ForceFaceSprite()
        StayAfterMovement(1, 0)
        SetXCollisionFromOrigin(200)
        DamageFromStateOnly('BurstDDAdd')

        def upon_OPPONENT_HIT():
            enterState('BurstDDAdd')
            SetBackground(1)

        def upon_OPPONENT_BLOCKS():
            PushbackX(39900)

        def upon_FALLING():
            clearUponHandler(FALLING)
            setGravity(5000)
            sendToLabel(1)
        uponSendToLabel(LANDING, 2)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            ScreenShake(10000, 50000)

        def upon_STATE_END():
            DepleteOD()
        if PreviousStateCheck('CmnActJumpPre'):
            enterState('BurstDD')
    sprite('kg406_00ex01', 2)
    E0EAEffect('BurstDDeff', 103)
    physicsXImpulse(21111)
    physicsYImpulse(7000)
    EndYPhysicsImpulse()
    JumpEffects(1, 0)
    Voiceline('kg280')
    sprite('kg406_01ex01', 3)
    label(0)
    sprite('kg406_02ex01', 3)
    sprite('kg406_03ex01', 3)
    sprite('kg406_04ex01', 3)
    gotoLabel(0)
    label(1)
    sprite('kg440_00', 3)
    sprite('kg440_01', 32767)
    PrivateSE('kgse_01')
    label(2)
    sprite('kg440_02', 3)
    AddX(1)
    EndMomentum(1)
    SetXCollisionFromOrigin(200)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    sprite('kg406_08ex01', 4)
    setInvincible(0)
    sprite('kg406_09ex01', 4)
    sprite('kg406_10ex01', 4)
    sprite('kg406_11ex01', 3)
    SetXCollisionFromOrigin(-1)
    LandingEffects(100, 1, 1)
    sprite('kg406_12ex01', 4)
    sprite('kg406_13ex01', 4)
    sprite('kg406_14ex01', 3)
    sprite('kg406_15ex01', 3)
    sprite('kg406_16ex01', 3)
    sprite('kg406_17ex01', 2)


@State
def BurstDDAdd():

    def upon_IMMEDIATE():
        AttackDefaults_Stage2ExceedAccel()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Hitstop(3)
        AirUntechableTime(60)
        HitsparkSize(500)
        UseSlashHitspark(1)
        MinimumDamage(10)
        AttackOff()
        DamageFromStateOnly('BurstDDAdd')
        SetBackground(1)
        EnableAfterimage(1)
        AfterimageInterval(3)
        AfterimageCount(3)
        AfterimageColor_1(150, 200, 200, 200)
        AfterimageColor_2(100, 100, 100, 100)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('kg440_03', 1)
    Voiceline('kg281')
    if SLOT_51:
        sendToLabel(100)
    sprite('kg440_03', 1)
    Damage(250)
    AirPushbackX(10000)
    AirPushbackY(-60000)
    GroundBounce(1)
    BouncePercentage(50)
    ShutUp(1)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    SetYCollisionFromOrigin(300)
    SetXCollisionFromOrigin(400)
    physicsXImpulse(2500)
    sprite('kg440_00', 2)
    XImpulseAcceleration(150)
    sprite('kg440_01', 2)
    XImpulseAcceleration(150)
    sprite('kg440_02', 2)
    CreateObject('efkg_440Slash', -1)
    XImpulseAcceleration(150)
    RefreshMultihit()
    sprite('kg440_03', 2)
    sprite('kg440_00', 2)
    sprite('kg440_01', 2)
    sprite('kg440_02', 2)
    RefreshMultihit()
    sprite('kg440_03', 2)
    sprite('kg440_00', 2)
    sprite('kg440_01', 2)
    sprite('kg440_02', 2)
    RefreshMultihit()
    sprite('kg440_03', 2)
    sprite('kg440_00', 2)
    sprite('kg440_01', 2)
    sprite('kg440_02', 2)
    RefreshMultihit()
    sprite('kg406_08ex01', 5)
    XImpulseAcceleration(80)
    TriggerUponForState('efkg_440Slash', 32)
    sprite('kg440_04', 5)
    XImpulseAcceleration(80)
    sprite('kg402_09ex01', 6)
    XImpulseAcceleration(80)
    sprite('kg402_10ex01', 6)
    XImpulseAcceleration(80)
    sprite('kg402_11ex01', 2)
    physicsXImpulse(10000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    CreateObject('efkg_440BlackFire', -1)
    PrivateSE('kgse_08')
    sprite('kg402_12ex01', 2)
    Voiceline('kg282')
    sprite('kg440_05', 3)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    ScreenShake(10000, 50000)
    AttackLevel_(5)
    Damage(1500)
    Hitstop(15)
    AirPushbackX(10000)
    AirPushbackY(40000)
    UseSlashHitspark(0)
    UsePunchHitspark(1)
    UseFireHitspark(1)
    ShutUp(0)
    GroundBounceReset()
    uponSendToLabel(LANDING, 202)
    SetXCollisionFromOrigin(150)
    sendToLabel(201)
    label(100)
    sprite('kg440_03', 2)
    Damage(500)
    AirPushbackX(10000)
    AirPushbackY(-60000)
    GroundBounce(1)
    BouncePercentage(35)
    ShutUp(1)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    SetYCollisionFromOrigin(300)
    SetXCollisionFromOrigin(400)
    physicsXImpulse(2500)
    sprite('kg440_00', 2)
    XImpulseAcceleration(150)
    sprite('kg440_01', 2)
    XImpulseAcceleration(150)
    sprite('kg440_02', 2)
    CreateObject('efkg_440Slash', -1)
    XImpulseAcceleration(150)
    RefreshMultihit()
    sprite('kg440_03', 2)
    sprite('kg440_00', 2)
    sprite('kg440_01', 2)
    sprite('kg440_02', 2)
    RefreshMultihit()
    sprite('kg440_03', 2)
    sprite('kg440_00', 2)
    sprite('kg440_01', 2)
    sprite('kg440_02', 2)
    RefreshMultihit()
    sprite('kg440_03', 2)
    sprite('kg440_00', 2)
    sprite('kg440_01', 2)
    sprite('kg440_02', 2)
    RefreshMultihit()
    sprite('kg406_08ex01', 5)
    TriggerUponForState('efkg_440Slash', 32)
    XImpulseAcceleration(80)
    sprite('kg440_04', 5)
    XImpulseAcceleration(80)
    sprite('kg402_09ex01', 6)
    XImpulseAcceleration(80)
    sprite('kg402_10ex01', 6)
    XImpulseAcceleration(80)
    sprite('kg402_11ex01', 2)
    physicsXImpulse(10000)
    physicsYImpulse(20000)
    EndYPhysicsImpulse()
    CreateObject('efkg_440BlackFireEx', -1)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('kg402_12ex01', 2)
    Voiceline('kg282')
    sprite('kg440_05', 3)
    RefreshMultihit()
    ScreenShake(10000, 50000)
    AttackLevel_(5)
    Hitstop(15)
    AirPushbackX(50000)
    AirPushbackY(6000)
    Wallbounce(1)
    WallbounceReboundTime(1)
    UseSlashHitspark(0)
    UsePunchHitspark(1)
    UseFireHitspark(1)
    ShutUp(0)
    GroundBounceReset()
    uponSendToLabel(LANDING, 202)
    SetXCollisionFromOrigin(150)
    sprite('kg440_05', 2)
    Hitstop(4)
    RefreshMultihit()
    sprite('kg440_05', 2)
    RefreshMultihit()
    sprite('kg440_05', 2)
    RefreshMultihit()
    sprite('kg440_05', 2)
    RefreshMultihit()
    sprite('kg440_05', 2)
    RefreshMultihit()
    sprite('kg440_05', 2)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    sendToLabel(201)
    TriggerUponForState('efkg_440BlackFireEx', 32)
    label(201)
    sprite('kg440_06', 2)
    sprite('kg440_07', 2)
    sprite('kg440_08', 2)
    gotoLabel(201)
    label(202)
    sprite('kg440_09', 2)
    sprite('kg402_15ex01', 5)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    sprite('kg402_16ex01', 6)
    sprite('kg402_17ex01', 6)
    sprite('kg402_18ex01', 6)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)


@Subroutine
def MouthTableInit():
    Unknown18011('kg309', 13665, 13411, 13665, 13411, 13665, 13411, 14433, 
        12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg313', 13665, 13411, 13665, 13411, 13665, 13411, 12641, 
        25395, 24886, 25398, 24884, 25398, 24886, 25398, 24886, 25398, 
        24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg316', 13921, 13411, 13921, 13411, 24888, 25398, 24884, 
        25398, 24884, 25398, 24884, 25398, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg318', 13921, 13411, 13921, 13411, 13921, 13411, 12641, 
        25392, 13877, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 
        13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('kg329', 13665, 13667, 13665, 13667, 13665, 13155, 13665, 
        13667, 13665, 13155, 24882, 25397, 24885, 25397, 24885, 25397, 
        24885, 25397, 13361, 13921, 13923, 13921, 13923, 13921, 13923, 
        14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg000', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg055', 13921, 13667, 13921, 13411, 13665, 13667, 13665, 
        12899, 24888, 25398, 24885, 25398, 24886, 12339, 13923, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg400', 14177, 13155, 24880, 25399, 24887, 25399, 24887, 
        25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg401', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg404', 14177, 14179, 14177, 14179, 14177, 12899, 24880, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg405', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg406', 14433, 13155, 24880, 25399, 24887, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 
        14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0)
    Unknown18011('kg407', 13411, 14177, 13411, 24885, 25399, 24887, 25399, 
        24887, 25399, 24887, 25399, 24887, 25398, 24884, 25398, 24886, 
        25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('kg408', 14433, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
        12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('kg411', 14177, 13667, 24885, 25399, 24887, 25399, 24887, 
        25399, 24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg412', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
        14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg413', 14435, 24888, 25399, 12849, 13921, 13923, 13921, 
        13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg414', 13921, 13923, 13921, 13411, 24888, 25399, 24887, 
        25399, 24887, 25399, 24887, 25399, 24887, 25397, 24885, 25398, 
        24886, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0)
    Unknown18011('kg415', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
        13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 
        24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14435, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg416', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0)
    Unknown18011('kg417', 12643, 24881, 25400, 24888, 25400, 24888, 25400, 
        56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('kg052', 14177, 14179, 14177, 14179, 13921, 13923, 13921, 
        13923, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if SLOT_44:
        Unknown18011('kg000', 14177, 14179, 14177, 14179, 14177, 14179, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg400', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
            14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg401', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg404', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
            14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg405', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 14433, 
            14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg406', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('kg407', 14177, 14179, 14177, 14179, 14433, 14435, 
            12641, 25397, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg408', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 
            25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg411', 12643, 24882, 25399, 24887, 25399, 24887, 
            25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0)
        Unknown18011('kg412', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 12899, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg413', 14177, 14179, 14177, 14179, 14177, 14179, 
            14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0)
        Unknown18011('kg414', 13921, 13923, 14177, 14179, 14689, 12643, 
            24888, 25399, 24887, 25397, 24885, 25399, 24887, 25399, 55, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('kg415', 13921, 13923, 13921, 13923, 13921, 13923, 
            14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0)
        Unknown18011('kg416', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg417', 14177, 14179, 14177, 14179, 13921, 13923, 
            13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 
            25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg052', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('kg156', 14177, 14179, 14177, 14179, 13921, 13923, 
            13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if not SLOT_86:
        if CharacterIDCheck('bn'):
            Unknown18011('kg000', 14433, 14435, 14433, 14433, 14435, 14433,
                12643, 24880, 25399, 24887, 25399, 24887, 25399, 12339, 
                14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg400', 12641, 25392, 12337, 12641, 25392, 12337,
                12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('kg401', 12641, 25392, 12337, 12641, 25392, 12337,
                12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('hb'):
            Unknown18011('kg000', 12641, 25392, 12342, 14433, 14433, 14435,
                14433, 14435, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg400', 12641, 25392, 12337, 12641, 25392, 12337,
                12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('kg401', 12641, 25392, 12337, 12641, 25392, 12337,
                12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('jn'):
            Unknown18011('kg502', 14177, 14691, 24880, 25398, 24886, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg503', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kg502', 14177, 14179, 14177, 14179, 14177, 
                    14179, 13921, 13923, 12897, 25392, 12339, 14177, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    12897, 25392, 24885, 13362, 13667, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg503', 12643, 24884, 25400, 12341, 13921, 
                    13923, 13921, 13923, 12641, 25392, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25397, 24885, 25397, 13361,
                    13665, 13667, 14177, 14179, 14177, 13667, 12897, 25392,
                    53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('no'):
            Unknown18011('kg504', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg505', 14177, 13923, 24880, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kg504', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 12340,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg505', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('rc'):
            if SLOT_140:
                Unknown18011('kg506', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg507', 14177, 14179, 14177, 13411, 24880, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
        if CharacterIDCheck('tk'):
            Unknown18011('kg508', 12643, 12336, 13921, 14435, 14433, 14435,
                14433, 13923, 24884, 25398, 24886, 12849, 25392, 54, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg509', 13921, 13923, 13921, 13923, 13921, 13411,
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('lc'):
            Unknown18011('kg512', 13921, 13923, 13921, 13923, 13921, 14435,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg513', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14689, 14691, 14177, 14179, 14177, 14179, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('bn'):
            if SLOT_138:
                Unknown18011('kg516', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13667, 24880, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg517', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14689, 14691, 14177, 14179, 14177,
                    14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            else:
                Unknown18011('kg516', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13667, 24885, 25398, 24886,
                    25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg517', 14433, 14435, 12897, 25392, 24886, 
                    25398, 24886, 25398, 24886, 25399, 24887, 25399, 24887,
                    12338, 14179, 12641, 25397, 24887, 25399, 24887, 25399,
                    24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_140:
                    Unknown18011('kg516', 13921, 13923, 24880, 25398, 24886,
                        25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                        24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                        25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    Unknown18011('kg517', 14177, 14179, 14177, 14179, 14177,
                        14179, 14177, 13411, 24880, 25401, 24889, 25399, 
                        24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                        25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ny'):
            Unknown18011('kg522', 13921, 25392, 24887, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                12339, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg523', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 13923, 24884, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('tb'):
            Unknown18011('kg524', 14177, 14179, 14177, 14179, 14177, 14691,
                24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg525', 14177, 14179, 14177, 14179, 14177, 14179,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 99, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('hz'):
            Unknown18011('kg526', 14177, 13923, 24880, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg527', 12641, 25392, 24887, 25399, 12337, 14177,
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('mk'):
            Unknown18011('kg530', 14177, 14179, 14177, 14179, 14177, 13411,
                24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg531', 14177, 13411, 24880, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('pt'):
            Unknown18011('kg534', 12643, 12338, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('kg535', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13409, 13667, 13409, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('iz'):
            Unknown18011('kg542', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13667, 24880, 25398, 
                24886, 25398, 12344, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13667, 24880, 25398, 24886, 25398, 24886, 
                25398, 24886, 25398, 12340, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg543', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 13665, 13667, 
                13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('am'):
            Unknown18011('kg540', 14177, 14435, 24880, 25398, 24886, 25398,
                24886, 12338, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg541', 14177, 14179, 14177, 14179, 12641, 25394,
                13618, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('bl'):
            Unknown18011('kg542', 12641, 25394, 12342, 12641, 25392, 24886,
                12337, 13923, 24880, 25398, 24886, 25399, 24887, 25399, 
                12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg543', 12641, 25397, 24887, 25399, 24887, 25399,
                24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 
                14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 
                14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('az'):
            Unknown18011('kg544', 13923, 24880, 25401, 24889, 25401, 24889,
                25401, 24889, 25401, 24889, 25401, 24889, 25401, 57, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg545', 14689, 13155, 24880, 25401, 24885, 25401,
                24885, 25401, 24885, 25401, 24885, 25401, 24885, 25401, 53,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('kk'):
            Unknown18011('kg548', 14177, 13667, 14177, 13667, 14177, 13667,
                14177, 13411, 24880, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('kg549', 14689, 13667, 14689, 13667, 14689, 13667,
                14689, 13667, 14689, 13667, 14689, 13667, 14689, 13667, 
                14689, 13667, 14689, 13667, 14689, 13667, 14689, 13667, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kg548', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177,
                    14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0)
                Unknown18011('kg549', 14177, 14179, 14177, 14179, 14177, 
                    14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ce'):
            Unknown18011('kg553', 13153, 25392, 24886, 25398, 24886, 25398,
                24886, 25398, 24886, 14385, 14435, 24880, 25398, 24886, 
                25398, 24886, 12849, 13923, 13921, 13923, 13921, 13923, 
                13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg554', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 24880, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_140:
                Unknown18011('kg553', 12643, 12337, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg554', 14177, 14179, 14177, 12899, 24885, 
                    25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887,
                    25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('rm'):
            Unknown18011('kg554', 14177, 13923, 24880, 25398, 24886, 25398,
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 13876, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 13409, 25392, 24886, 
                25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 
                25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0)
            Unknown18011('kg555', 14177, 13923, 13921, 13923, 13921, 13923,
                13921, 13411, 24880, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                24886, 25398, 24886, 25398, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('hb'):
            Unknown18011('kg556_1', 13921, 13923, 13921, 13923, 13921, 99, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg556_2', 13409, 12643, 24882, 25400, 12340, 
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 
                24880, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 
                12340, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg557', 13409, 13923, 13921, 13923, 24880, 25398,
                24886, 25398, 24886, 25398, 12340, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 
                13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ph'):
            Unknown18011('kg558', 14689, 14691, 14689, 14691, 14689, 13923,
                24880, 25401, 24889, 25401, 24889, 25401, 24889, 25401, 
                12343, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 
                14691, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0)
            Unknown18011('kg559', 13921, 13923, 13921, 13923, 13921, 13923,
                13921, 13923, 13921, 13923, 13921, 13923, 13921, 13411, 
                24885, 25398, 24886, 25398, 24886, 25398, 24886, 12337, 
                13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0)
        if CharacterIDCheck('mi'):
            if SLOT_138:
                pass
            else:
                Unknown18011('kg562', 13921, 13923, 13921, 13923, 13921, 
                    13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921,
                    13667, 24885, 25398, 24886, 25398, 24886, 25398, 24886,
                    25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                Unknown18011('kg563', 14433, 14435, 14433, 14435, 14433, 
                    13923, 12897, 25392, 12342, 14689, 13923, 14689, 14179,
                    14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179,
                    12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0)
                if SLOT_140:
                    Unknown18011('kg562', 13921, 13923, 13921, 13923, 13921,
                        13923, 13921, 13923, 13921, 13923, 13921, 14179, 
                        24885, 25399, 24887, 25399, 24887, 25399, 24887, 
                        25399, 24887, 25399, 13622, 14177, 14179, 14177, 
                        14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    Unknown18011('kg563', 14177, 14179, 14177, 14179, 14177,
                        14179, 14177, 13411, 24880, 25399, 24887, 25399, 
                        24887, 25399, 24887, 25399, 24887, 25399, 24887, 
                        25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('es'):
            Unknown18011('kg566', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 
                24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg567', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 
                24887, 25399, 24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        if CharacterIDCheck('ma'):
            Unknown18011('kg568', 12641, 25400, 12342, 14177, 14179, 14177,
                14179, 12641, 25396, 13620, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 
                14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0)
            Unknown18011('kg569', 14177, 14179, 14177, 14179, 14177, 14179,
                14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 
                24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


@State
def CmnActEntry():
    SLOT_121 = 0
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jn'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2110)
        else:
            gotoLabel(110)
    if CharacterIDCheck('jn'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('rc'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2130)
    if CharacterIDCheck('tk'):
        SyncEntry()
        gotoLabel(140)
    if CharacterIDCheck('lc'):
        SyncEntry()
        gotoLabel(160)
    if CharacterIDCheck('bn'):
        if SLOT_138:
            gotoLabel(180)
        elif SLOT_139:
            gotoLabel(1180)
        else:
            gotoLabel(2180)
    if CharacterIDCheck('ny'):
        SyncEntry()
        gotoLabel(210)
    if CharacterIDCheck('tb'):
        SyncEntry()
        gotoLabel(220)
    if CharacterIDCheck('hz'):
        SyncEntry()
        gotoLabel(230)
    if CharacterIDCheck('mk'):
        SyncEntry()
        gotoLabel(250)
    if CharacterIDCheck('pt'):
        SyncEntry()
        gotoLabel(270)
    if CharacterIDCheck('iz'):
        SyncEntry()
        gotoLabel(290)
    if CharacterIDCheck('am'):
        SyncEntry()
        gotoLabel(300)
    if CharacterIDCheck('bl'):
        SyncEntry()
        gotoLabel(310)
    if CharacterIDCheck('az'):
        SyncEntry()
        gotoLabel(320)
    if CharacterIDCheck('kk'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2340)
        else:
            gotoLabel(340)
    if CharacterIDCheck('ce'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2360)
        else:
            gotoLabel(360)
    if CharacterIDCheck('rm'):
        SyncEntry()
        gotoLabel(370)
    if CharacterIDCheck('hb'):
        SyncEntry()
        gotoLabel(380)
    if CharacterIDCheck('ph'):
        SyncEntry()
        gotoLabel(390)
    if CharacterIDCheck('mi'):
        SyncEntry()
        if SLOT_140:
            gotoLabel(2410)
        else:
            gotoLabel(410)
    if CharacterIDCheck('es'):
        SyncEntry()
        gotoLabel(430)
    if CharacterIDCheck('ma'):
        SyncEntry()
        gotoLabel(440)
    label(482)
    if not CharacterIDCheck('ca'):
        if random_(2, 0, 33):
            conditionalSendToLabel(10)
    if random_(2, 0, 50):
        conditionalSendToLabel(20)
    label(0)
    sprite('kg600_00', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(1)
    sprite('kg600_00', 32767)
    uponSendToLabel(57, 2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('kg600_00', 1)
    Voiceline('kg412')
    label(3)
    sprite('kg600_00', 30)
    sprite('kg600_01', 8)
    sprite('kg600_02', 8)
    sprite('kg600_03', 30)
    CommonSE('021_bonecleak_0')
    sprite('kg600_02', 8)
    sprite('kg600_01', 8)
    if SLOT_97:
        conditionalSendToLabel(3)
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    if SLOT_43:
        DemoTimer(110)
    else:
        DemoTimer(50)
    loopRest()
    ExitState()
    label(10)
    sprite('null', 1)
    ScreenCollision(0)
    EnableCollision(0)
    XPositionRelativeFacing(-1000000)
    label(11)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(11)
    sprite('null', 20)
    Voiceline('kg416')
    sprite('kg603_00', 2)
    SetZVal(500)
    PrivateSE('kgse_10')
    PrivateSE('kgse_10')
    physicsXImpulse(80000)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_01', 2)
    CreateParticle('kgef_603smoke00', -1)
    sprite('kg603_00', 2)
    sprite('null', 20)
    sprite('kg603_01', 2)
    Flip()
    sprite('kg603_02', 2)
    PrivateSE('kgse_10')
    PrivateSE('kgse_13')
    physicsXImpulse(80000)
    SetZVal(-500)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    Flip()
    sprite('kg603_02', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_02', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_02', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_02', 2)
    SetAcceleration(2500)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_02', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_02', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 2)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_02', 1)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_03', 1)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_04', 3)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg603_05', 3)
    ParticleFacing(1)
    CallCustomizableParticle('kgef_603smoke01', -1)
    sprite('kg112_01', 3)
    CreateObject('EntryBike', -1)
    RegisterObject(4, 1)
    EndMomentum(1)
    physicsXImpulse(7200)
    AbsoluteY(200000)
    physicsYImpulse(22000)
    setGravity(1500)
    uponSendToLabel(LANDING, 13)

    def RunOnObject_4():
        RotationAngle(10000)
        AddRotationPerFrame(1000)
    sprite('kg112_02', 1)
    sprite('kg112_02', 1)
    sprite('kg112_02', 1)
    sprite('kg112_03', 3)
    sprite('kg112_04', 3)
    sprite('kg112_05', 3)
    sprite('kg112_06', 3)
    sprite('kg112_07', 3)
    sprite('kg112_08', 3)
    sprite('kg112_09', 3)
    label(12)
    sprite('kg020_07', 4)
    sprite('kg020_08', 4)
    gotoLabel(12)
    label(13)
    sprite('kg409_13', 4)
    clearUponHandler(LANDING)
    LandingEffects(100, 1, 1)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    DeleteObject(4)
    PrivateSE('kgse_14')
    PrivateSE('kgse_14')
    sprite('kg409_14', 4)
    sprite('kg409_15', 4)
    sprite('kg409_16', 5)
    sprite('kg024_03', 5)
    sprite('kg024_04', 5)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    Voiceline('kg417')
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    if SLOT_43:
        DemoTimer(70)
    else:
        DemoTimer(120)
    loopRest()
    ExitState()
    label(20)
    Unknown61(0, 1, 0, 4, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_121 = SLOT_0
    if SLOT_121 == 1:
        gotoLabel(30)
    if SLOT_121 == 2:
        gotoLabel(40)
    if SLOT_121 == 3:
        gotoLabel(50)
    if SLOT_121 == 4:
        gotoLabel(60)
    label(30)
    sprite('kg601_00a', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 41)
    label(31)
    sprite('kg601_00a', 1)
    if SLOT_17:
        conditionalSendToLabel(31)
    sprite('kg601_00a', 8)
    sprite('kg601_01a', 8)
    Voiceline('kg414')
    CreateObject('kgef_enter', 0)
    label(32)
    sprite('kg601_01a', 8)
    if SLOT_97:
        conditionalSendToLabel(32)
    sprite('kg601_02a', 8)
    sprite('kg601_03a', 8)
    CreateObject('kgef_enter2', 0)
    sprite('kg601_04a', 8)
    sprite('kg601_05a', 8)
    sprite('keep', 1)
    CreateObject('EntryKaguraGirl', 0)
    ObjectUpon(STATE_END, 32)
    CommonSE('004_swing_grap_1_0')
    SubVoice(1, 'gs006')
    sendToLabel(29)
    label(40)
    sprite('kg601_00b', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 41)
    label(41)
    sprite('kg601_00b', 1)
    if SLOT_17:
        conditionalSendToLabel(41)
    sprite('kg601_00b', 8)
    sprite('kg601_01b', 8)
    Voiceline('kg414')
    CreateObject('kgef_enter', 0)
    label(42)
    sprite('kg601_01b', 8)
    if SLOT_97:
        conditionalSendToLabel(42)
    sprite('kg601_02b', 8)
    sprite('kg601_03b', 8)
    CreateObject('kgef_enter2', 0)
    sprite('kg601_04b', 8)
    sprite('kg601_05b', 8)
    sprite('keep', 1)
    CreateObject('EntryKaguraGirl', 0)
    ObjectUpon(STATE_END, 33)
    CommonSE('004_swing_grap_1_0')
    SubVoice(1, 'gs000')
    sendToLabel(29)
    label(50)
    sprite('kg601_00c', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 41)
    label(51)
    sprite('kg601_00c', 1)
    if SLOT_17:
        conditionalSendToLabel(51)
    sprite('kg601_00c', 8)
    sprite('kg601_01c', 8)
    Voiceline('kg414')
    CreateObject('kgef_enter', 0)
    label(52)
    sprite('kg601_01c', 8)
    if SLOT_97:
        conditionalSendToLabel(52)
    sprite('kg601_02c', 8)
    sprite('kg601_03c', 8)
    CreateObject('kgef_enter2', 0)
    sprite('kg601_04c', 8)
    sprite('kg601_05c', 8)
    sprite('keep', 1)
    CreateObject('EntryKaguraGirl', 0)
    ObjectUpon(STATE_END, 34)
    CommonSE('004_swing_grap_1_0')
    SubVoice(1, 'gs003')
    sendToLabel(29)
    label(60)
    sprite('kg601_00d', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    ObjectUpon(FALLING, 41)
    label(61)
    sprite('kg601_00d', 1)
    if SLOT_17:
        conditionalSendToLabel(61)
    sprite('kg601_00d', 8)
    sprite('kg601_01d', 8)
    Voiceline('kg414')
    CreateObject('kgef_enter', 0)
    label(62)
    sprite('kg601_01d', 8)
    if SLOT_97:
        conditionalSendToLabel(62)
    sprite('kg601_02d', 8)
    sprite('kg601_03d', 8)
    CreateObject('kgef_enter2', 0)
    sprite('kg601_04d', 8)
    sprite('kg601_05d', 8)
    sprite('keep', 1)
    CreateObject('EntryKaguraGirl', 0)
    ObjectUpon(STATE_END, 35)
    CommonSE('004_swing_grap_1_0')
    SubVoice(1, 'gs009')
    sendToLabel(29)
    label(29)
    sprite('kg601_06', 8)
    sprite('kg601_07', 8)
    sprite('kg601_08', 8)
    sprite('kg601_09', 8)
    sprite('kg601_10', 8)
    sprite('kg600_09', 9)
    ObjectUpon(FALLING, 32)
    sprite('kg600_10', 9)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 8)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 8)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 8)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 8)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    Voiceline('kg415')
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    if SLOT_43:
        DemoTimer(180)
    else:
        DemoTimer(120)
    loopRest()
    ExitState()
    label(110)
    sprite('kg300_04', 10)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(110)
    sprite('kg300_04', 1)
    Voiceline('kg502')
    label(111)
    sprite('kg300_04', 6)
    if SLOT_97:
        conditionalSendToLabel(111)
    sprite('kg300_04', 30)
    sprite('kg300_05', 6)
    sprite('kg300_06', 6)
    sprite('kg300_07', 6)
    sprite('kg300_08', 8)
    sprite('kg300_09', 8)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2110)
    sprite('null', 1)
    XPositionRelativeFacing(-1000000)
    ScreenCollision(0)
    EnableCollision(0)

    def upon_32():
        SetActionMark(1)
    label(2111)
    sprite('null', 1)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2111)
    sprite('null', 10)
    ObjectUpon(22, 32)
    AttackDefaults_StandingSpecial()
    sprite('null', 5)
    sprite('kg405_00', 2)
    CreateObject('405Slash', -1)
    CommonSE('000_airdash_1')
    sprite('kg405_01', 2)
    sprite('kg405_02', 2)
    physicsXImpulse(6000)
    AddX(100000)
    sprite('kg405_03', 3)
    XImpulseAcceleration(200)
    sprite('kg405_04', 2)
    XImpulseAcceleration(200)
    sprite('kg405_05', 2)
    sprite('kg405_04', 2)
    sprite('kg405_05', 2)
    sprite('kg405_06', 2)
    JumpEffects(1, 0)
    DashEffects(100, 1, 1)
    TriggerUponForState('405Slash', 32)
    XImpulseAcceleration(250)
    PrivateSE('kgse_12')
    sprite('kg405_07', 2)
    sprite('kg405_08', 2)
    XImpulseAcceleration(60)
    sprite('kg405_09', 4)
    XImpulseAcceleration(50)
    sprite('kg405_10', 4)
    XImpulseAcceleration(25)
    sprite('kg405_11', 4)
    XImpulseAcceleration(25)
    sprite('kg405_12', 4)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('kg405_13', 5)
    sprite('kg405_14', 5)
    label(2112)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(2112)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    Voiceline('kg502')
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    SetActionMark(4)
    label(2113)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    AddActionMark(-1)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(2113)
    loopRest()
    ExitState()
    label(120)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(121)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(121)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForNO', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg504')
    label(122)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(122)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(2120)
    sprite('null', 2)
    XPositionRelativeFacing(-960000)
    ScreenCollision(0)
    label(2121)
    sprite('null', 2)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2121)
    sprite('null', 2)

    def upon_EVERY_FRAME():
        if SLOT_29 < 720000:
            ObjectUpon(22, 32)
        if SLOT_29 < 520000:
            clearUponHandler(EVERY_FRAME)
            uponSendToLabel(32, 2124)
            XPositionRelativeFacing(-260000)
            EndMomentum(1)
            sendToLabel(2123)
    label(2122)
    sprite('kg030_02', 7)
    physicsXImpulse(5500)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(2122)
    label(2123)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(2123)
    label(2124)
    sprite('kg001_00', 7)
    Voiceline('kg504')
    sprite('kg001_01', 7)
    sprite('kg001_02', 180)
    sprite('kg001_01', 7)
    sprite('kg001_00', 7)
    DemoTimer(90)
    loopRest()
    ExitState()
    label(2130)
    sprite('kg600_00', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    uponSendToLabel(57, 2131)
    sprite('kg600_00', 32767)
    loopRest()
    label(2131)
    sprite('kg600_00', 20)
    sprite('kg600_00', 30)
    Voiceline('kg506')
    sprite('kg600_01', 8)
    sprite('kg600_02', 8)
    sprite('kg600_03', 30)
    CommonSE('021_bonecleak_0')
    sprite('kg600_02', 8)
    sprite('kg600_01', 8)
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoTimer(50)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(140)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(141)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(141)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForTK', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg508')
    label(142)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(142)
    sprite('kg602_02', 6)
    ObjectUpon(22, 32)

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(160)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(161)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(161)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForLC', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg512')
    label(162)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(122)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    ObjectUpon(22, 32)

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(180)
    sprite('kg602_06', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)

    def upon_32():
        SetActionMark(1)
    label(181)
    sprite('kg602_06', 6)
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(181)
    sprite('kg602_06', 6)
    Voiceline('kg516')
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    sprite('kg602_06', 6)
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    SetActionMark(2)
    label(182)
    sprite('kg602_06', 6)
    AddActionMark(-1)
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(182)
    label(183)
    sprite('kg602_09', 6)
    sprite('kg602_10', 6)
    sprite('kg602_11', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoTimer(40)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    loopRest()
    ExitState()
    label(1180)
    sprite('kg602_06', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)

    def upon_32():
        SetActionMark(1)
        Voiceline('kg516')
        DemoTimer(300)
    label(1181)
    sprite('kg602_06', 6)
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    loopRest()
    if not SLOT_2:
        notConditionalSendToLabel(1181)
    sprite('kg602_06', 6)
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    SetActionMark(8)
    label(1182)
    sprite('kg602_06', 6)
    AddActionMark(-1)
    sprite('kg602_07', 6)
    sprite('kg602_08', 6)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(1182)
    label(1183)
    sprite('kg602_09', 6)
    sprite('kg602_10', 6)
    sprite('kg602_11', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    loopRest()
    ExitState()
    label(2180)
    sprite('kg600_00', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    uponSendToLabel(32, 2181)
    sprite('kg600_00', 32767)
    loopRest()
    label(2181)
    sprite('kg600_00', 6)
    Voiceline('kg516')
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoTimer(140)
    loopRest()
    ExitState()
    label(210)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(211)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(211)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForNU', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 220)
    ObjectUpon(5, 35)
    Voiceline('kg522')
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    ObjectUpon(22, 32)
    DemoTimer(30)
    ExitState()
    label(220)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(221)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(221)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForTB', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg524')
    label(222)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(222)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    ObjectUpon(22, 32)

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(230)
    sprite('kg600_00', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    uponSendToLabel(32, 232)
    label(231)
    sprite('kg600_00', 6)
    loopRest()
    gotoLabel(231)
    label(232)
    sprite('kg600_00', 1)
    clearUponHandler(32)
    Voiceline('kg526')
    DemoTimer(200)
    sprite('kg600_00', 30)
    sprite('kg600_01', 8)
    sprite('kg600_02', 8)
    sprite('kg600_03', 60)
    CommonSE('021_bonecleak_0')
    sprite('kg600_02', 8)
    sprite('kg600_01', 8)
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    ExitState()
    label(250)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(250)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForMK', -1)
    RegisterObject(5, 1)
    sprite('kg000_02', 6)
    ObjectUpon(5, 33)
    sprite('kg000_03', 6)
    ObjectUpon(5, 34)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    Voiceline('kg530')
    DemoTimer(320)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    loopRest()
    ObjectUpon(5, 35)
    sprite('kg000_02', 6)
    ObjectUpon(22, 32)

    def RunOnObject_22():
        EndSprite(0)
    uponSendToLabel(33, 254)
    label(253)
    sprite('kg000_03', 6)
    sprite('kg000_04', 6)
    sprite('kg000_05', 6)
    sprite('kg000_06', 6)
    sprite('kg000_07', 6)
    sprite('kg000_00', 6)
    sprite('kg000_01', 6)
    sprite('kg000_02', 6)
    loopRest()
    gotoLabel(253)
    label(254)
    sprite('kg111_00', 3)
    physicsXImpulse(-25000)
    sprite('kg111_01', 3)
    sprite('kg111_02', 3)
    XImpulseAcceleration(40)
    sprite('kg111_03', 3)
    XImpulseAcceleration(40)
    sprite('kg111_04', 3)
    XImpulseAcceleration(40)
    sprite('kg111_06', 3)
    XImpulseAcceleration(40)
    sprite('kg111_07', 8)
    XImpulseAcceleration(40)
    sprite('kg111_08', 3)
    XImpulseAcceleration(0)
    sprite('kg111_09', 3)
    sprite('kg010_01', 4)
    sprite('kg010_00', 4)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(256)
    sprite('kg030_00', 7)
    physicsXImpulse(4500)
    sprite('kg030_01', 7)
    label(255)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(255)
    label(256)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    DemoTimer(30)
    ExitState()
    label(270)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(271)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(271)
    sprite('kg602_00', 20)
    sprite('kg602_00', 1)
    sprite('kg602_00', 50)
    ObjectUpon(22, 32)
    CreateObject('EntryMasterForPT', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 50)
    ObjectUpon(5, 33)
    sprite('kg602_01', 50)
    ObjectUpon(5, 34)
    sprite('kg602_02ex1', 8)
    ObjectUpon(5, 35)
    if CharacterIDCheck('pt'):
        Voiceline('kg534')
        DemoTimer(320)
    label(272)
    sprite('kg602_02ex1', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(272)
    uponSendToLabel(32, 273)
    sprite('kg602_02ex1', 60)
    sprite('kg602_02ex1', 600)
    ObjectUpon(22, 33)
    label(273)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(290)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(291)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(291)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForIZ', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 140)
    ObjectUpon(5, 35)
    Voiceline('kg542')
    sprite('kg602_02', 60)

    def RunOnObject_22():
        EndSprite(0)
    label(292)
    sprite('kg602_02ex1', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(292)
    sprite('kg602_02ex1', 600)
    uponSendToLabel(32, 293)
    ObjectUpon(22, 32)
    label(293)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(300)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(301)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(301)
    sprite('kg602_00', 20)
    sprite('kg602_00', 1)
    sprite('kg602_00', 50)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForAM', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 50)
    ObjectUpon(5, 33)
    sprite('kg602_01', 50)
    ObjectUpon(5, 34)
    sprite('kg602_02ex1', 8)
    ObjectUpon(5, 35)
    Voiceline('kg540')
    DemoTimer(320)
    label(302)
    sprite('kg602_02ex1', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(302)
    sprite('kg602_02ex1', 6)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    ObjectUpon(22, 32)

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoEndOnVoiceEnd(1)
    loopRest()
    ExitState()
    label(310)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(311)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(311)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForBL', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 140)
    ObjectUpon(5, 35)
    Voiceline('kg542')
    DemoTimer(320)
    label(312)
    sprite('kg602_02ex1', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(312)
    sprite('kg602_02ex1', 40)

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg602_02ex1', 600)
    uponSendToLabel(32, 313)
    ObjectUpon(22, 32)
    label(313)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(320)
    sprite('kg000_00', 1)
    XPositionRelativeFacing(-120000)
    label(321)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(321)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg411_00', 2)
    AttackDefaults_StandingSpecial()
    ObjectUpon(22, 32)
    sprite('kg411_01', 2)
    sprite('kg411_02', 1)
    DashEffects(100, 1, 1)
    sprite('kg411_02', 3)
    CreateObject('efkg_411Sub01', -1)
    sprite('kg411_03', 2)
    CommonSE('006_swing_blade_2')
    PrivateSE('kgse_01')
    CreateObject('efkg_411', -1)
    JumpEffects(2, 100)
    sprite('kg411_04', 3)
    uponSendToLabel(LANDING, 323)
    StartMultihit()
    physicsXImpulse(4000)
    setGravity(1800)
    PrivateSE('kgse_12')
    CreateObject('efkg_411Sub00', -1)
    StartMultihit()
    physicsYImpulse(30000)
    sprite('kg411_04', 2)
    YSpeed(-10000)
    HitsparkSize(500)
    sprite('kg411_04', 8)
    sprite('kg411_05', 3)
    sprite('kg412_00', 6)
    physicsXImpulse(-3000)
    physicsYImpulse(3000)
    setGravity(50)
    sprite('kg412_01', 3)
    sprite('kg412_02', 3)
    sprite('kg412_03', 2)
    physicsXImpulse(-6000)
    physicsYImpulse(19000)
    EndYPhysicsImpulse()
    sprite('kg412_04', 3)
    RefreshMultihit()
    CreateObject('efkg_412SlashEff', -1)
    PrivateSE('kgse_12')
    sprite('kg412_05', 3)
    sprite('kg412_06', 3)
    sprite('kg412_07', 3)
    sprite('kg412_08', 3)
    sprite('kg412_09', 3)
    sprite('kg412_10', 3)
    label(322)
    sprite('kg020_07', 3)
    sprite('kg020_08', 3)
    loopRest()
    gotoLabel(322)
    label(323)
    sprite('kg024_00', 3)
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    sprite('kg024_01', 3)
    sprite('kg024_02', 3)
    sprite('kg024_03', 3)
    sprite('kg024_04', 3)
    SetActionMark(6)
    label(324)
    sprite('kg000_00', 7)
    AddActionMark(-1)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(324)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    Voiceline('kg544')
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    SetActionMark(3)
    label(325)
    sprite('kg000_00', 7)
    AddActionMark(-1)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(325)
    loopRest()
    ExitState()
    label(340)
    sprite('kg300_04', 10)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(340)
    sprite('kg300_04', 1)
    Voiceline('kg548')
    label(341)
    sprite('kg300_04', 6)
    if SLOT_97:
        conditionalSendToLabel(341)
    sprite('kg300_04', 30)
    sprite('kg300_05', 6)
    sprite('kg300_06', 6)
    sprite('kg300_07', 6)
    sprite('kg300_08', 8)
    sprite('kg300_09', 8)
    ObjectUpon(22, 32)
    loopRest()
    ExitState()
    label(2340)
    sprite('kg600_00', 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    uponSendToLabel(57, 2341)
    sprite('kg600_00', 32767)
    loopRest()
    label(2341)
    sprite('kg600_00', 20)
    sprite('kg600_00', 120)
    Voiceline('kg548')
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    ObjectUpon(22, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(360)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(361)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(361)
    sprite('kg602_00', 20)
    sprite('kg602_00', 1)
    sprite('kg602_00', 50)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForCE', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 50)
    ObjectUpon(5, 33)
    sprite('kg602_01', 50)
    ObjectUpon(5, 34)
    sprite('kg602_02ex1', 8)
    ObjectUpon(5, 35)
    Voiceline('kg553')
    DemoTimer(320)

    def RunOnObject_22():
        EndSprite(0)
    uponSendToLabel(32, 363)
    label(362)
    sprite('kg602_02ex1', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(362)
    sprite('kg602_02ex1', 40)
    sprite('kg602_02ex1', 600)
    ObjectUpon(22, 32)
    label(363)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(2360)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(2361)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(2361)
    sprite('kg602_00', 20)
    sprite('kg602_00', 7)
    sprite('kg602_01', 7)
    sprite('kg602_02ex1', 8)
    Voiceline('kg553')
    sprite('kg602_02ex1', 250)
    sprite('kg602_02ex1', 7)
    ObjectUpon(22, 32)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(370)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(371)
    uponSendToLabel(32, 375)
    sprite('kg602_00', 6)
    loopRest()
    gotoLabel(371)
    label(375)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForRM', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 140)
    ObjectUpon(5, 35)
    Voiceline('kg554')
    DemoTimer(320)

    def RunOnObject_22():
        EndSprite(0)
    label(372)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(372)
    uponSendToLabel(33, 373)
    sprite('kg602_02', 600)
    ObjectUpon(22, 32)

    def RunOnObject_22():
        EndSprite(0)
    label(373)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(380)
    sprite('null', 1)
    Flip()
    AddX(-1000000)
    ScreenCollision(0)
    EnableCollision(0)
    label(381)
    sprite('null', 1)
    if SLOT_17:
        conditionalSendToLabel(381)
    sprite('null', 30)
    sprite('kg030_00', 7)
    physicsXImpulse(4000)
    sprite('kg030_01', 7)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 1)
    sprite('kg030_08', 6)
    ObjectUpon(22, 32)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg003_00ex', 3)
    Voiceline('kg556_1')
    EndMomentum(1)
    Flip()
    sprite('kg003_01', 3)
    sprite('kg003_00', 3)
    sprite('kg033_00', 2)
    sprite('kg033_01', 2)
    sprite('kg033_02', 1)
    AddX(-20000)
    physicsXImpulse(-6000)
    sprite('kg033_02', 2)
    XImpulseAcceleration(400)
    sprite('kg033_03', 3)
    setInvincible(0)
    XImpulseAcceleration(150)
    sprite('kg033_04', 3)
    XImpulseAcceleration(40)
    LandingEffects(100, 1, 1)
    sprite('kg033_05', 3)
    sprite('kg033_06', 3)
    XImpulseAcceleration(50)
    sprite('kg033_07', 3)
    XImpulseAcceleration(50)
    sprite('kg033_08', 3)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    uponSendToLabel(41, 383)
    label(382)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    gotoLabel(382)
    label(383)
    sprite('kg001_00', 7)
    clearUponHandler(41)
    sprite('kg001_01', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 10)
    Voiceline('kg556_2')
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 10)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 10)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 10)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 10)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_01', 7)
    sprite('kg001_00', 7)
    label(384)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(384)
    sprite('keep', 3)
    ObjectUpon(22, 33)
    loopRest()
    ExitState()
    label(390)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(391)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(391)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForPH', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg558')
    label(392)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(392)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    ObjectUpon(22, 32)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    DemoTimer(30)
    ExitState()
    label(410)
    sprite('kg300_04', 32767)
    uponSendToLabel(32, 411)
    loopRest()
    label(411)
    sprite('kg300_04', 1)
    Voiceline('kg562')
    label(412)
    sprite('kg300_04', 6)
    if SLOT_97:
        conditionalSendToLabel(412)
    sprite('kg300_04', 30)
    sprite('kg300_05', 6)
    sprite('kg300_06', 6)
    sprite('kg300_07', 6)
    sprite('kg300_08', 8)
    sprite('kg300_09', 8)
    loopRest()
    ExitState()
    label(2410)
    sprite('null', 1)
    XPositionRelativeFacing(-960000)
    ScreenCollision(0)
    EnableCollision(0)
    uponSendToLabel(57, 2411)

    def upon_32():
        Voiceline('kg562')

        def upon_EVERY_FRAME():
            AddActionMark(1)
            if SLOT_2 >= 200:
                clearUponHandler(EVERY_FRAME)
                sendToLabel(2414)

    def upon_EVERY_FRAME():
        if SLOT_19 < 520000:
            clearUponHandler(EVERY_FRAME)
            EndMomentum(1)
            XPositionRelativeFacing(-260000)
            sendToLabel(2413)
    sprite('null', 32767)
    loopRest()
    label(2411)
    sprite('null', 20)
    sprite('kg030_00', 7)
    physicsXImpulse(4000)
    sprite('kg030_01', 7)
    label(2412)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(2412)
    label(2413)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(2413)
    label(2414)
    sprite('kg333_00', 5)
    sprite('kg333_01', 5)
    sprite('kg333_02', 5)
    sprite('kg333_03', 30)
    sprite('kg333_04', 3)
    sprite('kg333_05', 6)
    CommonSE('302_spsys_burst')
    E0EAEffect('GuardCrushWind', 65535)
    ScreenShake(1000, 50000)

    def RunOnObject_1():
        Size(1400)
    sprite('kg333_06', 6)
    sprite('kg333_07', 6)
    sprite('kg333_05', 6)
    sprite('kg333_06', 6)
    sprite('kg333_07', 6)
    sprite('kg333_08', 6)
    sprite('kg333_09', 6)
    DemoTimer(50)
    loopRest()
    ExitState()
    label(430)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(431)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(431)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForES', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg566')
    label(432)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(432)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    ObjectUpon(22, 32)
    DemoTimer(30)
    loopRest()
    ExitState()
    label(440)
    sprite('kg602_00', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(441)
    sprite('kg602_00', 6)
    loopRest()
    if SLOT_17:
        conditionalSendToLabel(441)
    sprite('kg602_00', 20)
    sprite('kg602_00', 30)

    def RunOnObject_22():
        EndSprite(1)
    CreateObject('EntryMasterForMA', -1)
    RegisterObject(5, 1)
    sprite('kg602_01', 40)
    ObjectUpon(5, 33)
    sprite('kg602_02', 60)
    ObjectUpon(5, 34)
    sprite('kg602_02', 50)
    ObjectUpon(5, 35)
    Voiceline('kg568')
    label(442)
    sprite('kg602_02', 6)
    loopRest()
    if SLOT_97:
        conditionalSendToLabel(442)
    sprite('kg602_02', 15)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')

    def RunOnObject_22():
        EndSprite(0)
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    ObjectUpon(22, 32)
    DemoTimer(30)
    loopRest()
    ExitState()


@State
def CmnActRoundWin():
    StayAfterMovement(1, 0)
    sprite('kg615_00', 6)
    sprite('kg615_01', 6)
    sprite('kg615_02', 6)
    sprite('kg615_03', 6)
    sprite('kg615_04', 6)
    sprite('kg615_05', 6)
    if random_(2, 0, 50):
        Voiceline('kg400')
    else:
        Voiceline('kg401')
    sprite('kg615_06', 6)
    DemoEndOnVoiceEnd(1)
    sprite('kg615_07', 6)
    sprite('kg615_08', 6)
    sprite('kg615_04', 6)
    sprite('kg615_05', 6)
    sprite('kg615_06', 6)
    sprite('kg615_07', 6)
    sprite('kg615_08', 6)
    sprite('kg615_04', 6)
    sprite('kg615_05', 6)
    sprite('kg615_06', 6)
    sprite('kg615_07', 6)
    sprite('kg615_08', 6)
    sprite('kg615_09', 6)
    sprite('kg615_10', 6)
    sprite('kg615_11', 6)
    sprite('kg615_12', 32767)
    loopRest()


@State
def CmnActMatchWin():
    if SLOT_86:
        conditionalSendToLabel(482)
    if CharacterIDCheck('jn'):
        if SLOT_140:
            gotoLabel(2110)
        else:
            gotoLabel(110)
    if CharacterIDCheck('no'):
        if SLOT_140:
            gotoLabel(2120)
        else:
            gotoLabel(120)
    if CharacterIDCheck('rc'):
        if SLOT_140:
            gotoLabel(2130)
    if CharacterIDCheck('tk'):
        conditionalSendToLabel(140)
    if CharacterIDCheck('lc'):
        conditionalSendToLabel(160)
    if CharacterIDCheck('bn'):
        if SLOT_138:
            gotoLabel(180)
        elif SLOT_139:
            gotoLabel(1180)
        else:
            gotoLabel(2180)
    if CharacterIDCheck('ny'):
        conditionalSendToLabel(210)
    if CharacterIDCheck('tb'):
        conditionalSendToLabel(220)
    if CharacterIDCheck('hz'):
        conditionalSendToLabel(230)
    if CharacterIDCheck('mk'):
        conditionalSendToLabel(250)
    if CharacterIDCheck('pt'):
        conditionalSendToLabel(270)
    if CharacterIDCheck('iz'):
        conditionalSendToLabel(290)
    if CharacterIDCheck('am'):
        conditionalSendToLabel(300)
    if CharacterIDCheck('bl'):
        conditionalSendToLabel(310)
    if CharacterIDCheck('az'):
        conditionalSendToLabel(320)
    if CharacterIDCheck('kk'):
        if SLOT_140:
            gotoLabel(2340)
        else:
            gotoLabel(340)
    if CharacterIDCheck('ce'):
        if SLOT_140:
            gotoLabel(2360)
        else:
            gotoLabel(360)
    if CharacterIDCheck('rm'):
        conditionalSendToLabel(370)
    if CharacterIDCheck('hb'):
        conditionalSendToLabel(380)
    if CharacterIDCheck('ph'):
        conditionalSendToLabel(390)
    if CharacterIDCheck('mi'):
        if SLOT_140:
            gotoLabel(2410)
        else:
            gotoLabel(1410)
    if CharacterIDCheck('es'):
        conditionalSendToLabel(430)
    if CharacterIDCheck('ma'):
        conditionalSendToLabel(440)
    if CharacterIDCheck('ta'):
        conditionalSendToLabel(666)
    label(482)
    if SLOT_121 >= 1:
        conditionalSendToLabel(20)
    if random_(2, 0, 50):
        conditionalSendToLabel(10)
    label(0)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg406')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(1)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(1)
    label(10)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg408')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(11)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(11)
    label(20)
    SetXCollisionFromOrigin(200)
    sprite('kg620_00', 6)
    sprite('kg620_01', 6)
    sprite('kg620_02', 6)
    sprite('kg620_03', 6)
    sprite('kg611_00', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 15000)
    sprite('kg611_01', 6)
    sprite('kg611_02', 6)
    sprite('kg611_03', 6)
    sprite('kg611_04', 6)
    sprite('kg611_05', 6)
    sprite('kg611_06', 6)
    sprite('keep', 1)
    if SLOT_121 == 1:
        gotoLabel(30)
    if SLOT_121 == 2:
        gotoLabel(40)
    if SLOT_121 == 3:
        gotoLabel(50)
    if SLOT_121 == 4:
        gotoLabel(60)
    label(30)
    sprite('kg611_06', 15)
    CreateObject('MatchWinKaguraGirl', -1)
    ObjectUpon(STATE_END, 32)
    sprite('kg611_07a', 6)
    ObjectUpon(STATE_END, 41)
    CommonSE('024_getset_a')
    sprite('kg611_08a', 6)
    sprite('kg611_09a', 6)
    sprite('kg611_10a', 6)
    sprite('kg611_11a', 6)
    sprite('kg611_11ex00a', 1)
    Voiceline('kg407')
    label(31)
    sprite('kg611_11ex00a', 5)
    if SLOT_97:
        conditionalSendToLabel(31)
    sprite('kg611_11ex00a', 5)
    SubVoice(1, 'gs007')
    sprite('kg611_11ex01a', 5)
    sprite('kg611_12a', 20)
    sprite('kg611_13a', 32767)
    CreateParticle('kgef_win', 0)
    DemoEndOnVoiceEnd(1)
    label(40)
    sprite('kg611_06', 15)
    CreateObject('MatchWinKaguraGirl', -1)
    ObjectUpon(STATE_END, 33)
    sprite('kg611_07b', 6)
    ObjectUpon(STATE_END, 41)
    CommonSE('024_getset_a')
    sprite('kg611_08b', 6)
    sprite('kg611_09b', 6)
    sprite('kg611_10b', 6)
    sprite('kg611_11b', 6)
    sprite('kg611_11ex00b', 1)
    Voiceline('kg407')
    label(41)
    sprite('kg611_11ex00b', 5)
    if SLOT_97:
        conditionalSendToLabel(41)
    sprite('kg611_11ex00b', 5)
    SubVoice(1, 'gs001')
    sprite('kg611_11ex01b', 5)
    sprite('kg611_12b', 20)
    sprite('kg611_13b', 32767)
    CreateParticle('kgef_win', 0)
    DemoEndOnVoiceEnd(1)
    label(50)
    sprite('kg611_06', 15)
    CreateObject('MatchWinKaguraGirl', -1)
    ObjectUpon(STATE_END, 34)
    sprite('kg611_07c', 6)
    ObjectUpon(STATE_END, 41)
    CommonSE('024_getset_a')
    sprite('kg611_08c', 6)
    sprite('kg611_09c', 6)
    sprite('kg611_10c', 6)
    sprite('kg611_11c', 6)
    sprite('kg611_11ex00c', 1)
    Voiceline('kg407')
    label(51)
    sprite('kg611_11ex00c', 5)
    if SLOT_97:
        conditionalSendToLabel(51)
    sprite('kg611_11ex00c', 5)
    SubVoice(1, 'gs004')
    sprite('kg611_11ex01c', 5)
    sprite('kg611_12c', 20)
    sprite('kg611_13c', 32767)
    CreateParticle('kgef_win', 0)
    DemoEndOnVoiceEnd(1)
    label(60)
    sprite('kg611_06', 15)
    CreateObject('MatchWinKaguraGirl', -1)
    ObjectUpon(STATE_END, 35)
    sprite('kg611_07d', 6)
    ObjectUpon(STATE_END, 41)
    CommonSE('024_getset_a')
    sprite('kg611_08d', 6)
    sprite('kg611_09d', 6)
    sprite('kg611_10d', 6)
    sprite('kg611_11d', 6)
    sprite('kg611_11ex00d', 1)
    Voiceline('kg407')
    label(61)
    sprite('kg611_11ex00d', 5)
    if SLOT_97:
        conditionalSendToLabel(61)
    sprite('kg611_11ex00d', 5)
    SubVoice(1, 'gs010')
    sprite('kg611_11ex01d', 5)
    sprite('kg611_12d', 20)
    sprite('kg611_13d', 32767)
    CreateParticle('kgef_win', 0)
    DemoEndOnVoiceEnd(1)
    label(110)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg503')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(111)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(111)
    label(2110)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg503')
    DemoEndOnVoiceEnd(1)
    sprite('kg610_11', 6)
    label(2111)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(2111)
    label(120)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg505')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(121)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(121)
    label(2120)
    sprite('kg620_00', 6)
    StayAfterMovement(1, 0)
    sprite('kg620_01', 6)
    sprite('kg620_02', 8)
    sprite('kg611_00', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 3000)
    sprite('kg611_01', 6)
    sprite('kg611_02', 6)
    sprite('kg602_05', 6)
    Voiceline('kg505')
    DemoEndOnVoiceEnd(1)
    AddX(-150000)
    ScreenCollision(0)
    CreateObject('MatchWinSword', -1)
    RegisterObject(4, 1)

    def RunOnObject_4():
        AddX(56000)
        SetZVal(500)
    sprite('kg602_04', 6)
    sprite('kg602_03', 6)
    sprite('kg602_01', 32767)
    loopRest()
    ExitState()
    label(2130)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg507')
    DemoEndOnVoiceEnd(1)
    sprite('kg610_11', 6)
    label(2131)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(2131)
    label(140)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg509')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(141)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(141)
    label(160)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg513')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(161)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(161)
    label(180)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg517')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(181)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(181)
    label(1180)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg517')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(1181)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(1181)
    label(2180)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg517')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(2181)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(2181)
    label(210)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg523')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(211)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(211)
    label(220)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    Voiceline('kg525')
    sprite('kg610_10', 6)
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(221)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(221)
    label(230)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg527')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(231)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(231)
    label(250)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg531')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(251)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(251)
    label(270)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg535')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(271)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(271)
    label(290)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg543')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(291)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(291)
    label(300)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg541')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(301)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(301)
    label(310)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg543')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(311)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(311)
    label(320)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg545')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(321)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(321)
    label(340)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg549')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(231)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(231)
    label(2340)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 32767)
    Voiceline('kg549')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(360)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg554')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(361)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(361)
    label(2360)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 32767)
    Voiceline('kg554')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(370)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg555')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(361)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(361)
    label(380)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg557')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(381)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(381)
    label(390)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg559')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(1)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(1)
    label(410)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg563')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(411)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(411)
    label(1410)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg563')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(1411)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(1411)
    label(2410)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg563')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(2411)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(2411)
    label(430)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    Voiceline('kg567')
    sprite('kg610_11', 6)
    DemoEndOnVoiceEnd(1)
    label(431)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(431)
    label(440)
    StayAfterMovement(1, 0)
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 32767)
    Voiceline('kg569')
    DemoEndOnVoiceEnd(1)
    loopRest()
    label(666)
    sprite('kg610_00', 6)
    StayAfterMovement(1, 0)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 6)
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    if random_(2, 0, 50):
        Voiceline('kg406')
    else:
        Voiceline('kg408')
    DemoEndOnVoiceEnd(1)
    sprite('kg610_11', 6)
    label(667)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    gotoLabel(667)


@State
def CmnActLose():
    sprite('kg620_00', 5)
    sprite('kg620_01', 5)
    sprite('kg620_02', 5)
    sprite('kg620_03', 5)
    Voiceline('kg411')
    sprite('kg620_04', 3)
    sprite('kg620_05', 6)
    CreateObject('TimeUpSword', -1)
    ScreenShake(0, 5000)
    sprite('kg620_06', 6)
    sprite('kg620_07', 6)
    sprite('kg620_08', 6)
    sprite('kg620_09', 6)
    sprite('kg620_10', 6)
    sprite('kg620_11', 6)
    sprite('kg620_12', 32767)
    DemoTimer(90)


@State
def EventDefEntryWait():
    label(0)
    sprite('rg000_00', 7)
    sprite('rg000_01', 7)
    sprite('rg000_02', 7)
    sprite('rg000_03', 7)
    sprite('rg000_04', 7)
    sprite('rg000_05', 7)
    sprite('rg000_06', 7)
    sprite('rg000_05', 7)
    sprite('rg000_04', 7)
    sprite('rg000_03', 7)
    sprite('rg000_02', 7)
    sprite('rg000_01', 7)
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
    sprite('kg010_02', 6)
    sprite('kg010_03', 6)
    sprite('kg010_04', 6)
    sprite('kg010_05', 6)
    sprite('kg010_06', 6)
    sprite('kg010_07', 6)
    sprite('kg010_08', 6)
    sprite('kg010_09', 6)
    gotoLabel(0)


@State
def EventCrouchToStand():
    sprite('kg010_00', 4)
    sprite('kg010_01', 4)
    enterState('CmnActStand')


@State
def EventDefWin2():
    XPositionRelativeFacing(-60000)
    label(0)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(0)


@State
def EventKGBladeDown():
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 32767)
    loopRest()


@State
def EventDefChouhatsu():
    sprite('kg300_00', 7)
    sprite('kg300_01', 7)
    sprite('kg300_02', 7)
    sprite('kg300_03', 7)
    sprite('kg300_04', 32767)
    loopRest()


@State
def EventDefChouhatsuEnd():
    sprite('kg300_04', 7)
    sprite('kg300_05', 7)
    sprite('kg300_06', 7)
    sprite('kg300_07', 7)
    sprite('kg300_08', 7)
    sprite('kg300_09', 7)
    loopRest()
    enterState('CmnActStand')


@State
def EventKGWalkEntryWait():
    sprite('null', 1)
    ScreenCollision(0)
    EnableCollision(0)
    sprite('null', 1)
    AddX(-770000)
    sprite('null', 32767)
    loopRest()


@State
def EventKGWalkEntry():
    ScreenCollision(0)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 520000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('kg030_00', 7)
    physicsXImpulse(4500)
    sprite('kg030_01', 7)
    label(0)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def EventKGGirlsEntryWait():
    sprite('kg602_02', 32767)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)


@State
def EventKGGirlsEntryWait2():
    sprite('kg602_01', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg602_00', 32767)


@State
def EventKGGirlsEntry():
    sprite('kg602_01', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg602_02', 6)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventBDashOut():
    sprite('kg033_00', 4)
    ScreenCollision(0)
    WallCollisionDetection(0)
    EnableCollision(0)
    sprite('kg033_01', 4)
    sprite('kg033_02', 4)
    AddX(-20000)
    physicsXImpulse(-61000)
    physicsYImpulse(36000)
    setGravity(1550)
    JumpSoundEffects()
    JumpEffects(3, 100)
    sprite('kg033_02', 4)
    sprite('kg033_03', 4)
    sprite('kg033_04', 5)
    sprite('kg033_05', 5)
    sprite('kg033_06', 5)
    sprite('kg033_07', 5)
    sprite('kg033_08', 5)


@State
def EventTGVSKG():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-300000)
    enterState('EventDefLose')


@State
def EventKGVsCE():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    enterState('EventDefLose')


@State
def EventActionKamae():
    sprite('kg203_00', 6)
    sprite('kg203_01', 6)
    label(0)
    sprite('kg203_02', 6)
    sprite('kg203_03', 6)
    sprite('kg203_04', 6)
    sprite('kg203_05', 6)
    sprite('kg203_06', 6)
    loopRest()
    gotoLabel(0)


@State
def EventActionKamaeEnd():
    sprite('kg203_03', 6)
    sprite('kg203_02', 6)
    sprite('kg203_01', 6)
    sprite('kg203_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefChouhatsu2():
    RunLoopUpon(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    CommonSE('401_nesica_pass')
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    CommonSE('401_nesica_pass')
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    gotoLabel(0)
    label(1)
    sprite('kg300_00', 7)
    sprite('kg300_01', 7)
    sprite('kg300_02', 7)
    sprite('kg300_03', 7)
    sprite('kg300_04', 32767)
    loopRest()


@State
def EventReverseWait():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 10)
    label(0)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('kg003_00', 6)
    sprite('kg003_01', 6)
    sprite('kg003_00', 6)
    Flip()
    label(1)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(1)


@State
def EventKamaeWait():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-100000)
    label(0)
    sprite('kg203_02', 6)
    sprite('kg203_03', 6)
    sprite('kg203_04', 6)
    sprite('kg203_05', 6)
    sprite('kg203_06', 6)
    loopRest()
    gotoLabel(0)


@State
def EventCreateHB():
    sprite('keep', 2)
    CreateObject('EventHB', 0)
    loopRest()
    enterState('EventKamaeWait')


@State
def EventHBKamaeEnd():
    sprite('kg203_03', 6)
    sprite('kg203_02', 6)
    sprite('kg203_01', 6)
    sprite('kg203_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventDefReverseWait():
    sprite('kg003_00', 6)
    sprite('kg003_01', 6)
    sprite('kg003_00', 6)
    Flip()
    label(1)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(1)


@State
def EventDefChouhatsuWait():
    sprite('kg300_04', 32767)
    loopRest()


@State
def EventActionVsCELoop():
    sprite('kg410_00', 6)
    sprite('kg410_09', 6)
    sprite('kg410_10', 6)
    sprite('kg410_11', 6)
    sprite('kg410_12', 6)
    label(0)
    sprite('kg410_13', 6)
    sprite('kg410_14', 6)
    sprite('kg410_15', 6)
    loopRest()
    gotoLabel(0)


@State
def EventActionVsCELoopEnd():
    sprite('kg410_16', 6)
    sprite('kg410_17', 6)
    sprite('kg410_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def EventKGBladeDownToLoop():
    sprite('kg610_08', 6)
    sprite('kg610_09', 6)
    sprite('kg610_10', 6)
    sprite('kg610_11', 6)
    label(0)
    sprite('kg610_12', 5)
    sprite('kg610_13', 5)
    sprite('kg610_14', 5)
    sprite('kg610_15', 5)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_kkvskg_00():
    sprite('kg600_00', 32767)
    uponSendToLabel(32, 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(1)
    sprite('kg600_00', 20)
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    enterState('CmnActStand')


@State
def Act2Event_Down():
    sprite('kg060_14', 32767)


@State
def Act2Event_Recover():
    sprite('kg061_00', 6)
    sprite('kg061_01', 6)
    sprite('kg061_02', 6)
    sprite('kg061_03', 6)
    sprite('kg061_04', 6)
    sprite('kg061_05', 6)
    sprite('kg061_06', 6)
    sprite('kg061_07', 6)
    sprite('kg061_08', 6)
    sprite('kg061_09', 6)
    enterState('CmnActStand')


@State
def Act2Event_Reaciton():
    sprite('kg001_00', 6)
    sprite('kg001_01', 6)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 7)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 7)
    sprite('kg001_03', 7)
    sprite('kg001_02', 7)
    sprite('kg001_03', 7)
    sprite('kg001_04', 7)
    sprite('kg001_03', 7)
    sprite('kg001_01', 6)
    sprite('kg001_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Visibility(1)

        def upon_STATE_END():
            Visibility(0)
    sprite('null', 32767)
    loopRest()


@State
def Act2Event_Chouhatsu():
    sprite('kg300_00', 7)
    sprite('kg300_01', 7)
    sprite('kg300_02', 7)
    sprite('kg300_03', 7)
    sprite('kg300_04', 32767)
    loopRest()


@State
def Act2Event_ChouhatsuEnd():
    sprite('keep', 2)
    sprite('kg300_05', 7)
    sprite('kg300_06', 7)
    sprite('kg300_07', 7)
    sprite('kg300_08', 7)
    sprite('kg300_09', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Win():
    sprite('kg610_00', 6)
    sprite('kg610_01', 6)
    sprite('kg610_02', 6)
    sprite('kg610_03', 6)
    sprite('kg610_04', 6)
    sprite('kg610_05', 6)
    sprite('kg610_06', 6)
    AltKnockdownEffects(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('kg610_07', 32767)
    loopRest()


@State
def Act2Event_WalkIn():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-960000)
        ScreenCollision(0)

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
    label(9)
    sprite('kg030_02', 7)
    physicsXImpulse(5500)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_kgvsmk_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-960000)
        ScreenCollision(0)

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
        uponSendToLabel(32, 2)
    label(9)
    sprite('kg030_02', 7)
    physicsXImpulse(5500)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 1)
    label(1)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('kg072_00', 20)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_3')
    ScreenShake(5000, 30000)
    sprite('kg072_01', 3)
    physicsXImpulse(-50000)
    sprite('kg072_02', 3)
    label(3)
    sprite('kg072_01', 3)
    sprite('kg072_02', 3)
    loopRest()
    gotoLabel(3)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_kgvsmk_01():
    sprite('null', 1)
    EndMomentum(1)
    ScreenShake(20000, 50000)
    CommonSE('100_hit_grap_2')


@State
def Act2Event_kgvsmk_02():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-180000)
    sprite('keep', 1)
    loopRest()
    enterState('Act2Event_Chouhatsu')


@State
def Act2Event_kgvsmk_03():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        uponSendToLabel(32, 0)
    sprite('keep', 2)
    sprite('kg300_05', 7)
    sprite('kg300_06', 7)
    sprite('kg300_07', 7)
    sprite('kg300_08', 7)
    sprite('kg300_09', 7)
    label(9)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('kg077_00', 24)
    CreateParticle('ef_hitmd', 103)
    CommonSE('102_hit_counter_grap_2')
    ScreenShake(30000, 60000)
    sprite('kg077_01', 2)
    physicsXImpulse(-55000)
    sprite('kg077_00ex01', 2)
    sprite('kg077_01ex01', 2)
    sprite('kg077_00ex02', 2)
    sprite('kg077_01ex02', 2)
    sprite('kg077_00ex03', 2)
    sprite('kg077_01ex03', 2)
    sprite('null', 32767)
    EndMomentum(1)
    loopRest()


@State
def Act2Event_kgvsmk_04():
    sprite('null', 1)
    EndMomentum(1)
    ScreenShake(40000, 80000)
    CommonSE('100_hit_grap_3')


@State
def Act2Event_WaitingEntry_01():
    sprite('kg600_00', 32767)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    loopRest()


@State
def Act2Event_WaitingEntry_02():
    sprite('kg600_00', 8)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg600_01', 8)
    sprite('kg600_02', 8)
    sprite('kg600_03', 32767)
    loopRest()


@State
def Act2Event_WaitingEntryEnd():
    sprite('kg600_04', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Walk():
    sprite('kg030_00', 7)
    physicsXImpulse(2000)
    sprite('kg030_01', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_02', 7)
    sprite('kg030_03', 7)
    sprite('kg030_04', 7)
    sprite('kg030_05', 7)
    sprite('kg030_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg030_07', 7)
    sprite('kg030_08', 7)
    sprite('kg030_09', 7)
    sprite('kg030_10', 7)
    sprite('kg030_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    EndMomentum(1)
    enterState('CmnActStand')


@State
def Act2Event_Back():
    sprite('kg031_00', 7)
    physicsXImpulse(-2000)
    sprite('kg031_01', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg031_02', 7)
    sprite('kg031_03', 7)
    sprite('kg031_04', 7)
    sprite('kg031_05', 7)
    sprite('kg031_06', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('kg031_07', 7)
    sprite('kg031_08', 7)
    sprite('kg031_09', 7)
    sprite('kg031_10', 7)
    sprite('kg031_11', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    EndMomentum(1)
    XPositionRelativeFacing(-260000)
    enterState('CmnActStand')


@State
def Act2EventChouhatsu():
    sprite('kg300_00', 7)
    sprite('kg300_01', 7)
    sprite('kg300_02', 7)
    sprite('kg300_03', 7)
    sprite('kg300_04', 32767)
    loopRest()


@State
def Act2EventChouhatsuEnd():
    sprite('kg300_04', 7)
    sprite('kg300_05', 7)
    sprite('kg300_06', 7)
    sprite('kg300_07', 7)
    sprite('kg300_08', 7)
    sprite('kg300_09', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_OverDrive():
    sprite('kg333_00', 6)
    sprite('kg333_01', 6)
    sprite('kg333_02', 6)
    sprite('kg333_03', 32767)
    loopRest()


@State
def Act2Event_Kamae():
    sprite('kg203_00', 6)
    sprite('kg203_01', 6)
    label(0)
    sprite('kg203_02', 6)
    sprite('kg203_03', 6)
    sprite('kg203_04', 6)
    sprite('kg203_05', 6)
    sprite('kg203_06', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_KamaeEnd():
    sprite('kg203_03', 6)
    sprite('kg203_02', 6)
    sprite('kg203_01', 6)
    sprite('kg203_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_OverDriveActivate():
    sprite('keep', 2)
    sprite('kg333_04', 4)
    CommonSE('302_spsys_drivemotion')
    CommonSE('302_spsys_burst')
    ScreenShake(30000, 60000)
    label(0)
    sprite('kg333_05', 5)
    sprite('kg333_06', 5)
    sprite('kg333_07', 5)
    loopRest()
    gotoLabel(0)


@State
def Act2Event_OverDriveEnd():
    sprite('keep', 2)
    sprite('kg333_08', 6)
    sprite('kg333_09', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Posing():
    sprite('kg070_13', 6)
    sprite('kg070_12', 6)
    sprite('kg070_11', 32767)
    loopRest()


@State
def Act2Event_PosingEnd():
    sprite('kg070_12', 5)
    sprite('kg070_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Yoroke():
    sprite('kg070_02', 15)
    sprite('kg070_03', 32767)
    loopRest()


@State
def Act2Event_YorokeToDown():
    sprite('kg070_04', 6)
    sprite('kg070_05', 6)
    sprite('kg070_06', 6)
    sprite('kg070_07', 6)
    sprite('kg070_08', 6)
    sprite('kg070_09', 6)
    sprite('kg063_09', 6)
    CreateParticle('ef_grndshock', 104)
    CommonSE('209_down_normal_0')
    sprite('kg063_10', 32767)


@State
def Act2Event_YorokeEnd():
    sprite('kg070_10', 5)
    sprite('kg070_11', 5)
    sprite('kg070_12', 5)
    sprite('kg070_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_kgvsaz_00():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('kg070_00', 15)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 103)
    CommonSE('102_hit_counter_grap_1')
    AddInertia(-11000)
    ScreenShake(10000, 30000)
    sprite('kg070_01', 4)
    sprite('kg070_02', 4)
    sprite('kg070_03', 32767)
    loopRest()


@State
def Act2Event_kgvsaz_01():
    sprite('kg032_00', 4)
    sprite('kg032_01', 4)
    sprite('kg032_02', 3)
    physicsXImpulse(8000)
    sprite('kg032_02', 2)
    physicsXImpulse(20000)
    sprite('kg032_03', 3)
    sprite('kg032_10', 3)
    XImpulseAcceleration(30)
    LandingEffects(100, 1, 1)
    sprite('kg032_11', 3)
    sprite('kg032_12', 3)
    XImpulseAcceleration(50)
    sprite('kg032_13', 3)
    EndMomentum(1)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_Crouch2Stand():
    sprite('kg010_01', 4)
    sprite('kg010_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act2Event_YureMotion():
    sprite('kg050_00', 4)
    CreateObject('Act2Event_Yure', -1)
    sprite('kg050_01', 6)
    sprite('kg050_02', 6)
    sprite('kg050_01', 6)
    sprite('kg050_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_rgvskg_00():
    sprite('kg600_00', 2)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg600_00', 32767)
    loopRest()


@State
def Act3Event_rgvskg_01():
    sprite('kg600_00', 2)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg600_01', 6)
    sprite('kg600_02', 6)
    sprite('kg600_03', 32767)
    loopRest()


@State
def Act3Event_rgvskg_02():
    sprite('kg600_04', 6)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_rgvskg_03():
    sprite('kg001_00', 7)
    sprite('kg001_01', 7)
    sprite('kg001_02', 32767)
    loopRest()


@State
def Act3Event_rgvskg_04():
    sprite('kg001_02', 7)
    sprite('kg001_01', 7)
    sprite('kg001_00', 7)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_rgvskg_05():
    sprite('kg202_06', 3)
    PrivateSE('kgse_01')
    sprite('kg202_07', 2)
    AltKnockdownEffects(100, 1, 0)
    sprite('kg202_08', 13)
    sprite('kg202_09', 3)
    sprite('kg202_10', 4)
    sprite('kg202_11', 4)
    sprite('kg202_12', 5)
    sprite('kg202_13', 5)
    sprite('kg202_14', 4)
    sprite('kg202_15', 4)
    sprite('kg202_16', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_rgvskg_06():
    sprite('kg050_00', 5)
    sprite('kg050_01', 10)
    sprite('kg050_00', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_jnvskg_00():
    sprite('kg202_06', 3)
    PrivateSE('kgse_01')
    sprite('kg202_07', 2)
    AltKnockdownEffects(100, 1, 0)
    sprite('kg202_08', 23)
    sprite('kg202_09', 3)
    sprite('kg202_10', 4)
    sprite('kg202_11', 4)
    sprite('kg202_12', 6)
    sprite('kg202_13', 7)
    sprite('kg202_14', 6)
    sprite('kg202_15', 6)
    sprite('kg202_16', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvskg_00():

    def upon_IMMEDIATE():
        CreateObject('EntrySword', -1)
        RegisterObject(4, 1)
    sprite('kg602_00', 32767)


@State
def Act3Event_mkvskg_01():

    def upon_IMMEDIATE():
        CreateObject('EntrySword', -1)
        RegisterObject(4, 1)
    sprite('kg602_00', 6)
    sprite('kg602_01', 6)
    sprite('kg602_02ex1', 32767)


@State
def Act3Event_mkvskg_02():

    def upon_IMMEDIATE():
        CreateObject('EntrySword', -1)
        RegisterObject(4, 1)
    sprite('kg602_03', 6)
    sprite('kg602_04', 6)
    sprite('kg602_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_09', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_10', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_11', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_12', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_13', 6)
    CommonSE('008_swing_pole_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mkvskg_03():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-160000)
    sprite('kg000_00', 7)
    sprite('kg070_00', 17)
    CreateParticle('ef_hitmd', 103)
    CommonSE('100_hit_grap_1')
    ScreenShake(1000, 20000)
    sprite('kg070_01', 4)
    AddInertia(-11000)
    sprite('kg070_02', 4)
    sprite('kg070_03', 32767)
    loopRest()


@State
def Act3Event_mkvskg_04():
    sprite('kg070_10', 5)
    sprite('kg070_11', 5)
    sprite('kg070_12', 5)
    sprite('kg070_13', 5)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_mivskg_00():
    sprite('kg600_00', 32767)
    uponSendToLabel(32, 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(1)
    sprite('kg600_00', 10)
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kgvsrg_00():
    sprite('kg600_00', 32767)
    AddX(80000)
    uponSendToLabel(32, 1)
    CreateObject('EntrySword', -1)
    RegisterObject(4, 1)
    label(1)
    sprite('kg600_00', 10)
    sprite('kg600_04', 6)
    sprite('kg600_05', 6)
    sprite('kg600_06', 6)
    sprite('kg600_07', 6)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    ObjectUpon(FALLING, 32)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_08', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_09', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_10', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_11', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_12', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_13', 6)
    CommonSE('004_swing_grap_1_2')
    sprite('kg600_14', 6)
    CommonSE('100_hit_grap_0')
    DeleteObject(4)
    sprite('kg600_15', 6)
    sprite('kg600_16', 6)
    sprite('kg600_17', 6)
    sprite('kg600_18', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kgvsrg_01():
    sprite('kg040_02', 3)
    sprite('kg090_00', 14)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdm', 103)
    CommonSE('105_guard_slash_2')
    ScreenShake(5000, 20000)
    sprite('kg090_01', 4)
    AddInertia(-11000)
    sprite('kg090_02', 4)
    sprite('kg090_03', 4)
    sprite('kg090_04', 5)
    sprite('kg090_04', 1)
    EndMomentum(1)
    sprite('kg090_04', 1)
    XPositionRelativeFacing(-260000)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kgvsrg_02():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
        AddX(90000)
    sprite('kg202_00', 3)
    sprite('kg202_01', 2)
    sprite('kg202_02', 2)
    sprite('kg202_03', 2)
    sprite('kg202_04', 3)
    sprite('kg202_05', 3)
    sprite('kg202_06', 3)
    PrivateSE('kgse_01')
    sprite('kg202_07', 12)
    AltKnockdownEffects(100, 1, 0)
    CreateObject('efkg_202', -1)
    CreateObject('Eventoffset_Sosai_kgvsrg', 0)
    sprite('kg090_01', 2)
    ScreenShake(5000, 20000)
    sprite('kg090_01', 2)
    AddInertia(-11000)
    sprite('kg090_02', 4)
    sprite('kg090_03', 4)
    sprite('kg090_04', 5)
    sprite('kg090_04', 1)
    EndMomentum(1)
    sprite('kg090_04', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_kgvshb_00():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)
    sprite('kg211_00', 2)
    sprite('kg211_01', 2)
    sprite('kg211_02', 3)
    sprite('kg211_03', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('kg211_04', 17)
    ObjectUpon(22, 32)
    sprite('kg211_05', 2)
    sprite('kg211_06', 3)
    sprite('kg211_07', 3)
    sprite('kg211_08', 4)
    sprite('kg211_09', 4)
    sprite('kg211_10', 4)
    sprite('kg211_11', 4)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Turn():
    sprite('kg003_00ex', 3)
    Flip()
    sprite('kg003_01', 3)
    sprite('kg003_00', 3)
    label(0)
    sprite('kg000_00', 7)
    sprite('kg000_01', 7)
    sprite('kg000_02', 7)
    sprite('kg000_03', 7)
    sprite('kg000_04', 7)
    sprite('kg000_05', 7)
    sprite('kg000_06', 7)
    sprite('kg000_07', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_DashOut():
    sprite('kg032_00', 2)
    physicsXImpulse(14400)
    SetAcceleration(250)
    EnableCollision(0)
    ScreenCollision(0)
    sprite('kg032_01', 2)
    sprite('kg032_02', 4)
    sprite('kg032_03', 4)
    DashEffects(100, 1, 1)
    sprite('kg032_04', 4)
    sprite('kg032_05', 4)
    sprite('kg032_06', 4)
    sprite('kg032_07', 4)
    DashEffects(100, 1, 1)
    sprite('kg032_08', 4)
    sprite('kg032_09', 4)
    loopRest()
    sprite('kg032_02', 4)
    sprite('kg032_03', 4)
    DashEffects(100, 1, 1)
    sprite('kg032_04', 4)
    sprite('kg032_05', 4)
    sprite('kg032_06', 4)
    sprite('kg032_07', 4)
    DashEffects(100, 1, 1)
    sprite('kg032_08', 4)
    sprite('kg032_09', 4)
    loopRest()
    sprite('kg032_02', 4)
    sprite('kg032_03', 4)
    sprite('kg032_04', 4)
    sprite('kg032_05', 4)
    sprite('kg032_06', 4)
    sprite('kg032_07', 4)
    sprite('kg032_08', 4)
    sprite('kg032_09', 4)
    sprite('null', 32767)
    loopRest()


@State
def Act3Event_kgvsmu_00():

    def upon_IMMEDIATE():
        AddX(-80000)
    label(0)
    sprite('kg233_03', 5)
    sprite('kg233_04', 5)
    sprite('kg233_05', 5)
    sprite('kg233_06', 5)
    sprite('kg233_02', 5)
    gotoLabel(0)


@State
def Act3Event_kgvsmu_01():

    def upon_IMMEDIATE():
        StayAfterMovement(1, 0)

        def upon_FALLING():
            clearUponHandler(FALLING)
            setGravity(5000)
            sendToLabel(1)
        uponSendToLabel(LANDING, 2)
    sprite('kg233_02', 3)
    sprite('kg406_00', 3)
    physicsXImpulse(10000)
    physicsYImpulse(22000)
    setGravity(3000)
    JumpEffects(1, 0)
    sprite('kg406_01', 3)
    label(0)
    sprite('kg406_02', 3)
    sprite('kg406_03', 3)
    sprite('kg406_04', 3)
    gotoLabel(0)
    label(1)
    sprite('kg406_05', 3)
    sprite('kg406_06', 32767)
    PrivateSE('kgse_01')
    label(2)
    sprite('kg406_07', 3)
    CreateObject('406slash00', -1)
    EndMomentum(1)
    SetXCollisionFromOrigin(200)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('kgse_03')
    AbsoluteY(0)
    CreateObject('Eventoffset_Sosai_kgvsmu', 0)
    sprite('kg406_07', 1)
    AddX(3000)
    sprite('kg406_07', 1)
    AddX(-3000)
    sprite('kg406_07', 1)
    AddX(3000)
    sprite('kg406_07', 1)
    AddX(-3000)
    sprite('kg406_07', 1)
    AddX(3000)
    sprite('kg406_07', 1)
    AddX(-3000)
    sprite('kg406_07', 1)
    AddX(3000)
    sprite('kg406_07', 1)
    AddX(-3000)
    sprite('kg406_07', 1)
    AddX(3000)
    sprite('kg406_07', 1)
    AddX(-3000)
    sprite('kg090_01', 4)
    AddInertia(-11000)
    sprite('kg090_02', 4)
    sprite('kg090_03', 4)
    sprite('kg090_04', 5)
    sprite('kg090_04', 1)
    EndMomentum(1)
    sprite('kg090_04', 1)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_Kamae2():
    sprite('kg213_00', 4)
    sprite('kg213_01', 4)
    label(0)
    sprite('kg213_02', 5)
    sprite('kg213_03', 5)
    sprite('kg213_04', 5)
    sprite('kg213_05', 5)
    sprite('kg213_06', 5)
    gotoLabel(0)


@State
def Act3Event_Kamae2End():
    sprite('kg213_01', 6)
    sprite('kg213_00', 6)
    loopRest()
    enterState('CmnActStand')


@State
def Act3Event_OverDrive():
    sprite('kg333_00', 5)
    sprite('kg333_01', 5)
    sprite('kg333_02', 5)
    sprite('kg333_03', 32767)


@State
def Act3Event_OverDriveEnd():
    sprite('kg333_04', 3)
    sprite('kg333_05', 6)
    CommonSE('302_spsys_burst')
    E0EAEffect('GuardCrushWind', 65535)
    ScreenShake(3000, 50000)

    def RunOnObject_1():
        Size(1400)
    sprite('kg333_06', 6)
    sprite('kg333_07', 6)
    sprite('kg333_05', 6)
    sprite('kg333_06', 6)
    sprite('kg333_07', 6)
    sprite('kg333_06', 6)
    sprite('kg333_05', 6)
    sprite('kg333_08', 6)
    sprite('kg333_09', 6)
    loopRest()
    enterState('CmnActStand')
