@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_TB.DIG', 'ef_emb_TB_motion_000.mmot')
        RenderLayer(5)
        Visibility(1)
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
def EMB_TB_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_TB.DIG', 'ef_emb_TB_motion_000.mmot')
        RenderLayer(5)
        Visibility(1)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 20)


@State
def EMB_TB_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AbsoluteY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_TB.DIG', 'ef_emb_TB_motion_000.mmot')
        RenderLayer(5)
        Visibility(1)
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
def Install():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_wind.DIG', 'tbef_wind_motion_000.mmot')
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        ColorForTransition(16763135)
        BlendMode_Add()
        Size(300)
        AddX(16000)
        AlphaValue(255)
        uponSendToLabel(56, 1)
        uponSendToLabel(32, 1)
    sprite('null', 10)
    ConstantAlphaModifier(20)
    SetScaleSpeed(20)
    loopRest()
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(1)
    sprite('null', 5)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(200)
    ConstantAlphaModifier(-50)


@State
def InstallMagicCircle():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_magiccircle00.DIG', 'tbef_magiccircle00_motion_000.m'
            )
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        RenderLayer(2)
        BlendMode_Add()
        Size(250)
        AddX(20000)
        AddY(20000)
        AlphaValue(160)
        RotationAngle(0)
        uponSendToLabel(56, 1)
        uponSendToLabel(32, 1)
    sprite('null', 10)
    ColorForTransition(4291328255)
    ColorTransition(4294958335, 10)
    SetScaleSpeed(20)
    CreateObject('InstallMagicCircleAfterImage', -1)
    loopRest()
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(1)
    clearUponHandler(LANDING)
    sprite('null', 6)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    TriggerUponForState('InstallMagicCircleAfterImage', 32)
    AlphaValue(120)
    ConstantAlphaModifier(-20)


@State
def InstallMagicCircleAfterImage():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_magiccircle00.DIG', 'tbef_magiccircle00_motion_000.m'
            )
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RenderLayer(5)
        BlendMode_Add()
        AddY(-1000)
        Size(300)
        uponSendToLabel(32, 1)
    sprite('null', 10)
    ColorForTransition(4291328255)
    SetScaleSpeed(5)
    loopRest()
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(1)
    sprite('null', 5)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(200)
    ConstantAlphaModifier(-50)


@State
def MagicBookLoop():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        RenderLayer(1)
        SetZVal(-500)
        AddX(5000)

        def upon_30():
            TriggerUponForState('MagicBookAura', 32)
            TriggerUponForState('TBEFFont', 32)
    sprite('tb203_loop00', 6)
    CreateObject('MagicBookAura', -1)
    CreateObject('TBEFFont', 0)
    CreateObject('TBEFFont', 1)
    CreateObject('TBEFFont', 2)
    label(0)
    sprite('tb203_loop00', 3)
    physicsYImpulse(250)
    sprite('tb203_loop01', 3)
    sprite('tb203_loop02', 3)
    sprite('tb203_loop03', 3)
    sprite('tb203_loop04', 3)
    sprite('tb203_loop00', 3)
    physicsYImpulse(200)
    sprite('tb203_loop01', 3)
    sprite('tb203_loop02', 3)
    sprite('tb203_loop03', 3)
    sprite('tb203_loop04', 3)
    sprite('tb203_loop00', 3)
    physicsYImpulse(100)
    sprite('tb203_loop01', 3)
    sprite('tb203_loop02', 3)
    sprite('tb203_loop03', 3)
    sprite('tb203_loop04', 3)
    physicsYImpulse(0)
    sprite('tb203_loop00', 3)
    physicsYImpulse(-250)
    sprite('tb203_loop01', 3)
    sprite('tb203_loop02', 3)
    sprite('tb203_loop03', 3)
    sprite('tb203_loop04', 3)
    sprite('tb203_loop00', 3)
    physicsYImpulse(-200)
    sprite('tb203_loop01', 3)
    sprite('tb203_loop02', 3)
    sprite('tb203_loop03', 3)
    sprite('tb203_loop04', 3)
    sprite('tb203_loop00', 3)
    physicsYImpulse(-100)
    sprite('tb203_loop01', 3)
    sprite('tb203_loop02', 3)
    sprite('tb203_loop03', 3)
    sprite('tb203_loop04', 3)
    physicsYImpulse(0)
    loopRest()
    gotoLabel(0)


@State
def MagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
        Size(0)
        AddX(100000)
        AddY(190000)
        ColorForTransition(4294912080)

        def upon_56():
            EndObject()
        uponSendToLabel(32, 1)
    sprite('vref_env', 10)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    SetScaleSpeed(300)
    label(0)
    sprite('vref_env', 10)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 10)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def TBEFFont():

    def upon_IMMEDIATE():
        LinkParticle('tbef_font')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Size(750)
        IgnoreScreenfreeze(1)
        BlendMode_Add()

        def upon_56():
            EndObject()
        uponSendToLabel(32, 99)
    sprite('null', 32767)
    label(99)
    sprite('null', 1)


@State
def WingDust():

    def upon_IMMEDIATE():
        LinkParticle('tbef_hanelight')
    sprite('null', 60)


@State
def WeaponDelDust():

    def upon_IMMEDIATE():
        LinkParticle('tbef_dellight')
    sprite('null', 30)


@State
def TBEF201zanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(240)
        PaletteColor3(241)
        PaletteColor4(250)
        AlphaValue(245)
    sprite('vrtbef201_00', 2)
    ConstantAlphaModifier(-5)
    sprite('vrtbef201_00', 2)
    AlphaValue(150)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('vrtbef201_00', 13)
    AlphaValue(100)


@State
def TBEF231zanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(240)
        PaletteColor3(241)
        PaletteColor4(250)
        AlphaValue(245)
    sprite('vrtbef231_00', 2)
    ConstantAlphaModifier(-5)
    sprite('vrtbef231_01', 2)
    AlphaValue(150)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('vrtbef231_01', 10)
    AlphaValue(100)


@State
def AirNormalShotHit():

    def upon_IMMEDIATE():
        LinkParticle('tbef_airshothit_n')
        BlendMode_Add()
        Size(3000)
    sprite('null', 90)


@State
def AirPowerUpShotHit():

    def upon_IMMEDIATE():
        LinkParticle('tbef_airshothit')
        BlendMode_Add()
        Size(3000)
    sprite('null', 90)


@State
def AssaultAir1st_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        SameMoveProration(50)
        AirPushbackX(10000)
        AirPushbackY(20000)
        physicsXImpulse(1000)
        SetAcceleration(100)
        setGravity(100)
        AirUntechableTime(20)
        Hitstop(0)
        EnemyHitstopAddition(11, 11, 13)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 100)
        MoveAttributes(0, 0, 0, 1, 0)
        UseStrongHitspark(0)
        DamageEffect(2, 'AirNormalShotHit')

        def upon_LANDING():
            Unknown23090(23)
        BlendMode_Add()
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    loopRest()
    sprite('vrtbef404atkdmy', 90)
    CreateObject('AssaultAir1stEx_ShotNormal', 0)
    RegisterObject(4, 1)
    Visibility(1)
    sprite('keep', 10)
    EndMomentum(1)
    AttackOff()
    ObjectUpon(FALLING, 33)
    label(101)
    sprite('keep', 15)
    AttackOff()
    SetActionMark(0)
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    ParticleSize(2000)
    ParticleColor(4294953215, 4294953215, 4294953215)
    CallCustomizableParticle('tbef_lockdd', -1)
    PrivateSE('tbse_10')
    loopRest()
    ExitState()
    label(100)
    sprite('keep', 15)
    AttackOff()
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    gotoLabel(101)


@State
def AssaultAir1stEx_Shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        SameMoveProration(50)
        physicsXImpulse(10)
        physicsYImpulse(-30)
        SetAcceleration(150)
        setGravity(150)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirUntechableTime(20)
        Hitstop(0)
        EnemyHitstopAddition(11, 11, 13)
        MoveAttributes(0, 0, 0, 1, 0)
        UseStrongHitspark(0)
        DamageEffect(2, 'AirPowerUpShotHit')

        def upon_32():
            HeatGainMultiplier(200)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
        uponSendToLabel(54, 100)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(101)

        def upon_LANDING():
            sendToLabel(101)

        def upon_EVERY_FRAME():
            ObjectUpon24(23, 100, 3, 103)
            if SLOT_0 < 300000:
                TriggerUponForState('AirTackleEx', 33)
                TriggerUponForState('AirTackleEx_Hasei', 33)
        BlendMode_Add()
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrtbef404atkdmy', 180)
    CreateObject('LandShot_Ex', 0)
    RegisterObject(4, 1)
    Visibility(1)
    sprite('keep', 10)
    EndMomentum(1)
    AttackOff()
    ObjectUpon(FALLING, 33)
    label(101)
    sprite('keep', 1)
    AttackOff()
    SetActionMark(0)
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    ParticleSize(2000)
    ParticleColor(4294953215, 4294953215, 4294953215)
    CallCustomizableParticle('tbef_lockdd', -1)
    PrivateSE('tbse_11')
    loopRest()
    ExitState()
    label(100)
    sprite('keep', 25)
    AttackOff()
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    gotoLabel(101)


@State
def AssaultAir1stEx_ShotStart():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_taikuseedStart')
        BlendMode_Add()
        Size(3000)
        RotationAngle(40000)
    sprite('null', 30)


@State
def AssaultAir1stEx_ShotNormal():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_taikuseed')
        BlendMode_Add()
        Size(2000)
        RotationAngle(-40000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 30)
    RemoveOnCallStateEnd(0)
    SetScaleSpeed(15)
    ConstantAlphaModifier(-8)
    clearUponHandler(32)
    clearUponHandler(33)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 10)
    RemoveOnCallStateEnd(0)
    SetScaleSpeed(100)
    AlphaValue(100)
    clearUponHandler(32)
    clearUponHandler(33)
    PrivateSE('tbse_10')


@State
def AssaultAir1stEx_ShotEx():

    def upon_IMMEDIATE():
        ParticleColor(4294953160, 4294953160, 16711935)
        CallPrivateEffect('tbef_taikuseedEx')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(255)
        AddX(50000)
        AddY(-100000)
        Size(2400)
        RotationAngle(-40000)
        uponSendToLabel(32, 0)
    sprite('null', 4)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(150)
    ConstantAlphaModifier(-5)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def AssaultLand1stEx_ShotEx():

    def upon_IMMEDIATE():
        ParticleColor(4294953160, 4294953160, 16711935)
        CallPrivateEffect('tbef_taikuseedEx')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(255)
        AddX(50000)
        AddY(50000)
        Size(2400)
        RotationAngle(-90000)
        uponSendToLabel(32, 0)
    sprite('null', 4)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(150)
    ConstantAlphaModifier(-5)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def AssaultLand1stEx_ShotStart():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_taikuseedStart')
        BlendMode_Add()
        Size(3000)
    sprite('null', 30)


@State
def LandShot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        SameMoveProration(50)
        AirPushbackX(10000)
        AirPushbackY(16000)
        physicsXImpulse(6000)
        SetAcceleration(300)
        setGravity(0)
        AirUntechableTime(20)
        Hitstop(0)
        EnemyHitstopAddition(11, 11, 13)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 100)
        MoveAttributes(0, 0, 0, 1, 0)
        UseStrongHitspark(0)
        DamageEffect(2, 'AirNormalShotHit')
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrtbef404atkdmy', 10)
    CreateObject('LandShot_Normal', 0)
    RegisterObject(4, 1)
    Visibility(1)
    sprite('vrtbef404atkdmy', 20)
    sprite('vrtbef404atkdmy', 20)
    sprite('vrtbef404atkdmy', 20)
    sprite('keep', 10)
    EndMomentum(1)
    AttackOff()
    ObjectUpon(FALLING, 33)
    label(101)
    sprite('keep', 15)
    AttackOff()
    SetActionMark(0)
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    ParticleSize(1400)
    ParticleColor(4294953215, 4294953215, 4294953215)
    CallCustomizableParticle('tbef_lockdd', -1)
    PrivateSE('tbse_10')
    loopRest()
    ExitState()
    label(100)
    sprite('keep', 15)
    AttackOff()
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    gotoLabel(101)


@State
def LandShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(600)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        SameMoveProration(50)
        AirPushbackX(10000)
        AirPushbackY(16000)
        physicsXImpulse(1000)
        SetAcceleration(100)
        setGravity(0)
        AirUntechableTime(20)
        Hitstop(0)
        EnemyHitstopAddition(11, 11, 13)
        MoveAttributes(0, 0, 0, 1, 0)
        UseStrongHitspark(0)
        DamageEffect(2, 'AirPowerUpShotHit')
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)
        uponSendToLabel(54, 100)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(101)

        def upon_EVERY_FRAME():
            ObjectUpon24(23, 100, 3, 103)
            if SLOT_0 < 300000:
                TriggerUponForState('LandTackleEx', 33)
        BlendMode_Add()
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrtbef404atkdmy', 60)
    Size(1100)
    CreateObject('LandShot_Ex', 0)
    RegisterObject(4, 1)
    Visibility(1)
    sprite('vrtbef404atkdmy', 30)
    SetAcceleration(3000)
    sprite('vrtbef404atkdmy', 5)
    sprite('keep', 5)
    EndMomentum(1)
    AttackOff()
    ObjectUpon(FALLING, 33)
    label(101)
    sprite('keep', 1)
    AttackOff()
    EndMomentum(1)
    ParticleSize(2300)
    ParticleColor(4294953215, 4294953215, 4294953215)
    CallCustomizableParticle('tbef_lockdd', -1)
    PrivateSE('tbse_11')
    loopRest()
    ExitState()
    label(100)
    sprite('keep', 25)
    AttackOff()
    EndMomentum(1)
    ObjectUpon(FALLING, 32)
    gotoLabel(101)


