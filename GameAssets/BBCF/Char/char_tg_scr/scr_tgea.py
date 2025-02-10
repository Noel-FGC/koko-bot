@State
def EMB_tg():

    def upon_IMMEDIATE():
        BlendMode_Add()
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_TG.DIG', 'ef_emb_TG_motion_000.mmot')
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
def EMB_TG_OD():

    def upon_IMMEDIATE():
        BlendMode_Add()
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_TG.DIG', 'ef_emb_TG_motion_000.mmot')
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
def EMB_TG_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_TG.DIG', 'ef_emb_TG_motion_000.mmot')
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


@State
def tgef_plas_mc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef_plas_mc05', -1)


@State
def AddMagnetPtc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1000)
    CallCustomizableParticle('tgef_exptc00', -1)


@State
def tgef203mc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1500)
    CallCustomizableParticle('tgef203_mc05', -1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1500)
    CallCustomizableParticle('tgef_thunder00', -1)


@State
def tgef233mc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef233_mc05', -1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef_thunder00', -1)


@State
def tgef213mc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1500)
    CallCustomizableParticle('tgef253_mc05', -1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1500)
    CallCustomizableParticle('tgef_thunder00', -1)


@State
def tgef253mc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1500)
    CallCustomizableParticle('tgef253_mc05', -1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(1500)
    CallCustomizableParticle('tgef_thunder00', -1)


@State
def ShockA():
    sprite('null', 1)
    Visibility(1)
    CreateParticle('tgef_shock01', -1)
    CreateParticle('tgef_shock02', -1)
    CreateParticle('tgef_shock03', -1)


@State
def ShockB():
    sprite('null', 1)
    Visibility(1)
    CreateParticle('tgef_shock01', -1)
    CreateParticle('tgef_shock02', -1)
    CreateParticle('tgef_shock03', -1)
    CreateParticle('tgef_shock04', -1)
    CreateParticle('tgef_shock05', -1)
    CreateParticle('tgef_shock06', -1)
    CreateParticle('tgef_shock07', -1)


@State
def GETBFallBody():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('tgef432_fall')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 120)


@State
def GETBJumpEFF():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('tgef_shock06', -1)


@State
def MagneticStorm():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(239, 236, 224)
    CallCustomizableParticle('tgef400maghand', -1)


@State
def LoopHandAtk():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('tgef251ptc')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RotationAngle(-30000)
    sprite('null', 120)


@State
def HeadBatAtk():

    def upon_IMMEDIATE():
        Visibility(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 1)
    CreateParticle('tgef_side_shockA', -1)


@State
def tgef403chgptc():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(175, 175, 175)
    CallCustomizableParticle('tgef403chg', -1)


@State
def ShotObjCharge():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RandRotationAngle()
        AddRotationPerFrame(90000)
    sprite('vrtgef403sht_chg00', 1)
    BlendMode_Add()
    AlphaValue(255)
    Size(200)
    SetScaleSpeed(200)
    CreateObject('tgef403chgptc', -1)
    sprite('vrtgef403sht_chg01', 1)
    sprite('vrtgef403sht_chg00', 1)
    sprite('vrtgef403sht_chg01', 1)
    CreateObject('tgef403chgptc', -1)
    sprite('vrtgef403sht_chg00', 1)
    SetScaleSpeed(20)
    Size(1200)
    sprite('vrtgef403sht_chg01', 1)
    sprite('vrtgef403sht_chg00', 1)
    CreateObject('tgef403chgptc', -1)
    sprite('vrtgef403sht_chg01', 1)
    sprite('vrtgef403sht_chg00', 1)
    sprite('vrtgef403sht_chg01', 1)
    CreateObject('tgef403chgptc', -1)


