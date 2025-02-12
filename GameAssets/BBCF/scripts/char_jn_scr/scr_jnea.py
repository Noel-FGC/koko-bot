@State
def EMB_JN():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_JN.DIG', '')
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
    sprite('null', 80)


@State
def EMB_JN_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_JN.DIG', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 80)


@State
def EMB_JN_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_JN.DIG', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 80)


@Subroutine
def CheckOverDriveShotFreeze():
    if SLOT_OverdriveTimer:
        ResetAttackP2()
        FreezeCount(3)
        EnemyHitstopAddition(6, 0, 5)

        def upon_OPPONENT_HIT():
            ScreenShake(20000, 20000)


@Subroutine
def CheckOverDriveSpecial():
    if SLOT_OverdriveTimer:
        HeatGainMultiplier(100)
        HeatCooldown(0)


@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('jnef_mc_sta.DIG', '')
        FaceSpawnLocation()
        RenderLayer(2)
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 42)


@State
def ModelMagicCircle2():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('jnef_mc_sit.DIG', '')
        FaceSpawnLocation()
        RenderLayer(2)
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 42)


@State
def ModelMagicCircle3():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('jnef_mc_jum.DIG', '')
        FaceSpawnLocation()
        RenderLayer(2)
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 30)


@State
def ModelMagicCircle4():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('jnef_mc_fsi.DIG', '')
        FaceSpawnLocation()
        RenderLayer(2)
        PaletteIndex(1)
        ColorFromPaletteIndex(240)
    sprite('null', 42)


@State
def jn_DD_2_ex():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        AddX(128000)
        AddY(256000)
        ParticleFacing(2)
        CallPrivateEffect('jnef_DD_ex')
    sprite('null', 300)


@State
def EffNoutou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        ContinueState(12)
    sprite('null', 12)
    Visibility(1)
    LinkParticle('jnef_bl')
    PrivateSE('jnse_00')


@State
def EffYukikaze():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AbsoluteY(0)
    sprite('null', 32767)
    LinkParticle('jnef_yukikaze')


@State
def IceBreakPtcL():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(96, 96, 96)
    CallCustomizableParticle('jnef_icebrl', -1)


@State
def IceBreakPtcM():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(96, 96, 96)
    CallCustomizableParticle('jnef_icebrm', -1)


@State
def IceBreakPtcS():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(96, 96, 96)
    CallCustomizableParticle('jnef_icebrs', -1)


@State
def IceMakePtc():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    CreateParticle('jnef_icesmoke00', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_iceptc00', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_iceptc', -1)


@State
def IceCirclePtc():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(175, 175, 175)
    CallCustomizableParticle('jnef_circle00', -1)


@State
def IceBreakPtc601():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(96, 96, 96)
    ParticleSize(500)
    CallCustomizableParticle('jnef_icebrm', -1)


@State
def jnef601ptc():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(175, 96, 240)
    CallCustomizableParticle('jnef601_mc00', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef601_mc01', -1)
    ParticleColorFromPalette(175, 175, 175)
    CallCustomizableParticle('jnef601_mc02', -1)
    ParticleColorFromPalette(175, 175, 175)
    CallCustomizableParticle('jnef601_mc03', -1)
    ParticleColorFromPalette(175, 175, 175)
    CallCustomizableParticle('jnef601_circle00', -1)
    ParticleColorFromPalette(175, 175, 175)
    CallCustomizableParticle('jnef601', -1)


@State
def jnef611_hane():
    sprite('null', 1)
    PaletteIndex(1)
    Visibility(1)
    ParticleColorFromPalette(175, 175, 1)
    CallCustomizableParticle('jnef611_hane', 2)


@State
def jnef_25percent():
    sprite('null', 1)
    AddY(300000)
    CallCustomizableParticle('jnef_25percent', -1)


@State
def zan_a0():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan_a0', 20)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(8)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def zan_b0():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan202', 24)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(10)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def zan_d0():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan_d0', 1)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(8)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)
    sprite('vrzan_d1', 1)
    sprite('vrzan_d2', 12)


@State
def zan_e0():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan_e0', 12)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(6)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def zan407():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan407', 12)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(10)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def zan408():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan408_16z', 6)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(14)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def zan409():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan409_06z', 6)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(14)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def zan412():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan412_00', 2)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(8)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)
    sprite('vrzan412_01', 2)
    sprite('vrzan412_01', 16)
    physicsYImpulse(-4000)


@State
def zan414():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrzan414_00', 2)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(14)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)
    sprite('vrzan414_01', 20)


@State
def zan235():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        PaletteIndex(1)
        AddX(130000)
        AddY(-20000)
    sprite('vrzan235_00', 24)
    TurnParticleColorable1(1)
    PaletteEffType(1)
    PaletteColor1(10)
    PaletteColor2(242)
    PaletteColor3(241)
    PaletteColor4(250)