@State
def LandShot_Normal():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_taikuseed')
        BlendMode_Add()
        Size(2000)
        AddX(15000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 30)
    RemoveOnCallStateEnd(0)
    SetScaleSpeed(15)
    ConstantAlphaModifier(-8)
    clearUponHandler(32)
    clearUponHandler(33)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 10)
    RemoveOnCallStateEnd(0)
    SetScaleSpeed(100)
    AlphaValue(100)
    clearUponHandler(32)
    clearUponHandler(33)
    PrivateSE('tbse_10')


@State
def LandShot_Ex():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_406eff_sub')
        BlendMode_Add()
        Size(1200)
        AddX(15000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 30)
    RemoveOnCallStateEnd(0)
    SetScaleSpeed(15)
    ConstantAlphaModifier(-8)
    clearUponHandler(32)
    clearUponHandler(33)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 10)
    RemoveOnCallStateEnd(0)
    SetScaleSpeed(100)
    AlphaValue(100)
    clearUponHandler(32)
    clearUponHandler(33)
    PrivateSE('tbse_11')


@State
def ULMagicBookLoop():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        RenderLayer(1)
        SetZVal(-500)
        AddY(64000)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)

        def upon_33():
            sendToLabel(99)
    sprite('tb203_loop00', 3)
    CreateObject('ULMagicBookAura', -1)
    RegisterObject(4, 1)
    CreateObject('TBEFFont', 0)
    RegisterObject(5, 1)
    CreateObject('TBEFFont', 1)
    RegisterObject(6, 1)
    CreateObject('TBEFFont', 2)
    RegisterObject(7, 1)
    label(0)
    sprite('tb203_loop00', 2)
    physicsYImpulse(250)
    sprite('tb203_loop01', 2)
    sprite('tb203_loop02', 2)
    sprite('tb203_loop03', 2)
    sprite('tb203_loop04', 2)
    sprite('tb203_loop00', 2)
    physicsYImpulse(200)
    sprite('tb203_loop01', 2)
    sprite('tb203_loop02', 2)
    sprite('tb203_loop03', 2)
    sprite('tb203_loop04', 2)
    sprite('tb203_loop00', 2)
    physicsYImpulse(100)
    sprite('tb203_loop01', 2)
    sprite('tb203_loop02', 2)
    sprite('tb203_loop03', 2)
    sprite('tb203_loop04', 2)
    physicsYImpulse(0)
    sprite('tb203_loop00', 2)
    physicsYImpulse(-250)
    sprite('tb203_loop01', 2)
    sprite('tb203_loop02', 2)
    sprite('tb203_loop03', 2)
    sprite('tb203_loop04', 2)
    sprite('tb203_loop00', 2)
    physicsYImpulse(-200)
    sprite('tb203_loop01', 2)
    sprite('tb203_loop02', 2)
    sprite('tb203_loop03', 2)
    sprite('tb203_loop04', 2)
    sprite('tb203_loop00', 2)
    physicsYImpulse(-100)
    sprite('tb203_loop01', 2)
    sprite('tb203_loop02', 2)
    sprite('tb203_loop03', 2)
    sprite('tb203_loop04', 2)
    physicsYImpulse(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    DeleteObject(5)
    DeleteObject(6)
    DeleteObject(7)

    def RunOnObject_4():
        SetScaleSpeed(400)
        ConstantAlphaModifier(-10)
    CreateObject('ULMagicBookAtk', -1)
    RegisterObject(8, 1)
    CreateObject('UltimateLockStart', -1)
    label(2)
    sprite('null', 2)
    loopRest()
    gotoLabel(2)
    label(99)
    ObjectUpon(FALLING, 32)
    ObjectUpon(8, 32)


@State
def ULMagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(0)
        AddX(100000)
        AddY(190000)
        ColorForTransition(4294912080)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleSpeed(300)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def ULMagicBookAtk():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        RenderLayer(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)

        def upon_33():
            sendToLabel(99)
        StopCharacterFlash1(-1)
        CharacterFlash2(-16777216, 20)
    label(1)
    sprite('vrtbef430book00', 20)
    AddX(110000)
    AddY(200000)
    StartMultihit()
    label(2)
    sprite('vrtbef430book00', 3)
    StopCharacterFlash2()
    StartMultihit()
    loopRest()
    gotoLabel(2)
    label(99)


@State
def UltimateLock_First():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        UsePunchHitspark(1)
        Damage(1000)
        MinimumDamage(15)
        AttackP1(80)
        AttackP2(65)
        MoveAttributes(0, 1, 0, 0, 0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        DefeatOpponentBehavior(1)
        OnlyHitPlayer(1)
        AirPushbackX(64000)
        AirPushbackY(10)
        Hitstop(0)
        YImpulseBeforeWallbounce(0)
        Wallbounce(1)
        StickToWall(1)
        AirUntechableTime(50)
        OppPositionOnHit(1, 0, -200000)
        IgnoreComboTime(1)
        GuardCrush(1, 1)
        StarterRating(2)
        if SLOT_6:
            CopyFromRightToLeft(23, 2, 63, 3, 2, 63)
            if SLOT_63 == -1:
                DamageFromStateOnly('UltimateLock_SeedLvC_OD')
            else:
                DamageFromStateOnly('UltimateLock_D_OD')
        else:
            CopyFromRightToLeft(23, 2, 63, 3, 2, 63)
            if SLOT_63 == 0:
                DamageFromStateOnly('UltimateLock_SeedLv0')
            if SLOT_63 == 1:
                DamageFromStateOnly('UltimateLock_SeedLv1')
            if SLOT_63 == 2:
                DamageFromStateOnly('UltimateLock_SeedLv2')
            if SLOT_63 == 3:
                DamageFromStateOnly('UltimateLock_SeedLv3')
            if SLOT_63 == 4:
                DamageFromStateOnly('UltimateLock_SeedLv4')
            if SLOT_63 == 5:
                DamageFromStateOnly('UltimateLock_SeedLv5')
            if SLOT_63 == -1:
                DamageFromStateOnly('UltimateLock_SeedLvC')

        def upon_OPPONENT_HIT():
            SLOT_51 = 2
            ObjectUpon(EVERY_FRAME, 32)
            CreateObject('UltimateLockMagic', -1)
            CreateObject('UltimateLock_DangerCircle', -1)
            RegisterObject(4, 1)

            def RunOnObject_3():
                EnableRapidCancel(0)

        def upon_EVERY_FRAME():
            if SLOT_51:
                ExtendNonCornerWallbounce(30)

                def RunOnObject_4():
                    AddAlpha(255)
                if not SLOT_63 == -1:
                    SLOT_51 = SLOT_51 + -1
                    if not SLOT_51:
                        Unknown23090(23)
        HitsPerCall(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            sendToLabel(0)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Visibility(1)

        def upon_45():
            if SLOT_63 == -1:
                clearUponHandler(45)
                ObjectUpon(LANDING, 41)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrtbef430book00', 32767)
    loopRest()
    label(0)
    sprite('null', 10)
    ObjectUpon(FALLING, 33)
    SLOT_51 = 0
    EndMomentum(1)


@State
def UltimateLock_DangerCircle():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_lockmagic.DIG', 'tbef_lockmagic_motion_000.mmot')
        ColorForTransition(2164195528)
        ColorTransition(4294967295, 25)
        TeleportToObject(22)
        E0EAEffectPosition(22)
        RenderLayer(5)
        IgnoreScreenfreeze(1)
        AddX(32000)
        AddY(220000)
        BlendMode_Add()
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
    sprite('null', 5)
    Size(500)
    SetScaleSpeed(100)
    Flip()
    AlphaValue(0)
    sprite('null', 20)
    Size(1200)
    SetScaleSpeed(1)
    sprite('null', 50)
    label(0)
    sprite('null', 15)
    E0EAEffectPosition(0)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 10)
    ColorTransition(0, 10)
    SetScaleSpeed(-100)


@State
def ULMCircleA():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(1)
        HitsPerCall(1, 0, 0, 0, 0, 1, 1, 1)
        uponSendToLabel(54, 99)
        uponSendToLabel(56, 99)
        SetPosXByScreenPer(50)
    label(0)
    sprite('null', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(50000)
    SetAcceleration(-1000)
    Unknown1082(16)
    label(2)
    sprite('null', 2)
    CreateObject('ULMCircleAdd', -1)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 15)
    clearUponHandler(32)
    clearUponHandler(54)
    TriggerUponForState('ULMCircleAdd', 32)


@State
def ULMCircleB():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(1)
        uponSendToLabel(54, 99)
        uponSendToLabel(56, 99)
        SetPosXByScreenPer(0)
        AddX(520000)
    label(0)
    sprite('null', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(60000)
    SetAcceleration(-1000)
    Unknown1082(16)
    label(2)
    sprite('null', 2)
    CreateObject('ULMCircleAdd', -1)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 15)
    TriggerUponForState('ULMCircleAdd', 32)


@State
def ULMCircleC():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(1)
        uponSendToLabel(54, 99)
        uponSendToLabel(56, 99)
        SetPosXByScreenPer(90)
        AddX(-600000)
    label(0)
    sprite('null', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(48000)
    SetAcceleration(-1000)
    Unknown1082(16)
    label(2)
    sprite('null', 2)
    CreateObject('ULMCircleAdd', -1)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 15)
    TriggerUponForState('ULMCircleAdd', 32)


@State
def ULMCircleAdd():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_lockball.DIG', 'tbef_lockball_motion_000.mmot')
        BlendMode_Add()
        Visibility(1)
        RenderLayer(1)
        Size(800)
        AlphaValue(0)
        StopCharacterFlash1(-65408)
        uponSendToLabel(32, 99)
        uponSendToLabel(56, 99)
    sprite('null', 8)
    ConstantAlphaModifier(15)
    physicsXImpulse(-2000)
    sprite('null', 32767)
    ConstantAlphaModifier(-3)
    loopRest()
    label(99)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(-2)


@State
def ULBookC():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
        StopCharacterFlash1(-8355712)
        CharacterFlash2(-16777216, 15)
    sprite('vrtbef430book00', 10)
    sprite('vrtbef430book03', 6)
    StopCharacterFlash2()
    SetZVal(500)
    AddX(-20000)
    AddY(8000)
    physicsXImpulse(-1000)
    physicsYImpulse(2000)
    sprite('vrtbef430book04', 6)
    sprite('vrtbef430book05', 6)
    loopRest()
    EndMomentum(1)
    label(0)
    sprite('vrtbef430book06', 10)
    physicsYImpulse(250)
    sprite('vrtbef430book06', 10)
    physicsYImpulse(200)
    sprite('vrtbef430book06', 10)
    physicsYImpulse(100)
    sprite('vrtbef430book06', 2)
    physicsYImpulse(0)
    sprite('vrtbef430book06', 10)
    physicsYImpulse(-250)
    sprite('vrtbef430book06', 10)
    physicsYImpulse(-200)
    sprite('vrtbef430book06', 10)
    physicsYImpulse(-100)
    sprite('vrtbef430book06', 2)
    physicsYImpulse(0)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 1)


@State
def ULBook():

    def upon_IMMEDIATE():
        HitsPerCall(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(33)
            sendToLabel(99)
        uponSendToLabel(56, 99)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(33)
            ObjectUpon(CORNERED, 32)

        def upon_33():
            clearUponHandler(32)
            clearUponHandler(33)
            sendToLabel(1)
        StopCharacterFlash1(-8355712)
        CharacterFlash(-16777216, 5, 19)
    label(0)
    sprite('vrtbef430book00', 32767)
    CreateObject('ULChange', -1)
    RegisterObject(7, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrtbef430book01', 3)
    sprite('vrtbef430book02', 32767)
    loopRest()
    label(99)
    sprite('vrtbef430book05', 3)
    SetZVal(500)
    AddX(-32000)
    physicsXImpulse(-42000)
    SetAcceleration(2000)
    physicsYImpulse(2000)
    sprite('vrtbef430book06', 3)
    loopRest()
    ExitState()


@State
def UltimateLockStart():

    def upon_IMMEDIATE():
        LinkParticle('tbef_lockshockwave')
        Size(1500)
        BlendMode_Add()
        AddX(50000)
        AddY(200000)
    sprite('null', 10)
    ConstantAlphaModifier(255)
    SetScaleSpeed(200)
    sprite('null', 15)
    SetScaleSpeed(10)
    AlphaValue(150)
    ConstantAlphaModifier(-10)


@State
def ULChange():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        LinkParticle('tbef_lockchange')
        BlendMode_Add()
        AlphaValue(255)
        Size(1500)

        def upon_32():
            sendToLabel(99)
        HitsPerCall(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            clearUponHandler(32)
            sendToLabel(99)
    label(0)
    sprite('null', 2)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 15)
    SetScaleSpeed(800)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    sprite('null', 5)
    SetScaleSpeed(100)


@State
def UltimateLockMagic():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        ContinueState(15)
        AbsoluteY(200000)
    label(0)
    sprite('null', 2)
    CreateParticle('tbef_wallpush', -1)
    loopRest()
    gotoLabel(0)


@State
def ULChangeEff():

    def upon_IMMEDIATE():
        LinkParticle('tbef_lockdd')
        Size(3000)
    sprite('null', 200)


@State
def UltimateLockBallSeed():

    def upon_IMMEDIATE():
        LinkParticle('tbef_lockballseed')
        E0EAEffectPosition(2)
        Size(1200)
        BlendMode_Add()

        def upon_33():
            sendToLabel(0)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 1)
    AlphaValue(0)


@State
def UltimateLock_BallLvC():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLvC')
        Size(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(90)
    label(0)
    sprite('null', 2)
    SetScaleSpeed(0)
    Size(1000)
    Rotation(10000)
    ParticleSize(1000)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1000)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(4000)
    SetScaleSpeed(-100)
    AlphaValue(50)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4278255360, 255)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    sprite('null', 35)


@State
def UltimateLock_SeedLvC():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        Hitstop(3)
        AirHitstunAnimation(18)
        AirPushbackY(32000)
        AirPushbackX(1000)
        YImpulseBeforeWallbounce(1500)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(3, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            sendToLabel(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ObjectUpon(EVERY_FRAME, 34)
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            XImpulseAcceleration(20)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        Visibility(1)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrtbef430_tex1', 1)
    SetAcceleration(3000)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLvC', -1)
    RegisterObject(4, 1)
    label(1)
    sprite('vrtbef430_tex1', 1)
    RefreshMultihit()
    gotoLabel(1)
    label(0)
    sprite('vrtbef430_tex1', 10)
    ObjectUpon(FALLING, 33)
    EndAttack()
    SetScaleSpeed(40)
    ConstantAlphaModifier(-20)
    EndMomentum(1)
    sprite('vrtbef430_tex1', 30)
    RefreshMultihit()


@State
def UltimateLock_SeedLvC_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        Hitstop(3)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        AirPushbackY(2000)
        AirPushbackX(100)
        YImpulseBeforeWallbounce(1500)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        DefeatOpponentBehavior(1)
        MinimumDamage(15)
        HitsPerCall(3, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            sendToLabel(0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ObjectUpon(EVERY_FRAME, 34)
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            XImpulseAcceleration(20)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        Visibility(1)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrtbef430_tex1', 1)
    SetAcceleration(3000)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLvC', -1)
    RegisterObject(4, 1)
    label(1)
    sprite('vrtbef430_tex1', 1)
    RefreshMultihit()
    gotoLabel(1)
    label(0)
    sprite('vrtbef430_tex1', 10)
    ObjectUpon(FALLING, 33)
    EndAttack()
    SetScaleSpeed(40)
    ConstantAlphaModifier(-20)
    EndMomentum(1)
    sprite('vrtbef430_tex1', 30)
    RefreshMultihit()


@State
def UltimateLock_BallLv0():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLv0')
        Size(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(90)
    label(0)
    sprite('null', 2)
    SetScaleSpeed(0)
    Size(1000)
    ParticleSize(1000)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1000)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(4000)
    SetScaleSpeed(-100)
    AlphaValue(50)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    ParticleColor(4294953215, 4294953215, 4294953215)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4278190335, 4278190335, 255)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    sprite('null', 35)


@State
def UltimateLock_SeedLv0():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(2500)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        AirPushbackX(24000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        WallbounceReboundTime(5)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            ObjectUpon(EVERY_FRAME, 34)
            sendToLabel(0)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
    sprite('null', 12)
    SetAcceleration(4000)
    CreateObject('UltimateLockBallSeed', -1)
    RegisterObject(5, 1)
    sprite('null', 9)
    PrivateSE('tbse_17')
    ObjectUpon(5, 33)
    EndMomentum(1)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLv0', -1)
    RegisterObject(6, 1)
    sprite('null', 1)
    if SLOT_6:
        conditionalSendToLabel(9)
    loopRest()
    sprite('vrtbef430_tex1', 32767)
    Visibility(1)
    BlendMode_Normal()
    RenderLayer(1)
    SetAcceleration(6500)
    Size(1000)
    AddX(32000)
    loopRest()
    label(9)
    sprite('vrtbef430_tex1', 16)
    Visibility(1)
    BlendMode_Normal()
    RenderLayer(1)
    SetAcceleration(500)
    Size(1000)
    AddX(32000)
    SLOT_6 = 10
    ObjectUpon(EVERY_FRAME, 33)
    loopRest()
    label(0)
    sprite('vrtbef430_tex1', 30)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    ObjectUpon(6, 33)
    EndAttack()
    EndMomentum(1)


@State
def UltimateLock_BallLv1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLv1')
        Size(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(150)
    label(0)
    sprite('null', 4)
    SetScaleSpeed(0)
    Size(1500)
    ParticleSize(1250)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1500)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(2000)
    SetScaleSpeed(-100)
    AlphaValue(100)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    ParticleColor(4294953215, 4294953215, 4294953215)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711680)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    sprite('null', 35)


@State
def UltimateLock_SeedLv1():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(3000)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        AirPushbackX(24000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        WallbounceReboundTime(5)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            ObjectUpon(EVERY_FRAME, 34)
            sendToLabel(0)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
    sprite('null', 12)
    SetAcceleration(4000)
    CreateObject('UltimateLockBallSeed', -1)
    RegisterObject(5, 1)
    sprite('null', 9)
    PrivateSE('tbse_17')
    ObjectUpon(5, 33)
    EndMomentum(1)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLv1', -1)
    RegisterObject(6, 1)
    sprite('null', 1)
    if SLOT_6:
        conditionalSendToLabel(9)
    loopRest()
    sprite('vrtbef430_tex1', 32767)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(5500)
    Size(1000)
    AddX(32000)
    loopRest()
    label(9)
    sprite('vrtbef430_tex1', 16)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(500)
    Size(1000)
    AddX(32000)
    SLOT_6 = 11
    ObjectUpon(EVERY_FRAME, 33)
    sprite('vrtbef430_tex4', 1)
    Visibility(1)
    loopRest()
    label(0)
    sprite('vrtbef430_tex1', 30)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    ObjectUpon(6, 33)
    EndAttack()
    ColorForTransition(16752800)
    EndMomentum(1)


@State
def UltimateLock_BallLv2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLv2')
        Size(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(150)
    label(0)
    sprite('null', 4)
    SetScaleSpeed(0)
    Size(1500)
    ParticleSize(1250)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1500)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(3000)
    SetScaleSpeed(-100)
    AlphaValue(100)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    ParticleColor(4294967040, 4294967040, 16777215)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711680)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    sprite('null', 35)


@State
def UltimateLock_SeedLv2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(4000)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        AirPushbackX(24000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        WallbounceReboundTime(5)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            ObjectUpon(EVERY_FRAME, 34)
            sendToLabel(0)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
    sprite('null', 12)
    SetAcceleration(4000)
    CreateObject('UltimateLockBallSeed', -1)
    RegisterObject(5, 1)
    sprite('null', 9)
    PrivateSE('tbse_17')
    ObjectUpon(5, 33)
    EndMomentum(1)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLv2', -1)
    RegisterObject(6, 1)
    sprite('null', 1)
    if SLOT_6:
        conditionalSendToLabel(9)
    loopRest()
    sprite('vrtbef430_tex2', 32767)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(4500)
    Size(1000)
    AddX(32000)
    loopRest()
    label(9)
    sprite('vrtbef430_tex2', 16)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(500)
    Size(1000)
    AddX(32000)
    SLOT_6 = 12
    ObjectUpon(EVERY_FRAME, 33)
    sprite('vrtbef430_tex4', 1)
    Visibility(1)
    loopRest()
    label(0)
    sprite('vrtbef430_tex2', 30)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    ObjectUpon(6, 33)
    EndAttack()
    ColorForTransition(16752800)
    EndMomentum(1)


@State
def UltimateLock_BallLv3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLv3')
        Size(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(150)
    label(0)
    sprite('null', 4)
    SetScaleSpeed(0)
    Size(2000)
    ParticleSize(1250)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1500)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(4000)
    SetScaleSpeed(-100)
    AlphaValue(100)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711935)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711680)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711935)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 35)


@State
def UltimateLock_SeedLv3():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(5000)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        AirPushbackX(24000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        WallbounceReboundTime(5)
        AirUntechableTime(50)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            ObjectUpon(EVERY_FRAME, 34)
            sendToLabel(0)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
    sprite('null', 12)
    SetAcceleration(4000)
    CreateObject('UltimateLockBallSeed', -1)
    RegisterObject(5, 1)
    sprite('null', 9)
    PrivateSE('tbse_17')
    ObjectUpon(5, 33)
    EndMomentum(1)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLv3', -1)
    RegisterObject(6, 1)
    sprite('null', 1)
    if SLOT_6:
        conditionalSendToLabel(9)
    loopRest()
    sprite('vrtbef430_tex3', 32767)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(3500)
    Size(1000)
    AddX(32000)
    loopRest()
    label(9)
    sprite('vrtbef430_tex3', 16)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(500)
    Size(1000)
    AddX(32000)
    SLOT_6 = 13
    ObjectUpon(EVERY_FRAME, 33)
    sprite('vrtbef430_tex4', 1)
    Visibility(1)
    loopRest()
    label(0)
    sprite('vrtbef430_tex3', 30)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    ObjectUpon(6, 33)
    EndAttack()
    ColorForTransition(16752800)
    EndMomentum(1)


@State
def UltimateLock_CircleLv4():

    def upon_IMMEDIATE():

        def upon_33():
            sendToLabel(0)
    sprite('vrtbef430book00', 32767)
    loopRest()
    label(0)
    sprite('vrtbef430book00', 12)
    SetZVal(500)
    physicsXImpulse(-46000)
    SetAcceleration(2000)


@State
def UltimateLock_BallLv4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLv4')
        Size(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(280)
    label(0)
    sprite('null', 4)
    SetScaleSpeed(0)
    Size(3200)
    ParticleSize(1100)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1300)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(6000)
    SetScaleSpeed(-100)
    AlphaValue(100)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    ParticleColor(4278190335, 4278190335, 255)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4278255615, 4278255615, 65535)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4278190335, 4278190335, 255)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 35)