@State
def ShotMagicCircle():
    sprite('null', 1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef_tg403mc', 1)


@State
def ShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(80)
        AttackP2(82)
        SameMoveProration(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(90000)
        AirPushbackY(30000)
        AirUntechableTime(80)
        Wallbounce(1)
        WallbounceReboundTime(35)
        Hitstop(0)
        EnemyHitstopAddition(16, 18, 18)
        ProjectileLevel(2)
        AddMagnetism(480)
        BlendMode_Add()
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)

        def upon_32():
            AddMagnetism(1200)
    label(0)
    sprite('vrtgef403es_00', 2)
    physicsXImpulse(70000)
    Size(1000)
    SetScaleSpeed(-100)
    PerAngleSpeed(90000)
    CreateObject('shot_plas', -1)
    sprite('vrtgef403es_01', 2)
    Size(1000)
    SetScaleSpeed(-100)
    CreateObject('shot_plas', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(2000)
    CallCustomizableParticle('tgef430_break', -1)


@State
def AntiAirShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(80)
        AttackP2(82)
        SameMoveProration(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(90000)
        AirPushbackY(50000)
        AirUntechableTime(80)
        Wallbounce(1)
        WallbounceReboundTime(25)
        Hitstop(0)
        EnemyHitstopAddition(16, 18, 18)
        ProjectileLevel(2)
        AddMagnetism(480)
        BlendMode_Add()
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)

        def upon_32():
            AddMagnetism(1200)
    label(0)
    sprite('vrtgef403es_00', 2)
    physicsXImpulse(55000)
    physicsYImpulse(22000)
    Size(1000)
    SetScaleSpeed(-100)
    PerAngleSpeed(90000)
    CreateObject('shot_plas', -1)
    sprite('vrtgef403es_01', 2)
    Size(1000)
    SetScaleSpeed(-100)
    CreateObject('shot_plas', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(2000)
    CallCustomizableParticle('tgef430_break', -1)


@State
def tgef_tg403pla():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef_tg403pla_00', -1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef_tg403pla_01', -1)


@State
def shot_plas():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef403_sht00', -1)
    ParticleColorFromPalette(160, 170, 175)
    CallCustomizableParticle('tgef403_sht01', -1)


@State
def GroundShake430():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(239, 239, 239)
    ParticleSize(2000)
    CallCustomizableParticle('tgef_430a00', -1)
    ParticleColorFromPalette(239, 239, 239)
    ParticleSize(2000)
    CallCustomizableParticle('tgef_430a01', -1)
    ParticleColorFromPalette(232, 216, 212)
    ParticleSize(2000)
    CallCustomizableParticle('tgef_430a02', -1)
    ParticleColorFromPalette(232, 216, 212)
    ParticleSize(2000)
    CallCustomizableParticle('tgef_430a', -1)


@State
def tgef_430_light():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(224, 230, 239)
    CallCustomizableParticle('tgef_430_light', -1)


@State
def tgef_DD_MH_finish():
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(207, 223, 239)
    CallCustomizableParticle('tgef_DD_MH_finish', -1)


@State
def StayMagneticA():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(1000)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    ParticleColorFromPalette(232, 216, 212)
    ParticleSize(1000)
    CallCustomizableParticle('tgef_staymagA', -1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticA_nl():

    def upon_IMMEDIATE():
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(1000)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    ParticleColorFromPalette(232, 216, 212)
    ParticleSize(1000)
    CallCustomizableParticle('tgef_staymagA', -1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticA400():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(800)
    SetScaleSpeed(50)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticA402():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(2000)
    SetScaleSpeed(10)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticA404():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(800)
    SetScaleSpeed(100)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticA432():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(1000)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticA430b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(1500)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)


@State
def StayMagneticA431():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmga00', 1)
    Size(2000)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmga03', 1)


@State
def StayMagneticB():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmgb00', 1)
    Size(1000)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)


@State
def StayMagneticB203():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
    sprite('vrtgef_stmgb00', 1)
    Size(1500)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)
    sprite('null', 1)


@State
def StayMagneticB233():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
    sprite('vrtgef_stmgb00', 1)
    Size(1500)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)
    sprite('null', 1)


@State
def StayMagneticB253():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Add()
    sprite('vrtgef_stmgb00', 1)
    Size(1500)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb00', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb01', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb02', 1)
    sprite('null', 1)
    sprite('vrtgef_stmgb03', 1)
    sprite('null', 1)


@State
def tgef210_ShotDelete():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('vrtgef210atk_00', 3)
    BlendMode_Add()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    sprite('vrtgef210atk_01', 3)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    sprite('vrtgef210atk_02', 2)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    sprite('vrtgef210atk_03', 2)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    CreateObject('StayMagneticA_nl', 3)
    sprite('vrtgef210atk_04', 2)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    CreateObject('StayMagneticA_nl', 3)
    CreateObject('StayMagneticA_nl', 4)
    CreateObject('StayMagneticA_nl', 5)
    AlphaValue(255)
    sprite('vrtgef210atk_05', 2)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    CreateObject('StayMagneticA_nl', 3)
    CreateObject('StayMagneticA_nl', 4)
    CreateObject('StayMagneticA_nl', 5)
    sprite('vrtgef210atk_06', 3)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    ConstantAlphaModifier(-30)
    sprite('vrtgef210atk_07', 3)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)
    sprite('vrtgef210atk_08', 3)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)


@State
def tgef210_ShotDeleteex1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('vrtgef210atk_00', 2)
    BlendMode_Add()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)


