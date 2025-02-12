@State
def IgnisCreate():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        NoDamageAction(1)
        SLOT_89 = 50
        ShadowOffsetY(-75000)
        AddX(-460000)
        AbsoluteY(0)
        CreateDecalOn(1)
        FloorCollision(1)
        SLOT_59 = -150000
        SLOT_61 = 2
    sprite('null', 32767)
    Visibility(1)
    SLOT_63 = 0
    PrivateFunction2('IGAct_Wait', 100)


@Subroutine
def OnFrameStep():
    if SLOT_OverdriveTimer:
        SLOT_63 = 0
        if SLOT_62 > 0:
            SLOT_61 = -15
        else:
            SLOT_61 = -45
    else:
        SLOT_61 = 2

    def upon_59():
        SLOT_61 = 2
    if SLOT_65:
        SLOT_65 = SLOT_65 + -1


@Subroutine
def IG_ActReset():
    CallObject('')
    AttackDefaults_Projectile()
    AttackOff()
    ResourceBarIcon(0, 35)
    ColorForTransition(4294967295)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    EnableCollision(0)
    WallCollisionDetection(1)
    SetZVal(500)
    IgnoreScreenfreeze(0)
    BlendMode_Off()
    ForceShadowOn(1)
    HitBackReturnObject(1)
    SLOT_5 = 0

    def upon_53():
        EndObject()


@Subroutine
def IG_SetupIntrptSignal():

    def upon_VALUE_RECEIVED():
        if SLOT_ReceivedValue == 1:
            PrivateFunction2('IGAct_Startup', 900)
        if SLOT_ReceivedValue == 21:
            PrivateFunction2('IGAct_Delete', 900)
        if SLOT_ReceivedValue == 101:
            PrivateFunction2('IGAct_Attack01', 50)
        if SLOT_ReceivedValue == 102:
            PrivateFunction2('IGAct_Attack02', 50)
        if SLOT_ReceivedValue == 103:
            PrivateFunction2('IGAct_Attack03', 50)
        if SLOT_ReceivedValue == 201:
            PrivateFunction2('IGAct_AirAttack01', 50)
        if SLOT_ReceivedValue == 202:
            PrivateFunction2('IGAct_AirAttack02', 50)
        if SLOT_ReceivedValue == 203:
            PrivateFunction2('IGAct_AirAttack03', 50)
        if SLOT_ReceivedValue == 301:
            PrivateFunction2('IGAct_SpAttack01', 100)
        if SLOT_ReceivedValue == 302:
            PrivateFunction2('IGAct_SpAttack02', 100)
        if SLOT_ReceivedValue == 303:
            PrivateFunction2('IGAct_SpAttack03', 100)
        if SLOT_ReceivedValue == 304:
            PrivateFunction2('IGAct_SpAttack04', 100)
        if SLOT_ReceivedValue == 305:
            PrivateFunction2('IGAct_SpAttack05', 100)
        if SLOT_ReceivedValue == 401:
            SLOT_64 = SLOT_49
            PrivateFunction2('IGAct_AirSpAttack01', 100)
        if SLOT_ReceivedValue == 402:
            PrivateFunction2('IGAct_SpThrow', 100)
        if SLOT_ReceivedValue == 501:
            PrivateFunction2('IGAct_AddAttack01', 100)
        if SLOT_ReceivedValue == 502:
            PrivateFunction2('IGAct_AddAttack02', 100)
        if SLOT_ReceivedValue == 503:
            PrivateFunction2('IGAct_AddAttack03', 100)
        if SLOT_ReceivedValue == 601:
            PrivateFunction2('IGAct_DDAttack01', 200)
        if SLOT_ReceivedValue == 603:
            PrivateFunction2('IGAct_DDAttack01OD', 200)
        if SLOT_ReceivedValue == 602:
            PrivateFunction2('IGAct_DDAttack02', 200)
        if SLOT_ReceivedValue == 604:
            PrivateFunction2('IGAct_DDAttack02OD', 200)
        if SLOT_ReceivedValue == 701:
            PrivateFunction2('IGAct_AstralHeat', 200)
        if SLOT_ReceivedValue == 801:
            PrivateFunction2('IGAct_MatchWin1', 200)
        if SLOT_ReceivedValue == 901:
            PrivateFunction2('IGAct_EventVsCA00', 200)
        if SLOT_ReceivedValue == 1001:
            PrivateFunction2('IGAct_EventAct2_azvsrl', 200)
        if SLOT_ReceivedValue == 810:
            PrivateFunction2('IGAct_EntryVsCa0', 200)
        if SLOT_ReceivedValue == 811:
            PrivateFunction2('IGAct_EntryVsCa1', 200)
        if SLOT_ReceivedValue == 814:
            PrivateFunction2('IGAct_EntryVsRg0', 200)
        if SLOT_ReceivedValue == 830:
            PrivateFunction2('IGAct_EntryVsHa0', 200)
        if SLOT_ReceivedValue == 840:
            PrivateFunction2('IGAct_EntryVsVh0', 200)
        if SLOT_ReceivedValue == 850:
            PrivateFunction2('IGAct_EntryVsCaAct3_0', 200)
        if SLOT_ReceivedValue == 820:
            if SLOT_4 == 2:
                PrivateFunction2('IGAct_Delete', 200)
        if SLOT_ReceivedValue == 821:
            PrivateFunction2('IGAct_SwitchFollow', 200)


@Subroutine
def IG_AttackInit():
    callSubroutine('IG_ActReset')
    callSubroutine('IG_SetupIntrptSignal')
    CallObject('IgnisAttack')
    SLOT_4 = 10
    SLOT_53 = 1
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    DollAttackAttributes(1)
    if SLOT_OverdriveTimer:
        SLOT_55 = 1
    if SLOT_66:
        EnableCollision(1)


@Subroutine
def IG_SpAttackInit():
    if SLOT_4 == 0:
        SLOT_51 = 1
    callSubroutine('IG_ActReset')
    CallObject('IgnisAttack')
    SLOT_4 = 11
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    DollAttackAttributes(1)
    if SLOT_OverdriveTimer:
        SLOT_55 = 1


@Subroutine
def IG_DDAttackInit():
    if SLOT_4 == 0:
        SLOT_51 = 1
    callSubroutine('IG_ActReset')
    AttackDefaults_SuperProjectile()
    CallObject('IgnisAttack')
    SLOT_4 = 11
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    DollAttackAttributes(1)


@Subroutine
def IG_AHAttackInit():
    if SLOT_4 == 0:
        SLOT_51 = 1
    callSubroutine('IG_ActReset')
    AttackDefaults_AstralHeatProjectile()
    CallObject('IgnisAttack')
    SLOT_4 = 11
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    DollAttackAttributes(1)


@Subroutine
def IG_FollowInit():
    callSubroutine('IG_ActReset')
    callSubroutine('IG_SetupIntrptSignal')
    CallObject('IgnisFollow')
    NoDamageAction(1)
    SLOT_4 = 2


@Subroutine
def IG_DamageInit():
    callSubroutine('IG_ActReset')
    CallObject('IgnisDamage')
    NoDamageAction(1)
    SLOT_4 = 20


@State
def IGAct_Wait():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        callSubroutine('IG_SetupIntrptSignal')
        NoDamageAction(1)
        SLOT_4 = 0
        ResourceBarIcon(0, 37)
        ResourceGaugeX(0, 0)

    def upon_EVERY_FRAME():
        if SLOT_62 > 0:
            SLOT_62 = SLOT_62 + -1
            ResourceBarColor(0, 4278234042)
            ResourceBarFullColor(0, 4278234042)
        else:
            ResourceBarColor(0, 4291559526)
            ResourceBarFullColor(0, 4294967295)
        if SLOT_63 > 0:
            SLOT_63 = SLOT_63 + -1
        elif SLOT_62 > 0:
            if SLOT_OverdriveTimer:
                SLOT_31 = SLOT_31 + 50
            else:
                SLOT_31 = SLOT_31 + 0
        elif SLOT_OverdriveTimer:
            SLOT_31 = SLOT_31 + 75
        else:
            SLOT_31 = SLOT_31 + 75
    sprite('null', 32767)
    Visibility(1)
    loopRest()