@State
def UltimateLock_SeedLv4():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        UsePunchHitspark(1)
        AttackP2(100)
        Damage(1200)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(24000)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        WallbounceReboundTime(5)
        AirUntechableTime(50)
        Hitstop(4)
        EnemyHitstopAddition(2, 2, 2)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(5, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            ObjectUpon(EVERY_FRAME, 34)
            sendToLabel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            XImpulseAcceleration(50)
            ColorForTransition(520069280)
            ColorTransition(16752800, 30)
            HitAnywhere(1)
        BlendMode_Add()
        AddX(200000)
        AddY(260000)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
    sprite('null', 12)
    SetAcceleration(4000)
    CreateObject('UltimateLockBallSeed', -1)
    RegisterObject(5, 1)
    sprite('null', 9)
    PrivateSE('tbse_17')
    ObjectUpon(5, 33)
    EndMomentum(1)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLv4', -1)
    RegisterObject(6, 1)
    AddX(100000)
    sprite('null', 1)
    if SLOT_6:
        conditionalSendToLabel(9)
    loopRest()
    label(0)
    sprite('vrtbef430_tex4', 1)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(400)
    Size(1000)
    RefreshMultihit()
    ConstantAlphaModifier(-10)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrtbef430_tex4', 16)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(500)
    Size(1000)
    AddX(32000)
    SLOT_6 = 14
    ObjectUpon(EVERY_FRAME, 33)
    sprite('vrtbef430_tex4', 1)
    Visibility(1)
    loopRest()
    label(1)
    sprite('vrtbef430_tex4', 30)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    ObjectUpon(6, 33)
    EndAttack()
    EndMomentum(1)


@State
def UltimateLock_BallLv5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lockballLv5')
        Size(1000)

        def upon_33():
            sendToLabel(1)
    sprite('null', 10)
    SetScaleSpeed(200)
    loopRest()
    SetScaleSpeed(10)
    label(0)
    sprite('null', 2)
    SetScaleSpeed(30)
    ParticleSize(1100)
    CallCustomizableParticle('tbef_fontexp', -1)
    ParticleSize(1300)
    CallCustomizableParticle('tbef_lockball_move', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Size(6000)
    SetScaleSpeed(-100)
    AlphaValue(100)
    ConstantAlphaModifier(-5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711935)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4278255615, 4278255615, 65535)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 5)
    ParticleSize(3000)
    ParticleColor(4294901760, 4294901760, 16711935)
    CallCustomizableParticle('tbef_lockdd', -1)
    sprite('null', 35)


@State
def UltimateLock_SeedLv5():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        UsePunchHitspark(1)
        AttackP2(100)
        Damage(1000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(24000)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        WallbounceReboundTime(5)
        AirUntechableTime(50)
        Hitstop(4)
        EnemyHitstopAddition(2, 2, 2)
        OnlyHitPlayer(1)
        MinimumDamage(15)
        HitsPerCall(9, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            ObjectUpon(EVERY_FRAME, 34)
            sendToLabel(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            XImpulseAcceleration(50)
            ColorForTransition(520069280)
            ColorTransition(16752800, 30)
            HitAnywhere(1)
        BlendMode_Add()
        AddX(80000)
        AddY(260000)
        RemoveOnCallStateEnd(3)
        CHStateIfCHStart(2)
    sprite('null', 14)
    SetAcceleration(4000)
    CreateObject('UltimateLockBallSeed', -1)
    RegisterObject(5, 1)
    sprite('null', 9)
    PrivateSE('tbse_17')
    ObjectUpon(5, 33)
    EndMomentum(1)
    CreateObject('ULChangeEff', -1)
    CreateObject('UltimateLock_BallLv5', -1)
    RegisterObject(6, 1)
    AddX(200000)
    sprite('null', 1)
    if SLOT_6:
        conditionalSendToLabel(9)
    loopRest()
    label(0)
    sprite('vrtbef430_tex5', 1)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(400)
    Size(1000)
    RefreshMultihit()
    ConstantAlphaModifier(-10)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vrtbef430_tex5', 16)
    BlendMode_Normal()
    RenderLayer(1)
    ColorForTransition(4294942880)
    SetAcceleration(500)
    Size(1000)
    AddX(32000)
    SLOT_6 = 15
    ObjectUpon(EVERY_FRAME, 33)
    sprite('vrtbef430_tex5', 1)
    Visibility(1)
    loopRest()
    label(1)
    sprite('vrtbef430_tex5', 30)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    ObjectUpon(6, 33)
    EndAttack()
    EndMomentum(1)


@State
def UltimateLock_TackleEf():

    def upon_IMMEDIATE():
        CallPrivateEffect('tbef_airexattack')
        if SLOT_6 == 10:
            ParticleColor(4294953215, 4294953215, 4294953215)
        if SLOT_6 == 11:
            ParticleColor(4294953215, 4294953215, 4294953215)
        if SLOT_6 == 12:
            ParticleColor(4294967040, 4294967040, 16777215)
        if SLOT_6 == 13:
            ParticleColor(4294901760, 4294901760, 16711935)
        if SLOT_6 == 14:
            ParticleColor(4278190335, 4278190335, 255)
        if SLOT_6 == 15:
            ParticleColor(4294901760, 4294901760, 16711935)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AddX(50000)
        AlphaValue(255)
        RotationAngle(-45000)
        RunLoopUpon(17, 120)
        uponSendToLabel(17, 0)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    Size(3000)
    SetScaleSpeed(-10)
    label(0)
    sprite('null', 15)
    SetScaleSpeed(-100)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-40)


@State
def UltimateInstall():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_wind.DIG', 'tbef_wind_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        ColorForTransition(16763135)
        BlendMode_Add()
        Size(600)
        AddX(16000)

        def upon_32():
            sendToLabel(1)
    sprite('null', 10)
    ConstantAlphaModifier(20)
    SetScaleSpeed(20)
    label(0)
    sprite('null', 30)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 25)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleXPerFrame(10)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(10)
    ConstantAlphaModifier(-15)


@State
def UltimateInstallMagicCircle():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_magiccircle00.DIG', 'tbef_magiccircle00_motion_000.m'
            )
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        Size(500)
        AddX(20000)
        AddY(20000)
        AlphaValue(160)

        def upon_32():
            sendToLabel(1)
    sprite('null', 10)
    ColorForTransition(4291328255)
    ColorTransition(4294958335, 10)
    SetScaleSpeed(20)
    CreateObject('UltimateMagicCircleAfterImage', -1)
    RegisterObject(4, 1)
    label(0)
    sprite('null', 2)
    E0EAEffectPosition(0)
    SetScaleSpeed(0)
    gotoLabel(0)
    label(1)
    sprite('null', 25)
    ObjectUpon(FALLING, 32)
    RemoveOnCallStateEnd(0)
    AlphaValue(100)
    SetScaleSpeed(-5)
    ConstantAlphaModifier(-15)