@State
def tgef210_ShotDeleteex2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('vrtgef210atk_00', 2)
    BlendMode_Add()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    CreateObject('StayMagneticA_nl', 0)
    CreateObject('StayMagneticA_nl', 1)
    CreateObject('StayMagneticA_nl', 2)


@State
def MTH_rotate():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('vrtgef430a_02', 2)
    sprite('vrtgef430a_03', 2)
    sprite('vrtgef430a_04', 2)
    sprite('vrtgef430a_05', 2)
    sprite('vrtgef430a_06', 2)
    sprite('vrtgef430a_07', 2)


@State
def MTH_rotate_end():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('vrtgef430a_08', 3)
    sprite('vrtgef430a_09', 4)
    sprite('vrtgef430a_10', 5)


@State
def MTH_punch_down():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('vrtgef430b_00', 4)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    CreateObject('StayMagneticA', 3)
    CreateObject('StayMagneticA', 4)
    CreateObject('StayMagneticA', 5)
    CreateObject('StayMagneticA', 6)
    CreateObject('StayMagneticA', 7)
    CreateObject('StayMagneticA', 8)
    sprite('vrtgef430b_01', 4)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    CreateObject('StayMagneticA', 3)
    E0EAEffectPosition(0)
    sprite('vrtgef430b_02', 5)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    sprite('vrtgef430b_03', 2)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    sprite('vrtgef430b_04', 3)
    AddX(140000)
    sprite('vrtgef430b_05', 5)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    CreateObject('StayMagneticA', 3)
    CreateObject('StayMagneticA', 4)
    CreateObject('StayMagneticA', 5)
    sprite('vrtgef430b_06', 5)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    CreateObject('StayMagneticA', 3)
    CreateObject('StayMagneticA', 4)
    CreateObject('StayMagneticA', 5)
    CreateObject('StayMagneticA', 6)
    CreateObject('StayMagneticA', 7)
    CreateObject('StayMagneticA', 8)
    sprite('vrtgef430b_07', 5)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    CreateObject('StayMagneticA', 2)
    sprite('vrtgef430b_08', 5)
    CreateObject('StayMagneticA', 0)
    CreateObject('StayMagneticA', 1)
    sprite('vrtgef430b_09', 5)


@State
def MTH_punch_str():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        AlphaValue(255)
    sprite('vrtgef431_00', 4)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    sprite('vrtgef431_01', 4)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    sprite('vrtgef431_02', 6)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    sprite('vrtgef431_03', 3)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    sprite('vrtgef431_04', 3)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    sprite('vrtgef431_05', 3)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    sprite('vrtgef431_06', 3)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    CreateObject('StayMagneticA431', 3)
    CreateObject('StayMagneticA431', 4)
    CreateObject('StayMagneticA431', 5)
    CreateObject('StayMagneticA431', 6)
    CreateObject('StayMagneticA431', 7)
    sprite('vrtgef431_07', 3)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    CreateObject('StayMagneticA431', 3)
    CreateObject('StayMagneticA431', 4)
    CreateObject('StayMagneticA431', 5)
    CreateObject('StayMagneticA431', 6)
    CreateObject('StayMagneticA431', 7)
    sprite('vrtgef431_08', 5)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    CreateObject('StayMagneticA431', 3)
    CreateObject('StayMagneticA431', 4)
    CreateObject('StayMagneticA431', 5)
    sprite('vrtgef431_09', 5)
    CreateObject('StayMagneticA431', 0)
    CreateObject('StayMagneticA431', 1)
    CreateObject('StayMagneticA431', 2)
    CreateObject('StayMagneticA431', 3)
    CreateObject('StayMagneticA431', 4)
    ConstantAlphaModifier(-20)
    sprite('vrtgef431_10', 5)
    CreateObject('StayMagneticA431', 0)


@State
def RollingAttackEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetScaleX(1000)
        SetScaleY(1500)
    sprite('null', 2)
    Visibility(1)
    CreateParticle('tgef_side_shockA', 0)
    sprite('vrtgef401_00', 2)
    BlendMode_Add()
    Visibility(0)
    AddX(30000)
    AddY(30000)
    sprite('vrtgef401_01', 2)
    sprite('vrtgef401_02', 2)
    ConstantAlphaModifier(-30)
    sprite('vrtgef401_03', 2)
    E0EAEffectPosition(0)
    sprite('vrtgef401_04', 2)
    sprite('vrtgef401_05', 2)


@State
def RollAtkShotBreak():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(232, 216, 212)
    ParticleSize(2000)
    CallCustomizableParticle('tgef430_break', -1)