@State
def IcicleSub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SpecialProjectile()
        E0EAEffectRotation(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrjnef233_00', 3)
    CreateObject('IceMakePtc', -1)
    sprite('vrjnef233_01', 3)
    sprite('vrjnef233_02', 3)
    sprite('vrjnef233_03', 13)
    AlphaValue(200)
    ConstantAlphaModifier(-20)
    ParticleColorFromPalette(111, 111, 111)
    ParticleSize(400)
    CallCustomizableParticle('jnef_icebrm', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceMakePtc', -1)
    sprite('vrjnef233_04', 12)


@State
def Icicle_Env():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vrjnef233env', 3)
    Size(200)
    SetScaleSpeed(30)
    ConstantAlphaModifier(10)
    sprite('vrjnef233env', 3)
    Size(900)
    sprite('vrjnef233env', 3)
    Size(950)
    sprite('vrjnef233env', 16)
    SetScaleSpeed(-10)
    ConstantAlphaModifier(-10)


@State
def IcicleAttack():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(960)
        AttackP1(90)
        AttackP2(82)
        AirPushbackX(-6000)
        PushbackX(-12000)
        Hitstop(18)
        UseSlashHitspark(1)
        UseFreezeHitspark(1)
        FreezeCount(1)
        FreezeTime(40)
        MoveAttributes(0, 0, 0, 1, 0)
        AddX(-50000)
        BlendMode_Add()
        Size(1000)
        AlphaValue(255)
        callSubroutine('CheckOverDriveShotFreeze')
        if SLOT_OverdriveTimer:
            FreezeTime(55)
        HitsPerCall(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            AttackOff()
    sprite('vrjnef233atk_00', 3)
    SetScaleSpeed(-5)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef233atk_01', 3)
    Size(800)
    SetScaleSpeed(-5)
    CreateObject('Icicle_Env', -1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef233atk_02ex01', 3)
    SetScaleSpeed(0)
    Size(900)
    sprite('vrjnef233atk_02', 3)
    Size(1000)
    SetScaleSpeed(5)
    CommonSE('017_freeze_1')
    CommonSE('017_freeze_1')
    sprite('vrjnef233atk_03', 3)
    SetScaleSpeed(0)
    AlphaValue(200)
    ConstantAlphaModifier(-15)
    sprite('vrjnef233atk_04', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceCirclePtc', 2)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcL', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 6)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 6)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    CommonSE('018_ice_break_1')
    sprite('vrjnef233atk_05', 10)


@State
def EffAtk5D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        AlphaValue(255)
    sprite('vrjnef203_01ex', 2)
    CreateObject('EffAtk5D_Env', -1)
    SetScaleX(750)
    SetScaleY(900)
    CommonSE('017_freeze_0')
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef203_01ex', 2)
    SetScaleX(900)
    SetScaleY(950)
    CommonSE('017_freeze_0')
    sprite('vrjnef203_01', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    Size(1000)
    SetScaleSpeed(1)
    CommonSE('017_freeze_1')
    sprite('vrjnef203_02', 4)
    sprite('vrjnef203_03', 4)
    CreateObject('IceCirclePtc', 2)
    CreateObject('IceCirclePtc', 3)
    CreateObject('IceCirclePtc', 9)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 6)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcM', 9)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 6)
    CreateObject('IceBreakPtcS', 10)
    CreateObject('IceBreakPtcS', 11)
    CreateObject('IceBreakPtcS', 12)
    CommonSE('018_ice_break_1')
    sprite('vrjnef203_04', 20)


@State
def EffAtk5D_Env():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('vrjnef203env', 10)
    BlendMode_Add()
    Size(1000)
    SetScaleSpeed(2)
    AlphaValue(0)
    ConstantAlphaModifier(16)
    sprite('vrjnef203env', 20)
    SetScaleSpeed(-5)
    AlphaValue(160)
    ConstantAlphaModifier(-8)


@State
def EffAtk6D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_Projectile()
        AttackLevel_(5)
        Damage(1000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(26)
        AttackP2(84)
        BonusProration(110)
        AirPushbackY(20000)
        PushbackX(12000)
        Hitstop(20)
        FreezeCount(1)
        FreezeTime(45)
        MoveAttributes(0, 0, 0, 1, 0)
        UseSlashHitspark(1)
        UseFreezeHitspark(1)
        HitsPerCall(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            AttackOff()
        callSubroutine('CheckOverDriveShotFreeze')
        if SLOT_OverdriveTimer:
            FreezeTime(55)
    sprite('vrjnef213_00', 3)
    CreateObject('EffAtk6D_Env', -1)
    BlendMode_Add()
    AlphaValue(128)
    Size(600)
    SetScaleSpeed(-3)
    CommonSE('017_freeze_0')
    NoAttackDuringAction(1)
    sprite('vrjnef213_00', 3)
    AlphaValue(255)
    Size(900)
    SetScaleSpeed(-3)
    CommonSE('017_freeze_0')
    sprite('vrjnef213_00', 6)
    Size(1100)
    SetScaleSpeed(-3)
    CommonSE('017_freeze_1')
    NoAttackDuringAction(0)
    sprite('vrjnef213_01', 4)
    AlphaValue(200)
    ConstantAlphaModifier(-20)
    physicsXImpulse(1200)
    XSpeed(10)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceCirclePtc', 2)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcL', 2)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 6)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CommonSE('018_ice_break_1')
    sprite('vrjnef213_03', 4)
    sprite('vrjnef213_05', 4)


@State
def EffAtk6D_Env():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    sprite('vrjnef213env', 10)
    BlendMode_Add()
    Size(1000)
    SetScaleSpeed(20)
    AlphaValue(0)
    ConstantAlphaModifier(24)
    physicsXImpulse(800)
    sprite('vrjnef213env', 10)
    SetScaleSpeed(-5)
    AlphaValue(240)
    ConstantAlphaModifier(-24)
    physicsXImpulse(1000)


@State
def EffAtk8D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrjnef253_00', 2)
    CreateObject('EffAtk8D_Env', -1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    Size(400)
    SetScaleSpeed(-3)
    CommonSE('017_freeze_0')
    sprite('vrjnef253_00', 2)
    Size(650)
    SetScaleSpeed(-3)
    CommonSE('017_freeze_0')
    sprite('vrjnef253_00', 12)
    Size(800)
    SetScaleSpeed(5)
    AlphaValue(255)
    ConstantAlphaModifier(-24)
    CommonSE('017_freeze_1')


@State
def EffAtk8D_Env():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        BlendMode_Add()
    sprite('vrjnef253env', 4)
    Size(300)
    SetScaleSpeed(100)
    AlphaValue(0)
    ConstantAlphaModifier(24)
    sprite('vrjnef253env', 8)
    SetScaleSpeed(5)
    AlphaValue(240)
    ConstantAlphaModifier(-20)


@State
def jnef311():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrjnef311_00', 2)
    CreateDecal(1, 'FLORE_FROST', -1, 2000, 2000)
    AlphaValue(192)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef311_01', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef311_02', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef311_03', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef311_04', 2)
    CommonSE('017_freeze_1')
    CommonSE('017_freeze_1')
    sprite('vrjnef311_05', 25)
    sprite('vrjnef311_06', 3)
    sprite('vrjnef311_07', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceCirclePtc', 6)
    CreateObject('IceBreakPtcL', 6)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcM', 9)
    CreateObject('IceBreakPtcM', 10)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    CreateObject('IceBreakPtcS', 10)
    CommonSE('018_ice_break_1')
    sprite('vrjnef311_08', 12)
    ConstantAlphaModifier(-30)


@State
def jnef321top():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(2)
        BlendMode_Add()
        Size(-1000)
    sprite('vrjnef321_00', 2)
    AlphaValue(192)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef321_01', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef321_02', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef321_03', 2)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('vrjnef321_04', 2)
    CommonSE('017_freeze_1')
    CommonSE('017_freeze_1')
    sprite('vrjnef321_05', 25)
    sprite('vrjnef321_06', 3)
    sprite('vrjnef321_07', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcM', 9)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    CommonSE('018_ice_break_1')
    sprite('vrjnef321_08', 12)
    ConstantAlphaModifier(-30)


@State
def jnef321bottom():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrjnef321_00', 2)
    AlphaValue(192)
    sprite('vrjnef321_01', 2)
    sprite('vrjnef321_02', 2)
    sprite('vrjnef321_03', 2)
    sprite('vrjnef321_04', 2)
    sprite('vrjnef321_05', 25)
    sprite('vrjnef321_06', 3)
    sprite('vrjnef321_07', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcM', 9)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    sprite('vrjnef321_08', 12)
    ConstantAlphaModifier(-30)


@State
def EFF28AtkA():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrjnef405_00', 1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef405_01', 3)
    sprite('vrjnef405_02', 3)
    sprite('vrjnef405_03', 3)
    sprite('vrjnef405_04', 3)
    sprite('vrjnef405_05', 3)
    sprite('vrjnef405_06', 8)
    AlphaValue(200)
    ConstantAlphaModifier(-30)


@State
def EFF28AtkB():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        AlphaValue(255)
        Size(1000)
    sprite('vrjnef405_00', 3)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef405_01', 3)
    sprite('vrjnef405_02', 3)
    sprite('vrjnef405_03', 3)
    sprite('vrjnef405_04', 3)
    sprite('vrjnef405_05', 3)
    sprite('vrjnef405_06', 8)
    AlphaValue(200)
    ConstantAlphaModifier(-30)


@State
def EFF28AtkC():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        SetScaleY(1400)
        AlphaValue(255)
    sprite('vrjnef406_00', 2)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef406_01', 2)
    sprite('vrjnef406_02', 2)
    sprite('vrjnef406_03', 2)
    sprite('vrjnef406_04', 2)
    sprite('vrjnef406_05', 2)
    sprite('vrjnef406_06', 2)
    sprite('vrjnef406_07', 2)
    sprite('vrjnef406_08', 6)
    AlphaValue(200)
    ConstantAlphaModifier(-40)


@State
def EFF28AtkD():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        AlphaValue(255)
        Size(1000)
    sprite('vrjnef407_00', 3)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef407_01', 2)
    sprite('vrjnef407_02', 2)
    sprite('vrjnef407_03', 2)
    sprite('vrjnef407_04', 2)
    sprite('vrjnef407_05', 6)
    physicsXImpulse(-3000)
    physicsYImpulse(750)
    AlphaValue(200)
    ConstantAlphaModifier(-30)


@State
def EFF413C():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AddY(224000)
        Size(2000)
    sprite('vrjnef413_00', 3)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    sprite('vrjnef413_01', 6)
    sprite('vrjnef413_02', 3)
    sprite('vrjnef413_03', 8)
    AlphaValue(200)
    ConstantAlphaModifier(-30)


@State
def EFF413D():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AddY(224000)
        Size(2000)
    sprite('vrjnef413_10', 3)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('vrjnef413_11', 3)
    sprite('vrjnef413_12', 3)
    sprite('vrjnef413_13', 3)
    AlphaValue(200)
    ConstantAlphaModifier(-30)


@State
def IceBoard():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        SetZVal(100)
        BlendMode_Add()
        AddY(110000)

        def upon_45():
            if not SLOT_51:
                CopyFromRightToLeft(23, 2, 83, 3, 2, 83)

        def upon_32():
            SLOT_51 = 1
            E0EAEffectPosition(3)
            XPositionRelativeFacing(0)
        ContinueState(50)
    sprite('vrjnef408_00', 2)
    CreateObject('IceMakePtc', 0)
    SetScaleY(0)
    SetScaleSpeedY(100)
    CommonSE('017_freeze_0')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_1')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_1')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_0')
    label(0)
    sprite('vrjnef408_00', 4)
    ParticleSize(2000)
    CallCustomizableParticle('jnef_iceshot', 0)
    SetScaleSpeedY(0)
    loopRest()
    gotoLabel(0)


@State
def IceBoard_koware():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(0)
        SetZVal(100)
        BlendMode_Add()
        AddY(110000)
    sprite('vrjnef408_00', 3)
    CreateObject('IceMakePtc', 0)
    ParticleSize(1500)
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef_icebrb', 0)
    physicsXImpulse(35000)
    XSpeed(-15000)
    AlphaValue(164)
    ConstantAlphaModifier(-20)
    Size(1000)
    SetScaleSpeed(-15)
    CommonSE('018_ice_break_0')
    sprite('vrjnef408_00', 3)
    CommonSE('018_ice_break_1')
    sprite('vrjnef408_00', 3)
    CommonSE('018_ice_break_0')
    sprite('vrjnef408_00', 3)
    sprite('vrjnef408_00', 3)
    CommonSE('018_ice_break_0')
    sprite('vrjnef408_00', 5)


@State
def ice_shot():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        Hitstop(8)
        CHGroundedHitstunAnimation(1)
        StarterRating(2)
        Unknown12052(1)

        def upon_32():
            FreezeCount(5)
            FreezeTime(30)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                PrivateFunction5(105)
                if SLOT_XDistanceFromCenterOfStage < SLOT_0:
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if SLOT_XDistanceFromCenterOfStage > SLOT_0:
                    DeleteObject(23)
        Size(750)
        CollideWithWall(1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 1)
        RunLoopUpon(17, 75)

        def upon_17():
            Unknown23090(23)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrjnef400_00', 1)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_01', 1)
    sprite('vrjnef400_02', 1)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_03', 1)
    sprite('vrjnef400_04', 1)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_05', 1)
    sprite('vrjnef400_06', 1)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_07', 1)
    sprite('vrjnef400_08', 1)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_1')
    SetAcceleration(2200)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    label(0)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    Damage(600)
    if SLOT_137:
        DamageMultiplier(80)
    ResetCHGroundedHitstunAnimation()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)
    EndMomentum(1)
    StartMultihit()
    ConstantAlphaModifier(-25)
    CommonSE('018_ice_break_1')
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef_icebr', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    clearUponHandler(54)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)


@State
def air_ice_shot():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        Hitstop(8)
        StarterRating(2)
        Unknown12052(1)

        def upon_32():
            FreezeCount(5)
            FreezeTime(30)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                PrivateFunction5(105)
                if SLOT_XDistanceFromCenterOfStage < SLOT_0:
                    DeleteObject(23)
            else:
                PrivateFunction5(105)
                if SLOT_XDistanceFromCenterOfStage > SLOT_0:
                    DeleteObject(23)
        Size(650)
        CollideWithWall(1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 1)
        RunLoopUpon(17, 75)

        def upon_17():
            Unknown23090(23)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrjnef400_00', 2)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_01', 2)
    sprite('vrjnef400_02', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_03', 2)
    CreateObject('IceMakePtc', 0)
    sprite('vrjnef400_04', 1)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_05', 2)
    sprite('vrjnef400_06', 1)
    CreateObject('IceMakePtc', 0)
    CommonSE('017_freeze_0')
    sprite('vrjnef400_07', 2)
    sprite('vrjnef400_08', 2)
    CommonSE('017_freeze_1')
    RotationSomething(0)
    physicsXImpulse(8000)
    SetAcceleration(900)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    label(0)
    sprite('vrjnef400_09', 3)
    CreateParticle('jnef_iceshot', 0)
    Damage(600)
    ResetCHGroundedHitstunAnimation()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)
    ConstantAlphaModifier(-25)
    EndAttack()
    CommonSE('018_ice_break_1')
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef_icebr', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    clearUponHandler(54)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)


@State
def ice_shot_ex2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        AirPushbackX(0)
        AirPushbackY(16000)
        FreezeCount(10)
        FreezeTime(36)
        PushbackX(6000)
        StarterRating(2)
        Unknown12052(1)
        HitsPerCall(3, 1, 1, 1, 1, 0, 3, 0)
        SetZVal(-100)
        SetActionMark(-2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)

        def upon_EVERY_FRAME():
            if not SLOT_2:
                clearUponHandler(OPPONENT_HIT_OR_BLOCK)
                clearUponHandler(EVERY_FRAME)
                ResetPushback()
                AirPushbackY(36000)
                ResetGravity()
                PushbackX(30400)
        WallCollisionDetection(1)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
        callSubroutine('CheckOverDriveSpecial')
        AddX(50000)
        AttackOff()
        uponSendToLabel(54, 9)
        RunLoopUpon(17, 180)

        def upon_17():
            Unknown23090(23)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrjnef400_50', 10)
    CreateObject('EffAtk8D_Env', -1)
    Size(450)
    SetScaleSpeed(50)
    AlphaValue(64)
    ConstantAlphaModifier(20)
    CreateObject('jnef_400ice_pt', -1)
    CreateObject('ModelMagicCircle3', -1)

    def RunOnObject_1():
        Size(1000)
    sprite('vrjnef400_50', 1)
    CreateObject('jnef_400_env', -1)
    Size(1000)
    SetScaleSpeed(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    label(0)
    sprite('vrjnef400_50col', 6)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrjnef400_50', 30)
    ConstantAlphaModifier(-12)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcS', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CommonSE('018_ice_break_1')
    TriggerUponForState('jnef_400_env', 32)
    TriggerUponForState('jnef_400ice_pt', 32)


@State
def air_ice_shot_ex2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(600)
        AttackP1(90)
        AirPushbackX(0)
        AirPushbackY(16000)
        FreezeCount(10)
        FreezeTime(36)
        PushbackX(6000)
        StarterRating(2)
        Unknown12052(1)
        HitsPerCall(3, 1, 1, 1, 1, 0, 3, 0)
        SetZVal(-100)
        SetActionMark(-2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)

        def upon_EVERY_FRAME():
            if not SLOT_2:
                clearUponHandler(OPPONENT_HIT_OR_BLOCK)
                clearUponHandler(EVERY_FRAME)
                ResetPushback()
                ResetGravity()
                PushbackX(30400)
        WallCollisionDetection(1)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
        callSubroutine('CheckOverDriveSpecial')
        AddX(120000)
        AddY(30000)
        AttackOff()
        uponSendToLabel(54, 9)
        RunLoopUpon(17, 180)

        def upon_17():
            Unknown23090(23)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrjnef400_50', 10)
    CreateObject('EffAtk8D_Env', -1)
    Size(450)
    SetScaleSpeed(50)
    AlphaValue(64)
    ConstantAlphaModifier(20)
    CreateObject('jnef_400ice_pt', -1)
    CreateObject('ModelMagicCircle3', -1)

    def RunOnObject_1():
        Size(1000)
    sprite('vrjnef400_50', 1)
    CreateObject('jnef_400_env', -1)
    Size(1000)
    SetScaleSpeed(0)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    label(0)
    sprite('vrjnef400_50col', 6)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrjnef400_50', 30)
    ConstantAlphaModifier(-12)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcS', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CommonSE('018_ice_break_1')
    TriggerUponForState('jnef_400_env', 32)
    TriggerUponForState('jnef_400ice_pt', 32)


@State
def jnef_400_env():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        AlphaValue(96)
    label(0)
    sprite('vrjnef400env', 15)
    CreateParticle('jnef_400bk', -1)
    gotoLabel(0)
    label(0)
    sprite('vrjnef400env', 32)
    ConstantAlphaModifier(-4)


@State
def jnef_400ice_pt():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        uponSendToLabel(32, 0)
    sprite('null', 5)
    Size(500)
    SetScaleSpeed(50)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_400icesmoke', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_400iceptc00', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_400iceptc', -1)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('null', 5)
    CommonSE('017_freeze_1')
    CommonSE('017_freeze_1')
    label(0)
    sprite('null', 10)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_400icesmoke', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_400iceptc00', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_400iceptc', -1)
    gotoLabel(0)
    label(0)
    sprite('null', 0)


@State
def UltimateSlashShotObj():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1600)
        AttackP1(80)
        AttackP2(72)
        SingleProration(1)
        GroundedHitstunAnimation(2)
        PushbackX(40000)
        Stagger(40)
        Crumple(30)
        CHGroundedHitstunAnimation(9)
        AirUntechableTime(28)
        AirPushbackX(30000)
        AirPushbackY(1000)
        Floorslide(20)
        Hitstop(0)
        UseSlashHitspark(1)
        HitsparkSize(600)
        HeatGainMultiplier(0)
        StarterRating(2)
        physicsXImpulse(50000)
        SetAcceleration(800)
        ContinueState(120)
        CollideWithWall(1)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(3)
        AfterimageCount(4)
        AfterimageSize_1(1000)
        AfterimageSize_2(500)
        BlendMode_Add()

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            AddActionMark(1)
            if SLOT_2 >= 5:
                EndAttack()
        if SLOT_137:
            DamageMultiplier(80)

        def upon_EVERY_FRAME():
            if SLOT_51:
                clearUponHandler(EVERY_FRAME)
                Damage(400)
                if SLOT_137:
                    DamageMultiplier(80)
    label(0)
    sprite('vrjnef430_00', 1)
    RefreshMultihit()
    AlphaValue(255)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_00', 1)
    sprite('vrjnef430_01', 1)
    RefreshMultihit()
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_01', 1)
    sprite('vrjnef430_02', 1)
    RefreshMultihit()
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_02', 1)
    loopRest()
    gotoLabel(0)


@State
def OverDriveSlashShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1600)
        AttackP1(80)
        AttackP2(72)
        SingleProration(1)
        GroundedHitstunAnimation(2)
        PushbackX(40000)
        Stagger(50)
        Crumple(40)
        CHGroundedHitstunAnimation(9)
        AirUntechableTime(28)
        AirPushbackX(30000)
        AirPushbackY(1000)
        Floorslide(20)
        Hitstop(0)
        FreezeCount(20)
        FreezeTime(100)
        UseSlashHitspark(1)
        HitsparkSize(600)
        HeatGainMultiplier(0)
        StarterRating(2)
        physicsXImpulse(50000)
        SetAcceleration(800)
        ContinueState(120)
        CollideWithWall(1)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(3)
        AfterimageCount(4)
        AfterimageSize_1(1000)
        AfterimageSize_2(500)
        BlendMode_Add()

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1

        def upon_45():
            if SLOT_2 >= 5:
                clearUponHandler(45)
                ObjectUpon(EVERY_FRAME, 41)
        SetActionMark(0)

        def upon_OPPONENT_HIT():
            ObjectUpon(EVERY_FRAME, 32)
            AddActionMark(1)
            if SLOT_2 >= 5:
                EndAttack()
        if SLOT_137:
            DamageMultiplier(80)

        def upon_EVERY_FRAME():
            if SLOT_51:
                clearUponHandler(EVERY_FRAME)
                Damage(400)
                if SLOT_137:
                    DamageMultiplier(80)
    label(0)
    sprite('vrjnef430_00', 1)
    RefreshMultihit()
    AlphaValue(255)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_00', 1)
    sprite('vrjnef430_01', 1)
    RefreshMultihit()
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_01', 1)
    sprite('vrjnef430_02', 1)
    RefreshMultihit()
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_02', 1)
    loopRest()
    gotoLabel(0)