@State
def UltimateMagicCircleAfterImage():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_magiccircle00.DIG', 'tbef_magiccircle00_motion_000.m'
            )
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        AddY(-1000)
        Size(600)

        def upon_32():
            sendToLabel(1)
    sprite('null', 10)
    ColorForTransition(4291328255)
    SetScaleSpeed(5)
    label(0)
    sprite('null', 2)
    E0EAEffectPosition(0)
    SetScaleSpeed(0)
    gotoLabel(0)
    label(1)
    sprite('null', 25)
    RemoveOnCallStateEnd(0)
    AlphaValue(100)
    SetScaleSpeed(-10)
    ConstantAlphaModifier(-10)


@State
def UCMagicBookLoop():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        SetZVal(-500)
        IgnoreScreenfreeze(1)

        def upon_32():
            sendToLabel(1)

        def upon_33():
            sendToLabel(99)
    sprite('tb431_loop00', 3)
    CreateObject('UCMagicBookAura', -1)
    RegisterObject(4, 1)
    CreateObject('TBEFFont', 0)
    RegisterObject(5, 1)
    CreateObject('TBEFFont', 1)
    RegisterObject(6, 1)
    CreateObject('TBEFFont', 2)
    RegisterObject(7, 1)
    label(0)
    sprite('tb431_loop01', 2)
    physicsYImpulse(250)
    sprite('tb431_loop02', 2)
    sprite('tb431_loop03', 2)
    sprite('tb431_loop04', 2)
    sprite('tb431_loop01', 2)
    physicsYImpulse(200)
    sprite('tb431_loop02', 2)
    sprite('tb431_loop03', 2)
    sprite('tb431_loop04', 2)
    sprite('tb431_loop01', 2)
    physicsYImpulse(100)
    sprite('tb431_loop02', 2)
    sprite('tb431_loop03', 2)
    sprite('tb431_loop04', 2)
    physicsYImpulse(0)
    sprite('tb431_loop01', 2)
    physicsYImpulse(-250)
    sprite('tb431_loop02', 2)
    sprite('tb431_loop03', 2)
    sprite('tb431_loop04', 2)
    sprite('tb431_loop01', 2)
    physicsYImpulse(-200)
    sprite('tb431_loop02', 2)
    sprite('tb431_loop03', 2)
    sprite('tb431_loop04', 2)
    sprite('tb431_loop01', 2)
    physicsYImpulse(-100)
    sprite('tb431_loop02', 2)
    sprite('tb431_loop03', 2)
    sprite('tb431_loop04', 2)
    physicsYImpulse(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tb431_loop05', 2)
    DeleteObject(5)
    DeleteObject(6)
    DeleteObject(7)

    def RunOnObject_4():
        SetScaleSpeed(400)
        ConstantAlphaModifier(-10)
    label(2)
    sprite('null', 2)
    loopRest()
    gotoLabel(2)
    label(99)
    ObjectUpon(FALLING, 32)


@State
def UCMagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddX(-100000)
        AbsoluteY(0)
        Size(0)
        ColorForTransition(681594960)
        CreateObject('UCMagicBookAuraBack', -1)
        RegisterObject(4, 1)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleXPerFrame(600)
    SetScaleSpeedY(600)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    ObjectUpon(FALLING, 32)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def UCMagicBookAuraBack():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        Size(0)
        ColorForTransition(4294586930)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleXPerFrame(800)
    SetScaleSpeedY(800)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def UltimateCharge_TextField():

    def upon_IMMEDIATE():
        LinkParticle('tbef_ultmfont_all')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(255)
        AddX(60000)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 48)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 34)
    ConstantAlphaModifier(-7)


@State
def UltimateCharge_DataField():

    def upon_IMMEDIATE():
        LinkParticle('tbef_ultmdata_all')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(200)
        AddX(60000)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 60)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def TBEF_AngelRing():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_ultmring')
        BlendMode_Add()
        AlphaValue(255)
        Size(800)
        AddX(-10000)
        AddY(420000)
        uponSendToLabel(32, 1)
    sprite('null', 80)
    loopRest()
    label(1)
    sprite('null', 20)
    E0EAEffectPosition(0)


@State
def yugami_ring():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(2000)
    sprite('vr_yugami', 5)
    SetScaleSpeed(800)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami', 10)
    SetScaleSpeed(200)
    Unknown3059(-3200)


@State
def Atk5C_arm():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
    sprite('vrtbef202_arm01', 2)
    CreateObject('TBEF_ArmChange', -1)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    physicsXImpulse(-2200)
    physicsYImpulse(-800)
    sprite('vrtbef202_arm00', 3)
    BlendMode_Off()
    physicsXImpulse(60000)
    physicsYImpulse(10000)
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 3)
    CreateObject('EffectAura', 4)
    sprite('vrtbef202_arm01', 3)
    EndMomentum(1)
    RemoveOnCallStateEnd(0)
    sprite('vrtbef202_arm01', 4)
    E0EAEffectPosition(0)
    AddX(-22000)
    AddY(-6000)
    physicsXImpulse(-1100)
    physicsYImpulse(-400)
    sprite('vrtbef202_arm01', 10)
    BlendMode_Normal()
    AlphaValue(150)
    ConstantAlphaModifier(-15)
    CreateObject('WeaponDelDust', 0)
    CreateObject('WeaponDelDust', 1)
    CreateObject('WeaponDelDust', 2)
    CreateObject('WeaponDelDust', 3)
    CreateObject('WeaponDelDust', 4)


@State
def Atk5C_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        LinkParticle('tbef_5Cmagic')
        BlendMode_Add()
        RotationAngle(50000)
        AddRotationPerFrame(-10000)
    sprite('null', 5)
    sprite('null', 15)
    AddRotationPerFrame(0)


@State
def AtkAIR6C_sword():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Off()
    sprite('vrtbef212_arm00', 1)
    CreateObject('EffectAura', -1)
    StopCharacterFlash1(9868950)
    CharacterFlash2(0, 6)
    sprite('vrtbef212_arm01', 2)
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 1)
    CreateObject('EffectAura', 2)
    CreateObject('EffectAura', 3)
    CreateObject('EffectAura', 4)
    CreateObject('EffectAura', 5)
    CreateObject('EffectAura', 6)
    sprite('vrtbef212_arm02', 3)
    sprite('vrtbef212_arm03', 3)
    StopCharacterFlash2()
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 1)
    CreateObject('EffectAura', 2)
    CreateObject('EffectAura', 3)
    CreateObject('EffectAura', 4)
    CreateObject('EffectAura', 5)
    CreateObject('EffectAura', 6)
    sprite('vrtbef212_arm02ex01', 3)
    sprite('vrtbef212_arm03ex01', 2)
    sprite('vrtbef212_arm02ex02', 2)
    sprite('vrtbef212_arm03ex02', 5)
    CreateObject('WeaponDelDust', 0)
    CreateObject('WeaponDelDust', 1)
    CreateObject('WeaponDelDust', 2)
    CreateObject('WeaponDelDust', 3)
    CreateObject('WeaponDelDust', 4)
    CreateObject('WeaponDelDust', 5)
    CreateObject('WeaponDelDust', 6)


@State
def AtkAIR5C_mace():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()

        def upon_32():
            sendToLabel(1)
    sprite('vrtbef252_mace', 5)
    CreateObject('TBEF_ArmChange_link', -1)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    AddY(240000)
    physicsXImpulse(-2000)
    physicsYImpulse(2000)
    label(0)
    sprite('vrtbef252_mace', 4)
    BlendMode_Off()
    EndMomentum(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrtbef252_mace', 4)
    AddY(-115000)
    AddX(120000)
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 3)
    CreateObject('EffectAura', 4)
    RemoveOnCallStateEnd(0)
    sprite('vrtbef252_mace', 4)
    AddY(10000)
    AddX(-10000)
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    sprite('vrtbef252_mace', 5)
    E0EAEffectPosition(0)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-20)
    CreateObject('WeaponDelDust', 0)
    CreateObject('WeaponDelDust', 1)
    CreateObject('WeaponDelDust', 2)
    CreateObject('WeaponDelDust', 3)
    CreateObject('WeaponDelDust', 4)


@State
def ThrowLock_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('tbef_lockmagic2.DIG', 'tbef_lockmagic2_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        AddY(220000)
        ColorForTransition(4294967220)
        Unknown23130(16727100, 60, -1)

        def upon_32():
            sendToLabel(99)

        def upon_33():
            sendToLabel(100)
    sprite('null', 32767)
    ConstantAlphaModifier(-5)
    loopRest()
    label(99)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)
    loopRest()
    label(100)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    loopRest()


@State
def ThrowBackLock_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('tbef_lockmagic2.DIG', 'tbef_lockmagic2_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        AddY(220000)
        ColorForTransition(4294967220)
        Unknown23130(16727100, 60, -1)

        def upon_32():
            sendToLabel(99)

        def upon_33():
            sendToLabel(100)
    sprite('null', 5)
    ConstantAlphaModifier(-5)
    sprite('null', 32767)
    ConstantAlphaModifier(-10)
    loopRest()
    label(99)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)
    loopRest()
    label(100)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    loopRest()


@State
def AirThrowLock_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('tbef_lockmagic2.DIG', 'tbef_lockmagic2_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        ColorForTransition(4294967220)
        Unknown23130(16727100, 60, -1)

        def upon_32():
            sendToLabel(99)

        def upon_33():
            sendToLabel(100)
    sprite('null', 32767)
    ConstantAlphaModifier(-5)
    loopRest()
    label(99)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)
    loopRest()
    label(100)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    loopRest()


@State
def Effect6CArmSpot():

    def upon_IMMEDIATE():
        CallPrivateEffect('tbef_6Carmspot')
        BlendMode_Add()
    sprite('null', 60)


@State
def AssaultLand2ndEff():

    def upon_IMMEDIATE():
        LinkParticle('tbef_assault2nd')
        IgnoreScreenfreeze(1)
    sprite('null', 20)


@State
def AssaultLand2ndExEff():

    def upon_IMMEDIATE():
        LinkParticle('tbef_assault2ndEx')
        IgnoreScreenfreeze(1)
    sprite('null', 20)


@State
def AssaultLand2ndBladeEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        LinkParticle('tbef_assault2ndBlade')
        AddX(120000)
        AddY(-64000)
    sprite('null', 12)


@State
def AssaultLandExAuraEff():

    def upon_IMMEDIATE():
        CallPrivateEffect('tbef_assault2ndExAura')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
    sprite('null', 25)
    ConstantAlphaModifier(-10)


@State
def AssaultLand3rdEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tbef_assault3rd')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
    sprite('null', 60)
    ConstantAlphaModifier(40)


@State
def AssaultLand3rdExEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tbef_assault3rdEx')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
    sprite('null', 60)
    ConstantAlphaModifier(40)


@State
def AssaultLand3rdBladeEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        LinkParticle('tbef_assault3rdBlade')
        AddX(250000)
        AddY(140000)
    sprite('null', 12)


@State
def AssaultExAura():

    def upon_IMMEDIATE():
        LinkParticle('tbef_assaultExAura')
    sprite('null', 24)


@State
def AssaultHoldOpt():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tbef_assaultHoldOpt')
        AddY(200000)
        uponSendToLabel(32, 1)
        uponSendToLabel(56, 1)
    sprite('null', 32767)
    loopRest()
    label(1)
    sprite('null', 15)
    clearUponHandler(32)
    clearUponHandler(56)
    AlphaValue(150)
    ConstantAlphaModifier(-10)