@State
def SledgeHammerEFF():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        Size(1200)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('vrtgef402atk_00', 1)
    AddY(50000)
    AddX(50000)
    AlphaValue(128)
    sprite('vrtgef402atk_00', 1)
    AlphaValue(255)
    AddX(50000)
    sprite('vrtgef402atk_01', 1)
    ConstantAlphaModifier(-20)
    physicsYImpulse(-10000)
    AddY(-340000)
    SetScaleSpeed(-20)
    CreateObject('StayMagneticA402', 0)
    CreateObject('StayMagneticA402', 1)
    CreateObject('StayMagneticA402', 2)
    CreateObject('StayMagneticA402', 3)
    CreateObject('StayMagneticA402', 4)
    sprite('vrtgef402atk_02', 20)
    sprite('null', 12)
    Visibility(1)


@State
def ShockB402():
    sprite('null', 1)
    Visibility(1)
    CreateParticle('tgef_430ring', -1)


@State
def AntiAirDmyMagnet():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    sprite('null', 10000)
    Visibility(1)
    MagnetismLevel(0, 3000)


@State
def AntiAirDmyMagnet2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    sprite('null', 10000)
    Visibility(1)
    MagnetismLevel(0, 2500)


@State
def tgefGETBexpl():
    sprite('null', 1)
    Visibility(1)
    ParticleSize(20000)
    CallCustomizableParticle('tgef_explC2', -1)


@State
def GETB_Crash():
    sprite('null', 85)
    BlendMode_Normal()
    Visibility(1)
    Eff3DEffect('eftg_gr_crash.DIG', 'eftg_gr_crash_motion_000.mmot')


@State
def GETB_Fall():
    sprite('null', 80)
    BlendMode_Add()
    Eff3DEffect('eftg_getb.DIG', 'eftg_getb_motion_000.mmot')
    E0EAEffectPosition(3)


@State
def tgef_appA():
    sprite('null', 1)
    ParticleColorFromPalette(215, 220, 225)
    CallCustomizableParticle('tgef_appA', 0)


@State
def tgef_appB():
    sprite('null', 1)
    ParticleColorFromPalette(150, 160, 170)
    CallCustomizableParticle('tgef_appB', 0)


@State
def tgef_guardcrash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 1)
    ParticleColorFromPalette(208, 208, 208)
    CallCustomizableParticle('tgef_guardcrash00', 0)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('tgef_guardcrash02', 0)
    ParticleColorFromPalette(239, 239, 239)
    CallCustomizableParticle('tgef_guardcrash', 0)


@State
def tgef_guardcrash_stump():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 1)
    ParticleColorFromPalette(208, 208, 208)
    CallCustomizableParticle('tgef_guardcrash_stamp00', 0)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('tgef_guardcrash_stamp02', 0)
    ParticleColorFromPalette(233, 233, 233)
    CallCustomizableParticle('tgef_guardcrash_stamp', 0)


@State
def tgef_guardcrash_stump_b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 1)
    ParticleColorFromPalette(233, 233, 233)
    CallCustomizableParticle('tgef_guardcrash_stamp_b', 0)


@State
def tgef_overdrive_bigen():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 1)
    ParticleColorFromPalette(208, 208, 208)
    CallCustomizableParticle('tgef_overdrive_bigen00', -1)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('tgef_overdrive_bigen02', -1)
    ParticleColorFromPalette(233, 233, 233)
    CallCustomizableParticle('tgef_overdrive_bigen', -1)


@State
def tgef_overdrive_loop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 60)
    ParticleColorFromPalette(208, 208, 208)
    CallPrivateEffect('tgef_overdrive_loop00')


@State
def tgef_overdrive_loop2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 60)
    ParticleColorFromPalette(224, 224, 224)
    CallPrivateEffect('tgef_overdrive_loop02')


@State
def tgef_overdrive_loop3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 60)
    ParticleColorFromPalette(233, 233, 233)
    CallPrivateEffect('tgef_overdrive_loop')


@State
def tgef_overdrive():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 1)
    ParticleColorFromPalette(208, 208, 208)
    CallCustomizableParticle('tgef_overdrive00', -1)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('tgef_overdrive02', -1)
    ParticleColorFromPalette(233, 233, 233)
    CallCustomizableParticle('tgef_overdrive', -1)


@State
def tgef_overdrive_thunder():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 1)
    ParticleColorFromPalette(208, 208, 208)
    CallCustomizableParticle('tgef_overdrive_thunder', -1)
    ParticleColorFromPalette(224, 224, 224)
    CallCustomizableParticle('tgef_overdrive_thunder', -1)


@State
def tgef_overdrive_eye():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)
    LinkParticle('tgef_overdrive_eye')


@State
def tgef_overdrive_eye_keep():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)
    LinkParticle('tgef_overdrive_eye_keep')


@State
def tgef_overdrive_eyeflash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)
    LinkParticle('tgef_overdrive_eyeflash')