@State
def IceBow():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnorePauses(2)
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1200)

        def upon_33():
            E0EAEffectPosition(0)
            AddX(50000)
            AddY(-100000)
            Rotation(80000)
    sprite('vrjnef431_00', 6)
    RotationAngle(-18000)
    AlphaValue(0)
    ConstantAlphaModifier(45)
    Size(1200)
    sprite('vrjnef431_00', 26)
    ConstantAlphaModifier(0)
    sprite('vrjnef431_01', 2)
    AlphaValue(255)
    sprite('vrjnef431_02', 2)
    sprite('vrjnef431_03', 10)
    PrivateSE('jnse_20')
    PrivateSE('jnse_20')
    AlphaValue(212)
    ConstantAlphaModifier(-10)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceCirclePtc', 2)
    CreateObject('IceCirclePtc', 3)
    CreateObject('IceCirclePtc', 4)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 6)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 6)
    CreateObject('IceBreakPtcM', 7)
    sprite('vrjnef431_03', 3)
    PrivateSE('jnse_20')
    PrivateSE('jnse_20')
    CreateObject('IceBreakPtcS', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 6)
    CreateObject('IceBreakPtcS', 7)
    sprite('vrjnef431_03', 20)


@State
def IceCircleA():

    def upon_IMMEDIATE():

        def upon_33():
            AddX(225000)
            AddY(-200000)
            Rotation(80000)
    PaletteIndex(1)
    sprite('vrjnef431b_00', 9)
    Size(1000)
    SetScaleSpeed(200)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrjnef431b_00', 12)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(10)