@State
def Entry2MagicCircle():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_magiccircle00.DIG', 'tbef_magiccircle00_motion_000.m'
            )
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        Size(500)
        AddX(-20000)
        AddY(20000)
        AlphaValue(160)
    sprite('null', 10)
    ColorForTransition(4291328255)
    ColorTransition(4294958335, 10)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(20)
    CreateObject('Entry2Wind', -1)
    RegisterObject(4, 1)
    sprite('null', 10)
    E0EAEffectPosition(0)
    AlphaValue(100)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    sprite('null', 30)
    ObjectUpon(FALLING, 32)
    SetScaleSpeed(5)
    ConstantAlphaModifier(-4)


@State
def Entry2Wind():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_wind.DIG', 'tbef_wind_motion_000.mmot')
        FaceSpawnLocation()
        ColorForTransition(16763135)
        BlendMode_Add()
        Size(300)
    sprite('null', 10)
    ConstantAlphaModifier(20)
    SetScaleSpeed(20)
    sprite('null', 10)
    sprite('null', 10)
    SetScaleXPerFrame(20)
    SetScaleSpeedY(-50)
    SetScaleSpeedZ(20)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def EffectAuraAssaltAir():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RenderLayer(5)
        CallPrivateEffect('tbef_airenvlight')
        BlendMode_Add()
        AlphaValue(0)
        uponSendToLabel(32, 0)
        uponSendToLabel(56, 0)
        AddX(-32000)
        AddY(-16000)
    sprite('null', 32767)
    ConstantAlphaModifier(5)
    Size(4000)
    label(0)
    sprite('null', 15)
    clearUponHandler(32)
    clearUponHandler(56)
    AlphaValue(150)
    ConstantAlphaModifier(-10)


@State
def EffectAuraAssaltAirExOpt():

    def upon_IMMEDIATE():
        LinkParticle('tbef_airexattack')
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        BlendMode_Add()
        AlphaValue(255)
        RunLoopUpon(17, 10)
        uponSendToLabel(17, 0)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    Size(2500)
    SetScaleSpeed(-10)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(-100)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-40)


@State
def EffectAuraAssaltAirEx():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        LinkParticle('tbef_airexattack')
        BlendMode_Add()
        AlphaValue(255)
        RunLoopUpon(17, 12)
        uponSendToLabel(17, 0)
        uponSendToLabel(32, 1)
        AddX(100000)
        AddY(-150000)
    sprite('null', 32767)
    Size(2500)
    SetScaleSpeed(-10)
    label(0)
    sprite('null', 15)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-40)


@State
def EffectAuraAssaltLandExOpt():

    def upon_IMMEDIATE():
        LinkParticle('tbef_airexattack')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AddX(50000)
        AlphaValue(255)
        RotationAngle(-45000)
        RunLoopUpon(17, 120)
        uponSendToLabel(17, 0)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    Size(3000)
    SetScaleSpeed(-10)
    label(0)
    sprite('null', 15)
    SetScaleSpeed(-100)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-40)


@State
def TBEF_ArmChange():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        LinkParticle('tbef_armchange')
        ContinueState(62)
    sprite('null', 2)
    sprite('null', 60)
    E0EAEffectPosition(0)


@State
def TBEF_ArmChange_link():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        ContinueState(62)
    sprite('null', 1)
    sprite('null', 1)
    LinkParticle('tbef_armchange')
    sprite('null', 60)
    E0EAEffectPosition(3)


@State
def TBEF_ArmSummon():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        Size(1250)
        LinkParticle('tbef_armsummon')
        ParticleColorFromPalette(55, 51, 53)
        CallCustomizableParticle('tbef_armsummon01', -1)
        ContinueState(62)
        IgnoreScreenfreeze(1)
    sprite('null', 2)
    sprite('null', 60)


@State
def EffectAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        RenderLayer(5)
        CallPrivateEffect('tbef_envlight')
    sprite('null', 4)
    SetScaleY(900)
    SetScaleX(900)
    sprite('null', 15)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-20)


@State
def Atk6A_gauntlet():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        SetZVal(-500)
    sprite('vrtbef210_gauntlet00', 3)
    AddY(-12000)
    CreateObject('EffectAura', 0)
    sprite('vrtbef210_gauntlet01', 2)
    AddY(-2000)
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 1)
    sprite('vrtbef210_gauntlet01', 4)
    sprite('vrtbef210_gauntlet01', 2)
    AddY(12000)
    physicsYImpulse(3000)
    sprite('vrtbef210_gauntlet01', 2)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-20)
    CreateObject('WeaponDelDust', 0)
    CreateObject('WeaponDelDust', 1)


@State
def Atk6A_lightcircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_lightball')
        BlendMode_Add()
    sprite('null', 30)


@State
def Atk6B_mcircle():

    def upon_IMMEDIATE():
        LinkParticle('tbef_6Bmcircle')
        AddX(190000)
        AddY(5000)
        CancelIfPlayerHit(3)
    sprite('null', 7)
    sprite('vrtbef211_00', 3)
    sprite('vrtbef211_01', 4)
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 1)
    CreateObject('EffectAura', 2)
    CreateObject('EffectAura', 3)
    sprite('vrtbef211_02', 4)
    CreateObject('WingDust', 1)
    CreateObject('WingDust', 3)
    CreateObject('WeaponDelDust', 0)
    CreateObject('WeaponDelDust', 1)
    CreateObject('WeaponDelDust', 2)
    CreateObject('WeaponDelDust', 3)


@State
def AssaultLand1stEff():

    def upon_IMMEDIATE():
        LinkParticle('tbef_assault1st')
        IgnoreScreenfreeze(1)
    sprite('null', 26)


@State
def AssaultLand1stEffEx():

    def upon_IMMEDIATE():
        LinkParticle('tbef_assault1stEx')
        IgnoreScreenfreeze(1)
    sprite('null', 36)


@State
def AssaultLand1st_airdash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_assault1st_airdash')
    sprite('null', 14)


@State
def AssaultLand1st_airdashEx():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_assault1st_airdashEx')
    sprite('null', 14)


@State
def AssaultLand1stA_mcircle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_assault1st_mcircle')
    sprite('null', 20)


@State
def AssaultLand1stA_mcircleEx():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        LinkParticle('tbef_assault1st_mcircleEx')
    sprite('null', 20)


@State
def AssaultLand1st_lightball():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tbef_assault1st_lightball')
    sprite('null', 75)


@State
def AssaultLand1st_lightballEx():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tbef_assault1st_lightballEx')
    sprite('null', 75)


@State
def AssaultLand1st_MagicBookchage():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RenderLayer(1)

        def upon_32():
            sendToLabel(1)
    label(0)
    sprite('tb400_book00', 2)
    CharacterFlash(16724608, 3, 2)
    sprite('tb400_book01', 2)
    sprite('tb400_book02', 2)
    sprite('tb400_book00', 2)
    sprite('tb400_book01', 2)
    sprite('tb400_book02', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 1)


@State
def AssaultLand1st_MagicBook():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RenderLayer(1)

        def upon_32():
            sendToLabel(11)
    sprite('tb400_book03', 2)
    CreateObject('AssaultLand1stA_mcircle', 0)
    sprite('tb400_book04', 2)
    AddX(12000)
    sprite('tb400_book05', 2)
    sprite('tb400_book06', 2)
    sprite('tb400_book04', 2)
    sprite('tb400_book05', 2)
    sprite('tb400_book06', 2)
    sprite('tb400_book04', 2)
    sprite('tb400_book05', 2)
    sprite('tb400_book06', 2)
    label(11)
    sprite('null', 1)


@State
def AssaultLand1st_MagicBookEx():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RenderLayer(1)

        def upon_32():
            sendToLabel(11)
    sprite('tb400_book03', 2)
    CreateObject('AssaultLand1stA_mcircleEx', 0)
    sprite('tb400_book04', 2)
    AddX(12000)
    sprite('tb400_book05', 2)
    sprite('tb400_book06', 2)
    sprite('tb400_book04', 2)
    sprite('tb400_book05', 2)
    sprite('tb400_book06', 2)
    sprite('tb400_book04', 2)
    sprite('tb400_book05', 2)
    sprite('tb400_book06', 2)
    label(11)
    sprite('null', 1)


@State
def AssaultLand1stA_MagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        BlendMode_Add()
        Size(0)
        AddX(70000)
        AddY(215000)
        ColorForTransition(2164208256)

        def upon_14():
            sendToLabel(1)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleSpeed(300)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def AssaultLand1stB_MagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        BlendMode_Add()
        Size(0)
        AddX(70000)
        AddY(215000)
        ColorForTransition(2164208256)

        def upon_14():
            sendToLabel(1)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleSpeed(300)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def AssaultLand1stC_MagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        BlendMode_Add()
        Size(0)
        AddX(70000)
        AddY(215000)
        ColorForTransition(2164208256)

        def upon_14():
            sendToLabel(1)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleSpeed(300)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def AssaultLand1stEx_MagicBookAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        BlendMode_Add()
        Size(0)
        AddX(70000)
        AddY(215000)
        ColorForTransition(2164233948)

        def upon_14():
            sendToLabel(1)

        def upon_32():
            sendToLabel(1)
    sprite('vref_env', 10)
    SetScaleSpeed(300)
    label(0)
    sprite('vref_env', 10)
    SetScaleSpeed(0)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vref_env', 14)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def AntiAir_mcircle():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_antiair_mcircle')
        BlendMode_Add()

        def upon_32():
            sendToLabel(1)
    sprite('null', 40)
    AddX(155000)
    AddY(-6000)
    loopRest()
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-20)
    endState()


@State
def AntiAir_mcircleEx():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_antiair_mcircleEx')
        BlendMode_Add()

        def upon_32():
            sendToLabel(1)
    sprite('null', 40)
    AddX(155000)
    AddY(-6000)
    loopRest()
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-20)