@State
def TG_AST_A():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        Visibility(1)
        Eff3DEffect('tg_AH_A.DIG', 'tg_AH_A_mt_000.mmot')
        AddY(256000)
    sprite('null', 80)


@State
def TG_AST_B():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Normal()
        Eff3DEffect('tg_AH_B.DIG', 'tg_AH_B_mt_000.mmot')
    sprite('null', 80)
    Size(600)
    SetScaleXPerFrame(50)
    SetScaleSpeedY(5)


@State
def TG_AST_C():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        E0EAEffectScale(3)
        BlendMode_Normal()
        AlphaValue(0)
        Eff3DEffect('tg_AH_C.DIG', 'tg_AH_C_mt_000.mmot')
    sprite('null', 30)
    ConstantAlphaModifier(8)
    sprite('null', 150)
    ConstantAlphaModifier(0)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def TG_AST_D():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('tg_AH_D.DIG', 'tg_AH_D_mt_000.mmot')
        BlendMode_Add()
        AlphaValue(200)
    sprite('null', 250)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def TG_AST_E():

    def upon_IMMEDIATE():
        BlendMode_Add()
        AlphaValue(255)
        Size(800)
        AbsoluteY(-41200000)
        Eff3DEffect('tg_AH_E.DIG', 'tg_AH_E_mt_000.mmot')
    sprite('null', 60)


@State
def TG_AST_F():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        AlphaValue(255)
        Size(1000)
        Eff3DEffect('tg_AH_F.DIG', 'tg_AH_F_mt_000.mmot')
        IgnoreScreenfreeze(1)
    sprite('null', 60)


@State
def TG_AST_G():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        Eff3DEffect('tg_AH_G.DIG', 'tg_AH_G_mt_000.mmot')
        BlendMode_Normal()
        AlphaValue(255)
        Size(1000)
        IgnoreScreenfreeze(1)
    sprite('null', 120)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-3)


@State
def TG_AST_H():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(255)
        Size(200)
        SetScaleSpeed(10)
        AbsoluteY(-256000)
        physicsYImpulse(1000)
        Eff3DEffect('tg_AH_H.DIG', 'tg_AH_H_mt_000.mmot')
    sprite('null', 60)


@State
def TG_AST_I():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(240)
        Size(1000)
        AbsoluteY(-256000)
        Eff3DEffect('tg_AH_I.DIG', 'tg_AH_I_mt_000.mmot')
    sprite('null', 32767)


@State
def LookAtPos():

    def upon_IMMEDIATE():
        AddX(0)
        AbsoluteY(0)
    sprite('null', 32767)
    CameraControlEnable(1)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)


@State
def AstWhiteOut():

    def upon_IMMEDIATE():
        RenderLayer(4)
        BlendMode_Add()
        AlphaValue(0)
        AddY(-2048000)
        Size(100000000)
        SetScaleX(20000)
    sprite('vr_white', 200)
    ConstantAlphaModifier(3)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-9)


@State
def AstLight():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tgef_astlight')
    sprite('null', 32767)


@State
def AstBackLight():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('tgef_astairaura')
    sprite('null', 32767)


@State
def AstJumpExpl():
    sprite('null', 1)
    ParticleSize(2000)
    CallCustomizableParticle('tgef_astexpl', -1)
    sprite('null', 1)
    E0EAEffectPosition(2)
    ParticleSize(3000)
    CallCustomizableParticle('tgef_astexpl', -1)
    sprite('null', 1)
    ParticleSize(3000)
    CallCustomizableParticle('tgef_astexpl', -1)
    sprite('null', 1)
    ParticleSize(3000)
    CallCustomizableParticle('tgef_astexpl', -1)
    sprite('null', 1)
    ParticleSize(3000)
    CallCustomizableParticle('tgef_astexpl', -1)