@State
def IGAct_Startup():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        SLOT_4 = 1
        NoDamageAction(1)
        BlendMode_Normal()
    sprite('rl800_00', 4)
    TeleportToObject(2)
    TurnAround()
    AddX(-150000)
    AddY(0)
    Visibility(1)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    Visibility(0)
    StopCharacterFlash1(16777215)
    CharacterFlash2(0, 10)
    sprite('rl800_00', 2)
    StopCharacterFlash2()
    SetScaleXPerFrame(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_Delete():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        SLOT_4 = 3
        NoDamageAction(1)
    sprite('rl800_00', 15)
    sprite('rl800_00', 10)
    if SLOT_11:
        SLOT_31 = 0
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    sprite('keep', 100)
    if SLOT_OverdriveTimer:
        SLOT_63 = 0
    else:
        SLOT_63 = 180
    PrivateFunction2('IGAct_Wait', 100)


@State
def IGAct_DamageDelete():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        SLOT_4 = 3
        NoDamageAction(1)
    sprite('rl800_00', 15)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    sprite('keep', 100)
    if SLOT_62 <= 0:
        SLOT_62 = 261
        ResourceBarColor(0, 4278234042)
        ResourceBarFullColor(0, 4278234042)
    SLOT_63 = 0
    PrivateFunction2('IGAct_Wait', 100)


@State
def IGAct_OverHeat():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        SLOT_4 = 30
        ResourceBarIcon(0, 35)
        ResourceGaugeX(0, 1)
        ResourceBarColor(0, 4284506208)
        NoDamageAction(1)

    def upon_EVERY_FRAME():
        if SLOT_OverdriveTimer:
            SLOT_31 = SLOT_31 + 75
        else:
            SLOT_31 = SLOT_31 + 15
        if SLOT_31 >= 10000:
            ResourceGaugeFlash(0, 1)
            sendToLabel(1)
    sprite('rl814_00', 7)
    physicsYImpulse(-5000)
    CommonSE('014_electric_l')
    sprite('rl814_01', 7)
    CommonSE('014_electric_l')
    sprite('rl814_02', 7)
    CommonSE('014_electric_l')
    sprite('rl814_03', 7)
    sprite('rl814_04', 7)
    sprite('rl814_05', 7)
    CommonSE('014_electric_ml')
    sprite('rl814_06', 7)
    sprite('rl814_07', 7)
    sprite('rl814_08', 7)
    CommonSE('014_electric_sl')
    sprite('rl814_09', 7)
    label(0)
    sprite('rl814_10', 7)
    CreateParticle('rlef_ig_break', 0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rl814_10', 9)
    SLOT_62 = 0
    ResourceBarColor(0, 4291559526)
    ResourceBarFullColor(0, 4294967295)
    clearUponHandler(EVERY_FRAME)
    sprite('rl814_11', 8)
    sprite('rl814_12', 8)
    sprite('rl814_13', 8)
    sprite('rl814_14', 8)
    sprite('rl814_15', 8)
    sprite('rl814_16', 8)
    sprite('rl814_17', 8)
    sprite('rl814_18', 8)
    sprite('rl800_00', 15)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    sprite('keep', 100)
    SLOT_63 = 0
    PrivateFunction2('IGAct_Wait', 100)


@State
def IGAct_SwitchFollow():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
        SLOT_65 = 60
    sprite('keep', 32767)
    loopRest()


@State
def IGAct_Follow():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl800_07', 5)
    label(0)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(0)


@State
def IGAct_FMove():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl801_00', 2)
    label(0)
    sprite('rl801_01', 6)
    sprite('rl801_02', 6)
    sprite('rl801_03', 6)
    sprite('rl801_04', 6)
    sprite('rl801_05', 6)
    sprite('rl801_06', 6)
    sprite('rl801_07', 6)
    sprite('rl801_08', 6)
    loopRest()
    gotoLabel(0)


@State
def IGAct_FMoveEnd():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl801_00', 2)
    sprite('rl800_07', 2)
    sprite('keep', 32767)
    PrivateFunction2('IGAct_Follow', 100)


@State
def IGAct_BMove():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl802_00', 2)
    label(0)
    sprite('rl802_01', 6)
    sprite('rl802_02', 6)
    sprite('rl802_03', 6)
    sprite('rl802_04', 6)
    sprite('rl802_05', 6)
    sprite('rl802_06', 6)
    sprite('rl802_07', 6)
    sprite('rl802_08', 6)
    loopRest()
    gotoLabel(0)


@State
def IGAct_BMoveEnd():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl802_00', 2)
    sprite('rl800_07', 2)
    sprite('keep', 32767)
    PrivateFunction2('IGAct_Follow', 100)


@State
def IGAct_Turn():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
        Flip()
    sprite('rl807_01ex01', 3)
    sprite('rl807_00', 3)
    sprite('rl807_01', 3)
    sprite('keep', 32767)
    PrivateFunction2('IGAct_Follow', 100)


@State
def IGAct_Jump():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl811_00', 3)
    sprite('rl811_01', 3)
    sprite('rl811_02', 3)
    sprite('rl815_00', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_AirRelay', 100)


@State
def IGAct_AirF():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl808_00', 3)
    label(0)
    sprite('rl808_01', 7)
    sprite('rl808_02', 7)
    sprite('rl808_03', 7)
    sprite('rl808_04', 7)
    sprite('rl808_05', 7)
    loopRest()
    gotoLabel(0)


@State
def IGAct_AirFEnd():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl808_00', 3)
    sprite('rl815_00', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_AirRelay', 100)


@State
def IGAct_AirB():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl809_00', 3)
    label(0)
    sprite('rl809_01', 7)
    sprite('rl809_02', 7)
    sprite('rl809_03', 7)
    sprite('rl809_04', 7)
    sprite('rl809_05', 7)
    loopRest()
    gotoLabel(0)


@State
def IGAct_AirBEnd():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl809_00', 3)
    sprite('rl815_00', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_AirRelay', 100)


@State
def IGAct_AirD():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl813_00', 3)
    label(0)
    sprite('rl813_01', 7)
    sprite('rl813_02', 7)
    sprite('rl813_03', 7)
    loopRest()
    gotoLabel(0)


@State
def IGAct_AirDEnd():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl813_00', 3)
    sprite('rl815_00', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_AirRelay', 100)


@State
def IGAct_AirRelay():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('keep', 32767)
    loopRest()


@State
def IGAct_AirTurn():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
        Flip()
    sprite('rl810_01ex00', 4)
    sprite('rl810_00', 4)
    sprite('rl810_01', 4)
    sprite('keep', 100)
    PrivateFunction2('IGAct_AirRelay', 100)


@State
def IGAct_Landing():

    def upon_IMMEDIATE():
        callSubroutine('IG_FollowInit')
    sprite('rl812_00', 3)
    sprite('rl812_01', 3)
    sprite('rl812_02', 3)
    sprite('rl812_03', 3)
    sprite('rl812_04', 3)
    sprite('keep', 32767)
    PrivateFunction2('IGAct_Follow', 100)


@State
def IGAct_ReliusDamage():

    def upon_IMMEDIATE():
        callSubroutine('IG_DamageInit')
    sprite('rl804_00', 3)
    sprite('rl804_01', 3)
    sprite('rl804_02', 3)
    sprite('rl804_03', 3)
    sprite('rl804_04', 3)
    sprite('rl804_03', 3)
    sprite('rl804_02', 3)
    sprite('rl804_01', 3)
    sprite('rl804_00', 3)
    sprite('keep', 32767)
    PrivateFunction2('IGAct_DamageEnd', 100)


@State
def IGAct_DamageBody():

    def upon_IMMEDIATE():
        callSubroutine('IG_DamageInit')
    sprite('rl803_00', 3)
    sprite('rl803_01', 3)
    sprite('rl803_02', 3)
    sprite('rl803_03', 3)
    sprite('rl803_04', 3)
    sprite('rl803_03', 3)
    sprite('rl803_02', 3)
    sprite('rl803_01', 3)
    sprite('rl803_00', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_DamageEnd', 100)


@State
def IGAct_DamageLeg():

    def upon_IMMEDIATE():
        callSubroutine('IG_DamageInit')
    sprite('rl804_00', 3)
    sprite('rl804_01', 3)
    sprite('rl804_02', 3)
    sprite('rl804_03', 3)
    sprite('rl804_04', 3)
    sprite('rl804_03', 3)
    sprite('rl804_02', 3)
    sprite('rl804_01', 3)
    sprite('rl804_00', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_DamageEnd', 100)


@State
def IGAct_DamageEnd():

    def upon_IMMEDIATE():
        callSubroutine('IG_DamageInit')
    sprite('keep', 32767)
    loopRest()


@State
def IGAct_Attack01():

    def upon_IMMEDIATE():
        callSubroutine('IG_AttackInit')
        AttackLevel_(2)
        Damage(560)
        UseSlashHitspark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl800_00', 3)
    sprite('rl820_00', 2)
    sprite('rl820_01', 2)
    SLOT_31 = SLOT_31 + -1300
    sprite('rl820_02', 2)
    sprite('rl820_03', 2)
    sprite('rl820_04', 2)
    AddX(40000)
    physicsXImpulse(12000)
    sprite('rl820_04', 3)
    physicsXImpulse(80000)
    CommonSE('005_swing_grap_2_2')
    sprite('rl820_05', 3)
    physicsXImpulse(0)
    RefreshMultihit()
    CreateObject('zan_5D', -1)
    sprite('rl820_06', 4)
    if SLOT_55:
        sendToLabel(30)
    sprite('rl820_07', 4)
    sprite('rl820_08', 4)
    sprite('rl820_09', 4)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl820_06', 1)
    sprite('rl820_07', 2)
    sprite('rl820_08', 2)
    sprite('rl820_09', 2)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_Attack02():

    def upon_IMMEDIATE():
        callSubroutine('IG_AttackInit')
        AttackLevel_(1)
        Damage(620)
        AirPushbackY(15000)
        PushbackX(7000)
        AirUntechableTime(20)
        Hitstun(16)
        Hitstop(6)
        UseSlashHitspark(1)
        StayAfterMovement(1, 0)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl821_00', 3)
    sprite('rl821_01', 3)
    sprite('rl821_02', 3)
    SLOT_31 = SLOT_31 + -2000
    sprite('rl821_03', 3)
    sprite('rl821_04', 3)
    sprite('rl821_05', 3)
    sprite('rl821_06', 3)
    sprite('rl821_07', 3)
    CommonSE('006_swing_blade_1')
    sprite('rl821_08', 3)
    CreateParticle('rlef_deleteaura', 0)
    CreateParticle('rlef_deleteaura', 1)
    CreateParticle('rlef_deleteaura', 2)
    RefreshMultihit()
    sprite('rl821_09', 9)
    sprite('rl821_10', 3)
    CommonSE('006_swing_blade_1')
    sprite('rl821_11', 3)
    CreateParticle('rlef_deleteaura', 0)
    CreateParticle('rlef_deleteaura', 1)
    RefreshMultihit()
    AttackLevel_(1)
    Damage(780)
    Hitstop(7)
    AirPushbackX(-10000)
    PushbackX(-24000)
    sprite('rl821_12', 3)
    if SLOT_55:
        sendToLabel(30)
    sprite('rl821_13', 6)
    sprite('rl821_14', 6)
    sprite('rl821_15', 6)
    sprite('rl821_16', 6)
    sprite('rl821_17', 6)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    label(30)
    sprite('rl821_12', 2)
    sprite('rl821_13', 2)
    sprite('rl821_14', 2)
    sprite('rl821_15', 2)
    sprite('rl821_16', 2)
    sprite('rl821_17', 2)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_Attack03():

    def upon_IMMEDIATE():
        callSubroutine('IG_AttackInit')
        AttackLevel_(4)
        Damage(850)
        AttackP1(80)
        AttackP2(82)
        BonusProration(110)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(30)
        AirPushbackY(38400)
        AirPushbackX(9000)
        HitAirUnblockable(3)
        UseSlashHitspark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        NonCornerWallbounce(1)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(3)
        Wallbounce(1)
        EndMomentum(0)
        RefreshMultihit()
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl843_00', 2)
    sprite('rl843_01', 3)
    sprite('rl843_02', 4)
    SLOT_31 = SLOT_31 + -1000
    sprite('rl843_03', 4)
    sprite('rl843_04', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('rl843_05', 9)
    sprite('rl843_06', 3)
    if SLOT_55:
        sendToLabel(30)
    sprite('rl843_07', 3)
    sprite('rl843_08', 3)
    sprite('rl843_09', 3)
    sprite('rl843_10', 3)
    sprite('rl843_11', 3)
    sprite('rl843_12', 3)
    sprite('rl843_13', 3)
    sprite('rl843_14', 3)
    sprite('rl843_15', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl843_06', 1)
    sprite('rl843_07', 1)
    sprite('rl843_08', 1)
    sprite('rl843_09', 1)
    sprite('rl843_10', 1)
    sprite('rl843_11', 1)
    sprite('rl843_12', 1)
    sprite('rl843_13', 1)
    sprite('rl843_14', 1)
    sprite('rl843_15', 1)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AirAttack01():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackLevel_(4)
        Damage(900)
        AirPushbackX(12000)
        AirPushbackY(20000)
        AttackP1(80)
        UseSlashHitspark(1)
        MoveAttributes(1, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_54:
                if SLOT_19 < 100000:
                    sendToLabel(0)
                    SLOT_54 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('Act_IG_AirAttack01', 32)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl830_00', 3)
    sprite('rl830_01', 3)
    physicsXImpulse(15000)
    sprite('rl830_02', 2)
    SLOT_31 = SLOT_31 + -1000
    physicsXImpulse(58000)
    SLOT_54 = 1
    sprite('rl830_01', 2)
    sprite('rl830_03', 2)
    sprite('rl830_04', 2)
    physicsXImpulse(30000)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('rl830_04', 1)
    CommonSE('006_swing_blade_2')
    sprite('rl830_05', 4)
    RefreshMultihit()
    CreateObject('air_5D', -1)
    physicsXImpulse(10000)
    sprite('rl830_06', 4)
    if SLOT_55:
        sendToLabel(30)
    physicsXImpulse(8000)
    sprite('rl830_07', 4)
    physicsXImpulse(4000)
    sprite('rl830_08', 4)
    physicsXImpulse(2000)
    sprite('rl830_09', 4)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl830_06', 1)
    physicsXImpulse(8000)
    sprite('rl830_07', 1)
    physicsXImpulse(4000)
    sprite('rl830_08', 1)
    physicsXImpulse(2000)
    sprite('rl830_09', 1)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AirAttack02():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        AirPushbackX(12000)
        AirPushbackY(20000)
        UseSlashHitspark(1)
        MoveAttributes(1, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_54:
                if SLOT_19 < 120000:
                    sendToLabel(0)
                    SLOT_54 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('Act_IG_AirAttack02', 32)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl832_00', 2)
    sprite('rl832_01', 2)
    physicsXImpulse(5000)
    physicsYImpulse(7500)
    sprite('rl832_02', 2)
    physicsXImpulse(20000)
    physicsYImpulse(25000)
    sprite('rl832_01', 1)
    SLOT_31 = SLOT_31 + -1000
    physicsXImpulse(60000)
    physicsYImpulse(35000)
    SLOT_54 = 1
    sprite('rl832_02', 2)
    sprite('rl832_03', 2)
    sprite('rl832_04', 2)
    physicsXImpulse(20000)
    physicsYImpulse(10000)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('rl832_04', 1)
    CommonSE('006_swing_blade_2')
    sprite('rl832_05', 3)
    CreateObject('air_6D', -1)
    RefreshMultihit()
    physicsXImpulse(10000)
    physicsYImpulse(5000)
    sprite('rl832_06', 4)
    if SLOT_55:
        sendToLabel(30)
    physicsXImpulse(8000)
    physicsYImpulse(4000)
    sprite('rl832_07', 4)
    physicsXImpulse(6000)
    physicsYImpulse(3000)
    sprite('rl832_08', 4)
    physicsXImpulse(4000)
    physicsYImpulse(2000)
    sprite('rl832_09', 4)
    physicsXImpulse(2000)
    physicsYImpulse(1000)
    sprite('rl832_10', 4)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    label(30)
    sprite('rl832_06', 1)
    physicsXImpulse(8000)
    physicsYImpulse(4000)
    sprite('rl832_07', 1)
    physicsXImpulse(6000)
    physicsYImpulse(3000)
    sprite('rl832_08', 1)
    physicsXImpulse(4000)
    physicsYImpulse(2000)
    sprite('rl832_09', 1)
    physicsXImpulse(2000)
    physicsYImpulse(1000)
    sprite('rl832_10', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AirAttack03():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        AirPushbackX(12000)
        AirPushbackY(20000)
        UseSlashHitspark(1)
        MoveAttributes(1, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_54:
                if SLOT_19 < 100000:
                    sendToLabel(0)
                    SLOT_54 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('Act_IG_AirAttack03', 32)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl831_00', 3)
    sprite('rl831_01', 2)
    physicsXImpulse(7500)
    physicsYImpulse(-3750)
    sprite('rl831_01', 1)
    SLOT_31 = SLOT_31 + -1000
    sprite('rl831_02', 2)
    physicsXImpulse(30000)
    physicsYImpulse(-20000)
    sprite('rl831_01', 2)
    SLOT_54 = 1
    physicsXImpulse(50000)
    physicsYImpulse(-35000)
    sprite('rl831_02', 2)
    sprite('rl831_03', 2)
    sprite('rl831_04', 2)
    physicsXImpulse(20000)
    physicsYImpulse(-10000)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('rl831_04', 1)
    CommonSE('006_swing_blade_2')
    sprite('rl831_05', 3)
    CreateObject('air_2D', -1)
    RefreshMultihit()
    physicsXImpulse(10000)
    physicsYImpulse(-5000)
    sprite('rl831_06', 4)
    if SLOT_55:
        sendToLabel(30)
    physicsXImpulse(8000)
    physicsYImpulse(-4000)
    sprite('rl831_07', 4)
    physicsXImpulse(6000)
    physicsYImpulse(-3000)
    sprite('rl831_08', 4)
    physicsXImpulse(4000)
    physicsYImpulse(-2000)
    sprite('rl831_09', 4)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl831_06', 1)
    physicsXImpulse(8000)
    physicsYImpulse(-4000)
    sprite('rl831_07', 1)
    physicsXImpulse(6000)
    physicsYImpulse(-3000)
    sprite('rl831_08', 1)
    physicsXImpulse(4000)
    physicsYImpulse(-2000)
    sprite('rl831_09', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpAttack01():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        EndMomentum(0)
        AttackLevel_(3)
        Damage(1050)
        AttackP1(90)
        SameMoveProration(70)
        PushbackX(39900)
        AirPushbackX(30000)
        AirPushbackY(12000)
        AirUntechableTime(40)
        Floorslide(25)
        UseSlashHitspark(1)
        GroundedHitstunAnimation(9)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        RefreshMultihit()
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    gotoLabel(20)
    label(10)
    sprite('rl800_00', 3)
    TeleportToObject(2)
    TurnAround()
    AddX(-150000)
    AddY(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    loopRest()
    label(20)
    sprite('rl840_00', 1)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl840_01', 1)
    sprite('rl840_02', 1)
    sprite('rl840_03', 1)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3000
    else:
        SLOT_31 = SLOT_31 + -1000
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -1000
    sprite('rl840_04', 2)
    physicsXImpulse(5000)
    sprite('rl840_05', 2)
    sprite('rl840_06', 2)
    sprite('rl840_07', 2)
    if SLOT_55:
        sendToLabel(30)
    sprite('rl840_08', 3)
    PrivateSE('rlse_12')
    XImpulseAcceleration(1500)
    CreateObject('SpAttack01Eff', 0)
    sprite('rl840_09', 3)
    CreateParticle('rlef_ignisparksAir', -1)
    sprite('rl840_10', 3)
    XImpulseAcceleration(50)
    sprite('rl840_08', 3)
    CreateParticle('rlef_ignisparksAir', -1)
    XImpulseAcceleration(75)
    sprite('rl840_09', 3)
    XImpulseAcceleration(75)
    sprite('rl840_10', 3)
    XImpulseAcceleration(75)
    CreateParticle('rlef_ignisparksAir', -1)
    sprite('rl840_11', 6)
    TriggerUponForState('SpAttack01Eff', 32)
    XImpulseAcceleration(80)
    sprite('rl840_12', 6)
    XImpulseAcceleration(80)
    sprite('rl840_13', 6)
    XImpulseAcceleration(80)
    sprite('rl840_14', 4)
    XImpulseAcceleration(50)
    sprite('rl840_15', 4)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirPushbackX(54000)
    AirPushbackY(32000)
    AirUntechableTime(70)
    Floorslide(40)
    sprite('rl840_07', 1)
    sprite('rl840_08', 3)
    PrivateSE('rlse_12')
    physicsXImpulse(70000)
    CreateObject('SpAttack01Eff', 0)
    sprite('rl840_09', 3)
    CreateParticle('rlef_ignisparksAir', -1)
    sprite('rl840_10', 3)
    sprite('rl840_08', 3)
    CreateParticle('rlef_ignisparksAir', -1)
    XImpulseAcceleration(90)
    sprite('rl840_09', 3)
    XImpulseAcceleration(80)
    sprite('rl840_10', 3)
    XImpulseAcceleration(70)
    sprite('rl840_11', 3)
    TriggerUponForState('SpAttack01Eff', 32)
    XImpulseAcceleration(60)
    sprite('rl840_12', 2)
    XImpulseAcceleration(30)
    sprite('rl840_13', 1)
    XImpulseAcceleration(20)
    sprite('rl840_14', 1)
    sprite('rl840_15', 1)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpAttack02():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        EndMomentum(0)
        AttackLevel_(4)
        Damage(1200)
        AttackP1(90)
        SameMoveProration(70)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(2)
        AirPushbackX(-2000)
        AirPushbackY(40000)
        AirUntechableTime(40)
        Stagger(40)
        Crumple(28)
        CHStagger(50)
        CHCrumple(40)
        PushbackX(42000)
        Hitstop(3)
        UseSlashHitspark(1)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(2)
        FatalCounter(1)
        EnableCollision(1)
        if SLOT_55:
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            AirPushbackX(0)
            AirPushbackY(52000)
            AirUntechableTime(80)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    sprite('rl800_00', 2)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    label(10)
    sprite('rl841_00', 4)
    TeleportToObject(22)
    TurnAround()
    Flip()
    AddX(-250000)
    AbsoluteY(0)
    EndMomentum(1)
    SetZVal(-100)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    loopRest()
    sprite('rl841_00', 6)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    CreateObject('IgActSignalLight', 0)
    sprite('rl841_00', 14)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3000
    else:
        SLOT_31 = SLOT_31 + -1500
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -1500
    sprite('rl841_01', 2)
    sprite('rl841_02', 2)
    sprite('rl841_03', 2)
    sprite('rl841_04', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('rl841_05', 3)
    CreateObject('SpAttack02zan', -1)
    RefreshMultihit()
    sprite('rl841_06', 3)
    if SLOT_55:
        sendToLabel(30)
    sprite('rl841_07', 3)
    sprite('rl841_08', 3)
    sprite('rl841_09', 3)
    sprite('rl841_10', 3)
    sprite('rl841_11', 3)
    sprite('rl841_12', 3)
    sprite('rl841_13', 3)
    sprite('rl841_14', 3)
    sprite('rl841_15', 3)
    sprite('rl841_16', 3)
    sprite('rl841_17', 3)
    sprite('rl841_18', 3)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl841_06', 1)
    sprite('rl841_07', 1)
    sprite('rl841_08', 1)
    sprite('rl841_09', 1)
    sprite('rl841_10', 1)
    sprite('rl841_11', 1)
    sprite('rl841_12', 1)
    sprite('rl841_13', 1)
    sprite('rl841_14', 1)
    sprite('rl841_15', 1)
    sprite('rl841_16', 1)
    sprite('rl841_17', 1)
    sprite('rl841_18', 1)
    sprite('rl841_19', 1)
    sprite('rl841_20', 1)
    sprite('rl841_21', 1)
    sprite('rl841_22', 1)
    sprite('rl841_23', 1)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpAttack03():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        EndMomentum(0)
        RefreshMultihit()
        AttackLevel_(5)
        Damage(660)
        SameMoveProration(70)
        AirUntechableTime(30)
        AirPushbackY(12000)
        PushbackX(12000)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        if SLOT_55:
            GroundedHitstunAnimation(9)

        def upon_EVERY_FRAME():
            if SLOT_54:
                if SLOT_19 < 320000:
                    sendToLabel(40)
                    SLOT_54 = 0
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        if SLOT_137:
            DamageMultiplier(80)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    gotoLabel(20)
    label(10)
    sprite('rl800_00', 10)
    TeleportToObject(2)
    TurnAround()
    AddX(-150000)
    AddY(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    loopRest()
    label(20)
    sprite('rl842_00', 3)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(4)
    sprite('rl842_01', 3)
    sprite('rl842_02', 3)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3000
    else:
        SLOT_31 = SLOT_31 + -1500
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -1500
    sprite('rl842_03', 3)
    CreateObject('IgActSignalLight', 0)
    CreateObject('IgActSignalLight', 1)
    sprite('rl842_04', 3)
    sprite('rl842_05', 3)
    sprite('rl842_06', 3)
    CreateParticle('rlef_ignisparksAir', 0)
    physicsXImpulse(3500)
    if SLOT_55:
        physicsXImpulse(5000)
    sprite('rl842_07', 3)
    XImpulseAcceleration(150)
    sprite('rl842_06', 3)
    SLOT_54 = 1
    XImpulseAcceleration(150)
    sprite('rl842_07', 3)
    CreateParticle('rlef_ignisparksAir', 0)
    XImpulseAcceleration(200)
    sprite('rl842_06', 3)
    XImpulseAcceleration(200)
    sprite('rl842_07', 3)
    label(40)
    clearUponHandler(EVERY_FRAME)
    SetAcceleration(0)
    sprite('rl842_08', 2)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_09', 2)
    sprite('rl842_10', 2)
    CommonSE('006_swing_blade_1')
    sprite('rl842_11', 3)
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    physicsXImpulse(16000)
    sprite('rl842_12', 6)
    CommonSE('006_swing_blade_1')
    sprite('rl842_13', 3)
    CreateObject('SpAttack03zan01', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    AirPushbackY(14400)
    physicsXImpulse(16000)
    sprite('rl842_14', 1)
    sprite('rl842_15', 1)
    sprite('rl842_16', 1)
    XImpulseAcceleration(50)
    sprite('rl842_17', 2)
    sprite('rl842_18', 2)
    sprite('rl842_19', 2)
    XImpulseAcceleration(40)
    sprite('rl842_20', 2)
    sprite('rl842_21', 2)
    sprite('rl842_22', 2)
    XImpulseAcceleration(30)
    CommonSE('006_swing_blade_2')
    sprite('rl842_23', 3)
    CreateObject('SpAttack03zan02', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    ResetPushbackX()
    AirPushbackY(26400)
    if SLOT_55:
        AirPushbackX(50000)
        Wallbounce(1)
        NonCornerWallbounce(1)
        Wallstick(1)
        WallstickDuration(30)
        AirHitstunAfterWallbounce(30)
    physicsXImpulse(16000)
    sprite('rl842_24', 3)
    XImpulseAcceleration(0)
    sprite('rl842_25', 3)
    sprite('rl842_26', 3)
    sprite('rl842_27', 3)
    sprite('rl841_18', 3)
    EnableAfterimage(0)
    if SLOT_55:
        sendToLabel(30)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl841_18', 1)
    EnableAfterimage(0)
    sprite('rl841_19', 1)
    sprite('rl841_20', 1)
    sprite('rl841_21', 1)
    sprite('rl841_22', 1)
    sprite('rl841_23', 1)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpAttack04():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackLevel_(4)
        Damage(920)
        AttackP1(90)
        AttackP2(82)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(13000)
        AirPushbackY(-44000)
        AirUntechableTime(30)
        GroundBounce(1)
        BouncePercentage(50)
        MoveAttributes(1, 0, 0, 0, 0)
        HitOverhead(2)
        UseSlashHitspark(1)
        StarterRating(2)
        SameMoveProration(10)
        if SLOT_55:
            AirUntechableTime(50)
            AirPushbackX(5000)
            AirPushbackY(-70000)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    gotoLabel(20)
    label(10)
    sprite('rl800_00', 10)
    TeleportToObject(2)
    TurnAround()
    AddX(-150000)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    AbsoluteY(0)
    physicsXImpulse(-2000)
    physicsYImpulse(8000)
    loopRest()
    GroundedHitstunAnimation(3)
    sprite('rl822_01', 1)
    XImpulseAcceleration(20)
    YAccel(20)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3500
    else:
        SLOT_31 = SLOT_31 + -1500
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -1500
    sprite('rl822_02', 6)
    sprite('rl822_03', 5)
    sprite('rl822_04', 4)
    sprite('rl822_05', 4)
    CommonSE('005_swing_grap_2_2')
    loopRest()
    gotoLabel(21)
    label(20)
    sprite('rl822_00', 5)
    sprite('rl822_01', 1)
    physicsXImpulse(-3000)
    physicsYImpulse(8000)
    sprite('rl822_01', 6)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3500
    else:
        SLOT_31 = SLOT_31 + -1500
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -2000
    sprite('rl822_02', 6)
    physicsYImpulse(7000)
    sprite('rl822_03', 5)
    sprite('rl822_04', 40)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    sprite('rl822_05', 4)
    CommonSE('005_swing_grap_2_2')
    loopRest()
    label(21)
    sprite('rl822_06', 3)
    CreateObject('SpAttack04Wind', 0)
    physicsXImpulse(50000)
    physicsYImpulse(-17500)
    RefreshMultihit()
    uponSendToLabel(LANDING, 40)
    label(30)
    sprite('rl822_07', 3)
    physicsXImpulse(30000)
    physicsYImpulse(-20000)
    SetAcceleration(3000)
    setGravity(2000)
    sprite('rl822_06', 3)
    gotoLabel(30)
    label(40)
    clearUponHandler(LANDING)
    sprite('rl822_08', 3)
    TriggerUponForState('zan_822', 32)
    AddX(50000)
    physicsYImpulse(-10000)
    XImpulseAcceleration(50)
    PerAcceleration(0)
    PerGravity(0)
    sprite('rl822_09', 3)
    if SLOT_55:
        sendToLabel(50)
    sprite('rl822_11', 3)
    CreateParticle('rlef_ignisparks_near', -1)
    XImpulseAcceleration(50)
    sprite('rl822_12', 4)
    CreateParticle('rlef_ignisparks_near', -1)
    XImpulseAcceleration(50)
    sprite('rl822_13', 4)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('rl822_14', 4)
    sprite('rl822_15', 4)
    sprite('rl822_16', 5)
    loopRest()
    gotoLabel(90)
    label(50)
    sprite('rl822_09', 1)
    sprite('rl822_11', 1)
    CreateParticle('rlef_ignisparks_near', -1)
    XImpulseAcceleration(50)
    sprite('rl822_12', 1)
    XImpulseAcceleration(50)
    sprite('rl822_13', 1)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('rl822_14', 1)
    sprite('rl822_15', 1)
    sprite('rl822_16', 1)
    label(90)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpThrow():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackDefaults_Throw('IGAct_SpThrow_Exe', 2, 0, 0)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        DollAttackAttributes(1)
        AttackP1(80)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(200000)
        ThrowTechWindow(-1)

        def upon_EVERY_FRAME():
            if SLOT_19 < 100000:
                XImpulseAcceleration(60)
            if SLOT_YDistanceFromFloor <= 150000:
                setGravity(1000)
                PreventGroundedHit(0)
                PreventAirborneHit(1)
            else:
                setGravity(0)
                PreventGroundedHit(1)
                PreventAirborneHit(0)

        def upon_OPPONENT_HIT():
            SLOT_52 = 1
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    gotoLabel(20)
    label(10)
    sprite('rl800_00', 10)
    TeleportToObject(2)
    TurnAround()
    AddX(-150000)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    loopRest()
    label(20)
    sprite('rl890_00', 6)
    sprite('rl890_01', 6)
    physicsXImpulse(2000)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3000
        XSpeed(1000)
        sendToLabel(30)
    else:
        SLOT_31 = SLOT_31 + -2000
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -2000
    sprite('rl890_02', 6)
    XImpulseAcceleration(300)
    sprite('rl890_03', 6)
    XImpulseAcceleration(400)
    sprite('rl890_04', 6)
    sprite('rl890_05', 1)
    XImpulseAcceleration(20)
    StartMultihit()
    sprite('rl890_05', 2)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_2')
    sprite('rl890_17', 4)
    sprite('rl890_18', 4)
    XImpulseAcceleration(0)
    sprite('rl890_19', 4)
    sprite('rl890_20', 4)
    sprite('rl890_21', 4)
    sprite('rl890_22', 4)
    sprite('rl841_18', 3)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(30)
    sprite('rl890_02', 6)
    XImpulseAcceleration(300)
    sprite('rl890_03', 6)
    XImpulseAcceleration(400)
    sprite('rl890_04', 6)
    sprite('rl890_05', 1)
    XImpulseAcceleration(20)
    StartMultihit()
    sprite('rl890_05', 2)
    RefreshMultihit()
    CommonSE('005_swing_grap_2_2')
    sprite('rl890_17', 3)
    sprite('rl890_18', 3)
    XImpulseAcceleration(0)
    sprite('rl890_19', 3)
    sprite('rl890_20', 3)
    sprite('rl890_21', 3)
    sprite('rl890_22', 3)
    sprite('rl841_18', 1)
    sprite('rl841_19', 1)
    sprite('rl841_20', 1)
    sprite('rl841_21', 1)
    sprite('rl841_22', 1)
    sprite('rl841_23', 1)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpThrow_Exe():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP2(60)
        SingleProration(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Hitstop(6)
        PushbackX(0)
        OppPositionOnHit(1, -256000, 0)
        UseSlashHitspark(1)
        HitAnywhere(1)
        NoAttackOffset(1)
        PassByArmor(1)
        OnlyHitPlayer(1)
        StarterRating(2)
        SameMoveProration(10)
        MoveAttributes(0, 1, 0, 0, 0)
        DisableOppPushCollision(1)
        IgnoreBurst(1)
        IgnoreComboTime(1)

        def upon_OPPONENT_HIT():
            ScreenShake(1000, 2000)
        NoDamageAction(1)
        SLOT_52 = 1
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        if SLOT_137:
            DamageMultiplier(80)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl890_05', 2)
    SetInertia(20000)
    StartMultihit()
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_06', 3)
    physicsYImpulse(-1000)
    setGravity(2000)
    OppThrowAnimation(8, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_07', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_08', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_09', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_10', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_11', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 8)
    sprite('rl890_11', 100)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 8)

    def upon_LANDING():
        if SLOT_55:
            sendToLabel(1)
        else:
            sendToLabel(0)
    label(0)
    sprite('rl890_12', 3)
    EndMomentum(1)
    RefreshMultihit()
    sprite('rl890_13', 3)
    RefreshMultihit()

    def upon_EVERY_FRAME():
        if not GuardpointNonProjectileCheck():
            clearUponHandler(EVERY_FRAME)
            NoAttackDuringAction(1)
            sendToLabel(9)
    sprite('rl890_14', 3)
    RefreshMultihit()
    sprite('rl890_12', 3)
    RefreshMultihit()
    sprite('rl890_13', 3)
    RefreshMultihit()
    sprite('rl890_14', 3)
    RefreshMultihit()
    NoAttackOffset(0)
    PushbackX(-19800)
    DisableOppPushCollision(0)
    IgnoreBurst(0)
    IgnoreComboTime(0)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('rl890_12', 1)
    EndMomentum(1)
    RefreshMultihit()
    Damage(420)
    sprite('rl890_12', 1)
    RefreshMultihit()
    if SLOT_137:
        DamageMultiplier(80)

    def upon_EVERY_FRAME():
        if not GuardpointNonProjectileCheck():
            clearUponHandler(EVERY_FRAME)
            NoAttackDuringAction(1)
            sendToLabel(9)
    sprite('rl890_13', 1)
    RefreshMultihit()
    sprite('rl890_13', 1)
    RefreshMultihit()
    sprite('rl890_14', 1)
    RefreshMultihit()
    sprite('rl890_14', 1)
    RefreshMultihit()
    sprite('rl890_12', 1)
    RefreshMultihit()
    sprite('rl890_12', 1)
    RefreshMultihit()
    sprite('rl890_13', 1)
    RefreshMultihit()
    sprite('rl890_13', 1)
    RefreshMultihit()
    sprite('rl890_14', 3)
    RefreshMultihit()
    NoAttackOffset(0)
    PushbackX(-19800)
    DisableOppPushCollision(0)
    IgnoreBurst(0)
    IgnoreComboTime(0)
    loopRest()
    gotoLabel(9)
    label(9)
    sprite('keep', 3)
    clearUponHandler(EVERY_FRAME)
    NoAttackDuringAction(1)
    EnableCollision(0)
    PreventSelfPush(0)
    sprite('rl890_15', 6)
    sprite('rl890_16', 6)
    sprite('rl843_10', 6)
    Flip()
    sprite('rl843_11', 6)
    sprite('rl843_12', 6)
    sprite('rl843_13', 6)
    sprite('rl843_14', 6)
    sprite('rl843_15', 6)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_SpAttack05_AtkObj():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(120)
        AttackP1(90)
        AttackP2(98)
        Hitstop(3)
        PushbackX(20000)
        AirPushbackY(-6000)
        HardKnockdown(1)
        UseSlashHitspark(1)
        HitLow(2)
        MoveAttributes(0, 0, 0, 1, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            AddActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2 >= 1:
                HitLow(0)
        RemoveOnCallStateEnd(2)
    sprite('vrrlef823atk_00', 4)
    AddRotationPerFrame(-20000)
    physicsXImpulse(35000)
    CreateObject('IGAct_SpAttack05_Particle', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 255, 0, 0)
    AfterimageMask_2(0, 200, 0, 0)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    CommonSE('009_swing_rapier_0')
    PrivateSE('rlse_12')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle', -1)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle', -1)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 3)
    CommonSE('009_swing_rapier_0')
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    physicsXImpulse(0)
    sprite('vrrlef823atk_00', 3)
    RefreshMultihit()
    CommonSE('009_swing_rapier_0')
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    PushbackX(-20000)
    AirPushbackX(-20000)
    physicsXImpulse(-35000)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    ObjectUpon(LANDING, 32)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 1)
    CreateObject('IGAct_SpAttack05_Particle_re', -1)


@State
def IGAct_SpAttack05_AtkObjOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(120)
        AttackP1(90)
        AttackP2(98)
        Hitstop(3)
        GroundedHitstunAnimation(9)
        AirPushbackY(-6000)
        GroundBounce(1)
        BouncePercentage(100)
        HardKnockdown(1)
        UseSlashHitspark(1)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            AddActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2 >= 1:
                HitLow(0)
        RemoveOnCallStateEnd(2)
    sprite('vrrlef823atk_00', 4)
    AddRotationPerFrame(-20000)
    physicsXImpulse(50000)
    CreateObject('IGAct_SpAttack05_Particle', -1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageColor_1(220, 100, 100, 100)
    AfterimageColor_2(60, 100, 100, 100)
    AfterimageMask_1(0, 255, 0, 0)
    AfterimageMask_2(0, 200, 0, 0)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    CommonSE('009_swing_rapier_0')
    PrivateSE('rlse_12')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle', -1)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle', -1)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 3)
    CommonSE('009_swing_rapier_0')
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    physicsXImpulse(0)
    sprite('vrrlef823atk_00', 3)
    RefreshMultihit()
    CommonSE('009_swing_rapier_0')
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    AirPushbackX(-10000)
    physicsXImpulse(-50000)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 4)
    RefreshMultihit()
    CreateObject('IGAct_SpAttack05_Particle_re', -1)
    ObjectUpon(LANDING, 32)
    CommonSE('009_swing_rapier_0')
    sprite('vrrlef823atk_00', 1)
    CreateObject('IGAct_SpAttack05_Particle_re', -1)


@State
def IGAct_SpAttack05_Particle():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ignisparks_near')
        BlendMode_Add()
        AlphaValue(255)
        AbsoluteY(-25000)
        IgnoreScreenfreeze(1)
    sprite('null', 32)


@State
def IGAct_SpAttack05_Particle_re():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ignisparks_near')
        BlendMode_Add()
        AlphaValue(255)
        AbsoluteY(-25000)
        IgnoreScreenfreeze(1)
        Flip()
    sprite('null', 32)


@State
def IGAct_AirSpAttack01():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        EndMomentum(0)
        AttackLevel_(4)
        Damage(280)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        AirHitstunAnimation(9)
        AirUntechableTime(50)
        AirPushbackX(0)
        AirPushbackY(-57000)
        YImpulseBeforeWallbounce(0)
        PushbackX(0)
        Hitstop(3)
        EnemyHitstopAddition(-1, -1, 6)
        MoveAttributes(1, 0, 0, 0, 0)
        UseSlashHitspark(1)
        HitsparkSize(600)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        BlendMode_Normal()
        if SLOT_137:
            DamageMultiplier(80)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    label(10)
    sprite('rl844_00', 6)
    if SLOT_64:
        TeleportToObject(22)
        ForceFaceSprite()
        AddX(-100000)
        AddY(800000)
    if SLOT_55:
        TeleportToObject(22)
        ForceFaceSprite()
        AddX(-100000)
        AddY(800000)
    else:
        TeleportToObject(3)
        TurnAround()
        AddX(200000)
        AddY(200000)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    loopRest()
    sprite('rl844_00', 4)
    if SLOT_55:
        SLOT_31 = SLOT_31 + -3000
    else:
        SLOT_31 = SLOT_31 + -1500
        if SLOT_51 == 1:
            SLOT_31 = SLOT_31 + -1500
    sprite('rl844_00', 3)
    Size(1000)
    SetScaleXPerFrame(0)
    sprite('rl844_01', 3)
    if SLOT_55:
        uponSendToLabel(LANDING, 50)
    else:
        uponSendToLabel(LANDING, 1)
    sprite('rl844_02', 3)
    setGravity(2000)
    sprite('rl844_03', 3)
    RefreshMultihit()
    CommonSE('008_swing_pole_1')
    physicsYImpulse(-40000)
    PrivateSE('rlse_12')
    label(0)
    sprite('rl844_04', 3)
    PrivateSE('rlse_12')
    CreateObject('AirSpAttackWind', 0)
    RefreshMultihit()
    sprite('rl844_05', 3)
    PrivateSE('rlse_12')
    RefreshMultihit()
    sprite('rl844_03', 3)
    PrivateSE('rlse_12')
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rl844_06', 3)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    PushbackX(30400)
    HardKnockdown(10)
    EnableEmergencyTechAirHit(1)
    LandingEffects(100, 1, 1)
    ScreenShake(0, 10000)
    CreateParticle('rlef_throw', -1)
    CreateObject('DownFallMcA', -1)
    CommonSE('213_bound_1')
    sprite('rl844_07', 3)
    ScreenShake(0, 10000)
    EndAttack()
    physicsXImpulse(8000)
    sprite('rl844_08', 3)
    ForceFaceSprite()
    ScreenShake(0, 10000)
    sprite('rl844_09', 3)
    ScreenShake(0, 10000)
    sprite('rl844_10', 3)
    sprite('rl844_11', 3)
    sprite('rl844_12', 3)
    XImpulseAcceleration(50)
    sprite('rl844_13', 3)
    sprite('rl844_14', 3)
    sprite('rl844_15', 3)
    sprite('rl844_16', 3)
    sprite('rl844_17', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(50)
    sprite('rl844_06', 1)
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    PushbackX(30400)
    CHHardKnockdown(10)
    LandingEffects(100, 1, 1)
    ScreenShake(0, 10000)
    CreateParticle('rlef_throw', -1)
    CreateObject('DownFallMcA', -1)
    CommonSE('213_bound_1')
    sprite('rl844_07', 1)
    ScreenShake(0, 10000)
    EndAttack()
    sprite('rl844_08', 1)
    ScreenShake(0, 10000)
    sprite('rl844_09', 1)
    ScreenShake(0, 10000)
    sprite('rl844_10', 1)
    sprite('rl844_11', 1)
    sprite('rl844_12', 1)
    sprite('rl844_13', 1)
    sprite('rl844_14', 1)
    sprite('rl844_15', 1)
    sprite('rl844_16', 1)
    sprite('rl844_17', 1)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AddAttack01():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        RefreshMultihit()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(82)
        SameMoveProration(90)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(-5000)
        AirUntechableTime(36)
        Hitstop(8)
        MoveAttributes(1, 0, 0, 0, 0)
        UseSlashHitspark(1)
        EndMomentum(0)
        if SLOT_55:
            AirUntechableTime(60)
            Floorslide(58)
        if SLOT_55:
            SLOT_31 = SLOT_31 + -2000
        else:
            SLOT_31 = SLOT_31 + -1000
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(20)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    gotoLabel(10)
    label(20)
    sprite('rl800_00', 10)
    Visibility(1)
    loopRest()
    label(10)
    sprite('rl840_00', 2)
    TeleportToObject(22)
    CopyFromRightToLeft(23, 2, 23, 3, 2, 23)
    TurnAround()
    AddX(-150000)
    Visibility(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(0)
    loopRest()
    sprite('rl840_01', 2)
    sprite('rl840_02', 2)
    sprite('rl840_03', 2)
    sprite('rl840_04', 2)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl840_05', 2)
    sprite('rl840_06', 2)
    sprite('rl840_07', 2)
    PrivateSE('rlse_12')
    sprite('rl840_08', 3)
    physicsXImpulse(70000)
    CreateObject('SpAttack01Eff', 0)
    sprite('rl840_09', 3)
    XImpulseAcceleration(80)
    sprite('rl840_10', 3)
    XImpulseAcceleration(70)
    sprite('rl840_11', 6)
    if SLOT_55:
        sendToLabel(50)
    TriggerUponForState('SpAttack01Eff', 32)
    XImpulseAcceleration(60)
    sprite('rl840_12', 3)
    XImpulseAcceleration(50)
    sprite('rl840_13', 3)
    XImpulseAcceleration(40)
    sprite('rl840_14', 3)
    sprite('rl840_15', 3)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(50)
    sprite('rl840_11', 1)
    sprite('rl840_12', 1)
    XImpulseAcceleration(50)
    sprite('rl840_13', 1)
    XImpulseAcceleration(40)
    sprite('rl840_14', 1)
    sprite('rl840_15', 1)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AddAttack02():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        AttackLevel_(4)
        Damage(300)
        SingleProration(1)
        SameMoveProration(10)
        AirHitstunAnimation(9)
        AirUntechableTime(25)
        AirPushbackX(0)
        AirPushbackY(-45750)
        YImpulseBeforeWallbounce(0)
        HardKnockdown(1)
        Hitstop(2)
        EnemyHitstopAddition(-1, -1, 6)
        MoveAttributes(1, 0, 0, 0, 0)
        UseSlashHitspark(1)
        HitsparkSize(600)
        EndMomentum(0)
        if SLOT_55:
            SLOT_31 = SLOT_31 + -4000
        else:
            SLOT_31 = SLOT_31 + -1000
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(20)
    sprite('rl800_00', 7)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    gotoLabel(10)
    label(20)
    sprite('rl800_00', 7)
    Visibility(1)
    loopRest()
    label(10)
    sprite('rl844_00', 10)
    TeleportToObject(22)
    TurnAround()
    AddX(440000)
    AddY(280000)
    Visibility(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    sprite('rl844_01', 3)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl844_00', 3)
    sprite('rl844_01', 3)
    if SLOT_55:
        uponSendToLabel(LANDING, 50)
    else:
        uponSendToLabel(LANDING, 1)
    sprite('rl844_02', 3)
    setGravity(2000)
    sprite('rl844_03', 3)
    RefreshMultihit()
    CommonSE('008_swing_pole_1')
    physicsYImpulse(-40000)
    PrivateSE('rlse_12')
    label(0)
    sprite('rl844_04', 3)
    PrivateSE('rlse_12')
    RefreshMultihit()
    sprite('rl844_05', 3)
    PrivateSE('rlse_12')
    RefreshMultihit()
    sprite('rl844_03', 3)
    PrivateSE('rlse_12')
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rl844_06', 3)
    Hitstop(0)
    HardKnockdownReset()
    RefreshMultihit()
    LandingEffects(100, 1, 1)
    ScreenShake(0, 10000)
    CreateParticle('rlef_throw', -1)
    CommonSE('213_bound_1')
    sprite('rl844_07', 2)
    ScreenShake(0, 10000)
    EndAttack()
    physicsXImpulse(5000)
    sprite('rl844_08', 2)
    ForceFaceSprite()
    ScreenShake(0, 10000)
    sprite('rl844_09', 2)
    ScreenShake(0, 10000)
    sprite('rl844_10', 2)
    sprite('rl844_11', 2)
    sprite('rl844_12', 3)
    XImpulseAcceleration(50)
    sprite('rl844_13', 2)
    sprite('rl844_14', 2)
    sprite('rl844_15', 2)
    sprite('rl844_16', 2)
    sprite('rl844_17', 2)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(50)
    sprite('rl844_06', 1)
    AirUntechableTime(60)
    AirPushbackY(40000)
    ResetGravity()
    Hitstop(0)
    HardKnockdownReset()
    RefreshMultihit()
    LandingEffects(100, 1, 1)
    ScreenShake(0, 10000)
    CreateParticle('rlef_throw', -1)
    CommonSE('213_bound_1')
    sprite('rl844_07', 1)
    ScreenShake(0, 10000)
    EndAttack()
    sprite('rl844_08', 1)
    ScreenShake(0, 10000)
    sprite('rl844_09', 1)
    ScreenShake(0, 10000)
    sprite('rl844_10', 1)
    sprite('rl844_11', 1)
    sprite('rl844_12', 1)
    sprite('rl844_13', 1)
    sprite('rl844_14', 1)
    sprite('rl844_15', 1)
    sprite('rl844_16', 1)
    sprite('rl844_17', 1)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()


@State
def IGAct_AddAttack03():

    def upon_IMMEDIATE():
        callSubroutine('IG_SpAttackInit')
        EndMomentum(0)
        RefreshMultihit()
        AttackLevel_(4)
        Damage(1000)
        SameMoveProration(10)
        AttackP2(72)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirUntechableTime(30)
        AirPushbackX(-4000)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        if SLOT_55:
            AirUntechableTime(60)
            AirPushbackX(-8000)
            AirPushbackY(50000)
        if SLOT_55:
            SLOT_31 = SLOT_31 + -4000
        else:
            SLOT_31 = SLOT_31 + -2000
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(20)
    sprite('rl800_00', 7)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    gotoLabel(10)
    label(20)
    sprite('rl800_00', 7)
    Visibility(1)
    loopRest()
    label(10)
    sprite('rl800_00', 5)
    TurnAround()
    TeleportToObject(22)
    CopyFromRightToLeft(23, 2, 23, 3, 2, 23)
    AddX(80000)
    Visibility(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    loopRest()
    sprite('rl842_00', 3)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(4)
    sprite('rl842_01', 2)
    sprite('rl842_02', 2)
    sprite('rl842_05', 2)
    sprite('rl842_06', 2)
    CreateParticle('rlef_ignisparksAir', 0)
    physicsXImpulse(10000)
    sprite('rl842_07', 2)
    sprite('rl842_08', 2)
    XImpulseAcceleration(200)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_09', 2)
    XImpulseAcceleration(200)
    sprite('rl842_10', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_11', 3)
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_12', 3)
    XImpulseAcceleration(50)
    sprite('rl842_24', 3)
    XImpulseAcceleration(50)
    sprite('rl842_25', 3)
    XImpulseAcceleration(50)
    sprite('rl842_26', 3)
    XImpulseAcceleration(50)
    sprite('rl842_27', 2)
    XImpulseAcceleration(50)
    sprite('rl841_18', 3)
    EnableAfterimage(0)
    if SLOT_55:
        sendToLabel(50)
    sprite('rl841_19', 3)
    XImpulseAcceleration(0)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    ExitState()
    label(50)
    sprite('rl841_18', 1)
    XImpulseAcceleration(0)
    sprite('rl841_19', 1)
    sprite('rl841_20', 1)
    sprite('rl841_21', 1)
    sprite('rl841_22', 1)
    sprite('rl841_23', 1)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_DDAttack01():

    def upon_IMMEDIATE():
        callSubroutine('IG_DDAttackInit')
        AttackLevel_(4)
        Damage(1000)
        MoveAttributes(0, 1, 0, 0, 0)
        AttackP1(80)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(210)
        Crumple(200)
        AirUntechableTime(200)
        PushbackX(0)
        Hitstop(0)
        OppPositionOnHit(1, 350000, 0)
        StarterRating(2)
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SLOT_52 = 1
        Unknown23042()
        AutoHitSignalSending(0)
        SLOT_31 = SLOT_31 + -1000
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        if SLOT_137:
            DamageMultiplier(80)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    if SLOT_YDistanceFromFloor >= 300:
        gotoLabel(60)
    else:
        gotoLabel(70)
    label(60)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    sprite('keep', 10)
    Visibility(1)
    sprite('rl800_00', 7)
    Visibility(0)
    AbsoluteY(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetZVal(-500)
    SetScaleX(300)
    SetScaleXPerFrame(100)
    gotoLabel(50)
    label(70)
    sprite('rl800_00', 27)
    loopRest()
    gotoLabel(50)
    label(10)
    sprite('keep', 10)
    Visibility(1)
    loopRest()
    label(20)
    sprite('keep', 10)
    Visibility(1)
    sprite('rl800_00', 7)
    Visibility(0)
    TeleportToObject(2)
    TurnAround()
    AddX(-250000)
    AbsoluteY(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetZVal(-500)
    SetScaleX(300)
    SetScaleXPerFrame(100)
    label(50)
    sprite('rl850_00', 4)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    EnableAfterimage(1)
    sprite('rl850_01', 4)
    sprite('rl850_02', 4)
    sprite('rl850_03', 4)
    sprite('rl850_04', 4)
    sprite('rl850_05', 4)
    ParticleLayer(1)
    CallCustomizableParticle('rlef_igshot_start', 0)
    sprite('rl850_06', 4)
    sprite('rl850_07', 4)
    CallCustomizableParticle('rlef_igshot_after', 0)
    CreateObject('IgnisShot_HasseiObj', 0)
    sprite('rl850_08', 4)
    sprite('rl850_09', 4)
    sprite('rl850_10', 4)
    sprite('rl850_11', 4)
    sprite('rl850_12', 4)
    sprite('rl850_13', 3)

    def upon_EVERY_FRAME():
        if SLOT_19 < 600000:
            sendToLabel(30)
    CreateObject('IgnisShot_TosshinObj', -1)
    RegisterObject(5, 1)
    physicsXImpulse(40000)
    CommonSE('015_blaze_1')
    sprite('rl850_14', 3)
    physicsXImpulse(50000)
    sprite('rl850_15', 3)
    physicsXImpulse(60000)
    label(30)
    sprite('rl850_16', 7)
    clearUponHandler(EVERY_FRAME)
    uponSendToLabel(OPPONENT_HIT, 40)
    XImpulseAcceleration(50)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    sprite('rl850_17', 3)
    XImpulseAcceleration(20)
    sprite('rl850_18', 2)
    ObjectUpon(5, 32)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    XImpulseAcceleration(10)
    CommonSE('005_swing_grap_2_2')
    sprite('rl850_19', 3)
    RefreshMultihit()
    XImpulseAcceleration(20)
    ScreenShake(15000, 15000)
    CreateObject('IgnisShot_AttackObj', -1)
    RegisterObject(6, 1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_igshot_wind', 2)
    sprite('rl850_20', 3)
    ObjectUpon(EVERY_FRAME, 33)
    ObjectUpon(6, 33)
    XImpulseAcceleration(10)
    PrivateSE('rlse_13')
    sprite('rl850_21', 3)
    XImpulseAcceleration(0)
    sprite('rl850_22', 3)
    sprite('rl850_23', 3)
    sprite('rl850_24', 3)
    sprite('rl850_25', 3)
    sprite('rl850_26', 3)
    sprite('rl850_27', 3)
    sprite('rl850_28', 3)
    sprite('rl850_29', 3)
    sprite('rl850_30', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    label(40)
    sprite('rl850_20', 1)
    physicsXImpulse(0)
    clearUponHandler(OPPONENT_HIT)
    ObjectUpon(EVERY_FRAME, 32)
    ObjectUpon(6, 32)
    SetZVal(-500)
    PrivateSE('rlse_09')
    sprite('rl850_20', 2)
    TeleportToObject(22)
    AddX(-400000)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    CommonSE('019_quake_0')
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    TriggerUponForState('IgnisShotHitCharge', 32)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_23_atk', 3)
    AutoHitSignalSending(1)
    RefreshMultihit()
    Damage(3200)
    DefeatOpponentBehavior(0)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackX(3000)
    AirPushbackY(58000)
    OppPositionOnHit(0, 0, 0)
    HitAnywhere(1)
    ScreenShake(20000, 20000)
    TriggerUponForState('big_volante_3D', 33)
    CommonSE('013_thunder_1')
    PrivateSE('rlse_14')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('rl850_24', 6)
    CreateObject('IgnisSparkReverse', 0)
    CreateObject('IgnisSparkReverse', 1)
    sprite('rl850_25', 6)
    CreateObject('IgnisSparkReverse', 0)
    CreateObject('IgnisSparkReverse', 1)
    sprite('rl850_26', 6)
    sprite('rl850_27', 6)
    sprite('rl850_28', 6)
    sprite('rl850_29', 6)
    sprite('rl850_30', 6)
    EnableAfterimage(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_DDAttack01OD():

    def upon_IMMEDIATE():
        callSubroutine('IG_DDAttackInit')
        AttackLevel_(4)
        Damage(1000)
        MoveAttributes(0, 1, 0, 0, 0)
        AttackP1(80)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(210)
        Crumple(200)
        AirUntechableTime(200)
        PushbackX(0)
        Hitstop(0)
        OppPositionOnHit(1, 350000, 0)
        StarterRating(2)
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SLOT_52 = 1
        Unknown23042()
        AutoHitSignalSending(0)
        SLOT_31 = SLOT_31 + -1000
        AttackType(4)
        DefeatOpponentBehavior(1)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

        def upon_EVERY_FRAME():
            if SLOT_19 < 600000:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(EVERY_FRAME, 41)
        if SLOT_137:
            DamageMultiplier(80)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    if SLOT_YDistanceFromFloor >= 300:
        gotoLabel(60)
    else:
        gotoLabel(70)
    label(60)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    sprite('keep', 10)
    Visibility(1)
    sprite('rl800_00', 7)
    Visibility(0)
    AbsoluteY(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetZVal(-500)
    SetScaleX(300)
    SetScaleXPerFrame(100)
    gotoLabel(50)
    label(70)
    sprite('rl800_00', 27)
    loopRest()
    gotoLabel(50)
    label(10)
    sprite('keep', 10)
    Visibility(1)
    loopRest()
    label(20)
    sprite('keep', 10)
    Visibility(1)
    sprite('rl800_00', 7)
    Visibility(0)
    TeleportToObject(2)
    TurnAround()
    AddX(-250000)
    AbsoluteY(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetZVal(-500)
    SetScaleX(300)
    SetScaleXPerFrame(100)
    label(50)
    sprite('rl850_00', 4)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    EnableAfterimage(1)
    sprite('rl850_01', 4)
    sprite('rl850_02', 4)
    sprite('rl850_03', 4)
    sprite('rl850_04', 4)
    sprite('rl850_05', 4)
    ParticleLayer(1)
    CallCustomizableParticle('rlef_igshot_start', 0)
    sprite('rl850_06', 4)
    sprite('rl850_07', 4)
    CallCustomizableParticle('rlef_igshot_after', 0)
    CreateObject('IgnisShot_HasseiObj', 0)
    sprite('rl850_08', 4)
    sprite('rl850_09', 4)
    sprite('rl850_10', 4)
    sprite('rl850_11', 4)
    sprite('rl850_12', 4)
    sprite('rl850_13', 3)

    def upon_EVERY_FRAME():
        if SLOT_19 < 600000:
            sendToLabel(30)
    CreateObject('IgnisShot_TosshinObj', -1)
    RegisterObject(5, 1)
    physicsXImpulse(40000)
    CommonSE('015_blaze_1')
    sprite('rl850_14', 3)
    physicsXImpulse(50000)
    sprite('rl850_15', 3)
    physicsXImpulse(60000)
    label(30)
    sprite('rl850_16', 7)
    clearUponHandler(EVERY_FRAME)
    uponSendToLabel(OPPONENT_HIT, 40)
    XImpulseAcceleration(50)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    sprite('rl850_17', 3)
    XImpulseAcceleration(20)
    sprite('rl850_18', 2)
    ObjectUpon(5, 32)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    XImpulseAcceleration(10)
    CommonSE('005_swing_grap_2_2')
    sprite('rl850_19', 3)
    RefreshMultihit()
    XImpulseAcceleration(20)
    ScreenShake(15000, 15000)
    CreateObject('IgnisShot_AttackObj', -1)
    RegisterObject(6, 1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_igshot_wind', 2)
    sprite('rl850_20', 3)
    ObjectUpon(EVERY_FRAME, 33)
    ObjectUpon(6, 33)
    XImpulseAcceleration(10)
    PrivateSE('rlse_13')
    sprite('rl850_21', 3)
    XImpulseAcceleration(0)
    sprite('rl850_22', 3)
    sprite('rl850_23', 3)
    sprite('rl850_24', 3)
    sprite('rl850_25', 3)
    sprite('rl850_26', 3)
    sprite('rl850_27', 3)
    sprite('rl850_28', 3)
    sprite('rl850_29', 3)
    sprite('rl850_30', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    label(40)
    sprite('rl850_20', 1)
    physicsXImpulse(0)
    clearUponHandler(OPPONENT_HIT)
    ObjectUpon(EVERY_FRAME, 32)
    ObjectUpon(6, 32)
    SetZVal(500)
    sprite('rl850_20', 2)
    TeleportToObject(22)
    AddX(-400000)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    PrivateSE('rlse_09')
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    CommonSE('019_quake_0')
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    TriggerUponForState('IgnisShotHitCharge', 32)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    ScreenShake(10000, 10000)
    sprite('rl850_20', 3)
    sprite('rl850_21', 3)
    sprite('rl850_22', 3)
    sprite('rl850_23_atk', 3)
    AutoHitSignalSending(1)
    RefreshMultihit()
    Damage(4300)
    DefeatOpponentBehavior(0)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackX(3000)
    AirPushbackY(58000)
    HardKnockdown(25)
    OppPositionOnHit(0, 0, 0)
    HitAnywhere(1)
    ScreenShake(20000, 20000)
    TriggerUponForState('big_volante_3D', 33)
    CommonSE('013_thunder_1')
    PrivateSE('rlse_14')
    if SLOT_137:
        DamageMultiplier(80)
    sprite('rl850_24', 6)
    CreateObject('IgnisSparkReverse', 0)
    CreateObject('IgnisSparkReverse', 1)
    sprite('rl850_25', 6)
    CreateObject('IgnisSparkReverse', 0)
    CreateObject('IgnisSparkReverse', 1)
    sprite('rl850_26', 6)
    sprite('rl850_27', 6)
    sprite('rl850_28', 6)
    sprite('rl850_29', 6)
    sprite('rl850_30', 6)
    EnableAfterimage(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def __850Cam():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 5)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    ScreenCollision(0)
    WallCollisionDetection(0)
    physicsXImpulse(14800)
    sprite('null', 100)
    physicsXImpulse(0)
    sprite('null', 20)
    physicsXImpulse(-3700)


@State
def IGAct_DDAttack02():

    def upon_IMMEDIATE():
        callSubroutine('IG_DDAttackInit')
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        AirUntechableTime(20)
        Hitstun(30)
        Blockstun(20)
        Hitstop(4)
        PushbackX(8000)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        StarterRating(2)
        DistanceCheck(1000000, 0, -1, -1)
        IgnoreScreenfreeze(1)
        SLOT_52 = 1
        SLOT_31 = SLOT_31 + -2000

        def upon_EVERY_FRAME():
            if SLOT_2 >= 10:
                sendToLabel(200)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    if SLOT_66:
        sendToLabel(50)
    else:
        sendToLabel(30)
    label(50)
    sprite('rl800_00', 37)
    gotoLabel(60)
    label(30)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    gotoLabel(20)
    label(10)
    sprite('keep', 10)
    Visibility(1)
    loopRest()
    label(20)
    sprite('keep', 18)
    Visibility(1)
    TeleportToObject(2)
    TurnAround()
    if SLOT_19 < 150000:
        TeleportToObject(22)
        AddX(-1000)
    else:
        AddX(150000)
    AbsoluteY(0)
    ForceFaceSprite()
    sprite('rl800_00', 10)
    Visibility(0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    label(60)
    sprite('rl800_00', 19)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl851_00', 4)
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('rl851_01', 3)
    sprite('rl851_02', 3)
    sprite('rl851_03', 3)
    physicsXImpulse(5000)
    sprite('rl851_04', 3)
    sprite('rl851_05', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_06', 3)
    sprite('rl851_07', 3)
    sprite('rl851_08', 3)
    sprite('rl851_09', 3)
    sprite('rl851_10', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_11', 3)
    sprite('rl851_12', 3)
    sprite('rl851_13', 3)
    sprite('rl851_14', 3)
    sprite('rl851_15', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_16', 3)
    sprite('rl851_17', 3)
    sprite('rl851_04', 3)
    sprite('rl851_05', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_06', 3)
    sprite('rl851_07', 3)
    sprite('rl851_08', 3)
    sprite('rl851_09', 3)
    sprite('rl851_10', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_11', 3)
    sprite('rl851_12', 3)
    sprite('rl851_13', 3)
    sprite('rl851_14', 3)
    sprite('rl851_15', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_16', 3)
    sprite('rl851_17', 3)
    sprite('rl851_18', 1)
    sprite('rl851_18', 1)
    sprite('rl851_19', 2)
    clearUponHandler(EVERY_FRAME)
    physicsXImpulse(4000)
    sprite('rl851_20', 2)
    sprite('rl851_21', 3)
    CommonSE('004_swing_grap_1_2')
    CreateObject('zan_851a', -1)
    CreateParticle('rlef_ig851upper04', -1)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_22', 3)
    physicsXImpulse(3000)
    sprite('rl851_23', 3)
    sprite('rl851_24', 3)
    physicsXImpulse(2000)
    sprite('rl851_25', 3)
    sprite('rl851_26', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851upper04', -1)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    UseSlashHitspark(1)
    physicsXImpulse(1000)
    sprite('rl851_27', 3)
    physicsXImpulse(0)
    sprite('rl851_28', 4)
    sprite('rl851_29', 4)
    sprite('rl851_30', 3)
    sprite('rl851_31', 3)
    sprite('rl851_32', 6)
    physicsXImpulse(6000)
    sprite('rl851_33', 3)
    sprite('rl851_34', 5)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851upper', -1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    ScreenShake(10000, 10000)
    physicsXImpulse(4000)
    RefreshMultihit()
    AirHitstunAnimation(10)
    AirPushbackY(30000)
    AirPushbackX(4000)
    AirUntechableTime(32)
    Hitstun(32)
    sprite('rl851_35', 3)
    physicsXImpulse(2000)
    sprite('rl851_36', 3)
    physicsXImpulse(1000)
    sprite('rl851_37', 3)
    physicsXImpulse(0)
    sprite('rl851_28', 3)
    sprite('rl851_29', 2)
    sprite('rl851_30', 2)
    sprite('rl851_31', 2)
    sprite('rl851_32', 6)
    physicsXImpulse(6000)
    sprite('rl851_33', 2)
    sprite('rl851_34', 5)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851upper', -1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    ScreenShake(10000, 10000)
    physicsXImpulse(4000)
    RefreshMultihit()
    AirPushbackY(40000)
    AirUntechableTime(44)
    Hitstun(44)
    sprite('rl851_35', 5)
    physicsXImpulse(2000)
    sprite('rl851_36', 5)
    physicsXImpulse(1000)
    sprite('rl851_37', 5)
    physicsXImpulse(0)
    sprite('rl851_28', 5)
    sprite('rl851_29', 2)
    sprite('rl851_30', 10)
    CreateParticle('rlef_ig851charge', 0)
    sprite('rl851_31', 2)
    sprite('rl851_32', 2)
    physicsXImpulse(6000)
    sprite('rl851_33', 2)
    sprite('rl851_34ex00', 6)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851finish', -1)
    CreateObject('zan_851b', -1)
    ScreenShake(50000, 20000)
    physicsXImpulse(4000)
    RefreshMultihit()
    Damage(1000)
    Hitstop(20)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirUntechableTime(60)
    AirPushbackY(50000)
    sprite('rl851_35', 6)
    physicsXImpulse(2000)
    sprite('rl851_36', 6)
    physicsXImpulse(1000)
    sprite('rl851_37', 6)
    physicsXImpulse(0)
    sprite('rl851_37', 5)
    sprite('rl851_38', 5)
    sprite('rl851_39', 5)
    sprite('rl851_40', 5)
    sprite('rl851_41', 5)
    sprite('rl851_42', 5)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_DDAttack02OD():

    def upon_IMMEDIATE():
        callSubroutine('IG_DDAttackInit')
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        AirUntechableTime(20)
        Hitstun(30)
        Blockstun(20)
        Hitstop(2)
        PushbackX(8000)
        MoveAttributes(0, 1, 0, 0, 0)
        UseSlashHitspark(1)
        AttackType(4)
        StarterRating(2)
        DistanceCheck(1000000, 0, -1, -1)
        IgnoreScreenfreeze(1)
        SLOT_52 = 1
        SLOT_31 = SLOT_31 + -2000

        def upon_EVERY_FRAME():
            if SLOT_2 >= 10:
                sendToLabel(200)
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(1, 1, 1, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(10)
    if SLOT_66:
        sendToLabel(50)
    else:
        sendToLabel(30)
    label(50)
    sprite('rl800_00', 37)
    gotoLabel(60)
    label(30)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    loopRest()
    gotoLabel(20)
    label(10)
    sprite('keep', 10)
    Visibility(1)
    loopRest()
    label(20)
    sprite('keep', 18)
    Visibility(1)
    TeleportToObject(2)
    TurnAround()
    if SLOT_19 < 150000:
        TeleportToObject(22)
        AddX(-1000)
    else:
        AddX(150000)
    AbsoluteY(0)
    ForceFaceSprite()
    sprite('rl800_00', 10)
    Visibility(0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    label(60)
    sprite('rl800_00', 19)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl851_00', 4)
    EnableCollision(1)
    EnableAfterimage(1)
    sprite('rl851_01', 3)
    sprite('rl851_02', 3)
    sprite('rl851_03', 3)
    physicsXImpulse(5000)
    sprite('rl851_04', 3)
    sprite('rl851_05', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_06', 3)
    sprite('rl851_07', 3)
    sprite('rl851_08', 3)
    sprite('rl851_09', 3)
    sprite('rl851_10', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_11', 3)
    sprite('rl851_12', 3)
    sprite('rl851_13', 3)
    sprite('rl851_14', 3)
    sprite('rl851_15', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851punch', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    sprite('rl851_16', 3)
    sprite('rl851_17', 3)
    sprite('rl851_18', 1)
    sprite('rl851_18', 1)
    sprite('rl842_08', 2)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_09', 2)
    sprite('rl842_10', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_11', 4)
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    Damage(150)
    AirPushbackY(10000)
    Hitstop(1)
    sprite('rl842_12', 4)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_13', 2)
    CreateObject('SpAttack03zan01', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    sprite('rl842_14', 2)
    sprite('rl842_08', 2)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_10', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_11', 4)
    RefreshMultihit()
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_12', 4)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_13', 3)
    CreateObject('SpAttack03zan01', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    sprite('rl842_14', 2)
    sprite('rl842_08', 2)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_10', 2)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_11', 4)
    RefreshMultihit()
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_12', 4)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_13', 3)
    CreateObject('SpAttack03zan01', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    sprite('rl842_14', 2)
    clearUponHandler(OPPONENT_HIT)
    sprite('rl842_15', 1)
    sprite('rl842_16', 1)
    sprite('rl842_17', 1)
    sprite('rl842_18', 1)
    sprite('rl842_19', 1)
    sprite('rl842_20', 1)
    sprite('rl842_21', 1)
    sprite('rl842_22', 1)
    CommonSE('004_swing_grap_1_2')
    sprite('rl842_23', 1)
    CreateObject('SpAttack03zan02', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    Hitstop(1)
    PushbackX(2500)
    AddActionMark(1)
    label(0)
    sprite('rl842_24', 1)
    sprite('rl842_20', 1)
    sprite('rl842_21', 1)
    sprite('rl842_22', 1)
    CommonSE('004_swing_grap_1_2')
    sprite('rl842_23', 1)
    CreateObject('SpAttack03zan02', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    AddActionMark(1)
    gotoLabel(0)
    label(200)
    sprite('rl851_19', 2)
    clearUponHandler(EVERY_FRAME)
    physicsXImpulse(4000)
    sprite('rl851_20', 2)
    sprite('rl851_21', 3)
    CommonSE('004_swing_grap_1_2')
    CreateObject('zan_851a', -1)
    CreateParticle('rlef_ig851upper04', -1)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    Damage(300)
    sprite('rl851_22', 3)
    physicsXImpulse(3000)
    sprite('rl851_23', 3)
    sprite('rl851_24', 3)
    physicsXImpulse(2000)
    sprite('rl851_25', 3)
    sprite('rl851_26', 3)
    CommonSE('004_swing_grap_1_2')
    CreateParticle('rlef_ig851upper04', -1)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    RefreshMultihit()
    Damage(300)
    UseSlashHitspark(1)
    physicsXImpulse(1000)
    sprite('rl851_27', 3)
    physicsXImpulse(0)
    sprite('rl851_28', 4)
    sprite('rl851_29', 4)
    sprite('rl851_30', 3)
    sprite('rl851_31', 3)
    sprite('rl851_32', 6)
    physicsXImpulse(6000)
    sprite('rl851_33', 3)
    sprite('rl851_34', 5)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851upper', -1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    ScreenShake(10000, 10000)
    physicsXImpulse(4000)
    RefreshMultihit()
    AirHitstunAnimation(10)
    AirPushbackY(30000)
    AirPushbackX(4000)
    AirUntechableTime(32)
    Hitstun(32)
    sprite('rl851_35', 3)
    physicsXImpulse(2000)
    sprite('rl851_36', 3)
    physicsXImpulse(1000)
    sprite('rl851_37', 3)
    physicsXImpulse(0)
    sprite('rl851_28', 3)
    sprite('rl851_29', 2)
    sprite('rl851_30', 2)
    sprite('rl851_31', 2)
    sprite('rl851_32', 6)
    physicsXImpulse(6000)
    sprite('rl851_33', 2)
    sprite('rl851_34', 5)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851upper', -1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    ScreenShake(10000, 10000)
    physicsXImpulse(4000)
    RefreshMultihit()
    AirPushbackY(40000)
    AirUntechableTime(44)
    Hitstun(44)
    sprite('rl851_35', 5)
    physicsXImpulse(2000)
    sprite('rl851_36', 5)
    physicsXImpulse(1000)
    sprite('rl851_37', 5)
    physicsXImpulse(0)
    sprite('rl851_28', 5)
    sprite('rl851_29', 2)
    sprite('rl851_30', 10)
    CreateParticle('rlef_ig851charge', 0)
    sprite('rl851_31', 2)
    sprite('rl851_32', 2)
    physicsXImpulse(6000)
    sprite('rl851_33', 2)
    sprite('rl851_34ex00', 6)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851finish', -1)
    CreateObject('zan_851b', -1)
    ScreenShake(50000, 20000)
    physicsXImpulse(4000)
    RefreshMultihit()
    Damage(1000)
    Hitstop(20)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirUntechableTime(120)
    AirPushbackY(70000)
    sprite('rl851_35', 6)
    physicsXImpulse(2000)
    sprite('rl851_36', 6)
    physicsXImpulse(1000)
    sprite('rl851_37', 6)
    physicsXImpulse(0)
    sprite('rl851_37', 5)
    sprite('rl851_38', 5)
    sprite('rl851_39', 5)
    sprite('rl851_40', 5)
    sprite('rl851_41', 5)
    sprite('rl851_42', 5)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AstralHeat():

    def upon_IMMEDIATE():
        callSubroutine('IG_AHAttackInit')
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(210)
        Crumple(200)
        AirUntechableTime(200)
        PushbackX(0)
        Hitstop(0)
        MoveAttributes(0, 1, 0, 0, 0)
        DamageFromStateOnly('IGAct_AstralHeat2nd')
        Damage(0)
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SLOT_52 = 1
        SetZVal(-500)
        OppPositionOnHit(1, 250000, 0)
        EnterStateIfEventID(12, 'IGAct_AstralHeat2nd')
        RefreshMultihit()
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    if SLOT_51 == 1:
        gotoLabel(0)
    sprite('rl800_00', 5)
    CreateParticle('rlef_warp_out', -1)
    SetScaleXPerFrame(-200)
    sprite('null', 30)
    Visibility(1)
    loopRest()
    gotoLabel(10)
    label(0)
    sprite('null', 35)
    Visibility(1)
    loopRest()
    label(10)
    sprite('rl800_00', 10)
    TeleportToObject(2)
    TurnAround()
    AddX(200000)
    AddY(0)
    Visibility(0)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    sprite('rl800_00', 7)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl860_00', 7)
    sprite('rl860_01', 8)
    sprite('rl860_02', 8)
    sprite('rl860_03', 9)
    sprite('rl860_04', 3)
    sprite('rl860_05_atk', 4)
    CommonSE('005_swing_grap_2_2')
    sprite('rl860_11', 7)
    sprite('rl860_12', 7)
    TriggerUponForState('AstStartMc', 32)
    TriggerUponForState('AstStartAura', 32)
    sprite('rl860_13', 7)
    ObjectUpon(EVERY_FRAME, 33)
    sprite('rl860_14', 7)
    sprite('rl860_15', 7)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AstralHeat2nd():

    def upon_IMMEDIATE():
        callSubroutine('IG_AHAttackInit')
        AttackDefaults_Throw('IGAct_AstralHeat3rd', 5, 0, 0)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        AttackLevel_(4)
        DamageFromStateOnly('IGAct_AstralHeat3rd')
        PreventAirborneHit(0)
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SLOT_52 = 1
        SetZVal(-500)
        AstralHeatCleanup(1, 0)
        RefreshMultihit()
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('rl860_05', 6)
    sprite('rl860_06_atk', 6)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AstralHeat3rd():

    def upon_IMMEDIATE():
        callSubroutine('IG_AHAttackInit')
        AttackDefaults_SuccessThrow(5, 0, 0)
        ThrowTechWindow(-1)
        AttackLevel_(1)
        Damage(0)
        AirHitstunAnimation(20)
        GroundedHitstunAnimation(20)
        OppState('RlAstralDamage')
        DamageFromStateOnly('IGAct_AstralHeatDoor')
        Hitstop(0)
        DamageEffect(5, '')
        IgnoreScreenfreeze(1)
        DefeatOpponentBehavior(1)
        SLOT_52 = 1
        SetZVal(-500)
        RefreshMultihit()
        setInvincible(1)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
    sprite('rl860_06', 6)
    ObjectUpon(EVERY_FRAME, 32)
    PlayPlayAstralBGM(1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    TriggerUponForState('AstStartMc', 32)
    TriggerUponForState('AstStartAura', 32)
    sprite('rl860_07', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CommonSE('022_magiccircle_b')
    sprite('rl860_08', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('rl860_09', 6)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('rl860_10', 20)
    CreateParticle('rlef_ashlock', 0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    sprite('rl860_10', 85)
    CreateObject('AstHitRing', 0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 0, 0, 0, 0)
    CreateObject('AstStartBlackOut', 0)
    EnableCollision(0)
    WallCollisionDetection(0)
    ScreenCollision(0)
    loopRest()
    sprite('rl860_10_atk', 10)
    sprite('rl800_07', 7)
    ObjectUpon(EVERY_FRAME, 34)
    FaceRight()
    XPositionRelativeFacing(-290000)
    AbsoluteY(5000)
    EndMomentum(1)
    SetZVal(500)
    label(0)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    PrivateSE('case_03')
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(0)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_AstralHeatDoor():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        IgnoreScreenfreeze(1)
        Visibility(1)
        HitAnywhere(1)
    sprite('null', 75)
    CreateObject('AstClosingDoor', -1)
    XPositionRelativeFacing(0)
    sprite('vrdmy', 35)
    RefreshMultihit()
    DefeatOpponentBehavior(3)
    HitLow(4)
    HitOverhead(4)
    HitAirUnblockable(4)
    AttackLevel_(4)
    Damage(36000)
    MinimumDamage(100)
    AirHitstunAnimation(20)
    GroundedHitstunAnimation(20)
    OppState('RlAstralDamage')
    Hitstop(0)
    AirPushbackX(0)
    AirPushbackY(0)
    DamageEffect(9, '')
    FinishBG(1)
    PrivateSE('rlse_11')
    sprite('null', 80)
    CreateObject('AstClosedDoor', -1)
    loopRest()


@State
def AstStartBlackOut():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(0)
        AbsoluteY(0)
        SetZVal(-1000)
        BlendMode_Normal()
        AlphaValue(0)
        SetScaleX(10000)
        SetScaleY(3000)
        ColorForTransition(0)
    sprite('vr_white', 100)
    ConstantAlphaModifier(3)
    sprite('vr_white', 100)
    ConstantAlphaModifier(-3)


@State
def EMB_RL():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_RL.DIG', 'ef_emb_RL_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 20)


@State
def EMB_RL_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_RL.DIG', 'ef_emb_RL_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 20)


@State
def EMB_RL_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_RL.DIG', 'ef_emb_RL_motion_000.mmot')
        RenderLayer(5)
        Size(900)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 20)


@State
def InstallFont():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultmfont')
        BlendMode_Add()
        AlphaValue(255)
        IgnoreScreenfreeze(1)
        RenderLayer(3)
    sprite('null', 30)
    loopRest()
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def StrikeMcircle():

    def upon_IMMEDIATE():
        LinkParticle('rlef_StrikeMc')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        AlphaValue(255)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
    sprite('null', 44)
    sprite('null', 6)
    ConstantAlphaModifier(-40)
    SetScaleSpeed(50)


@State
def StrikeUraManto():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        AlphaValue(255)
        SetZVal(500)
    sprite('rl400_05ex', 3)
    sprite('rl400_06ex', 6)
    sprite('rl400_07ex', 6)
    sprite('rl400_08ex', 6)
    sprite('rl400_09ex', 6)
    sprite('rl400_10ex', 6)


@State
def StrikeArm():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        SetZVal(-500)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('vrrlef400atk_00', 2)
    StopCharacterFlash1(13158600)
    CharacterFlash2(0, 4)
    AddX(200000)
    CreateObject('InstallFont', 0)
    sprite('vrrlef400atk_01', 1)
    sprite('vrrlef400atk_02', 1)
    ParticleRotationAngle(-55000)
    ParticleSize(1200)
    CallCustomizableParticle('rlef_Punchmc', 0)
    sprite('vrrlef400atk_03', 2)
    StopCharacterFlash2()
    sprite('vrrlef400atk_04', 3)
    sprite('vrrlef400atk_05', 4)
    sprite('vrrlef400atk_06', 4)
    sprite('vrrlef400atk_07', 3)
    sprite('vrrlef400atk_07', 5)
    ConstantAlphaModifier(-30)


@State
def StrikeGear():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PrivateSE('rlse_08')
        SetZVal(100)
        BlendMode_Normal()
    sprite('vrrlef400_00', 3)
    StopCharacterFlash1(13158600)
    CharacterFlash2(0, 6)
    AddX(-160000)
    AbsoluteY(5000)
    CreateObject('InstallFont', -1)
    sprite('vrrlef400_01', 3)
    sprite('vrrlef400_02', 12)
    StopCharacterFlash2()
    sprite('vrrlef400_03', 6)
    sprite('vrrlef400_04', 3)
    sprite('vrrlef400_05', 5)
    ConstantAlphaModifier(-30)


@State
def StrikeMcircleAir():

    def upon_IMMEDIATE():
        LinkParticle('rlef_StrikeMcAir')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(255)
        IgnoreScreenfreeze(1)
        Size(600)
        uponSendToLabel(32, 1)
    sprite('null', 120)
    label(1)
    sprite('null', 6)
    ConstantAlphaModifier(-40)
    SetScaleSpeed(50)


@State
def strikeair_eff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(500)
        BlendMode_Normal()
    sprite('vrrlef401atk_06', 3)
    AlphaValue(0)
    ParticleRotationAngle(-55000)
    ParticleSize(1200)
    CallCustomizableParticle('rlef_Punchmc', 0)
    sprite('vrrlef401atk_06', 3)
    AlphaValue(255)
    sprite('vrrlef401atk_07', 3)
    sprite('vrrlef401atk_08', 4)
    CreateParticle('rlef_ultmfont_part', 0)
    CreateParticle('rlef_ultmfont_part', 1)
    ConstantAlphaModifier(-30)
    sprite('vrrlef401atk_08', 3)


@State
def AssaultMcircle():

    def upon_IMMEDIATE():
        LinkParticle('rlef_StrikeMc')
        RemoveOnCallStateEnd(3)
        RenderLayer(2)
        BlendMode_Add()
        AlphaValue(255)
        Size(900)
        uponSendToLabel(32, 1)
    sprite('null', 120)
    label(1)
    sprite('null', 6)
    ConstantAlphaModifier(-40)
    SetScaleSpeed(50)


@State
def EffAssaultZan():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        TurnParticleColorable1(1)
        SetZVal(-500)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4278223048)
        ColorTransition(16777215, 18)
    sprite('vrrlef402zan_00', 3)
    sprite('vrrlef402zan_01', 3)
    sprite('vrrlef402zan_01', 5)
    physicsXImpulse(-5000)


@State
def KaihiMcircle():

    def upon_IMMEDIATE():
        LinkParticle('rlef_KaihiMc')
        RemoveOnCallStateEnd(3)
        RenderLayer(2)
        BlendMode_Add()
        AlphaValue(255)
        Size(800)
        AddX(-20000)
        uponSendToLabel(32, 1)
    sprite('null', 120)
    label(1)
    sprite('null', 4)
    ConstantAlphaModifier(-60)


@State
def rl404_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(840)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(15000)
        AirUntechableTime(30)
        Hitstop(5)
        PushbackX(0)
        UseSlashHitspark(1)
        MoveAttributes(0, 0, 0, 1, 0)
        SameMoveProration(10)
        AttackOff()

        def upon_32():
            AddX(150000)
            SLOT_51 = 1

        def upon_33():
            AddX(600000)
            SLOT_52 = 1

        def upon_34():
            AddX(1320000)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('null', 1)
    sprite('null', 1)
    SpriteIfNot0(17, 2, 51)
    SpriteIfNot0(9, 2, 52)
    CreateObject('rl404EnterEff', 0)
    PrivateSE('rlse_06')
    sprite('vrrlef404_00', 2)
    sprite('vrrlef404_01', 2)
    sprite('vrrlef404_02', 12)
    RefreshMultihit()
    label(580)
    sprite('vrrlef404_03', 2)
    AttackOff()
    sprite('vrrlef404_04', 2)
    sprite('vrrlef404_05', 2)
    sprite('vrrlef404_06', 2)


@State
def rl404EnterEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 2)
    sprite('null', 55)
    LinkParticle('rlef_404enter_tubu')


@State
def rl404Gear():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PrivateSE('rlse_08')
        SetZVal(-100)
        BlendMode_Normal()
        Flip()
        AddX(160000)
        AddY(-10000)
    sprite('vrrlef400_00', 3)
    StopCharacterFlash1(13158600)
    CharacterFlash2(0, 6)
    CreateObject('InstallFont', -1)
    sprite('vrrlef400_01', 3)
    sprite('vrrlef400_02', 5)
    StopCharacterFlash2()
    sprite('vrrlef400_03', 6)
    sprite('vrrlef400_04', 3)
    sprite('vrrlef400_05', 5)
    ConstantAlphaModifier(-30)


@State
def __404Manto():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        SetZVal(-500)
        AlphaValue(255)
    sprite('rl404_05ex', 2)
    sprite('rl404_06ex', 4)


@State
def UltimateFieldFire():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_fire')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RenderLayer(1)
    sprite('null', 33)


@State
def UltimateFieldFireOver():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_fire')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RenderLayer(1)
    sprite('null', 51)


@State
def UltimateFieldGears():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears.DIG', 'rl_gears_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        Size(1000)
        uponSendToLabel(33, 0)
    sprite('null', 20)
    ConstantAlphaModifier(12)
    AlphaValue(0)
    sprite('null', 9)
    StopCharacterFlash1(16777215)
    CharacterFlash2(0, 10)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('null', 15)
    StopCharacterFlash2()
    sprite('null', 6)
    ConstantAlphaModifier(-40)
    label(0)
    sprite('null', 6)
    ConstantAlphaModifier(-40)


@State
def UltimateFieldGearsBlack():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears_black.DIG', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        RenderLayer(2)
        Size(1000)
    sprite('null', 11)
    AlphaValue(0)
    sprite('null', 8)
    ConstantAlphaModifier(30)
    sprite('null', 20)
    AlphaValue(255)
    sprite('null', 15)
    sprite('null', 12)
    sprite('null', 6)
    ConstantAlphaModifier(-40)


@State
def UltimateFieldMcircleA():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_mcA')
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        uponSendToLabel(33, 0)
    sprite('null', 39)
    sprite('null', 9)
    sprite('null', 12)
    sprite('null', 12)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(10)
    label(0)
    sprite('null', 6)
    sprite('null', 12)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(10)


@State
def UltimateFieldMcircleLight():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_mclightA')
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        Size(1000)
    sprite('null', 9)
    sprite('null', 12)
    ConstantAlphaModifier(-20)


@State
def UltimateFieldMcUnderLight():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_mclightB')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(180)
    sprite('null', 9)
    sprite('null', 6)
    ConstantAlphaModifier(-30)


@State
def UltimateFieldGearsTowerStart():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears_tower_00.DIG', 'rl_gears_tower_00_motion_000.mm')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(5)
        Size(1000)
        AbsoluteY(0)
    sprite('null', 29)


@State
def UltimateFieldGearsTowerAtk():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears_tower_01.DIG', 'rl_gears_tower_01_motion_000.mm')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(5)
        Size(1000)
        AbsoluteY(0)
    sprite('null', 30)


@State
def UltimateFieldGearsTowerDel():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears_tower_02.DIG', 'rl_gears_tower_02_motion_000.mm')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(5)
        AbsoluteY(0)
    sprite('null', 30)
    sprite('null', 29)
    ConstantAlphaModifier(-20)


@State
def UltimateFieldGearsTowerEff():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears_tower_01_eff.DIG', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(5)
        AbsoluteY(0)
    sprite('null', 10)
    ConstantAlphaModifier(20)
    sprite('null', 50)
    AlphaValue(200)
    sprite('null', 10)
    ConstantAlphaModifier(-20)


@State
def UltimateFieldGearsTowerFront():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gearsparts.DIG', 'rl_gearsparts_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(1)
        Size(600)
        AddX(100000)
        AbsoluteY(0)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(25)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def UltimateFieldGearsBlackAtk():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gears_black.DIG', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(2)
        Size(400)
        AbsoluteY(0)
    sprite('null', 12)
    ConstantAlphaModifier(20)
    sprite('null', 92)
    AlphaValue(255)
    sprite('null', 6)
    ConstantAlphaModifier(-40)


@State
def UltimateFieldMcircleB():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_mcB')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1200)
        AbsoluteY(0)
    sprite('null', 130)
    sprite('null', 12)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(15)


@State
def UltFieldHitReverse():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_hit')
        IgnoreScreenfreeze(1)
        Flip()
    sprite('null', 30)


@State
def UltFieldHitReverseS():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_hit')
        IgnoreScreenfreeze(1)
        Flip()
    sprite('null', 30)
    Size(700)


@State
def UltFieldHitEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('vrrlef430hit_00', 15)
    CreateObject('UltFieldHitReverse', 0)
    ParticleSize(700)
    CallCustomizableParticle('rlef_ultimatefield_hit', 3)
    Visibility(1)
    sprite('vrrlef430hit_00', 15)
    CallCustomizableParticle('rlef_ultimatefield_hit', 1)
    CreateObject('UltFieldHitReverseS', 2)
    Visibility(1)
    sprite('vrrlef430hit_00', 15)
    CreateObject('UltFieldHitReverse', 5)
    CallCustomizableParticle('rlef_ultimatefield_hit', 4)
    Visibility(1)
    sprite('vrrlef430hit_00', 15)
    CreateObject('UltFieldHitReverse', 0)
    ParticleSize(700)
    CallCustomizableParticle('rlef_ultimatefield_hit', 3)
    Visibility(1)
    sprite('vrrlef430hit_00', 15)
    CallCustomizableParticle('rlef_ultimatefield_hit', 1)
    CreateObject('UltFieldHitReverse', 2)
    Visibility(1)
    sprite('vrrlef430hit_00', 15)
    CreateObject('UltFieldHitReverse', 0)
    CallCustomizableParticle('rlef_ultimatefield_hit', 4)
    Visibility(1)


@State
def UltimateFieldAtkObj():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(400)
        AttackP1(80)
        AttackP2(72)
        SingleProration(1)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(0)
        PushbackX(0)
        AirUntechableTime(40)
        EnemyHitstopAddition(10, 30, 30)
        UseSlashHitspark(1)
        MoveAttributes(0, 0, 0, 1, 0)
        StarterRating(2)
        OppMovementUnlock(1)
        IgnoreScreenfreeze(1)

        def upon_OPPONENT_HIT():
            sendToLabel(0)
    sprite('vrrlef430atk_00', 41)
    StartMultihit()
    sprite('vrrlef430atk_00', 19)
    CreateObject('UltimateFieldMcircleA', -1)
    CreateObject('UltimateFieldGearsBlack', -1)
    StartMultihit()
    sprite('vrrlef430atk_00', 20)
    CreateObject('UltimateFieldGears', -1)
    StartMultihit()
    sprite('vrrlef430atk_00', 9)
    CreateObject('UltimateFieldMcUnderLight', -1)
    CreateObject('UltimateFieldMcircleLight', -1)
    RefreshMultihit()
    ScreenShake(0, 20000)
    sprite('vrrlef430atk_00', 1)
    StartMultihit()
    loopRest()
    ExitState()
    label(0)
    sprite('vrrlef430atk_01', 10)
    Damage(200)
    clearUponHandler(OPPONENT_HIT)
    TeleportToObject(22)
    AbsoluteY(0)
    Visibility(1)
    StartMultihit()
    CreateObject('UltimateFieldMcircleB', -1)
    CreateObject('UltimateFieldGearsTowerFront', -1)
    CreateObject('UltimateFieldGearsTowerStart', -1)
    TriggerUponForState('UltimateFieldGears', 33)
    TriggerUponForState('UltimateFieldMcircleA', 33)
    PrivateSE('rlse_07')
    sprite('vrrlef430atk_01', 5)
    CreateObject('UltFieldHitEff', -1)
    sprite('vrrlef430atk_01', 9)
    RefreshMultihit()
    Visibility(1)
    sprite('vrrlef430atk_01', 5)
    CreateObject('UltimateFieldGearsBlackAtk', -1)
    PrivateSE('rlse_07')
    sprite('vrrlef430atk_01', 1)
    CreateObject('UltimateFieldGearsTowerEff', -1)
    CreateObject('UltimateFieldGearsTowerAtk', -1)
    sprite('vrrlef430atk_01', 15)
    RefreshMultihit()
    Visibility(1)
    sprite('vrrlef430atk_01', 13)
    PrivateSE('rlse_07')
    RefreshMultihit()
    Visibility(1)
    sprite('vrrlef430atk_01', 2)
    CreateObject('UltimateFieldGearsTowerAtk', -1)
    sprite('vrrlef430atk_01', 15)
    PrivateSE('rlse_07')
    RefreshMultihit()
    Visibility(1)
    sprite('vrrlef430atk_01', 12)
    RefreshMultihit()
    Visibility(1)
    sprite('vrrlef430atk_01', 3)
    CreateObject('UltimateFieldGearsTowerDel', -1)
    sprite('vrrlef430atk_01', 15)
    RefreshMultihit()
    Visibility(1)
    loopRest()


@State
def UltimateFieldAtkObjOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(400)
        AttackP1(80)
        AttackP2(72)
        SingleProration(1)
        AirHitstunAnimation(3)
        GroundedHitstunAnimation(3)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(0)
        PushbackX(0)
        AirUntechableTime(40)
        EnemyHitstopAddition(10, 30, 30)
        UseSlashHitspark(1)
        MoveAttributes(0, 0, 0, 1, 0)
        StarterRating(2)
        HeatGainMultiplier(0)
        OppMovementUnlock(1)
        IgnoreScreenfreeze(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            sendToLabel(0)
    sprite('vrrlef430atk_00', 41)
    StartMultihit()
    sprite('vrrlef430atk_00', 19)
    CreateObject('UltimateFieldMcircleA', -1)
    CreateObject('UltimateFieldGearsBlack', -1)
    StartMultihit()
    sprite('vrrlef430atk_00', 20)
    CreateObject('UltimateFieldGears', -1)
    StartMultihit()
    sprite('vrrlef430atk_00', 9)
    CreateObject('UltimateFieldMcUnderLight', -1)
    CreateObject('UltimateFieldMcircleLight', -1)
    RefreshMultihit()
    ScreenShake(0, 20000)
    sprite('vrrlef430atk_00', 1)
    StartMultihit()
    loopRest()
    ExitState()
    label(0)
    sprite('vrrlef430atk_01', 10)
    Damage(200)
    TeleportToObject(22)
    AbsoluteY(0)
    Visibility(1)
    StartMultihit()
    CreateObject('UltimateFieldMcircleB', -1)
    CreateObject('UltimateFieldGearsTowerFront', -1)
    CreateObject('UltimateFieldGearsTowerStart', -1)
    TriggerUponForState('UltimateFieldGears', 33)
    TriggerUponForState('UltimateFieldMcircleA', 33)
    PrivateSE('rlse_07')
    sprite('vrrlef430atk_01', 5)
    CreateObject('UltFieldHitEff', -1)
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 2)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 5)
    CreateObject('UltimateFieldGearsBlackAtk', -1)
    PrivateSE('rlse_07')
    sprite('vrrlef430atk_01', 1)
    CreateObject('UltimateFieldGearsTowerEff', -1)
    CreateObject('UltimateFieldGearsTowerAtk', -1)
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 8)
    PrivateSE('rlse_07')
    RefreshMultihit()
    sprite('vrrlef430atk_01', 6)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 2)
    CreateObject('UltimateFieldGearsTowerAtk', -1)
    sprite('vrrlef430atk_01', 8)
    PrivateSE('rlse_07')
    RefreshMultihit()
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 5)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 3)
    CreateObject('UltimateFieldGearsTowerDel', -1)
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    sprite('vrrlef430atk_01', 8)
    RefreshMultihit()
    loopRest()


@State
def UltimateFieldMcircleB_Over():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ultimatefield_mcB')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1200)
        AbsoluteY(0)
    sprite('null', 70)
    sprite('null', 12)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(15)


@State
def UltimateFieldGearsTowerFrontOve():

    def upon_IMMEDIATE():
        Eff3DEffect('rl_gearsparts.DIG', 'rl_gearsparts_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RenderLayer(1)
        Size(600)
        AddX(100000)
        AbsoluteY(0)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(25)
    sprite('null', 20)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def UltFieldHitEffOver():
    sprite('vrrlef430hit_00', 15)
    CreateObject('UltFieldHitReverse', 0)
    ParticleSize(700)
    CallCustomizableParticle('rlef_ultimatefield_hit', 3)
    Visibility(1)
    sprite('vrrlef430hit_00', 15)
    CallCustomizableParticle('rlef_ultimatefield_hit', 1)
    CreateObject('UltFieldHitReverseS', 2)
    Visibility(1)


@State
def UltimateFieldAtkObjOver():
    sprite('vrrlef430atk_00', 56)
    StartMultihit()
    sprite('vrrlef430atk_00', 19)
    CreateObject('UltimateFieldMcircleA', -1)
    CreateObject('UltimateFieldGearsBlack', -1)
    StartMultihit()
    sprite('vrrlef430atk_00', 20)
    CreateObject('UltimateFieldGears', -1)
    StartMultihit()
    sprite('vrrlef430atk_00', 1)
    CreateObject('UltimateFieldMcUnderLight', -1)
    CreateObject('UltimateFieldMcircleLight', -1)
    ScreenShake(0, 20000)
    sprite('null', 10)
    clearUponHandler(OPPONENT_HIT)
    TeleportToObject(22)
    AbsoluteY(0)
    Visibility(1)
    StartMultihit()
    CreateObject('UltimateFieldMcircleB_Over', -1)
    CreateObject('UltimateFieldGearsTowerFrontOve', -1)
    CreateObject('UltimateFieldGearsTowerStart', -1)
    TriggerUponForState('UltimateFieldGears', 33)
    TriggerUponForState('UltimateFieldMcircleA', 33)
    PrivateSE('rlse_07')
    sprite('null', 5)
    CreateObject('UltFieldHitEffOver', -1)
    sprite('null', 9)
    Visibility(1)
    sprite('null', 5)
    CreateObject('UltimateFieldGearsBlackAtk', -1)
    CreateObject('UltimateFieldGearsTowerDel', -1)
    PrivateSE('rlse_07')
    sprite('null', 15)


@State
def AstStartMc():

    def upon_IMMEDIATE():
        ParticleLayer(5)
        CallPrivateEffect('rlef_ashstart_mc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1200)
        AbsoluteY(0)
        uponSendToLabel(32, 1)
    sprite('null', 280)
    label(1)
    sprite('null', 20)
    ConstantAlphaModifier(-12)
    sprite('null', 1)
    AlphaValue(0)


@State
def AstStartAura():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ashstart_aura')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1200)
        AbsoluteY(0)
        uponSendToLabel(32, 1)
    sprite('null', 280)
    label(1)
    sprite('null', 20)
    ConstantAlphaModifier(-12)
    sprite('null', 1)
    AlphaValue(0)


@State
def AstChair():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        SetZVal(100)
    sprite('rl450_24ex00', 8)
    sprite('rl450_24ex01', 8)
    sprite('rl450_24ex02', 8)
    sprite('rl450_24ex03', 8)
    sprite('rl450_24ex04', 32767)


@State
def AstClosingDoor():

    def upon_IMMEDIATE():
        Eff3DEffect('rlef_door.DIG', 'rlef_door_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RenderLayer(1)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
    sprite('null', 110)
    XPositionRelativeFacing(0)
    PrivateSE('rlse_10')
    PrivateSE('rlse_10')


@State
def AstClosedDoor():

    def upon_IMMEDIATE():
        Eff3DEffect('rlef_door_close.DIG', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RenderLayer(1)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
    sprite('null', 32767)
    XPositionRelativeFacing(0)


@State
def AstHitRing():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(2000)
    sprite('vr_yugami', 5)
    SetScaleSpeed(50)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami', 24)
    SetScaleSpeed(80)
    Unknown3059(-3200)


@State
def DIST_TEST():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        IgnoreScreenfreeze(1)
        E0EAEffectRotation(2)
    sprite('vr_yugami', 8)
    SetScaleX(1000)
    SetScaleY(2000)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(150)
    sprite('vr_yugami', 10)
    SetScaleXPerFrame(0)
    SetScaleXPerFrame(0)
    ConstantAlphaModifier(-25)


@State
def zan_5D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        SetZVal(-500)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrrlef820_00', 3)
    sprite('vrrlef820_01', 6)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)


@State
def air_5D():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        SetZVal(-500)
        BlendMode_Add()
        AddY(120000)
        PaletteIndex(1)
    sprite('vrrlef830_00', 4)
    CreateParticle('rlef_deleteaura', 0)
    CreateParticle('rlef_deleteaura', 1)
    CreateParticle('rlef_deleteaura', 2)
    CreateParticle('rlef_deleteaura', 3)
    CreateParticle('rlef_deleteaura', 4)
    sprite('vrrlef830_01', 2)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)
    sprite('vrrlef830_02', 2)


@State
def air_2D():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        SetZVal(-500)
        BlendMode_Add()
        AddY(30000)
        AddX(-30000)
        PaletteIndex(1)
    sprite('vrrlef831_00', 4)
    CreateParticle('rlef_deleteaura', 0)
    CreateParticle('rlef_deleteaura', 1)
    CreateParticle('rlef_deleteaura', 2)
    CreateParticle('rlef_deleteaura', 3)
    sprite('vrrlef831_01', 2)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)
    sprite('vrrlef831_02', 2)


@State
def air_6D():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        SetZVal(-500)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrrlef832_00', 4)
    CreateParticle('rlef_deleteaura', 0)
    CreateParticle('rlef_deleteaura', 1)
    CreateParticle('rlef_deleteaura', 2)
    CreateParticle('rlef_deleteaura', 3)
    CreateParticle('rlef_deleteaura', 4)
    sprite('vrrlef832_01', 2)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)
    sprite('vrrlef832_02', 2)


@State
def IgActSignalLight():

    def upon_IMMEDIATE():
        LinkParticle('rlef_igLightsignal')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('null', 12)
    AddRotationPerFrame(3000)


@State
def SpAttack01Eff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        SetZVal(499)
        BlendMode_Normal()
        uponSendToLabel(32, 1)
    sprite('vrrlef840_00', 1)
    CreateObject('SpAttack01Par', -1)
    label(0)
    sprite('vrrlef840_00', 3)
    sprite('vrrlef840_01', 3)
    sprite('vrrlef840_02', 3)
    gotoLabel(0)
    label(1)
    sprite('vrrlef840_00', 3)
    TriggerUponForState('SpAttack01Par', 33)
    ConstantAlphaModifier(-80)
    sprite('vrrlef840_01', 3)
    AlphaValue(0)


@State
def SpAttack01Par():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('rlef_igRolling')
        uponSendToLabel(33, 1)
    sprite('null', 50)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-50)


@State
def SpAttack02zan():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        TurnParticleColorable1(1)
        SetZVal(-500)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711744, 8)
    sprite('vrrlef841zan_00', 1)
    sprite('vrrlef841zan_00', 7)
    CreateObject('SpAttack02zan01', -1)
    sprite('vrrlef841zan_00', 18)
    E0EAEffectPosition(0)
    AddAlpha(-100)


@State
def SpAttack02zan01():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        TurnParticleColorable1(1)
        SetZVal(-500)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711744, 8)
    sprite('vrrlef841zan_01', 8)
    sprite('vrrlef841zan_01', 18)
    E0EAEffectPosition(0)
    AddAlpha(-100)


@State
def SpAttack03zan00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        TurnParticleColorable1(1)
        SetZVal(-500)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711744, 8)
    sprite('vrrlef842zan_00', 3)
    sprite('vrrlef842zan_00', 18)
    E0EAEffectPosition(0)
    AddAlpha(-100)


@State
def SpAttack03zan01():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        TurnParticleColorable1(1)
        SetZVal(-500)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711744, 8)
    sprite('vrrlef842zan_01', 3)
    sprite('vrrlef842zan_01', 18)
    E0EAEffectPosition(0)
    AddAlpha(-100)


@State
def SpAttack03zan02():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        TurnParticleColorable1(1)
        SetZVal(-500)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711744, 12)
    sprite('vrrlef842zan_02', 3)
    sprite('vrrlef842zan_02', 18)
    E0EAEffectPosition(0)
    AddAlpha(-100)


@State
def DownFallMcA():

    def upon_IMMEDIATE():
        LinkParticle('rlef_fallwind')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        E0EAEffectRotation(2)
    sprite('null', 6)
    sprite('null', 24)
    E0EAEffectPosition(0)


@State
def SpAttack04Wind():

    def upon_IMMEDIATE():
        LinkParticle('rlef_igDrill')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 6)
    RotationAngle(40000)
    sprite('null', 24)
    E0EAEffectPosition(0)


@State
def AirSpAttackWind():

    def upon_IMMEDIATE():
        LinkParticle('rlef_igDrill')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 4)
    RotationAngle(90000)
    sprite('null', 24)
    E0EAEffectPosition(0)


@State
def IgnisShot_HasseiObj():

    def upon_IMMEDIATE():
        LinkParticle('rlef_igshotball')
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    SetScaleSpeed(-5)
    Size(1100)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 5)
    SetScaleSpeed(0)
    sprite('null', 2)
    ConstantAlphaModifier(0)
    AlphaValue(180)
    SetScaleSpeed(0)
    Size(1000)


@State
def IgnisShot_TosshinObj():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddX(-40000)
        AbsoluteY(270000)
        LinkParticle('rlef_igshotball')
        physicsXImpulse(0)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    label(0)
    sprite('null', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    AddX(10000)
    AddY(30000)
    sprite('null', 6)
    AddX(420000)
    AddY(-50000)


@State
def IgnisShot_AttackObj():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        AddX(390000)
        AbsoluteY(270000)
        IgnoreScreenfreeze(1)
        LinkParticle('rlef_igshotball')
        physicsXImpulse(0)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 10)
    sprite('null', 30)
    label(1)
    sprite('null', 1)
    AlphaValue(250)
    ConstantAlphaModifier(-25)
    sprite('null', 9)
    CreateObject('big_volante_3D', -1)
    sprite('null', 500)
    loopRest()
    label(10)
    sprite('null', 8)
    CreateParticle('rlef_igshot_break', -1)
    SetScaleSpeed(10)
    AlphaValue(250)
    ConstantAlphaModifier(-10)


@State
def IgnisShotHitCharge():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(1)
        LinkParticle('rlef_igshot_charge')
        physicsXImpulse(0)
        Size(1200)
        uponSendToLabel(32, 1)
    sprite('null', 120)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def big_volante_3D():

    def upon_IMMEDIATE():
        Eff3DEffect('rlef_DDvolante.DIG', 'rlef_DDvolante_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(100)
        AlphaValue(0)
        uponSendToLabel(33, 10)
    sprite('null', 15)
    SetScaleSpeed(65)
    ConstantAlphaModifier(20)
    EffectPosition(22, 103)
    ParticleLayer(6)
    CallCustomizableParticle('rlef_igshot_3D', -1)
    sprite('null', 10)
    CreateObject('IgnisShotHitCharge', -1)
    ConstantAlphaModifier(0)
    SetScaleSpeed(2)
    sprite('null', 30)
    SetScaleSpeed(1)
    sprite('null', 90)
    SetScaleSpeed(0)
    label(10)
    sprite('null', 2)
    ConstantAlphaModifier(-15)
    SetScaleSpeed(100)
    sprite('null', 15)
    CreateParticle('rlef_igshot_perge', -1)
    sprite('null', 1)


@State
def IgnisSparkReverse():

    def upon_IMMEDIATE():
        LinkParticle('rlef_ignisparks_near')
        IgnoreScreenfreeze(1)
        Flip()
    sprite('null', 40)


@State
def zan_851a():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        SetZVal(-500)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrrlef851_21', 2)
    ConstantAlphaModifier(-30)
    sprite('vrrlef851_21', 2)


@State
def zan_851b():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(2)
        SetZVal(-500)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrrlef851_34', 6)
    sprite('vrrlef851_35', 6)
    sprite('vrrlef851_35', 10)
    ConstantAlphaModifier(-24)


@State
def IGAct_MatchWin1():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        NoDamageAction(1)
        SLOT_4 = 90
    sprite('rl800_00', 32767)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    ForceShadowOff(1)
    loopRest()


@State
def IGAct_EntryVsCa0():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        AttackDefaults_SuperProjectile()
        SLOT_4 = 90
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        DollAttackAttributes(1)
        UseSlashHitspark(1)
        IgnoreScreenfreeze(1)
        NoDamageAction(1)
        AttackLevel_(5)
    sprite('keep', 10)
    Visibility(1)
    TeleportToObject(2)
    TurnAround()
    AddX(175000)
    AbsoluteY(0)
    ForceFaceSprite()
    sprite('rl800_00', 4)
    Visibility(0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    sprite('rl800_00', 4)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl800_00', 3)
    sprite('rl820_00', 3)
    sprite('rl820_01', 2)
    sprite('rl820_02', 1)
    sprite('rl820_03', 1)
    sprite('rl820_04', 2)
    physicsXImpulse(12000)
    sprite('rl820_04', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('rl820_05', 5)
    physicsXImpulse(0)
    RefreshMultihit()
    CreateObject('zan_5D', -1)
    sprite('rl820_06', 4)
    sprite('rl820_07', 4)
    sprite('rl820_08', 4)
    sprite('rl820_09', 4)
    sprite('keep', 100)
    PrivateFunction2('IGAct_EntryVsCa0Wait', 100)
    loopRest()


@State
def IGAct_EntryVsCa0Wait():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        callSubroutine('IG_SetupIntrptSignal')
        NoDamageAction(1)
        SLOT_4 = 90
    label(99)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(99)


@State
def IGAct_EntryVsCa1():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        callSubroutine('IG_SetupIntrptSignal')
        NoDamageAction(1)
        SLOT_4 = 90
    sprite('rl802_00', 2)
    physicsXImpulse(-4000)
    sprite('rl802_01', 6)
    sprite('rl802_02', 6)
    sprite('rl802_03', 6)
    sprite('rl802_04', 6)
    sprite('rl802_05', 6)
    sprite('rl802_06', 6)
    sprite('rl802_07', 6)
    sprite('rl802_08', 6)
    sprite('rl802_00', 2)
    physicsXImpulse(0)
    label(99)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(99)


@State
def IGAct_EntryVsRg0():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        AttackDefaults_SuperProjectile()
        SLOT_4 = 90
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        DollAttackAttributes(1)
        UseSlashHitspark(1)
        IgnoreScreenfreeze(1)
        NoDamageAction(1)
    sprite('rl842_00', 3)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(4)
    sprite('rl842_01', 3)
    sprite('rl842_02', 3)
    sprite('rl842_03', 3)
    CreateObject('IgActSignalLight', 0)
    CreateObject('IgActSignalLight', 1)
    sprite('rl842_04', 3)
    sprite('rl842_05', 3)
    sprite('rl842_06', 3)
    physicsXImpulse(20000)
    SetAcceleration(-500)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_07', 3)
    sprite('rl842_06', 3)
    sprite('rl842_07', 3)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_08', 2)
    sprite('rl842_08', 5)
    ObjectUpon(22, 32)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_09', 4)
    sprite('rl842_10', 4)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_11', 3)
    RefreshMultihit()
    CommonSE('010_swing_sword_2')
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_2')
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_12', 4)
    EndMomentum(1)
    CommonSE('004_swing_grap_1_1')
    sprite('rl842_13', 2)
    sprite('rl842_14', 1)
    sprite('rl842_15', 1)
    sprite('rl842_16', 1)
    sprite('rl842_17', 1)
    sprite('rl842_18', 1)
    sprite('rl842_19', 1)
    sprite('rl842_20', 2)
    sprite('rl842_21', 2)
    sprite('rl842_22', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('rl842_23', 3)
    RefreshMultihit()
    CommonSE('010_swing_sword_2')
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_2')
    CreateObject('SpAttack03zan02', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    physicsXImpulse(-40000)
    SetAcceleration(1800)
    sprite('rl842_24', 3)
    sprite('rl842_25', 3)
    sprite('rl842_26', 3)
    sprite('rl842_27', 3)
    sprite('rl841_18', 3)
    EnableAfterimage(0)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    EndMomentum(1)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    sprite('rl843_00', 4)
    sprite('rl843_01', 3)
    sprite('rl843_02', 3)
    SLOT_31 = SLOT_31 + -1000
    sprite('rl843_03', 4)
    sprite('rl843_04', 3)
    CommonSE('005_swing_grap_2_2')
    sprite('rl843_05', 9)
    RefreshMultihit()
    CommonSE('010_swing_sword_2')
    CommonSE('004_swing_grap_1_2')
    CommonSE('005_swing_grap_2_2')
    sprite('rl843_06', 3)
    sprite('rl843_07', 3)
    sprite('rl843_08', 3)
    sprite('rl843_09', 3)
    sprite('rl843_10', 3)
    sprite('rl843_11', 3)
    sprite('rl843_12', 3)
    sprite('rl843_13', 3)
    sprite('rl843_14', 3)
    sprite('rl843_15', 3)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    sprite('keep', 100)
    PrivateFunction2('IGAct_EntryVsRg0Wait', 100)


@State
def IGAct_EntryVsRg0Wait():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        callSubroutine('IG_SetupIntrptSignal')
        NoDamageAction(1)
        SLOT_4 = 90
    label(99)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(99)


@State
def IGAct_EntryVsHa0():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        AttackDefaults_SuperProjectile()
        SLOT_4 = 90
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        DollAttackAttributes(1)
        UseSlashHitspark(1)
        IgnoreScreenfreeze(1)
        NoDamageAction(1)
    sprite('rl800_00', 3)
    sprite('rl820_00', 2)
    sprite('rl820_01', 2)
    sprite('rl820_02', 2)
    sprite('rl820_03', 2)
    sprite('rl820_04', 2)
    AddX(40000)
    physicsXImpulse(12000)
    sprite('rl820_04', 3)
    physicsXImpulse(80000)
    CommonSE('005_swing_grap_2_2')
    sprite('rl820_05', 3)
    physicsXImpulse(0)
    RefreshMultihit()
    CreateObject('zan_5D', -1)
    sprite('rl820_06', 3)
    sprite('rl820_07', 3)
    sprite('rl820_08', 3)
    sprite('rl820_09', 3)
    sprite('rl841_00', 5)
    RefreshMultihit()
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    CreateObject('IgActSignalLight', 0)
    sprite('rl841_01', 3)
    sprite('rl841_02', 3)
    sprite('rl841_03', 3)
    sprite('rl841_04', 3)
    CommonSE('004_swing_grap_1_2')
    sprite('rl841_05', 3)
    CreateObject('SpAttack02zan', -1)
    sprite('rl841_06', 3)
    sprite('rl841_07', 3)
    sprite('rl841_08', 3)
    sprite('rl841_09', 3)
    sprite('rl841_10', 3)
    sprite('rl841_11', 3)
    sprite('rl841_12', 3)
    sprite('rl841_13', 3)
    sprite('rl841_14', 3)
    sprite('rl841_15', 3)
    sprite('rl841_16', 3)
    sprite('rl841_17', 3)
    sprite('rl841_18', 3)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    sprite('keep', 100)
    PrivateFunction2('IGAct_EntryVsRg0Wait', 100)


@State
def IGAct_EntryVsHa0Wait():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        callSubroutine('IG_SetupIntrptSignal')
        NoDamageAction(1)
        SLOT_4 = 90
    label(99)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(99)


@State
def IGAct_EntryVsVh0():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        AttackDefaults_SuperProjectile()
        SLOT_4 = 90
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        DollAttackAttributes(1)
        UseSlashHitspark(1)
        IgnoreScreenfreeze(1)
        NoDamageAction(1)
    sprite('rl800_00', 3)
    sprite('rl820_00', 2)
    sprite('rl820_01', 2)
    sprite('rl820_02', 2)
    sprite('rl820_03', 2)
    sprite('rl820_04', 2)
    AddX(40000)
    physicsXImpulse(12000)
    sprite('rl820_04', 3)
    physicsXImpulse(80000)
    CommonSE('005_swing_grap_2_2')
    sprite('rl820_05', 3)
    physicsXImpulse(0)
    RefreshMultihit()
    CreateObject('zan_5D', -1)
    sprite('rl820_06', 3)
    sprite('rl820_07', 3)
    sprite('rl820_08', 3)
    sprite('rl820_09', 3)
    sprite('rl841_00', 3)
    RefreshMultihit()
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    CreateObject('IgActSignalLight', 0)
    sprite('rl841_01', 3)
    sprite('rl841_02', 3)
    sprite('rl841_03', 2)
    sprite('rl841_04', 2)
    CommonSE('004_swing_grap_1_2')
    sprite('rl841_05', 3)
    CreateObject('SpAttack02zan', -1)
    sprite('rl841_06', 3)
    sprite('rl841_07', 3)
    sprite('rl841_08', 3)
    sprite('rl841_09', 3)
    sprite('rl841_10', 3)
    sprite('rl841_11', 3)
    sprite('rl841_12', 3)
    sprite('rl841_13', 3)
    sprite('rl841_14', 3)
    sprite('rl841_15', 3)
    sprite('rl841_16', 3)
    sprite('rl841_17', 3)
    sprite('rl841_18', 3)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)
    sprite('keep', 100)
    PrivateFunction2('IGAct_EntryVsRg0Wait', 100)


@State
def RlAstralDamageIG():

    def upon_IMMEDIATE():
        ScriptEndGroundBounce_()
        EnableCollision(0)
        SetZVal(100)
        XPositionRelativeFacing(-180000)
    label(0)
    sprite('rl814_10', 7)
    CreateParticle('rlef_ig_break', 0)
    loopRest()
    gotoLabel(0)


@State
def BurstDD_Wave():

    def upon_IMMEDIATE():
        SetActionMark(4)
        TeleportToObject(22)
        AddX(100000)
    sprite('null', 1)
    label(0)
    sprite('null', 12)
    AddX(-50000)
    CreateObject('BurstDD_Arm', -1)
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(0)
    sprite('null', 1)
    AddX(-50000)
    CreateObject('BurstDD_Arm', -1)
    ObjectUpon(STATE_END, 32)


@State
def BurstDD_Arm():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(300)
        AttackP2(100)
        SameMoveProration(-1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirUntechableTime(100)
        AirPushbackX(-30000)
        AirPushbackY(18000)
        Hitstop(8)
        FlipOnHit(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        DamageFromStateOnly('BurstDD_Arm')
        CHStateIfCHStart(3)
        OnlyHitPlayer(1)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
        if SLOT_51:
            Damage(600)

        def upon_32():
            DamageFromStateOnly('BurstDDAdd')
        Flip()
    sprite('vrrlef440_10', 4)
    CreateParticle('rlef_405enter_wind', -1)
    sprite('vrrlef440_10', 2)
    sprite('vrrlef440_11', 2)
    RefreshMultihit()
    sprite('vrrlef440_12', 2)
    sprite('vrrlef440_13', 2)
    sprite('vrrlef440_14', 2)


@State
def BurstDD_BGEff():

    def upon_IMMEDIATE():
        AddY(230000)
        AddX(200000)
        Flip()
    sprite('null', 2)
    ScreenShake(20000, 20000)
    ParticleLayer(11)
    CallCustomizableParticle('rlef_440atkeff', -1)
    sprite('null', 2)
    ScreenShake(10000, 10000)
    sprite('null', 2)
    ScreenShake(5000, 5000)


@State
def BurstDD_BGEffEX():

    def upon_IMMEDIATE():
        AddY(230000)
        AddX(200000)
        Flip()
    sprite('null', 2)
    ScreenShake(30000, 30000)
    ParticleSize(1300)
    ParticleLayer(11)
    CallCustomizableParticle('rlef_440atkeffEX', -1)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(10000, 10000)


@State
def BurstDD_ExEff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AddY(230000)
        AddX(480000)
        Size(1500)
        EnableAfterimage(1)
    sprite('vrrlef440_00', 15)
    sprite('vrrlef440_01', 3)
    sprite('vrrlef440_02', 3)
    sprite('vrrlef440_02', 3)
    ConstantAlphaModifier(-47)
    SetScaleSpeed(100)
    physicsXImpulse(20000)
    sprite('vrrlef440_03', 2)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def IGAct_EventVsCA00():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        NoAttackDuringAction(1)
        NoDamageAction(1)
        BlendMode_Normal()
    sprite('rl851_21', 3)
    TeleportToObject(2)
    CtrlDirectionVsTarget()
    SetZVal(-500)
    EnableCollision(0)
    WallCollisionDetection(0)
    AddX(150000)
    AddY(-50000)
    Visibility(1)
    sprite('rl851_21', 3)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    Visibility(0)
    sprite('rl851_21', 3)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl851_22', 3)
    sprite('rl851_23', 3)
    sprite('rl851_24', 15)
    sprite('rl851_24', 1)
    CommonSE('104_guard_grap_2')
    AddX(-5000)
    ParticleColor(4278223103, 4278202623, 4278190335)
    CallCustomizableParticle('ef_girdl', 107)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(5000)
    sprite('rl851_24', 1)
    AddX(-5000)
    sprite('rl851_24', 5)
    physicsXImpulse(-6000)
    sprite('rl851_24', 5)
    XImpulseAcceleration(50)
    sprite('rl851_24', 5)
    XImpulseAcceleration(30)
    sprite('rl851_24', 45)
    physicsXImpulse(0)
    sprite('rl851_25', 3)
    sprite('rl851_26', 3)
    sprite('rl851_27', 3)
    sprite('rl851_28', 4)
    sprite('rl851_29', 4)
    sprite('rl851_38', 5)
    sprite('rl851_39', 5)
    sprite('rl851_40', 5)
    sprite('rl851_41', 5)
    sprite('rl851_42', 5)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def IGAct_EventAct2_azvsrl():

    def upon_IMMEDIATE():
        callSubroutine('IG_ActReset')
        NoDamageAction(1)
        EnableCollision(0)
        WallCollisionDetection(0)
    sprite('rl851_32', 7)
    TeleportToObject(2)
    CtrlDirectionVsTarget()
    SetZVal(-500)
    AddX(-160000)
    AddY(-50000)
    physicsXImpulse(15000)
    Visibility(1)
    sprite('rl851_32', 4)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    Visibility(0)
    sprite('rl851_32', 4)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl851_32', 4)
    XImpulseAcceleration(50)
    sprite('rl851_33', 4)
    XImpulseAcceleration(50)
    sprite('rl851_34', 17)
    CommonSE('005_swing_grap_2_2')
    CreateParticle('rlef_ig851upper', -1)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    AddX(-5000)
    XImpulseAcceleration(50)
    sprite('rl851_34', 5)
    XImpulseAcceleration(50)
    sprite('rl851_35', 3)
    XImpulseAcceleration(50)
    sprite('rl851_36', 3)
    XImpulseAcceleration(50)
    sprite('rl851_37', 3)
    XImpulseAcceleration(0)
    sprite('rl851_38', 5)
    sprite('rl851_39', 5)
    sprite('rl851_40', 5)
    sprite('rl851_41', 5)
    sprite('rl851_42', 5)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('keep', 100)
    PrivateFunction2('IGAct_SwitchFollow', 100)


@State
def Act3Event_IGCreate():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        uponSendToLabel(41, 9)
        SetZVal(500)
    sprite('rl800_00', 4)
    XPositionRelativeFacing(-100000)
    Visibility(1)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_in', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    Visibility(0)
    StopCharacterFlash1(16777215)
    CharacterFlash2(0, 10)
    sprite('rl800_00', 2)
    StopCharacterFlash2()
    SetScaleXPerFrame(0)
    label(0)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rl801_00', 2)
    physicsXImpulse(1600)
    sprite('rl801_01', 6)
    sprite('rl801_02', 6)
    sprite('rl801_03', 6)
    sprite('rl801_04', 6)
    sprite('rl801_05', 6)
    sprite('rl801_06', 6)
    sprite('rl801_07', 6)
    sprite('rl801_08', 6)
    loopRest()
    sprite('rl801_00', 2)
    physicsXImpulse(0)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rl800_00', 15)
    physicsXImpulse(0)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    sprite('keep', 1)
    Visibility(1)


@State
def Act3Event_IGCreateYoin():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        uponSendToLabel(41, 9)
        SetZVal(500)
        NoAttackDuringAction(1)
        XPositionRelativeFacing(-600000)
    sprite('rl850_15', 3)
    physicsXImpulse(60000)
    sprite('rl850_16', 7)
    XImpulseAcceleration(50)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    sprite('rl850_17', 3)
    XImpulseAcceleration(20)
    sprite('rl850_18', 2)
    ObjectUpon(5, 32)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_ignisparks', 2)
    XImpulseAcceleration(10)
    CommonSE('005_swing_grap_2_2')
    sprite('rl850_19', 20)
    XImpulseAcceleration(20)
    ScreenShake(15000, 30000)
    CreateParticle('rlef_ignisparks', 0)
    CreateParticle('rlef_ignisparks', 1)
    CreateParticle('rlef_igshot_wind', 2)
    ObjectUpon(22, 32)
    sprite('rl850_20', 3)
    XImpulseAcceleration(10)
    PrivateSE('rlse_13')
    sprite('rl850_21', 3)
    XImpulseAcceleration(0)
    sprite('rl850_22', 3)
    sprite('rl850_23', 3)
    sprite('rl850_24', 3)
    sprite('rl850_25', 3)
    sprite('rl850_26', 3)
    sprite('rl850_27', 3)
    sprite('rl850_28', 3)
    sprite('rl850_29', 3)
    sprite('rl850_30', 3)
    label(0)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rl801_00', 2)
    physicsXImpulse(3200)
    sprite('rl801_01', 6)
    sprite('rl801_02', 6)
    sprite('rl801_03', 6)
    sprite('rl801_04', 6)
    sprite('rl801_05', 6)
    sprite('rl801_06', 6)
    sprite('rl801_07', 6)
    sprite('rl801_08', 6)
    sprite('rl801_00', 2)
    physicsXImpulse(0)
    loopRest()
    gotoLabel(0)
    label(2)
    SetActionMark(4)
    sprite('rl801_00', 2)
    physicsXImpulse(3200)
    CreateObject('Act3Event_IGCamera', -1)
    label(3)
    sprite('rl801_01', 6)
    sprite('rl801_02', 6)
    sprite('rl801_03', 6)
    sprite('rl801_04', 6)
    sprite('rl801_05', 6)
    sprite('rl801_06', 6)
    sprite('rl801_07', 6)
    sprite('rl801_08', 6)
    AddActionMark(-1)
    loopRest()
    if SLOT_2:
        conditionalSendToLabel(3)
    sprite('rl801_00', 2)
    physicsXImpulse(0)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rl800_00', 15)
    sprite('rl800_00', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)
    sprite('keep', 1)
    Visibility(1)


@State
def Act3Event_IGCamera():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddX(100000)
    sprite('null', 32767)
    CameraControlEnable(1)


@State
def Act3Event_lcvsrl_ig():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            if SLOT_54:
                if SLOT_19 < 200000:
                    sendToLabel(0)
                    SLOT_54 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('Act_IG_AirAttack03', 32)
        CreateDecalOn(1)
        FloorCollision(1)

    def upon_52():
        if GuardpointNonProjectileCheck():
            CreateParticle('ef_exgird', 102)
            CommonSE('105_guard_slash_2')
            GuardpointHitstop(8, -1)
        else:
            CommonSE('105_guard_slash_0')
        Unknown23099(240)
        Unknown23105(240)
        Unknown23111(240)
        Unknown23102(-48)
        Unknown23108(-48)
        Unknown23114(-48)
    sprite('rl831_00', 3)
    sprite('rl831_01', 2)
    physicsXImpulse(7500)
    physicsYImpulse(-3750)
    sprite('rl831_01', 1)
    SLOT_31 = SLOT_31 + -1000
    sprite('rl831_02', 2)
    physicsXImpulse(30000)
    physicsYImpulse(-20000)
    sprite('rl831_01', 2)
    SLOT_54 = 1
    physicsXImpulse(50000)
    physicsYImpulse(-35000)
    sprite('rl831_02', 2)
    sprite('rl831_03', 2)
    sprite('rl831_04', 2)
    physicsXImpulse(20000)
    physicsYImpulse(-10000)
    label(0)
    clearUponHandler(EVERY_FRAME)
    sprite('rl831_04', 1)
    CommonSE('006_swing_blade_2')
    sprite('rl831_05', 17)
    CreateObject('Act3Event_lcvsrl_ig_eff', -1)
    RefreshMultihit()
    EndMomentum(1)
    sprite('rl831_05', 1)
    physicsXImpulse(10000)
    physicsYImpulse(-5000)
    sprite('rl831_06', 4)
    physicsXImpulse(8000)
    physicsYImpulse(-4000)
    sprite('rl831_07', 4)
    physicsXImpulse(6000)
    physicsYImpulse(-3000)
    sprite('rl831_08', 4)
    physicsXImpulse(4000)
    physicsYImpulse(-2000)
    sprite('rl831_09', 4)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('keep', 10)
    PrivateSE('rlse_16')
    CreateParticle('rlef_warp_out', -1)
    CreateObject('DIST_TEST', 0)
    SetScaleXPerFrame(-100)


@State
def Act3Event_lcvsrl_ig_eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        SetZVal(-500)
        BlendMode_Add()
        AddY(30000)
        AddX(-30000)
        PaletteIndex(1)
    sprite('vrrlef831_00', 14)
    CreateParticle('rlef_deleteaura', 0)
    CreateParticle('rlef_deleteaura', 1)
    CreateParticle('rlef_deleteaura', 2)
    CreateParticle('rlef_deleteaura', 3)
    sprite('vrrlef831_01', 2)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)
    sprite('vrrlef831_02', 2)


@State
def IGAct_EntryVsCaAct3_0():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        NoDamageAction(1)

        def upon_EVERY_FRAME():

            def upon_OPPONENT_HIT_OR_BLOCK():
                XImpulseAcceleration(25)
                PushSpeedX()
                EndMomentum(1)

        def upon_32():
            PrivateFunction2('IGAct_Delete', 100)
        RunLoopUpon(17, 999)

        def upon_17():
            PrivateFunction2('IGAct_Delete', 100)
    sprite('rl800_00', 10)
    TeleportToObject(2)
    TurnAround()
    AddX(-150000)
    AddY(0)
    sprite('rl842_00', 3)
    SetScaleX(1000)
    SetScaleXPerFrame(0)
    sprite('rl842_01', 3)
    sprite('rl842_02', 3)
    sprite('rl842_03', 3)
    CreateObject('IgActSignalLight', 0)
    CreateObject('IgActSignalLight', 1)
    sprite('rl842_04', 3)
    sprite('rl842_05', 3)
    sprite('rl842_06', 3)
    CreateParticle('rlef_ignisparksAir', 0)
    physicsXImpulse(5000)
    if SLOT_55:
        physicsXImpulse(5000)
    sprite('rl842_07', 3)
    XImpulseAcceleration(150)
    sprite('rl842_06', 3)
    XImpulseAcceleration(150)
    sprite('rl842_07', 3)
    CreateParticle('rlef_ignisparksAir', 0)
    XImpulseAcceleration(200)
    sprite('rl842_06', 3)
    XImpulseAcceleration(250)
    sprite('rl842_07', 3)
    label(40)
    SetAcceleration(0)
    sprite('rl842_08', 2)
    CreateParticle('rlef_ignisparksAir', 0)
    sprite('rl842_09', 2)
    sprite('rl842_10', 2)
    CommonSE('006_swing_blade_1')
    sprite('rl842_11', 12)
    CreateObject('SpAttack03zan00', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    physicsXImpulse(16000)
    sprite('rl842_12', 6)
    PopSpeedX()
    CommonSE('006_swing_blade_1')
    sprite('rl842_13', 12)
    CreateObject('SpAttack03zan01', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    AirPushbackY(14400)
    physicsXImpulse(16000)
    sprite('rl842_14', 1)
    PopSpeedX()
    sprite('rl842_15', 1)
    sprite('rl842_16', 1)
    XImpulseAcceleration(50)
    sprite('rl842_17', 1)
    sprite('rl842_18', 1)
    sprite('rl842_19', 1)
    XImpulseAcceleration(40)
    sprite('rl842_20', 1)
    sprite('rl842_21', 1)
    sprite('rl842_22', 1)
    XImpulseAcceleration(30)
    CommonSE('006_swing_blade_2')
    sprite('rl842_23', 16)
    CreateObject('SpAttack03zan02', -1)
    CreateParticle('rlef_ignisparksAir', 0)
    RefreshMultihit()
    physicsXImpulse(16000)
    sprite('rl842_24', 3)
    PopSpeedX()
    sprite('rl842_25', 3)
    sprite('rl842_26', 3)
    sprite('rl842_27', 3)
    sprite('rl841_18', 3)
    XImpulseAcceleration(0)
    sprite('rl841_19', 3)
    sprite('rl841_20', 3)
    sprite('rl841_21', 3)
    sprite('rl841_22', 3)
    sprite('rl841_23', 3)
    physicsXImpulse(0)
    label(0)
    sprite('rl800_00', 7)
    sprite('rl800_01', 7)
    sprite('rl800_02', 7)
    sprite('rl800_03', 7)
    sprite('rl800_04', 7)
    sprite('rl800_05', 7)
    sprite('rl800_06', 7)
    sprite('rl800_07', 7)
    loopRest()
    gotoLabel(0)