@State
def AntiAir_auraA():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ParticleColor(4294967295, 4279835135, 4284769535)
        CallPrivateEffect('tbef_antiair_aura')
        BlendMode_Add()
    sprite('null', 6)
    AddX(10000)
    AddY(28000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('null', 20)
    ConstantAlphaModifier(0)
    sprite('null', 6)
    ConstantAlphaModifier(-20)


@State
def AntiAir_auraB():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        ParticleColor(4294967295, 4279893785, 4284809060)
        CallPrivateEffect('tbef_antiair_aura')
        BlendMode_Add()
    sprite('null', 6)
    SetScaleY(1100)
    AddX(10000)
    AddY(28000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('null', 20)
    ConstantAlphaModifier(0)
    sprite('null', 6)
    ConstantAlphaModifier(-20)


@State
def AntiAir_auraC():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        ParticleColor(4294967295, 4294908185, 4294927460)
        CallPrivateEffect('tbef_antiair_aura')
        BlendMode_Add()
    sprite('null', 6)
    SetScaleY(1200)
    AddX(10000)
    AddY(28000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('null', 20)
    ConstantAlphaModifier(0)
    sprite('null', 6)
    ConstantAlphaModifier(-20)


@State
def AntiAir_auraExA():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ParticleColor(4294967295, 4281479935, 4288059135)
        CallPrivateEffect('tbef_antiair_aura')
        BlendMode_Add()
    sprite('null', 4)
    AddX(10000)
    AddY(28000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('null', 22)
    ConstantAlphaModifier(0)
    sprite('null', 6)
    ConstantAlphaModifier(-20)


@State
def AntiAir_auraExB():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        ParticleColor(4294967295, 4281532210, 4288085910)
        CallPrivateEffect('tbef_antiair_aura')
        BlendMode_Add()
    sprite('null', 4)
    SetScaleY(1100)
    AddX(5000)
    AddY(28000)
    AlphaValue(0)
    ConstantAlphaModifier(15)
    sprite('null', 22)
    ConstantAlphaModifier(0)
    sprite('null', 6)
    ConstantAlphaModifier(-20)


@State
def AntiAir_auraEx():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        ParticleColor(4294967295, 4286067320, 4290005940)
        CallPrivateEffect('tbef_antiair_aura')
        BlendMode_Add()
    sprite('null', 4)
    SetScaleY(1100)
    AddY(28000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('null', 4)
    ConstantAlphaModifier(0)
    sprite('null', 18)
    sprite('null', 6)
    ConstantAlphaModifier(-20)


@State
def AntiAir_light():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        E0EAEffectPosition(2)
        BlendMode_Add()

        def upon_14():
            sendToLabel(1)
        uponSendToLabel(32, 99)
    label(0)
    sprite('null', 2)
    CreateParticle('tbef_antiair_lightball', -1)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 2)


@State
def AntiAir_swordC():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        EndMomentum(0)
        AttackLevel_(3)
        Damage(850)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(50)
        SameMoveProration(50)
        Blockstun(29)
        UseSlashHitspark(1)
        Hitstop(4)
        AirPushbackY(42000)
        AirUntechableTime(44)
        CHAirPushbackX(9000)
        CHAirPushbackY(48000)
        CHAirUntechableTime(60)
        EnemyHitstopAddition(0, 0, 0)
        BlendMode_Add()
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MoveAttributes(0, 0, 0, 1, 0)
        ProjectileLevel(0)
        StrikeProjectileLevel(1)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(0)
        AlphaValue(0)
        CancelIfPlayerHit(3)
    sprite('null', 2)
    CreateObject('AntiAir_mcircle', -1)
    RegisterObject(4, 1)
    sprite('vrtbef403_00ex', 3)
    StartMultihit()
    AddX(160000)
    AddY(80000)
    physicsXImpulse(200)
    physicsYImpulse(680)
    RotationSomething(0)
    ConstantAlphaModifier(20)
    CreateObject('TBEF_ArmChange', 2)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    CreateObject('AntiAir_auraC', -1)
    CreateObject('AntiAir_light', -1)
    sprite('vrtbef403_00ex', 40)
    physicsXImpulse(20000)
    physicsYImpulse(68000)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(2)
    AfterimageCount(12)
    AfterimageMask_1(0, 255, 75, 75)
    AfterimageMask_2(0, 255, 50, 50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(25)
    YAccel(25)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    TriggerUponForState('AntiAir_light', 32)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 10)
    ObjectUpon(FALLING, 32)


@State
def AntiAir_swordEx():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(650)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(50)
        SingleProration(1)
        SameMoveProration(50)
        Blockstun(24)
        UseSlashHitspark(1)
        Hitstop(4)
        AirPushbackX(3000)
        CHAirPushbackX(6000)
        AirPushbackY(42000)
        AirUntechableTime(44)
        Unknown11095(1)
        BlendMode_Add()
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MoveAttributes(0, 0, 0, 1, 0)
        ProjectileLevel(0)
        StrikeProjectileLevel(1)
        HitAirUnblockable(3)
        MoveAttributes(0, 1, 0, 0, 0)
        StarterRating(0)
        AlphaValue(0)
        CancelIfPlayerHit(3)
    sprite('null', 4)
    CreateObject('AntiAir_mcircleEx', -1)
    RegisterObject(4, 1)
    sprite('vrtbef403_00ex', 3)
    StartMultihit()
    AddX(200000)
    AddY(80000)
    Size(800)
    physicsXImpulse(160)
    physicsYImpulse(660)
    RotationSomething(0)
    ConstantAlphaModifier(20)
    CreateObject('TBEF_ArmChange', 2)
    StartMultihit()
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    CreateObject('AntiAir_auraEx', -1)
    CreateObject('AntiAir_light', -1)
    sprite('vrtbef403_00ex', 3)
    physicsXImpulse(16000)
    physicsYImpulse(66000)
    RefreshMultihit()
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(12)
    AfterimageMask_1(0, 0, 0, 255)
    AfterimageMask_2(0, 0, 0, 0)
    sprite('vrtbef403_00ex', 3)
    RefreshMultihit()
    CreateObject('EffectAura', 0)
    CreateObject('EffectAura', 2)
    CreateObject('EffectAura', 4)
    sprite('vrtbef403_00ex', 3)
    RefreshMultihit()
    sprite('vrtbef403_00ex', 40)
    StartMultihit()
    CreateObject('EffectAura', 1)
    CreateObject('EffectAura', 3)
    XImpulseAcceleration(25)
    YAccel(25)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    TriggerUponForState('AntiAir_light', 32)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()
    ObjectUpon(FALLING, 32)


@State
def AntiAir_swordA():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(600)
        AttackP1(70)
        AttackP2(74)
        Blockstun(29)
        UseSlashHitspark(1)
        Hitstop(3)
        AirPushbackX(4000)
        AirPushbackY(35000)
        AirUntechableTime(40)
        CHAirUntechableTime(40)
        BlendMode_Add()
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MoveAttributes(0, 0, 0, 1, 0)
        ProjectileLevel(1)
        AlphaValue(0)
        CancelIfPlayerHit(3)
    sprite('null', 2)
    CreateObject('AntiAir_mcircle', -1)
    RegisterObject(4, 1)
    sprite('vrtbef403_00ex', 3)
    StartMultihit()
    AddX(160000)
    AddY(80000)
    physicsXImpulse(120)
    physicsYImpulse(500)
    RotationSomething(0)
    ConstantAlphaModifier(20)
    CreateObject('TBEF_ArmChange', 2)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    CreateObject('AntiAir_auraA', -1)
    CreateObject('AntiAir_light', -1)
    sprite('vrtbef403_00ex', 7)
    physicsXImpulse(12000)
    physicsYImpulse(50000)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(10)
    AfterimageMask_1(0, 50, 50, 255)
    AfterimageMask_2(0, 50, 50, 255)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(25)
    YAccel(25)
    AlphaValue(120)
    ConstantAlphaModifier(-10)
    TriggerUponForState('AntiAir_light', 32)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()
    ObjectUpon(FALLING, 32)


@State
def AntiAir_swordB():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        EndMomentum(0)
        AttackLevel_(4)
        Damage(700)
        AttackP1(70)
        AttackP2(74)
        Blockstun(29)
        UseSlashHitspark(1)
        Hitstop(4)
        AirPushbackX(4000)
        AirPushbackY(35000)
        AirUntechableTime(40)
        CHAirUntechableTime(40)
        BlendMode_Add()
        HitAirUnblockable(3)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MoveAttributes(0, 0, 0, 1, 0)
        ProjectileLevel(1)
        AlphaValue(0)
        CancelIfPlayerHit(3)
    sprite('null', 2)
    CreateObject('AntiAir_mcircle', -1)
    RegisterObject(4, 1)
    sprite('vrtbef403_00ex', 3)
    StartMultihit()
    AddX(160000)
    AddY(80000)
    physicsXImpulse(160)
    physicsYImpulse(580)
    RotationSomething(0)
    ConstantAlphaModifier(20)
    CreateObject('TBEF_ArmChange', 2)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    CreateObject('AntiAir_auraB', -1)
    CreateObject('AntiAir_light', -1)
    sprite('vrtbef403_00ex', 7)
    physicsXImpulse(16000)
    physicsYImpulse(58000)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(10)
    AfterimageMask_1(0, 75, 255, 75)
    AfterimageMask_2(0, 50, 255, 50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(25)
    YAccel(25)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    TriggerUponForState('AntiAir_light', 32)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()
    ObjectUpon(FALLING, 32)


@State
def AntiAir_swordExA():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        BlendMode_Add()
        AlphaValue(0)
    sprite('null', 2)
    sprite('vrtbef403_00ex', 3)
    StartMultihit()
    Size(800)
    AddX(250000)
    AddY(80000)
    physicsXImpulse(100)
    physicsYImpulse(500)
    RotationSomething(0)
    ConstantAlphaModifier(20)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    CreateObject('AntiAir_auraExA', -1)
    CreateObject('AntiAir_light', -1)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()
    physicsXImpulse(10000)
    physicsYImpulse(50000)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(10)
    AfterimageMask_1(0, 50, 50, 255)
    AfterimageMask_2(0, 50, 50, 255)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(25)
    YAccel(25)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    TriggerUponForState('AntiAir_light', 32)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()


@State
def AntiAir_swordExB():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        BlendMode_Add()
        AlphaValue(0)
    sprite('null', 2)
    sprite('vrtbef403_00ex', 3)
    StartMultihit()
    Size(800)
    AddX(120000)
    AddY(80000)
    physicsXImpulse(200)
    physicsYImpulse(600)
    RotationSomething(0)
    ConstantAlphaModifier(20)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    CreateObject('AntiAir_auraExB', -1)
    CreateObject('AntiAir_light', -1)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()
    physicsXImpulse(20000)
    physicsYImpulse(60000)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(10)
    AfterimageMask_1(0, 75, 255, 75)
    AfterimageMask_2(0, 50, 255, 50)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    XImpulseAcceleration(25)
    YAccel(25)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    TriggerUponForState('AntiAir_light', 32)
    sprite('vrtbef403_00ex', 2)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 1)
    StartMultihit()
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('vrtbef403_00ex', 7)
    StartMultihit()


@State
def AssaultAir1st_auraA():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        ParticleColor(4294914688, 4294914688, 4294914688)
        CallPrivateEffect('tbef_AssaultAir1stAura')
        BlendMode_Add()
        AddX(20000)
        AddY(50000)
    sprite('null', 20)


@State
def AssaultAir1st_auraB():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        ParticleColor(4294914688, 4294914688, 4294914688)
        CallPrivateEffect('tbef_AssaultAir1stAura')
        BlendMode_Add()
        AddX(-50000)
    sprite('null', 20)


@State
def AssaultAir1st_auraC():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        ParticleColor(4294927460, 4294927460, 4294927460)
        CallPrivateEffect('tbef_AssaultAir1stAura')
        BlendMode_Add()
    sprite('null', 20)


@State
def Terikaeshi():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        Size(5000)
        AlphaValue(255)

        def upon_32():
            sendToLabel(1)
    sprite('vref_teridmy', 300)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    loopRest()
    label(1)
    sprite('vref_teridmy', 5)
    ConstantAlphaModifier(-30)


@State
def __407kokusokuray():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AlphaValue(255)
        uponSendToLabel(32, 1)
        RenderLayer(2)
    sprite('null', 32767)
    LinkParticle('tbef_407kousoku_thunder')
    label(1)
    sprite('null', 10)
    CreateParticle('tbef_407kousoku_fin', -1)
    SetScaleXPerFrame(-80)


@State
def AstWhite():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        XPositionRelativeFacing(0)
        AbsoluteY(7800000)
        Size(10000)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vr_white', 30)
    ConstantAlphaModifier(15)
    CommonSE('022_magiccircle_b')
    sprite('vr_white', 30)
    sprite('vr_white', 30)
    AlphaValue(240)
    ConstantAlphaModifier(-8)


@State
def AstWhitefinish():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        ScreenPosition(1)
        E0EAEffectPosition(3)
        SetPosXByScreenPer(50)
        Size(10000)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vr_white', 30)
    ConstantAlphaModifier(15)
    sprite('vr_white', 15)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-20)


@State
def AH_mcircle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        LinkParticle('tbef_AH_mcircle')
    sprite('null', 16)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    Size(50)
    SetScaleSpeed(80)
    sprite('null', 45)
    SetScaleSpeed(4)
    sprite('null', 12)
    SetScaleSpeed(100)
    AlphaValue(128)
    ConstantAlphaModifier(-10)


@State
def AH_wind():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_wind.DIG', 'tbef_wind_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
        Size(0)
        AddY(80000)
        uponSendToLabel(32, 0)
        uponSendToLabel(56, 0)
    sprite('null', 10)
    SetScaleY(120)
    SetScaleSpeed(50)
    AlphaValue(128)
    ConstantAlphaModifier(20)
    sprite('null', 32767)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    loopRest()
    label(0)
    sprite('null', 12)
    SetScaleXPerFrame(120)
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    sprite('null', 5)
    EndMomentum(1)


@State
def AH_changelight():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        LinkParticle('tbef_AH_light')
    sprite('vr_light', 20)
    SetScaleX(100)
    SetScaleXPerFrame(40)
    ColorForTransition(4278190080)
    ColorTransition(4292830454, 40)
    sprite('vr_light', 30)
    SetScaleXPerFrame(0)
    SetScaleX(1000)
    sprite('vr_light', 10)
    ColorForTransition(4292830454)
    ColorTransition(4278190080, 10)
    SetScaleXPerFrame(5)


@State
def AHCharge_TextField():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(128)
        LinkParticle('tbef_AHfont_all')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 48)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 12)
    ConstantAlphaModifier(-10)


@State
def AHCharge_DateField():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(200)
        LinkParticle('tbef_AHdate')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 128)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 16)
    ConstantAlphaModifier(-10)


@State
def AH_changelightC():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        LinkParticle('tbef_AH_changelightC')
    sprite('null', 60)


@State
def AH_changeBG():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        LinkParticle('tbef_AH_changeBG')
        uponSendToLabel(32, 90)
    sprite('null', 60)
    loopRest()
    label(90)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(-25)


@State
def AH_BG():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        IgnorePauses(3)
        LinkParticle('tbef_AH_BG')
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        uponSendToLabel(32, 1)
    sprite('null', 300)
    loopRest()
    label(1)
    sprite('null', 10)
    AlphaValue(255)
    ConstantAlphaModifier(-25)


@State
def AH_mcirclebook():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_AH_book')

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            sendToLabel(1)
    sprite('null', 14)
    sprite('null', 8)
    E0EAEffectPosition(0)
    SetScaleSpeed(60)
    AlphaValue(160)
    ConstantAlphaModifier(-20)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 6)
    SetScaleSpeed(40)
    AlphaValue(180)
    ConstantAlphaModifier(-30)