@State
def OiuchiBallEffect():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)

        def upon_EVERY_FRAME():
            MoveToCollision(3, 2, 0)
        uponSendToLabel(32, 1)
        Visibility(1)
    sprite('vrtgef406', 2)
    ParticleColorFromPalette(232, 223, 208)
    CallCustomizableParticle('tgef_oiuchilock', 106)
    label(0)
    sprite('vrtgef406', 1)
    ParticleColorFromPalette(232, 223, 208)
    CallCustomizableParticle('tgef_oiuchi', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(232, 223, 208)
    ParticleSize(2000)
    CallCustomizableParticle('tgef430_break', -1)


@State
def RLAstMagnetic():

    def upon_IMMEDIATE():
        Visibility(1)
        LinkParticle('tgef_RlAstmagnetic')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def AntiAirShotObj_Event():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        BlendMode_Add()
        CollideWithWall(1)
        uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 1)
        Hitstop(0)
        AttackLevel_(4)
        Damage(1100)
        AttackP1(65)
        AttackP2(80)
        Wallbounce(1)
        WallbounceReboundTime(35)
        CHWallbounceReboundTime(35)
        AirPushbackX(90000)
        AirPushbackY(30000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(80)
        GuardCrush(1, 1)
        AddMagnetism(360)
        EnemyHitstopAddition(18, 18, 18)
        ProjectileLevel(2)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    label(0)
    sprite('vrtgef403es_00', 2)
    physicsXImpulse(55000)
    physicsYImpulse(22000)
    Size(1000)
    SetScaleSpeed(-100)
    PerAngleSpeed(90000)
    CreateObject('shot_plas', -1)
    sprite('vrtgef403es_01', 2)
    Size(1000)
    SetScaleSpeed(-100)
    CreateObject('shot_plas', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    Visibility(1)
    ParticleColorFromPalette(160, 170, 175)
    ParticleSize(2000)
    CallCustomizableParticle('tgef430_break', -1)


@State
def NOISE():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_eventnoise.DIG', '')
        FaceSpawnLocation()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 60)
    loopRest()


@State
def NOISE_Long():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_eventnoise.DIG', '')
        FaceSpawnLocation()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 300)
    loopRest()


@State
def OdFallEff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        Size(600)
        AlphaValue(0)
        RotationAngle(180000)
        AddY(300000)
        Eff3DEffect('tg_AH_A.DIG', 'tg_AH_A_mt_000.mmot')
    sprite('null', 30)
    ConstantAlphaModifier(26)
    sprite('null', 60)
    ConstantAlphaModifier(0)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def OdFallThunder():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        RenderLayer(1)
        AddY(-200000)
    sprite('vrtgef432_00', 15)
    sprite('vrtgef432_01', 7)
    sprite('vrtgef432_02', 5)
    Size(1000)
    sprite('vrtgef432_03', 5)
    CreateObject('OdFallThunder_nigi00', -1)
    CreateObject('OdFallThunder_nigi01', -1)
    CreateObject('OdFallThunder_nigi02', -1)
    CreateObject('OdFallThunder_nigi03', -1)
    CreateObject('OdFallThunder_nigi03', -1)
    sprite('vrtgef432_04', 5)
    CreateObject('OdFallThunder2', -1)
    sprite('vrtgef432_05', 5)
    sprite('null', 21)


@State
def OdFallThunder2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(3)
        AddY(300000)
    sprite('null', 30)
    CreateParticle('tgef_odgetbfinish_02', -1)


@State
def OdFallThunder_nigi00():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        E0EAEffectPosition(2)
        RenderLayer(1)
        Size(500)
        AddY(150000)
        AddX(-600000)
    sprite('vrtgef432_06', 3)
    sprite('vrtgef432_07', 3)
    sprite('vrtgef432_08', 3)
    sprite('vrtgef432_09', 3)
    sprite('vrtgef432_10', 3)
    sprite('vrtgef432_11', 3)
    sprite('vrtgef432_12', 3)


@State
def OdFallThunder_nigi01():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        E0EAEffectPosition(2)
        RenderLayer(1)
        SetScaleX(-500)
        SetScaleY(-500)
        AddY(780000)
        AddX(400000)
    sprite('vrtgef432_06', 3)
    sprite('vrtgef432_07', 3)
    sprite('vrtgef432_08', 3)
    sprite('vrtgef432_09', 3)
    sprite('vrtgef432_10', 3)
    sprite('vrtgef432_11', 3)
    sprite('vrtgef432_12', 3)


@State
def OdFallThunder_nigi02():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        E0EAEffectPosition(2)
        RenderLayer(1)
        SetScaleX(500)
        SetScaleY(-500)
        AddY(780000)
        AddX(-400000)
    sprite('vrtgef432_06', 3)
    sprite('vrtgef432_07', 3)
    sprite('vrtgef432_08', 3)
    sprite('vrtgef432_09', 3)
    sprite('vrtgef432_10', 3)
    sprite('vrtgef432_11', 3)
    sprite('vrtgef432_12', 3)


@State
def OdFallThunder_nigi03():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        E0EAEffectPosition(2)
        RenderLayer(1)
        SetScaleX(-500)
        AddY(150000)
        AddX(600000)
    sprite('vrtgef432_06', 3)
    sprite('vrtgef432_07', 3)
    sprite('vrtgef432_08', 3)
    sprite('vrtgef432_09', 3)
    sprite('vrtgef432_10', 3)
    sprite('vrtgef432_11', 3)
    sprite('vrtgef432_12', 3)