@State
def IceCircleB():

    def upon_IMMEDIATE():

        def upon_33():
            AddX(250000)
            AddY(-225000)
            Rotation(80000)
    PaletteIndex(1)
    sprite('vrjnef431b_00', 9)
    Size(700)
    SetScaleSpeed(100)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrjnef431b_00', 20)
    ConstantAlphaModifier(-12)
    SetScaleSpeed(20)


@State
def IceCircleC():

    def upon_IMMEDIATE():

        def upon_33():
            AddX(275000)
            AddY(-250000)
            Rotation(80000)
    PaletteIndex(1)
    sprite('vrjnef431b_00', 9)
    Size(250)
    SetScaleSpeed(100)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrjnef431b_00', 30)
    ConstantAlphaModifier(-8)
    SetScaleSpeed(15)


@State
def IceArrow():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        EnemyHitstopAddition(0, 30, 30)
        FreezeCount(20)
        FreezeTime(45)
        ReduceHitEffects(1)
        UseFreezeHitspark(1)
        OppMovementUnlock(1)
        HeatGainMultiplier(0)
        StarterRating(2)
        MinimumDamage(15)
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        CollideWithWall(1)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        BlendMode_Add()
        AlphaValue(0)
        ConstantAlphaModifier(40)
        Size(0)
        SetScaleSpeed(100)
        XSpeed(-50)
        YSpeed(-50)
        SetActionMark(1)

        def upon_32():
            SetActionMark(12)
            AirPushbackX(55000)
            HitAirUnblockable(3)
            SLOT_51 = 1
            RotationAngle(-28000)
            HitboxMovement(120000, 28000)
            PushSpeedX()
            PushSpeedY()
            physicsXImpulse(0)
            physicsYImpulse(0)

        def upon_33():
            SetActionMark(12)
            YImpulseBeforeWallbounce(3000)
            AddY(200000)
            RotationAngle(50000)
            HitboxMovement(120000, -50000)
            PushSpeedX()
            PushSpeedY()
            physicsXImpulse(0)
            physicsYImpulse(0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            sendToLabel(3)

        def upon_EVERY_FRAME():
            if not SLOT_2:
                clearUponHandler(EVERY_FRAME)
                clearUponHandler(OPPONENT_HIT)
                sendToLabel(101)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrjnef431atk_00', 10)
    StartMultihit()
    SetBackground(1)
    sprite('vrjnef431atk_00', 24)
    StartMultihit()
    SetScaleSpeed(0)
    sprite('vrjnef431atk_00', 3)
    IgnorePauses(0)
    PopSpeedX()
    PopSpeedY()
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    loopRest()
    gotoLabel(55)
    label(3)
    sprite('vrjnef431atk_00', 1)
    if SLOT_51:

        def RunOnObject_25():
            TeleportToObject(24)
            AddX(-200000)
            AddY(-100000)
    else:

        def RunOnObject_25():
            TeleportToObject(24)
            AddX(-200000)
            AddY(-300000)
    ObjectUpon(EVERY_FRAME, 32)

    def upon_OPPONENT_HIT():
        XImpulseAcceleration(106)
        YAccel(106)
        CommonSE('017_freeze_1')
    Damage(200)
    if SLOT_137:
        DamageMultiplier(80)
    DamageEffect(4, 'ef_gird_damage')
    FreezeCountReset()
    PushSpeedX()
    PushSpeedY()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrjnef431atk_00', 19)
    if SLOT_51:
        TeleportToObject(22)
        AddY(100000)
        AddX(-200000)
    else:
        TeleportToObject(22)
        AddY(300000)
        AddX(-200000)
    sprite('vrjnef431atk_01', 3)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(1)
    YAccel(1)
    RefreshMultihit()
    ScreenShake(10000, 0)
    SetScaleSpeed(5)
    ParticleSize(1500)
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef431_icebr', 1)
    CallCustomizableParticle('jnef431_icebr', 1)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 4)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 4)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcS', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    sprite('vrjnef431atk_02', 3)
    RefreshMultihit()
    XImpulseAcceleration(106)
    YAccel(106)
    CommonSE('017_freeze_1')
    label(100)
    sprite('vrjnef431atk_03', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(0, 5000)
    sprite('vrjnef431atk_04', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(2500, 2500)
    sprite('vrjnef431atk_05', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(5000, 0)
    sprite('vrjnef431atk_04', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('vrjnef431atk_02', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    RefreshMultihit()
    Damage(1100)
    if SLOT_137:
        DamageMultiplier(80)
    EnemyHitstopAddition(0, 2, 5)
    if SLOT_51:
        YImpulseBeforeWallbounce(10)
        AirHitstunAnimation(12)
        WallbounceReboundTime(-1)
    else:
        pass
    XImpulseAcceleration(106)
    YAccel(106)
    CommonSE('017_freeze_1')
    CreateParticle('ef_hitlz', -1)
    sprite('vrjnef431atk_02', 30)
    ScreenShake(30000, 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(150)
    YAccel(150)
    CreateParticle('ef_hitlz', -1)
    CommonSE('017_freeze_1')
    sprite('vrjnef431atk_02', 30)
    loopRest()
    label(55)
    sprite('vrjnef431atk_02', 3)


@State
def IceArrow_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        AttackP2(82)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(80)
        Hitstop(0)
        EnemyHitstopAddition(0, 30, 30)
        FreezeCount(20)
        FreezeTime(45)
        ReduceHitEffects(1)
        UseFreezeHitspark(1)
        OppMovementUnlock(1)
        HeatGainMultiplier(0)
        AttackType(4)
        StarterRating(2)
        MinimumDamage(15)
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        CollideWithWall(1)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        BlendMode_Add()
        AlphaValue(0)
        ConstantAlphaModifier(40)
        Size(0)
        SetScaleSpeed(100)
        XSpeed(-50)
        YSpeed(-50)
        SetActionMark(1)

        def upon_32():
            SetActionMark(18)
            AirPushbackX(55000)
            HitAirUnblockable(3)
            SLOT_51 = 1
            RotationAngle(-28000)
            HitboxMovement(120000, 28000)
            PushSpeedX()
            PushSpeedY()
            physicsXImpulse(0)
            physicsYImpulse(0)

        def upon_33():
            SetActionMark(18)
            YImpulseBeforeWallbounce(3000)
            AddY(200000)
            RotationAngle(50000)
            HitboxMovement(120000, -50000)
            PushSpeedX()
            PushSpeedY()
            physicsXImpulse(0)
            physicsYImpulse(0)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            CreateObject('EffAtk8D', 0)
            sendToLabel(3)

        def upon_EVERY_FRAME():
            if not SLOT_2:
                clearUponHandler(EVERY_FRAME)
                clearUponHandler(OPPONENT_HIT)
                sendToLabel(101)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrjnef431atk_00', 10)
    StartMultihit()
    SetBackground(1)
    sprite('vrjnef431atk_00', 24)
    StartMultihit()
    SetScaleSpeed(0)
    sprite('vrjnef431atk_00', 3)
    IgnorePauses(0)
    PopSpeedX()
    PopSpeedY()
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    sprite('vrjnef431atk_00', 3)
    CreateParticle('jnef431_iceshot', -1)
    loopRest()
    gotoLabel(55)
    label(3)
    sprite('vrjnef431atk_00', 1)
    if SLOT_51:

        def RunOnObject_25():
            TeleportToObject(24)
            AddX(-200000)
            AddY(-100000)
    else:

        def RunOnObject_25():
            TeleportToObject(24)
            AddX(-200000)
            AddY(-300000)
    ObjectUpon(EVERY_FRAME, 32)

    def upon_OPPONENT_HIT():
        XImpulseAcceleration(106)
        YAccel(106)
        CommonSE('017_freeze_1')
    Damage(200)
    if SLOT_137:
        DamageMultiplier(80)
    DamageEffect(4, 'ef_gird_damage')
    FreezeCountReset()
    PushSpeedX()
    PushSpeedY()
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrjnef431atk_00', 19)
    if SLOT_51:
        TeleportToObject(22)
        AddY(100000)
        AddX(-200000)
    else:
        TeleportToObject(22)
        AddY(300000)
        AddX(-200000)
    sprite('vrjnef431atk_01', 3)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(1)
    YAccel(1)
    RefreshMultihit()
    ScreenShake(10000, 0)
    SetScaleSpeed(5)
    ParticleSize(1500)
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef431_icebr', 1)
    CallCustomizableParticle('jnef431_icebr', 1)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 4)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 4)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcS', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    sprite('vrjnef431atk_02', 3)
    RefreshMultihit()
    XImpulseAcceleration(106)
    YAccel(106)
    CommonSE('017_freeze_1')
    label(100)
    sprite('vrjnef431atk_03', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(0, 5000)
    sprite('vrjnef431atk_04', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(2500, 2500)
    sprite('vrjnef431atk_05', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(5000, 0)
    sprite('vrjnef431atk_04', 2)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(100)
    label(101)
    sprite('vrjnef431atk_02', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)
    RefreshMultihit()
    Damage(1100)
    if SLOT_137:
        DamageMultiplier(80)
    EnemyHitstopAddition(0, 2, 5)
    if SLOT_51:
        YImpulseBeforeWallbounce(10)
        AirHitstunAnimation(12)
        WallbounceReboundTime(-1)
    else:
        pass
    XImpulseAcceleration(106)
    YAccel(106)
    CommonSE('017_freeze_1')
    CreateParticle('ef_hitlz', -1)
    sprite('vrjnef431atk_02', 30)
    ScreenShake(30000, 0)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(150)
    YAccel(150)
    CreateParticle('ef_hitlz', -1)
    CommonSE('017_freeze_1')
    sprite('vrjnef431atk_02', 30)
    loopRest()
    label(55)
    sprite('vrjnef431atk_02', 3)


@State
def Yukikazedmy():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        AttackLevel_(4)
        Damage(3500)
        PushbackX(8000)
        AttackP2(60)
        Crumple(9999)
        Stagger(30)
        CHStagger(30)
        UseSlashHitspark(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        IgnoreComboTime(1)
        AttackDirection(3)
        DamageEffect(4, 'ef_non')
        FatalCounter(1)
        UseFreezeHitspark(1)
        CHStateIfCHStart(3)
        TeleportToObject(22)
    sprite('vrdmy_yukikaze', 1)
    CommonSE('018_ice_break_1')
    CreateObject('JNFreezeDamageBreakParts', -1)
    CreateObject('JNFreezeDamageBreakParts', -1)
    StartMultihit()
    sprite('vrdmy_yukikaze', 3)


@State
def YukikazedmyOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        AttackLevel_(4)
        Damage(3500)
        PushbackX(8000)
        Crumple(9999)
        Stagger(30)
        CHStagger(30)
        UseSlashHitspark(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        IgnoreComboTime(1)
        AttackDirection(3)
        DamageEffect(4, 'ef_non')
        FatalCounter(1)
        UseFreezeHitspark(1)
        CHStateIfCHStart(3)
        TeleportToObject(22)
        AttackType(4)
    sprite('vrdmy_yukikaze', 1)
    CommonSE('018_ice_break_1')
    CreateObject('JNFreezeDamageBreakParts', -1)
    CreateObject('JNFreezeDamageBreakParts', -1)
    StartMultihit()
    sprite('vrdmy_yukikaze', 3)


@State
def JNFreezeDamageBreakParts():

    def upon_IMMEDIATE():
        Visibility(1)
        PaletteIndex(1)
        AbsoluteY(256000)
    sprite('null', 200)
    ParticleColorFromPalette(175, 111, 111)
    CallPrivateEffect('jnef_freezebreak')


@State
def jnef600_envStart():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    sprite('vrjnef600env', 20)
    BlendMode_Add()
    Size(1000)
    AlphaValue(0)
    ConstantAlphaModifier(6)
    sprite('vrjnef600env', 2)
    AlphaValue(0)


@State
def jnef600_envLoop():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    sprite('vrjnef600env', 20)
    BlendMode_Add()
    AlphaValue(120)
    ConstantAlphaModifier(2)
    sprite('vrjnef600env', 20)
    ConstantAlphaModifier(-2)


@State
def jnef600_envEnd():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    sprite('vrjnef600env', 10)
    BlendMode_Add()
    Size(1000)
    SetScaleSpeed(-5)
    AlphaValue(120)
    ConstantAlphaModifier(-20)


@State
def jnef600iceSword():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        SetZVal(500)
        Size(1000)
        AlphaValue(255)
    sprite('vrjnef600_00', 3)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('jnef600_envStart', -1)
    CommonSE('017_freeze_0')
    sprite('vrjnef600_01', 3)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef600_02', 3)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    CommonSE('017_freeze_0')
    sprite('vrjnef600_03', 3)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    CommonSE('017_freeze_0')
    sprite('vrjnef600_04', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    CommonSE('017_freeze_0')
    sprite('vrjnef600_04ex01', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    CommonSE('017_freeze_0')
    sprite('vrjnef600_04ex02', 4)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    CommonSE('017_freeze_1')
    label(0)
    sprite('vrjnef600_04ex03', 20)
    CreateObject('jnef600_envLoop', -1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('vrjnef600_04ex03', 20)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrjnef600_05', 3)
    CreateObject('jnef600_envEnd', -1)
    sprite('vrjnef600_06', 3)
    AlphaValue(200)
    ConstantAlphaModifier(-5)
    sprite('vrjnef600_07', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceCirclePtc', 2)
    CreateObject('IceBreakPtcM', 0)
    CreateObject('IceBreakPtcM', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 6)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcM', 9)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 6)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    CommonSE('018_ice_break_1')
    sprite('vrjnef600_08', 3)


@State
def jnef601env():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        SetZVal(-500)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('vrjnef601env', 4)
    BlendMode_Add()
    Size(700)
    SetScaleSpeed(25)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrjnef601env', 20)
    SetScaleSpeed(5)
    ConstantAlphaModifier(-5)


@State
def jnef601makeSword():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        SetZVal(-100)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vrjnef601_00', 20)
    ConstantAlphaModifier(10)
    CreateObject('jnef601ptc', -1)
    CreateObject('jnef601env', -1)
    CreateObject('jnef601Sword', -1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    sprite('vrjnef601_01', 1)
    CreateObject('IceBreakPtc601', 0)
    CreateObject('IceBreakPtc601', 1)
    CreateObject('IceBreakPtc601', 2)
    CreateObject('IceBreakPtcS', 0)
    CreateObject('IceBreakPtcS', 1)
    CreateObject('IceBreakPtcS', 2)
    sprite('vrjnef601_02', 10)
    AlphaValue(200)
    ConstantAlphaModifier(-20)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    label(0)
    PaletteIndex(0)
    sprite('vrjnef601_03', 1)
    AlphaValue(255)
    BlendMode_Normal()
    loopRest()
    gotoLabel(0)
    label(1)
    PaletteIndex(0)
    sprite('vrjnef601_03', 6)


@State
def jnef601Sword():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        AlphaValue(0)
    sprite('vrjnef601_03', 20)
    ConstantAlphaModifier(15)
    sprite('vrjnef601_03', 4)
    AlphaValue(255)


@State
def jnef611icewing():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        EnableAfterimage(1)
        AfterimageCount(10)
        AfterimageMask_1(0, 0, 0, 0)
        AfterimageMask_2(0, 128, 128, 128)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        BlendMode_Add()
    sprite('jnef611_00', 4)
    SetZVal(-100)
    AddX(-60000)
    AddY(60000)
    RotationAngle(-50000)
    AddRotationPerFrame(500)
    physicsXImpulse(-1000)
    physicsYImpulse(500)
    Size(500)
    SetScaleXPerFrame(5)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    sprite('jnef611_00', 6)
    Size(700)
    sprite('jnef611_01', 6)
    SetScaleX(800)
    SetScaleY(800)
    sprite('jnef611_02', 6)
    CreateObject('IceMakePtc', 4)
    CreateParticle('jnef_iceptc', 5)
    CreateParticle('jnef_iceptc', 6)
    CreateObject('jnef611_hane', 0)
    CreateObject('jnef611_hane', 1)
    CreateObject('jnef611_hane', 2)
    AlphaValue(255)
    sprite('jnef611_03', 6)
    CreateObject('IceMakePtc', 0)
    CreateParticle('jnef_iceptc', 1)
    CreateParticle('jnef_iceptc', 2)
    CreateObject('jnef611_hane', 4)
    CreateObject('jnef611_hane', 5)
    sprite('jnef611_04', 6)
    CreateObject('IceMakePtc', 0)
    CreateParticle('jnef_iceptc', 1)
    CreateParticle('jnef_iceptc', 2)
    CreateObject('jnef611_hane', 0)
    sprite('jnef611_05', 6)
    CreateObject('IceMakePtc', 0)
    CreateParticle('jnef_iceptc', 1)
    CreateParticle('jnef_iceptc', 2)
    CreateObject('jnef611_hane', 2)
    sprite('jnef611_06', 4)
    CreateObject('IceMakePtc', 0)
    CreateParticle('jnef_iceptc', 1)
    CreateParticle('jnef_iceptc', 2)
    SetScaleXPerFrame(1)
    physicsXImpulse(200)
    physicsYImpulse(-400)
    sprite('jnef611_07', 4)
    AlphaValue(128)
    ConstantAlphaModifier(-5)
    sprite('jnef611_08', 6)
    CreateParticle('jnef_iceptc', 1)
    CreateParticle('jnef_iceptc', 2)
    sprite('jnef611_09', 24)
    sprite('null', 32)


@State
def cmp():
    sprite('vrtest00', 10)
    SetCompositeImage(0, 'vrtest88')
    SetCompositeSpeedX(0, 100)
    SetCompositeSpeedY(0, 200)
    Size(2000)
    label(0)
    sprite('vrtest00ex01', 10)
    SetCompositeImage(0, 'vrtest89')
    sprite('vrtest00', 10)
    sprite('vrtest01', 10)
    sprite('vrtest02', 10)
    sprite('vrtest03', 10)
    loopRest()
    gotoLabel(0)


@State
def ef_jnah_A():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_jnah_A.DIG', '')
        AlphaValue(160)
        SetScaleX(800)
        SetScaleY(1100)
        SetScaleSpeed(1)
    sprite('null', 255)
    PrivateSE('jnse_01')
    CommonSE('017_freeze_0')
    sprite('null', 30)
    CommonSE('018_ice_break_0')
    CommonSE('018_ice_break_1')
    ConstantAlphaModifier(-10)


@State
def ef_jnah_B():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_jnah_B.DIG', '')
        AbsoluteY(-30000)
        AlphaValue(128)
        Size(1000)
        SetScaleSpeed(1)
    sprite('null', 10)
    PrivateSE('jnse_01')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    sprite('null', 10)
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    sprite('null', 10)
    sprite('null', 10)
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('018_ice_break_0')
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('018_ice_break_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('018_ice_break_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_0')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('018_ice_break_0')
    CommonSE('018_ice_break_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    sprite('null', 10)
    CommonSE('018_ice_break_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('018_ice_break_0')
    CommonSE('017_freeze_0')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('017_freeze_1')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 5)
    sprite('null', 60)
    ConstantAlphaModifier(-10)


@State
def LookAtMe():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(0)
    sprite('null', 32767)
    loopRest()


@State
def AstralStartPtc():

    def upon_IMMEDIATE():
        LinkParticle('jnef_ast_start_snow')
        CancelIfPlayerHit(3)
        Flip()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(0)
    sprite('null', 32767)


@State
def AstralFinishPtc():

    def upon_IMMEDIATE():
        LinkParticle('jnef_ast_finish')
        Flip()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(0)
    sprite('null', 32767)
    CreateParticle('jnef_ast_snowfloor', -1)


@State
def JNEF_ast_attack():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    sprite('null', 300)
    LinkParticle('jnef_ast_attack')


@State
def EventEffSpKensei():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(7)
        BlendMode_Normal()

        def upon_PLAYER_DAMAGED():
            EndObject()
        Size(1100)
        AddX(720000)
        AddY(210000)
        Flip()
    sprite('vrhzef407_00', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef407_01', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    sprite('vrhzef407_02', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_Aura', 10)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    CreateObject('HZEF_AuraDelete', 10)
    sprite('vrhzef407_03', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_Aura', 10)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    CreateObject('HZEF_AuraDelete', 10)
    sprite('vrhzef407_04', 18)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_Aura', 10)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    CreateObject('HZEF_AuraDelete', 10)
    sprite('vrhzef407_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef407_06', 4)


@State
def HZEF_Aura():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        LinkParticle('hzef_envaura')
        BlendMode_Add()
        Size(800)
    sprite('null', 20)
    ConstantAlphaModifier(-15)


@State
def HZEF_AuraDelete():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        ParticleLayer(2)
        CallPrivateEffect('hzef_deleteaura')
        Size(600)
    sprite('null', 60)


@State
def RushAssaultFinishAtkObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        AttackLevel_(5)
        Damage(800)
        AttackP2(74)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(40000)
        YImpulseBeforeWallbounce(1600)
        PushbackX(-24000)
        Hitstop(0)
        UseSlashHitspark(1)
        AttackDirection(3)
        DamageEffect(4, 'ef_non')
        CHStateIfCHStart(3)
        Unknown12052(1)
        TeleportToObject(22)
        callSubroutine('CheckOverDriveSpecial')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            CommonSE('018_ice_break_1')
            CreateObject('JNFreezeDamageBreakParts', -1)
            CreateObject('JNFreezeDamageBreakParts', -1)
    sprite('vrdmy_yukikaze', 3)


@State
def UltimateShotOverDrive():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(400)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(100)
        AirPushbackY(20000)
        Hitstop(6)
        UseSlashHitspark(1)
        FreezeCount(100)
        FreezeTime(120)
        MoveAttributes(0, 0, 0, 1, 0)
        AttackDirection(2)
        DefeatOpponentBehavior(1)
        CHStateIfCHStart(3)
        VoodooDamageMultiplier(3)
        WallCollisionDetection(1)
        BlendMode_Add()
        TeleportToObject(22)
        AbsoluteY(0)
        Flip()

        def upon_32():
            Size(750)
            AddX(120000)

        def upon_33():
            Size(1000)
            AddX(-180000)
            Flip()
            AirPushbackX(-5500)
            AirPushbackY(-2000)
            PushbackX(-30400)

        def upon_34():
            Size(1100)
            AddX(60000)
            AirPushbackY(10000)

        def upon_OPPONENT_HIT():
            ObjectUpon(EVERY_FRAME, 32)

        def upon_PLAYER_DAMAGED():
            SLOT_51 = 1
        uponSendToLabel(41, 0)
    sprite('vrjnef233atk_00', 3)
    SetScaleSpeed(-5)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef233atk_01', 3)
    SetScaleSpeed(-5)
    CreateObject('Icicle_Env', -1)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateObject('IceMakePtc', 3)
    CreateObject('IceMakePtc', 4)
    CommonSE('017_freeze_0')
    sprite('vrjnef233atk_02ex01', 3)
    SetScaleSpeed(0)
    CommonSE('017_freeze_0')
    loopRest()
    if SLOT_51:
        conditionalSendToLabel(0)
    sprite('vrjnef233atk_02', 3)
    ScreenShake(30000, 30000)
    SetScaleSpeed(5)
    CommonSE('017_freeze_1')
    sprite('vrjnef233atk_02', 90)
    StartMultihit()
    SetScaleSpeed(0)
    loopRest()
    label(0)
    clearUponHandler(PLAYER_DAMAGED)
    sprite('vrjnef233atk_03', 3)
    SetScaleSpeed(0)
    AlphaValue(200)
    ConstantAlphaModifier(-15)
    sprite('vrjnef233atk_04', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceCirclePtc', 2)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcL', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceBreakPtcM', 6)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 6)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    CommonSE('018_ice_break_1')
    sprite('vrjnef233atk_05', 10)


@State
def OverDriveSlashShotFinish():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        AttackLevel_(4)
        Damage(1200)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(100)
        AttackType(4)
        PushbackX(8000)
        Crumple(9999)
        Stagger(30)
        HardKnockdown(15)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        AttackDirection(3)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        DamageEffect(4, 'ef_non')
        TeleportToObject(22)
    sprite('vrdmy_yukikaze', 1)
    CommonSE('018_ice_break_1')
    CreateObject('JNFreezeDamageBreakParts', -1)
    CreateObject('JNFreezeDamageBreakParts', -1)
    StartMultihit()
    sprite('vrdmy_yukikaze', 3)


@State
def BurstDD_Sword():

    def upon_IMMEDIATE():
        physicsYImpulse(36000)
        setGravity(1500)
    label(0)
    sprite('jn330_15z', 2)
    CommonSE('011_spin_1')
    sprite('jn330_16z', 2)
    CommonSE('011_spin_1')
    sprite('jn330_17z', 2)
    CommonSE('011_spin_1')
    sprite('jn330_18z', 2)
    CommonSE('011_spin_1')
    loopRest()
    gotoLabel(0)


@State
def BurstDD_IceNew():

    def upon_IMMEDIATE():
        Size(3200)
        PaletteIndex(1)
        ColorFromPaletteIndex(95)
        Eff3DEffect('jnef_430_ice', '')
        LinkParticle('jnef_440_root')
        BlendMode_Add()
        EffectPosition(22, 104)
        uponSendToLabel(32, 0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    SetScaleSpeed(75)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(15)
    CreateParticle('jnef_440_break', -1)


@State
def BurstDD_Slash():

    def upon_IMMEDIATE():
        LinkParticle('jnef_DD')
        RotationAngle(90000)
        EffectPosition(22, 104)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 41)
    ScreenShake(20000, 20000)


@State
def BurstDD_SlashEX():

    def upon_IMMEDIATE():
        SetScaleX(2500)
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(95)
        Eff3DEffect('jnef_430_slash', '')
        EffectPosition(22, 104)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    SetScaleXPerFrame(-45)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    CreateObject('BurstDD_Slash', -1)

    def RunOnObject_1():
        AddScale(500)


@State
def BurstDD_Ice():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleY(2800)
        SetScaleX(2000)
        EffectPosition(22, 104)
        uponSendToLabel(32, 0)
    sprite('vrjnef311_00', 2)
    CreateDecal(1, 'FLORE_FROST', -1, 2000, 2000)
    AlphaValue(192)
    CommonSE('017_freeze_0')
    sprite('vrjnef311_01', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef311_02', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef311_03', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef311_04', 2)
    CommonSE('017_freeze_1')
    sprite('vrjnef311_05', 32767)
    loopRest()
    label(0)
    sprite('vrjnef311_06', 3)
    sprite('vrjnef311_07', 3)
    CreateObject('IceCirclePtc', 0)
    CreateObject('IceCirclePtc', 1)
    CreateObject('IceBreakPtcL', 0)
    CreateObject('IceBreakPtcL', 1)
    CreateObject('IceBreakPtcM', 2)
    CreateObject('IceBreakPtcM', 3)
    CreateObject('IceBreakPtcM', 4)
    CreateObject('IceBreakPtcM', 5)
    CreateObject('IceCirclePtc', 6)
    CreateObject('IceBreakPtcL', 6)
    CreateObject('IceBreakPtcM', 7)
    CreateObject('IceBreakPtcM', 8)
    CreateObject('IceBreakPtcM', 9)
    CreateObject('IceBreakPtcM', 10)
    CreateObject('IceBreakPtcS', 2)
    CreateObject('IceBreakPtcS', 3)
    CreateObject('IceBreakPtcS', 4)
    CreateObject('IceBreakPtcS', 5)
    CreateObject('IceBreakPtcS', 7)
    CreateObject('IceBreakPtcS', 8)
    CreateObject('IceBreakPtcS', 9)
    CreateObject('IceBreakPtcS', 10)
    CommonSE('018_ice_break_1')
    CommonSE('018_ice_break_1')
    sprite('vrjnef311_08', 12)
    ConstantAlphaModifier(-30)


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        AddX(175000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
    sprite('null', 32767)
    label(0)
    sprite('null', 2)
    CameraPosition(1100)
    sprite('null', 2)
    CameraPosition(1200)
    sprite('null', 2)
    CameraPosition(1400)
    sprite('null', 2)
    CameraPosition(1600)
    sprite('null', 32767)
    CameraPosition(1800)
    label(1)
    sprite('null', 2)
    CameraPosition(1700)
    physicsYImpulse(5000)
    sprite('null', 2)
    CameraPosition(1600)
    sprite('null', 2)
    CameraPosition(1500)
    sprite('null', 2)
    CameraPosition(1400)
    sprite('null', 2)
    CameraPosition(1300)
    sprite('null', 2)
    CameraPosition(1200)
    sprite('null', 2)
    CameraPosition(1100)
    sprite('null', 32767)
    CameraPosition(1000)
    physicsYImpulse(0)
    label(2)
    sprite('null', 32767)
    CameraControlEnable(0)


@State
def ptPhantom():

    def upon_IMMEDIATE():
        PaletteIndex(6)
        AlphaValue(0)
        BlendMode_Normal()
        AddY(70000)
        uponSendToLabel(32, 1)
    sprite('pt999_00', 22)
    CommonSE('302_spsys_rapid')
    ConstantAlphaModifier(10)
    sprite('pt999_00', 6)
    ConstantAlphaModifier(0)
    CharacterFlash(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)
    physicsYImpulse(100)
    sprite('pt999_00', 50)
    sprite('pt999_00', 20)
    physicsYImpulse(0)
    sprite('pt999_00', 100)
    physicsYImpulse(-100)
    sprite('pt999_00', 10)
    physicsYImpulse(0)
    gotoLabel(0)
    label(1)
    sprite('pt999_00', 6)
    EndMomentum(1)
    ConstantAlphaModifier(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)


@State
def EventTBHitEff():
    sprite('null', 5)
    ParticleRandomRotation()
    CallCustomizableParticle('ef_hitlz', 108)
    CommonSE('101_hit_slash_3')


@State
def EventShakeObj():
    sprite('null', 40)
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    sprite('null', 8)
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    label(0)
    sprite('null', 8)
    ScreenShake(0, 5000)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    loopRest()
    gotoLabel(0)


@State
def EventIceMakePtc():
    sprite('null', 1)
    XPositionRelativeFacing(0)
    AbsoluteY(80000)
    DeviationX(-50000, 50000)
    DeviationY(-50000, 50000)
    PaletteIndex(1)
    Visibility(1)
    CreateParticle('jnef_icesmoke00', -1)
    ParticleColorFromPalette(175, 96, 48)
    CallCustomizableParticle('jnef_iceptc00', -1)
    ParticleColorFromPalette(175, 96, 48)
    ParticleSize(2000)
    CallCustomizableParticle('jnef_iceptc', -1)
    ParticleSize(2000)


@State
def Event_UltimateSlashShotObj():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        AttackDefaults_SuperProjectile()
        physicsXImpulse(50000)
        SetAcceleration(800)
        ContinueState(120)
        CollideWithWall(1)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(3)
        AfterimageCount(4)
        AfterimageSize_1(1000)
        AfterimageSize_2(500)
        BlendMode_Add()
        NoAttackDuringAction(1)
    label(0)
    sprite('vrjnef430_00', 1)
    AlphaValue(255)
    CreateObject('IceMakePtc', 0)
    CreateObject('IceMakePtc', 1)
    CreateObject('IceMakePtc', 2)
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_00', 1)
    sprite('vrjnef430_01', 1)
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_01', 1)
    sprite('vrjnef430_02', 1)
    CreateDecal(1, 'FLORE_FROST', -1, 900, 900)
    PrivateSE('jnse_01')
    sprite('vrjnef430_02', 1)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_ptPhantom_Renew():

    def upon_IMMEDIATE():
        PaletteIndex(6)
        AlphaValue(0)
        BlendMode_Normal()
        AddX(-50000)
        AddY(70000)
        SetZVal(-500)
        uponSendToLabel(32, 9)
    sprite('pt999_00', 45)
    CommonSE('302_spsys_rapid')
    ConstantAlphaModifier(5)
    CreateParticle('ef_tekitou_b', 0)
    sprite('pt999_00', 6)
    ConstantAlphaModifier(0)
    CharacterFlash(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)
    physicsYImpulse(100)
    sprite('pt999_00', 50)
    sprite('pt999_00', 20)
    physicsYImpulse(0)
    sprite('pt999_00', 100)
    physicsYImpulse(-100)
    sprite('pt999_00', 10)
    physicsYImpulse(0)
    gotoLabel(0)
    label(9)
    sprite('pt999_00', 6)
    EndMomentum(1)
    ConstantAlphaModifier(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)


@State
def ptPhantom_NoSound():

    def upon_IMMEDIATE():
        PaletteIndex(6)
        AlphaValue(0)
        BlendMode_Normal()
        AddY(70000)
        uponSendToLabel(32, 1)
    sprite('pt999_00', 22)
    ConstantAlphaModifier(10)
    sprite('pt999_00', 6)
    ConstantAlphaModifier(0)
    CharacterFlash(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)
    physicsYImpulse(100)
    sprite('pt999_00', 50)
    sprite('pt999_00', 20)
    physicsYImpulse(0)
    sprite('pt999_00', 100)
    physicsYImpulse(-100)
    sprite('pt999_00', 10)
    physicsYImpulse(0)
    gotoLabel(0)
    label(1)
    sprite('pt999_00', 6)
    EndMomentum(1)
    ConstantAlphaModifier(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)


@State
def Act3Event_IceBoard():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(3)
        SetZVal(100)
        BlendMode_Add()
        AddY(160000)

        def upon_45():
            if not SLOT_51:
                CopyFromRightToLeft(23, 2, 83, 3, 2, 83)

        def upon_32():
            SLOT_51 = 1
            E0EAEffectPosition(3)
            XPositionRelativeFacing(0)
        ContinueState(50)
    sprite('vrjnef408_00', 2)
    CreateObject('IceMakePtc', 0)
    SetScaleY(0)
    SetScaleSpeedY(100)
    CommonSE('017_freeze_0')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_1')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_0')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_1')
    sprite('vrjnef408_00', 2)
    CommonSE('017_freeze_0')
    label(0)
    sprite('vrjnef408_00', 4)
    ParticleSize(2000)
    CallCustomizableParticle('jnef_iceshot', 0)
    SetScaleSpeedY(0)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_IceBoard_koware():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(0)
        SetZVal(100)
        BlendMode_Add()
        AddY(160000)
    sprite('vrjnef408_00', 3)
    CreateObject('IceMakePtc', 0)
    ParticleSize(1500)
    ParticleColorFromPalette(111, 111, 111)
    CallCustomizableParticle('jnef_icebrb', 0)
    physicsXImpulse(35000)
    XSpeed(-15000)
    AlphaValue(164)
    ConstantAlphaModifier(-20)
    Size(1000)
    SetScaleSpeed(-15)
    CommonSE('018_ice_break_0')
    sprite('vrjnef408_00', 3)
    CommonSE('018_ice_break_1')
    sprite('vrjnef408_00', 3)
    CommonSE('018_ice_break_0')
    sprite('vrjnef408_00', 3)
    sprite('vrjnef408_00', 3)
    CommonSE('018_ice_break_0')
    sprite('vrjnef408_00', 5)


@State
def Act3Event_Offset():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(200000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)