@State
def AHLock_MagicCircle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('tbef_lockmagic2.DIG', 'tbef_lockmagic2_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(800)
        AddY(220000)
        ColorForTransition(4294967220)
        Unknown23130(16727100, 60, -1)

        def upon_32():
            sendToLabel(99)
    sprite('null', 32767)
    ConstantAlphaModifier(-5)
    loopRest()
    label(99)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    SetScaleXPerFrame(200)
    SetScaleSpeedY(100)


@State
def AH_locklight():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        LinkParticle('tbef_AH_locklight')
        uponSendToLabel(32, 1)
    sprite('null', 60)
    loopRest()
    label(1)
    sprite('null', 20)
    AlphaValue(255)
    ConstantAlphaModifier(-12)


@State
def AH_tsubaki():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Normal()
        FaceLeft()
        RenderLayer(3)
        AddX(-64000)
        AddY(24000)
        Size(600)
    sprite('null', 8)
    sprite('tb450_33', 6)
    CommonSE('019_quake_1')
    physicsYImpulse(100)
    CreateObject('AH_auracharge', 0)
    CreateObject('AH_auraRing', 0)
    RegisterObject(4, 1)
    CreateObject('AH_auraA', 0)
    sprite('tb450_34', 6)
    sprite('tb450_35', 6)
    sprite('tb450_33', 6)
    sprite('tb450_34', 6)
    sprite('tb450_35', 6)
    sprite('tb450_33', 6)
    CommonSE('019_quake_1')
    sprite('tb450_33', 6)
    sprite('tb450_34', 6)
    sprite('tb450_35', 6)
    sprite('tb450_34', 6)
    Voiceline('tb255')
    sprite('tb450_35', 6)
    sprite('tb450_33', 6)
    sprite('tb450_34', 6)
    CommonSE('019_quake_1')
    sprite('tb450_35', 6)
    sprite('tb450_33', 6)
    sprite('tb450_34', 6)
    sprite('tb450_35', 6)
    sprite('tb450_33', 6)
    CommonSE('019_quake_1')
    sprite('tb450_34', 6)
    sprite('tb450_35', 6)
    sprite('tb450_33', 6)
    sprite('tb450_34', 6)
    sprite('tb450_36', 8)
    CommonSE('019_quake_1')
    sprite('tb450_37', 8)
    sprite('tb450_38', 6)
    CommonSE('015_blaze_2')
    CreateObject('AH_auraB', 0)
    RegisterObject(5, 1)
    TriggerUponForState('AH_auraA', 32)
    sprite('tb450_38ex00', 6)
    CommonSE('019_quake_1')
    sprite('tb450_38ex01', 6)
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    sprite('tb450_38', 6)
    CommonSE('019_quake_1')
    Voiceline('tb256')
    sprite('tb450_38ex00', 6)
    CommonSE('015_blaze_2')
    sprite('tb450_38ex01', 6)
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    CommonSE('019_quake_1')
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    CommonSE('015_blaze_2')
    sprite('tb450_38ex01', 6)
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    CommonSE('019_quake_1')
    sprite('tb450_38ex01', 6)
    sprite('tb450_38', 6)
    CommonSE('014_electric_sl')
    sprite('tb450_38ex00', 6)
    CommonSE('015_blaze_2')
    sprite('tb450_38ex01', 6)
    EndMomentum(1)
    sprite('tb450_38', 6)
    CommonSE('014_electric_sl')
    CommonSE('019_quake_1')
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    sprite('tb450_38', 6)
    CommonSE('014_electric_sl')
    CommonSE('015_blaze_2')
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    CommonSE('014_electric_sl')
    CommonSE('019_quake_1')
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    CommonSE('014_electric_sl')
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    CommonSE('014_electric_sl')
    sprite('tb450_38', 6)
    CommonSE('019_quake_1')
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    CommonSE('014_electric_sl')
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    CommonSE('019_quake_1')
    sprite('tb450_38ex01', 6)
    CommonSE('014_electric_sl')
    sprite('tb450_38', 6)
    sprite('tb450_38ex00', 6)
    sprite('tb450_38ex01', 6)
    CharacterFlash(-1, 7, 2)
    sprite('tb450_39', 6)
    Voiceline('tb257')
    CommonSE('002_highjump_2')
    CreateObject('AH_auraC', 0)
    ObjectUpon(5, 32)
    ObjectUpon(FALLING, 32)
    sprite('tb450_40', 6)
    sprite('tb450_41', 48)
    sprite('tb450_41', 1)


@State
def AH_auracharge():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_AHauracharge')
    sprite('null', 282)
    sprite('null', 252)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def AH_auraA():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_AHauraA')
        Size(1400)
        AlphaValue(0)
        uponSendToLabel(32, 1)
        ContinueState(640)
    sprite('null', 255)
    ConstantAlphaModifier(1)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    loopRest()
    label(1)
    sprite('null', 6)
    AlphaValue(180)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_auraRing():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        ParticleLayer(1)
        CallPrivateEffect('tbef_AHauraRing')
        AddRotationPerFrame(350)
        AlphaValue(0)
        uponSendToLabel(32, 1)
        ContinueState(640)
    sprite('null', 255)
    ConstantAlphaModifier(1)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    loopRest()
    label(1)
    sprite('null', 6)
    AlphaValue(180)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_auraB():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_AHauraB')
        Size(900)
        uponSendToLabel(32, 1)
        ContinueState(400)
    sprite('null', 32767)
    loopRest()
    label(1)
    sprite('null', 6)
    SetScaleSpeed(40)
    AlphaValue(180)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_auraC():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_AHauraC')
    sprite('null', 16)


@State
def AH_FinishThunder():

    def upon_IMMEDIATE():
        RenderLayer(2)
        BlendMode_Add()
        FaceLeft()
        AbsoluteY(8050000)
        XPositionRelativeFacing(100000)
        RotationAngle(12000)
        Size(1200)
        LinkParticle('tbef_AH_finish_thunder')
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    sprite('null', 60)
    AlphaValue(128)
    sprite('null', 20)
    physicsYImpulse(1000)
    sprite('null', 37)
    physicsYImpulse(1800)
    sprite('null', 2)
    physicsYImpulse(2500)
    AddRotationPerFrame(-1000)
    sprite('null', 3)
    AddY(50000)
    physicsYImpulse(2500)
    physicsXImpulse(80000)
    AddRotationPerFrame(-1000)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_megamilight():

    def upon_IMMEDIATE():
        RenderLayer(5)
        BlendMode_Add()
        FaceLeft()
        AbsoluteY(8050000)
        XPositionRelativeFacing(0)
        RotationAngle(12000)
        LinkParticle('tbef_AH_megamilight')
    sprite('null', 90)
    sprite('null', 20)
    physicsYImpulse(1000)
    sprite('null', 36)
    physicsYImpulse(1800)
    sprite('null', 1)
    physicsYImpulse(-15000)
    sprite('null', 3)
    physicsYImpulse(-10000)
    AddRotationPerFrame(-1000)
    sprite('null', 2)
    physicsYImpulse(2000)
    physicsXImpulse(90000)
    AddRotationPerFrame(1000)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_FinishRedlight():

    def upon_IMMEDIATE():
        RenderLayer(2)
        LinkParticle('tbef_AH_finishBG_red')
        FaceLeft()
        AbsoluteY(7950000)
        XPositionRelativeFacing(0)
        Size(1400)
        uponSendToLabel(32, 0)
    sprite('null', 200)
    label(0)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_megami_aura():

    def upon_IMMEDIATE():
        ParticleLayer(2)
        ParticleColor(4286644223, 4286644223, 4286644223)
        CallPrivateEffect('tbef_AHmegami_aura')
        FaceLeft()
        BlendMode_Add()
        AlphaValue(0)
        XPositionRelativeFacing(-110000)
        Size(400)
        AddY(14000000)
        uponSendToLabel(32, 0)
    sprite('null', 5)
    physicsXImpulse(500)
    ConstantAlphaModifier(10)
    sprite('null', 200)
    ConstantAlphaModifier(0)
    physicsXImpulse(-400)
    sprite('null', 100)
    physicsXImpulse(-200)
    sprite('null', 200)
    physicsXImpulse(0)
    sprite('null', 100)
    SetScaleSpeed(10)
    sprite('null', 35)
    ConstantAlphaModifier(10)
    label(0)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_finishBG():

    def upon_IMMEDIATE():
        RenderLayer(2)
        LinkParticle('tbef_AH_finishBG')
        AbsoluteY(8500000)
        XPositionRelativeFacing(700000)
        AlphaValue(100)
        SetScaleX(1100)
        SetScaleY(1000)
        uponSendToLabel(32, 1)
    sprite('null', 800)
    label(1)
    sprite('null', 1)
    AlphaValue(0)


@State
def AH_finish():

    def upon_IMMEDIATE():
        RenderLayer(1)
        FaceLeft()
        LinkParticle('tbef_AH_finish')
        XPositionRelativeFacing(0)
        AddY(350000)
    sprite('null', 30)


@State
def AH_wing():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)

        def upon_32():
            EndObject()
    label(0)
    sprite('null', 2)
    CreateParticle('tbef_AH_wing', -1)
    loopRest()
    gotoLabel(0)


@State
def AH_Megami():

    def upon_IMMEDIATE():
        Eff3DEffect('tbef_ASTmegami.DIG', '')
        FaceLeft()
        AddX(-5120000)
        BlendMode_Normal()
        AbsoluteY(-6800000)
        SetScaleX(1600)
        SetScaleY(1600)
        SetScaleZ(1000)
        uponSendToLabel(32, 0)
    sprite('null', 297)
    CreateObject('AH_megami_aura', -1)
    setGravity(-1)
    physicsXImpulse(8000)
    sprite('null', 300)
    physicsXImpulse(0)
    setGravity(0)
    sprite('null', 8)
    physicsXImpulse(260000)
    physicsYImpulse(-260000)
    SetScaleXPerFrame(0)
    SetScaleSpeedY(0)
    sprite('null', 5)
    XImpulseAcceleration(25)
    YAccel(25)
    sprite('null', 5)
    XImpulseAcceleration(25)
    YAccel(25)
    sprite('null', 5)
    XImpulseAcceleration(50)
    YAccel(25)
    sprite('null', 5)
    XImpulseAcceleration(50)
    YAccel(25)
    sprite('null', 5)
    XImpulseAcceleration(50)
    YAccel(25)
    sprite('null', 5)
    XImpulseAcceleration(50)
    YAccel(25)
    label(0)
    sprite('null', 1)
    AlphaValue(0)


@State
def EventHazamaWalk():
    PaletteIndex(7)
    Flip()
    XPositionRelativeFacing(-900000)
    ScreenCollision(0)
    SetZVal(500)
    SetActionMark(1)

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_19 < 30000:
                SetActionMark(0)
                sendToLabel(1)
    sprite('hz030_00', 7)
    physicsXImpulse(5000)
    sprite('hz030_01', 7)
    label(0)
    sprite('hz030_02', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)
    sprite('hz030_04', 7)
    sprite('hz030_05', 7)
    sprite('hz030_06', 7)
    sprite('hz030_07', 7)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)
    sprite('hz030_09', 7)
    sprite('hz030_10', 7)
    sprite('hz030_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    enterState('EventHazamaStand')


@State
def EventHazamaStand():

    def upon_VALUE_RECEIVED():
        PaletteIndex(7)
        SetZVal(500)
        if SLOT_ReceivedValue == 10:
            enterState('EventHazamaBackJump')
    label(0)
    sprite('hz000_00', 8)
    sprite('hz000_01', 8)
    sprite('hz000_02', 8)
    sprite('hz000_03', 8)
    sprite('hz000_04', 8)
    sprite('hz000_05', 8)
    sprite('hz000_06', 8)
    sprite('hz000_07', 8)
    sprite('hz000_08', 8)
    loopRest()
    gotoLabel(0)


@State
def EventHazamaBackJump():

    def upon_IMMEDIATE():
        physicsXImpulse(0)
        physicsYImpulse(0)
        PaletteIndex(7)
        SetZVal(500)
        ContinueState(60)
    sprite('hz023_00', 3)
    sprite('hz023_01', 3)
    sprite('hz023_02', 3)
    sprite('hz022_00', 20)
    CommonSE('001_airbackdash_0')
    physicsXImpulse(-30000)
    physicsYImpulse(50000)
    loopRest()


@State
def RLAstLockmc():

    def upon_IMMEDIATE():
        Visibility(1)
        ParticleLayer(5)
        CallPrivateEffect('rlef_ashlock_mc')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def RLAstLockAura():

    def upon_IMMEDIATE():
        Visibility(1)
        CallPrivateEffect('rlef_ashlock_aura')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def UltimateShotMaster():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        RunLoopUpon(17, 200)

        def upon_17():
            sendToLabel(1)
        Visibility(1)
        NoDamageAction(1)

        def upon_41():
            Unknown2064(1)
            TriggerUponForState('UltimateShotTest', 41)
    sprite('tb432_07ex', 3)
    CreateObject('UltimateShotTest', 0)
    ObjectUpon(STATE_END, 32)
    sprite('tb432_08', 3)
    CreateObject('UltimateShotTest', 1)
    ObjectUpon(STATE_END, 33)
    sprite('tb432_09', 3)
    CreateObject('UltimateShotTest', 2)
    ObjectUpon(STATE_END, 34)
    sprite('tb432_07', 3)
    CreateObject('UltimateShotTest', 3)
    ObjectUpon(STATE_END, 35)
    sprite('tb432_08', 3)
    CreateObject('UltimateShotTest', 4)
    ObjectUpon(STATE_END, 36)
    sprite('tb432_09', 3)
    CreateObject('UltimateShotTest', 5)
    ObjectUpon(STATE_END, 37)
    sprite('tb432_07', 3)
    CreateObject('UltimateShotTest', 6)
    ObjectUpon(STATE_END, 38)
    sprite('tb432_08', 3)
    CreateObject('UltimateShotTest', 7)
    ObjectUpon(STATE_END, 39)
    sprite('tb432_09', 3)
    sprite('tb432_09', 300)
    label(1)
    sprite('null', 10)


@State
def UltimateShotMaster_OD():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        RunLoopUpon(17, 200)

        def upon_17():
            sendToLabel(1)
        Visibility(1)
        NoDamageAction(1)

        def upon_41():
            Unknown2064(1)
            TriggerUponForState('UltimateShotTest_OD', 41)
    sprite('tb432_07ex', 3)
    CreateObject('UltimateShotTest_OD', 0)
    ObjectUpon(STATE_END, 32)
    sprite('tb432_08', 3)
    CreateObject('UltimateShotTest_OD', 1)
    ObjectUpon(STATE_END, 33)
    sprite('tb432_09', 3)
    CreateObject('UltimateShotTest_OD', 2)
    ObjectUpon(STATE_END, 34)
    sprite('tb432_07', 3)
    CreateObject('UltimateShotTest_OD', 3)
    ObjectUpon(STATE_END, 35)
    sprite('tb432_08', 3)
    CreateObject('UltimateShotTest_OD', 4)
    ObjectUpon(STATE_END, 36)
    sprite('tb432_09', 3)
    CreateObject('UltimateShotTest_OD', 5)
    ObjectUpon(STATE_END, 37)
    sprite('tb432_07', 3)
    CreateObject('UltimateShotTest_OD', 6)
    ObjectUpon(STATE_END, 38)
    sprite('tb432_08', 3)
    CreateObject('UltimateShotTest_OD', 7)
    ObjectUpon(STATE_END, 39)
    sprite('tb432_09', 3)
    sprite('tb432_09', 300)
    label(1)
    sprite('null', 10)


@State
def UltimateShotTest():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('tbef_432jizoku_add')
        Eff3DEffect('tbef_432sord', '')
        AttackDefaults_SuperProjectile()
        Visibility(1)
        VoodooDamageMultiplier(2)
        AttackLevel_(2)
        Damage(450)
        AttackP1(60)
        AttackP2(96)
        StarterRating(0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(15000)
        Hitstop(0)
        AirUntechableTime(36)
        PushbackX(32000)
        UseSlashHitspark(1)
        RenderLayer(4)
        AlphaValue(255)
        Size(430)
        RotationAngle(20000)

        def upon_32():
            SLOT_51 = 1

        def upon_33():
            SLOT_52 = 1

        def upon_34():
            SLOT_53 = 1

        def upon_35():
            SLOT_54 = 1

        def upon_36():
            SLOT_55 = 1

        def upon_37():
            SLOT_56 = 1

        def upon_38():
            SLOT_57 = 1

        def upon_39():
            SLOT_58 = 1
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 100)
        AttackOff()

        def upon_45():
            if SLOT_ReceivedValue == 10:
                clearUponHandler(45)
                ObjectUpon(LANDING, 41)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(2)
        CHStateIfCHStart(2)
    sprite('vrtbef403_00ex', 10)
    CreateParticle('tbef_432spawn_thunder', 2)
    physicsXImpulse(400)
    physicsYImpulse(-500)
    ConstantAlphaModifier(25)
    sprite('vrtbef403_00ex', 40)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SpriteIfNot0(44, 2, 52)
    SpriteIfNot0(48, 2, 53)
    SpriteIfNot0(52, 2, 54)
    SpriteIfNot0(56, 2, 55)
    SpriteIfNot0(60, 2, 56)
    SpriteIfNot0(64, 2, 57)
    SpriteIfNot0(68, 2, 58)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('vrtbef403_00ex', 1)
    CallPrivateFunction('TBDDAngleSet', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrtbef403_00ex', 40)
    PopSpeedX()
    PopSpeedY()
    RefreshMultihit()
    CreateObject('432nokosibloom', -1)
    label(100)
    sprite('vrtbef403_00ex', 45)
    AttackOff()
    ConstantAlphaModifier(-6)


@State
def UltimateShotTest_OD():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('tbef_432jizoku_add2')
        Eff3DEffect('tbef_432sordOD', '')
        AttackDefaults_SuperProjectile()
        Visibility(1)
        VoodooDamageMultiplier(2)
        AttackLevel_(4)
        AttackType(4)
        Damage(600)
        AttackP1(60)
        AttackP2(96)
        StarterRating(0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(15000)
        Hitstop(2)
        AirUntechableTime(36)
        PushbackX(10000)
        UseSlashHitspark(1)
        RenderLayer(4)
        AlphaValue(255)
        Size(430)
        RotationAngle(20000)

        def upon_32():
            SLOT_51 = 1

        def upon_33():
            SLOT_52 = 1

        def upon_34():
            SLOT_53 = 1

        def upon_35():
            SLOT_54 = 1

        def upon_36():
            SLOT_55 = 1

        def upon_37():
            SLOT_56 = 1

        def upon_38():
            SLOT_57 = 1

        def upon_39():
            SLOT_58 = 1
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 100)
        AttackOff()

        def upon_45():
            if SLOT_ReceivedValue == 10:
                clearUponHandler(45)
                ObjectUpon(LANDING, 41)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(2)
        CHStateIfCHStart(2)
    sprite('vrtbef403_00ex', 10)
    CreateParticle('tbef_432spawn_thunder', 2)
    physicsXImpulse(400)
    physicsYImpulse(-500)
    ConstantAlphaModifier(25)
    sprite('vrtbef403_00ex', 40)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SpriteIfNot0(46, 2, 52)
    SpriteIfNot0(52, 2, 53)
    SpriteIfNot0(58, 2, 54)
    SpriteIfNot0(64, 2, 55)
    SpriteIfNot0(70, 2, 56)
    SpriteIfNot0(76, 2, 57)
    SpriteIfNot0(82, 2, 58)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('vrtbef403_00ex', 1)
    CallPrivateFunction('TBDDAngleSet', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrtbef403_00ex', 40)
    PopSpeedX()
    PopSpeedY()
    RefreshMultihit()
    CreateObject('432nokosibloom', -1)
    label(100)
    sprite('vrtbef403_00ex', 45)
    AttackOff()
    ConstantAlphaModifier(-6)


@State
def __432nokosibloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
        E0EAEffectRotation(2)

        def upon_14():
            sendToLabel(1)
        uponSendToLabel(32, 99)
    label(0)
    sprite('null', 5)
    CreateObject('432bloom', -1)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 2)


@State
def __432bloom():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
    sprite('null', 30)
    LinkParticle('tbef_432nokosi_bloom')


@State
def __407bookloop():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 99)
    label(0)
    sprite('tb407_book00', 3)
    sprite('tb407_book01', 3)
    sprite('tb407_book02', 3)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 1)