@State
def OdHandThunder():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        uponSendToLabel(32, 1)
        PaletteIndex(0)
        ColorFromPaletteIndex(230)
        Eff3DEffect('tg_432handthunder', 'tg_432handthunder')
        FaceSpawnLocation()
    label(0)
    sprite('null', 5)
    Size(1000)
    sprite('null', 5)
    Size(650)
    gotoLabel(0)
    label(1)
    sprite('null', 1)


@State
def KK_lose():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        SetZVal(500)
    sprite('tg920_00', 3)
    sprite('tg920_01', 3)
    sprite('tg920_02', 3)
    sprite('tg920_03', 3)
    sprite('tg920_04', 3)
    sprite('tg920_05', 3)
    sprite('tg920_06', 3)
    sprite('tg920_07', 3)
    sprite('tg920_08', 3)
    loopRest()


@State
def BurstSippaiEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        RenderLayer(1)
        AddX(-75000)
    sprite('vrtgef440_06', 2)
    ParticleLayer(3)
    CallCustomizableParticle('tgef_430coresub', -1)
    ParticleSize(650)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunder', -1)
    sprite('vrtgef440_07', 2)
    sprite('vrtgef440_08', 2)
    sprite('vrtgef440_09', 2)


@State
def BurstHodenEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        AddY(225000)
        AddX(150000)
        RandAddScale(0, 800)
        RandAddRotation(-100000, 100000)
        RenderLayer(1)
    sprite('vrtgef440_06', 2)
    ParticleLayer(3)
    CallCustomizableParticle('tgef_430coresub', -1)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunder', -1)
    CreateObject('BurstHodenEffSub', -1)
    sprite('vrtgef440_07', 2)
    CreateObject('BurstHodenEffSub2', -1)
    sprite('vrtgef440_08', 2)
    CreateObject('BurstHodenEffSub3', -1)
    sprite('vrtgef440_09', 2)
    CreateObject('BurstHodenEffSub4', -1)


@State
def BurstHodenEffSub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        Size(1500)
        RandAddScale(0, 800)
        RandAddRotation(20000, 90000)
        ParticleColorFromPalette(223, 207, 191)
        ParticleLayer(11)
        CallPrivateEffect('tgef_440bloom')
    sprite('vrtgef440_10', 1)
    sprite('vrtgef440_11', 1)
    sprite('vrtgef440_12', 1)
    sprite('vrtgef440_13', 1)


@State
def BurstHodenEffSub2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        Size(1500)
        RandAddScale(0, 800)
        RandAddRotation(-90000, -20000)
        ParticleColorFromPalette(223, 207, 191)
        ParticleLayer(11)
        CallPrivateEffect('tgef_440bloom')
    sprite('vrtgef440_10', 1)
    sprite('vrtgef440_11', 1)
    sprite('vrtgef440_12', 1)
    sprite('vrtgef440_13', 1)


@State
def BurstHodenEffSub3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        Size(1200)
        RandAddScale(0, 800)
        RandAddRotation(95000, 160000)
        ParticleColorFromPalette(223, 207, 191)
        ParticleLayer(11)
        CallPrivateEffect('tgef_440bloom')
    sprite('vrtgef440_10', 1)
    sprite('vrtgef440_11', 1)
    sprite('vrtgef440_12', 1)
    sprite('vrtgef440_13', 1)


@State
def BurstHodenEffSub4():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        Size(1200)
        RandAddScale(0, 800)
        RandAddRotation(-160000, -95000)
        ParticleColorFromPalette(223, 207, 191)
        ParticleLayer(11)
        CallPrivateEffect('tgef_440bloom')
    sprite('vrtgef440_10', 1)
    sprite('vrtgef440_11', 1)
    sprite('vrtgef440_12', 1)
    sprite('vrtgef440_13', 1)


@State
def BurstHodenEndLoop():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(0)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 8)
    CreateObject('BurstHodenEnd', -1)
    gotoLabel(0)


@State
def BurstHodenEndStop():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('vrtgef440arm_00', 3)
    CreateObject('BurstHodenEndStopB', 0)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 0)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 1)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 2)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 3)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 4)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 5)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 6)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 7)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 8)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 9)
    sprite('vrtgef440arm_01', 3)
    IgnorePauses(2)
    sprite('null', 2)
    sprite('vrtgef440arm_02', 3)
    sprite('null', 2)
    sprite('vrtgef440arm_03', 3)
    sprite('null', 2)
    sprite('vrtgef440arm_04', 3)
    CreateObject('BurstHodenEffSub2', 0)
    CreateObject('BurstHodenEffSub4', 1)
    CreateObject('BurstHodenEffSub', 2)

    def RunOnObject_1():
        Size(800)
    CreateObject('BurstHodenEffSub3', 3)

    def RunOnObject_1():
        Size(800)