@State
def AssaultLand2nd_mcircle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        LinkParticle('tbef_assault1st_mcircle')
        AddX(180000)
        AddY(230000)
    sprite('null', 20)


@State
def BurstDD_Test():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        uponSendToLabel(32, 1)

        def upon_33():
            SLOT_2 = 1
    sprite('null', 1)
    label(0)
    sprite('null', 3)
    CreateObject('BurstDD_Testtama', 0)
    if SLOT_2:
        ObjectUpon(STATE_END, 33)
    sprite('null', 3)
    CreateObject('BurstDD_Testtama', 0)
    if SLOT_2:
        ObjectUpon(STATE_END, 33)
    sprite('null', 3)
    CreateObject('BurstDD_Testtama', 0)
    if SLOT_2:
        ObjectUpon(STATE_END, 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    CreateObject('BurstDD_Testtama', 0)
    ObjectUpon(STATE_END, 32)
    if SLOT_2:
        ObjectUpon(STATE_END, 33)


@State
def BurstDD_Testtama():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(120)
        Hitstop(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AttackP2(100)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        MinimumDamage(10)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        AirPushbackX(5000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(5)
        WallbounceReboundTime(5)
        AirUntechableTime(60)
        HardKnockdown(1)
        UseSlashHitspark(1)
        HitsparkSize(500)
        ContinueState(120)
        SameMoveProration(-1)
        OnlyHitPlayer(1)
        DeviationY(-300000, 100000)
        physicsXImpulse(100000)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 9)
        Visibility(1)

        def upon_32():
            AirPushbackX(60000)
            AttackType(4)
            DefeatOpponentBehavior(0)

        def upon_33():
            Damage(160)
        CHStateIfCHStart(3)
    sprite('null', 1)
    label(0)
    sprite('tb440tama', 4)
    sprite('tb440tama', 4)
    loopRest()
    gotoLabel(0)
    label(9)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    sprite('null', 1)


@State
def BurstDD_Yumi():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('vrtbef440_yumi00', 4)
    sprite('vrtbef440_yumi01', 4)
    sprite('vrtbef440_yumi02', 4)
    sprite('vrtbef440_yumi03', 4)
    sprite('vrtbef440_yumi04', 32767)
    CreateObject('BurstDD_Core', 0)
    CreateObject('BurstDD_YumiC', 1)
    CreateParticle('tbef_440hane', 2)
    CreateParticle('tbef_440hane', 3)
    CreateParticle('tbef_440hane', 4)
    CreateParticle('tbef_440hane', 5)
    CreateParticle('tbef_440kira_mato', 4)
    CreateParticle('tbef_440kira_mato', 5)
    label(0)
    sprite('vrtbef440_yumi05', 6)
    DespawnEAEffect('BurstDD_Core')
    DespawnEAEffect('BurstDD_YumiC')
    sprite('vrtbef440_yumi06', 4)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(80)
    AddX(250000)
    AddY(255000)
    CreateParticle('tbef_440hane2', 0)
    CreateParticle('tbef_440hane2', 1)
    CreateParticle('tbef_440hane2', 2)
    CreateParticle('tbef_440hane2', 3)
    CreateParticle('tbef_440hane2', 4)
    CreateParticle('tbef_440hane2', 5)
    sprite('vrtbef440_yumi06', 6)
    CreateParticle('tbef_440hane2', 0)
    CreateParticle('tbef_440hane2', 1)
    CreateParticle('tbef_440hane2', 2)
    CreateParticle('tbef_440hane2', 3)
    CreateParticle('tbef_440hane2', 4)
    CreateParticle('tbef_440hane2', 5)


@State
def BurstDD_YumiC():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('tbef_440circle', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddX(25000)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    SetScaleSpeed(45)
    sprite('null', 32767)
    SetScaleSpeed(0)


@State
def BurstDD_Core():

    def upon_IMMEDIATE():
        LinkParticle('tbef_440_syuyaku')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 4)
    Size(500)
    sprite('null', 32767)
    Size(1000)


@State
def BurstDD_BeamMato2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AddX(-150000)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    CreateObject('BurstDD_BeamMatoCore', -1)
    ScreenShake(20000, 20000)
    label(0)
    sprite('null', 9)
    CreateObject('BurstDD_Beam', -1)
    ScreenShake(5000, 5000)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    TriggerUponForState('BurstDD_BeamMatoCore', 32)


@State
def BurstDD_BeamMatoCore():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_440_shootcore')
        AddY(250000)
        AddX(400000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-26)
    CreateParticle('tbef_440kira_mato2', -1)


@State
def BurstDD_BeamMato2EX():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AddX(-150000)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    CreateObject('BurstDD_BeamMatoCoreEX', -1)
    ScreenShake(20000, 20000)
    label(0)
    sprite('null', 9)
    CreateObject('BurstDD_BeamEX', -1)
    ScreenShake(5000, 5000)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    TriggerUponForState('BurstDD_BeamMatoCoreEX', 32)


@State
def BurstDD_BeamMatoEX():
    sprite('null', 5)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(300000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(350000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(400000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(450000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(300000)
        SetScaleY(-1000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(350000)
        SetScaleY(-1000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(400000)
        SetScaleY(-1000)
    CreateObject('BurstDD_Beam', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(450000)
        SetScaleY(-1000)


@State
def BurstDD_BeamMatoCoreEX():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('tbef_440_shootcoreEX')
        AddY(250000)
        AddX(400000)
        Size(1200)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-26)
    CreateParticle('tbef_440kira_mato2', -1)


@State
def BurstDD_BeamEX():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('tbef_440beam01', '')
        AddY(250000)
        AddX(300000)
        SetScaleX(1200)
    sprite('null', 15)
    sprite('null', 24)
    CreateObject('BurstDD_EffPos', -1)

    def RunOnObject_1():
        SetScaleX(800)
    CreateObject('BurstDD_EffPos', -1)

    def RunOnObject_1():
        SetScaleY(-800)
        SetScaleX(800)


@State
def BurstDD_Beam():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('tbef_440beam00', '')
        AddY(250000)
        AddX(300000)
        SetScaleX(1200)
    sprite('null', 15)
    sprite('null', 24)
    CreateObject('BurstDD_EffPos', -1)

    def RunOnObject_1():
        SetScaleX(800)
    CreateObject('BurstDD_EffPos', -1)

    def RunOnObject_1():
        SetScaleY(-800)
        SetScaleX(800)


@State
def BurstDD_EffPos():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 0)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 1)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 2)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 3)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 4)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 5)
    sprite('vrtbef440_particlepos', 4)
    CreateParticle('tbef_440_zansho', 6)


@State
def Fade1():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        E0EAEffectPosition(3)
        AlphaValue(0)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('vr_fade', 10)
    Size(20000)
    ColorForTransition(4278190080)
    ConstantAlphaModifier(25)
    SetBackground(2)
    sprite('vr_fade', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    label(1)
    sprite('vr_fade', 20)
    SetBackground(0)
    sprite('vr_fade', 10)
    ConstantAlphaModifier(-25)


@State
def EventJNYoroke():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 2)
        LoadSpritePalette(0)
        XPositionRelativeFacing(-100000)
    sprite('jn620_08', 32767)
    label(0)
    sprite('jn620_08', 5)
    sprite('jn620_07', 5)
    sprite('jn620_06', 5)
    sprite('jn620_05', 5)
    sprite('jn620_04', 5)
    sprite('jn620_03', 5)
    sprite('jn620_02', 5)
    sprite('jn620_01', 5)
    sprite('jn620_00', 5)
    label(1)
    sprite('jn000_00', 7)
    sprite('jn000_01', 7)
    sprite('jn000_02', 7)
    sprite('jn000_03', 7)
    sprite('jn000_04', 7)
    sprite('jn000_05', 7)
    sprite('jn000_06', 7)
    sprite('jn000_07', 7)
    sprite('jn000_08', 7)
    sprite('jn000_09', 7)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('jn032_00', 4)
    Flip()
    physicsXImpulse(26000)
    sprite('jn032_01', 4)
    sprite('jn032_02', 4)
    sprite('jn032_03', 4)
    sprite('jn032_04', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_05', 4)
    sprite('jn032_06', 4)
    sprite('jn032_07', 4)
    sprite('jn032_08', 4)
    sprite('jn032_09', 4)
    DashEffects(100, 1, 1)
    sprite('jn032_10', 4)
    sprite('jn032_11', 4)
    sprite('jn032_12', 4)


@State
def Act2Event_Fade():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AlphaValue(0)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('null', 60)
    Size(20000)
    ColorForTransition(4278190080)
    ConstantAlphaModifier(4)
    SetBackground(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)


@State
def Act2Event_NagenukeEff():

    def upon_IMMEDIATE():
        AddX(210000)
        AddY(222000)
    sprite('null', 3)
    CreateParticle('ef_nagenuke', 0)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def EventNoYoroke():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 0)
        XPositionRelativeFacing(-200000)
        LoadSpritePalette(0)
        SetZVal(-500)
    sprite('no064_04', 32767)
    label(0)
    sprite('no064_05', 4)
    sprite('no064_06', 4)
    sprite('no064_07', 4)
    sprite('no064_08', 4)
    sprite('no032_00', 4)
    Flip()
    physicsXImpulse(26000)
    sprite('no032_01', 4)
    sprite('no032_02', 4)
    sprite('no032_03', 4)
    sprite('no032_04', 4)
    DashEffects(100, 1, 1)
    sprite('no032_05', 4)
    sprite('no032_06', 4)
    sprite('no032_07', 4)
    DashEffects(100, 1, 1)