@State
def BurstHodenEndStopB():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(0)
    sprite('vrtgef440heart_00', 3)
    sprite('vrtgef440heart_01', 3)
    IgnorePauses(2)
    sprite('vrtgef440heart_02', 3)
    AddScale(100)
    sprite('vrtgef440heart_03', 3)
    AddScale(100)


@State
def BurstHodenBodyRay():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Visibility(1)
    label(0)
    sprite('vrtgef440arm_00', 7)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 0)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 1)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 2)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 3)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 4)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 5)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 6)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 7)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 8)
    ParticleColorFromPalette(223, 207, 191)
    ParticleLayer(11)
    CallCustomizableParticle('tgef_430thunderbody_core', 9)
    gotoLabel(0)


@State
def BurstDDSmokeA():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('tg_440smoke00', '')
        AlphaValue(200)
    sprite('null', 10)
    CreateObject('BurstDDSmokeB', -1)
    sprite('null', 10)
    CreateObject('BurstDDSmokeB', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def BurstDDSmokeB():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('tg_440smoke01', '')
        AlphaValue(200)
    sprite('null', 24)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def BurstDDthunderdome():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('tg_440thunderdome00', '')
        IgnorePauses(2)
        Size(1100)
        PaletteIndex(0)
        ColorFromPaletteIndex(239)
        AddX(-25000)
    sprite('null', 3)
    CreateObject('BurstDDthunderdomeB', -1)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 3)
    AlphaValue(255)
    AddScale(50)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 1)
    AlphaValue(255)
    AddScale(50)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 1)
    AlphaValue(255)
    AddScale(50)


@State
def BurstDDthunderdomeB():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('tg_440thunderdome00b', '')
        IgnorePauses(2)
        E0EAEffectScale(2)
        PaletteIndex(0)
        ColorFromPaletteIndex(207)
    sprite('null', 3)
    sprite('null', 2)
    AlphaValue(128)
    sprite('null', 3)
    AlphaValue(255)
    sprite('null', 2)
    AlphaValue(128)
    sprite('null', 1)
    AlphaValue(255)
    sprite('null', 1)
    AlphaValue(128)
    sprite('null', 1)
    AlphaValue(255)


@State
def tgef_412_throw():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Flip()
    sprite('null', 2)
    CreateParticle('tgef_412throw2', -1)
    CreateParticle('tgef_412throw', -1)
    sprite('null', 2)
    CreateParticle('tgef_412throw', -1)
    sprite('null', 2)
    CreateParticle('tgef_412throw', -1)
    sprite('null', 2)
    CreateParticle('tgef_412throw', -1)
    sprite('null', 2)
    CreateParticle('tgef_412throw', -1)
    sprite('null', 2)
    CreateParticle('tgef_412throw', -1)
    sprite('null', 2)
    CreateParticle('tgef_412throw', -1)


@State
def tgef_412_throw_add():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add', -1)


@State
def tgef_412_throw_add_bg():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(100)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add2', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add2', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add2', -1)
    sprite('null', 1)
    CreateParticle('tgef_412throw_add2', -1)


@State
def EventBL():

    def upon_IMMEDIATE():
        LoadSpritePalette(7)
        uponSendToLabel(32, 10)
        XPositionRelativeFacing(-220000)
    label(0)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('bl033_00', 1)
    sprite('bl033_00', 2)
    physicsXImpulse(-30000)
    physicsYImpulse(38300)
    setGravity(1550)
    JumpEffects(3, 100)
    sprite('bl033_01', 2)
    sprite('bl033_02', 2)
    sprite('bl033_01', 2)
    setInvincible(0)
    sprite('bl033_02', 2)
    loopRest()

    def upon_LANDING():
        sendToLabel(12)
    label(11)
    sprite('bl033_01', 2)
    sprite('bl033_02', 2)
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('bl033_03', 2)
    physicsXImpulse(0)
    sprite('bl033_04', 2)
    sprite('bl033_05', 2)
    sprite('bl033_06', 2)
    sprite('bl033_07', 2)


@State
def EventBL2():

    def upon_IMMEDIATE():
        LoadSpritePalette(7)
        XPositionRelativeFacing(-260000)
    label(0)
    sprite('bl000_00', 6)
    sprite('bl000_01', 6)
    sprite('bl000_02', 6)
    sprite('bl000_03', 6)
    sprite('bl000_04', 6)
    sprite('bl000_05', 6)
    sprite('bl000_06', 6)
    sprite('bl000_07', 6)
    loopRest()
    gotoLabel(0)


@State
def Act2EventCamera_tgvsha():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        uponSendToLabel(32, 0)
        AddX(400000)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    TeleportToObject(2)
