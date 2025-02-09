@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        RenderLayer(5)
        Eff3DEffect('ef_emb_hb.DIG', '')
        AddY(265000)
        Size(1450)
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
def EMB_HB_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_hb.DIG', '')
        RenderLayer(5)
        AddY(265000)
        Size(1450)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 80)

@State
def EMB_HB_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_hb.DIG', '')
        RenderLayer(5)
        AddY(265000)
        Size(1450)
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
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        FaceSpawnLocation()
        ColorFromPaletteIndex(224)
        IgnoreScreenfreeze(1)
    sprite('null', 74)

@State
def hbef_test():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('hbef_test', '')
        FaceSpawnLocation()
        BlendMode_Normal()
    sprite('null', 120)

@State
def hbef_Drive():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 0)
    sprite('null', 6)
    CallPrivateEffect('hbef_Drive')
    PrivateSE('hbse_00')
    label(0)
    sprite('null', 30)
    E0EAEffectPosition(0)

@State
def hbef_D_feather():

    def upon_IMMEDIATE():
        AddX(-40000)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('hbef_D_feather', 100)

@State
def hbef_2D_feather():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('hbef_2D_feather', 100)

@State
def hbef_Air2D_feather():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('hbef_405feather', 100)

@State
def hbef_crow():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddY(190000)
    sprite('null', 4)
    LinkParticle('hbef_BunshinDelete')
    CreateObject('hbef_BunshinSmoke', 100)
    sprite('null', 6)
    E0EAEffectPosition(0)
    sprite('null', 60)

@State
def hbef_BunshinSmoke():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('hbef_bunsin', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        ConstantAlphaModifier(-10)
        Size(500)
        SetScaleSpeed(10)
    sprite('null', 120)

@Subroutine
def Bunshin_Black():
    ColorTransition(0, 10)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    AfterimageInterval(0)
    AfterimageCount(5)
    EnableAfterimagePulse(1)

@Subroutine
def Bunshin_Alpha():
    ConstantAlphaModifier(-17)

@Subroutine
def Bunshin_Zanzou():
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageColor_1(127, 255, 255, 255)
    AfterimageMask_2(0, 0, 63, 191)
    AfterimageCount(4)
    AfterimageInterval(1)

@State
def hbef_201_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef201_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 3)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)
    sprite('null', 5)
    sprite('null', 8)
    ConstantAlphaModifier(-32)

@State
def hbef_201_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vr_hb201_10', 4)
    sprite('vr_hb201_11', 30)

@State
def hbef_202_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef202_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(150000)
    sprite('null', 16)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)
    ConstantAlphaModifier(-16)

@State
def hbef_203_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef203_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(192000)
        AddX(-192000)
    sprite('null', 5)
    ConstantRedModifier(-25)
    ConstantGreenModifier(-25)
    sprite('null', 5)

@State
def hbef_210_slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(200)
        AddY(32000)
    sprite('vr_hb210_00', 2)
    CreateObject('hbef_210_lead', 100)
    sprite('vr_hb210_01', 3)

@State
def hbef_210_lead():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
    sprite('vr_hb210_10', 9)
    CreateParticle('hbef_210stuck', 0)
    sprite('vr_hb210_10', 15)
    ConstantAlphaModifier(-16)

@State
def hbef_211_slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(200)
        AddX(-70000)
    sprite('vr_hb211_00', 3)
    sprite('vr_hb211_01', 6)
    ConstantAlphaModifier(-20)

@State
def hbef_211_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef211_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 8)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)
    sprite('null', 8)
    ConstantAlphaModifier(-32)

@State
def hbef_212_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(100)
        AlphaValue(245)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(1)
        CustomPalette(-200)
    sprite('vr_hb212_00', 120)

@State
def hbef_212_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef212_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddX(180000)
        AddY(32000)
    sprite('null', 10)
    ConstantRedModifier(-25)
    ConstantGreenModifier(-25)

@State
def hbef_213_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef213_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(256000)
    sprite('null', 10)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)

@State
def hbef_213_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef213_slash2', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(242000)
    sprite('null', 10)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)

@State
def hbef_213_slash3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef213_slash3', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(242000)
    sprite('null', 10)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)

@State
def hbef_231_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef231_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 8)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)
    sprite('null', 8)
    ConstantAlphaModifier(-32)

@State
def hbef_231_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vr_hb231_10', 3)
    SetZVal(100)
    sprite('vr_hb231_11', 30)
    SetZVal(-100)

@State
def hbef_232_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef232_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 10)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)

@State
def hbef_234_slash():

    def upon_IMMEDIATE():
        Flip()
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef234_slash', '')
        BlendMode_Add()
    sprite('null', 9)
    ConstantRedModifier(-28)
    ConstantGreenModifier(-28)

@State
def hbef_234_shadow():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 15)
    LinkParticle('hbef_234shadow')
    sprite('null', 15)
    ConstantAlphaModifier(-17)

@State
def hbef_234_shadow_b():

    def upon_IMMEDIATE():
        Unknown4022(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    CreateParticle('hbef_234shadow_b', 100)

@State
def hbef_251_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef251_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 7)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)

@State
def hbef_251_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(200)
    sprite('vr_hb251_10', 2)
    sprite('vr_hb251_11', 4)

@State
def hbef_252_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef252_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(120000)
        IgnorePauses(2)
    sprite('null', 1)
    ConstantRedModifier(-15)
    ConstantGreenModifier(-15)
    sprite('null', 9)
    sprite('null', 7)
    ConstantAlphaModifier(-36)

@State
def hbef_253_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef253_slash', '')
        BlendMode_Add()
        AddY(192000)
    sprite('null', 3)
    ConstantRedModifier(-16)
    ConstantGreenModifier(-16)
    sprite('null', 5)

@State
def hbef_254_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef254_slash', '')
        BlendMode_Add()
    sprite('null', 9)
    ConstantRedModifier(-28)
    ConstantGreenModifier(-28)

@Subroutine
def Drive_Bunshin_Init():
    AttackLevel_(3)
    Damage(900)
    AttackP1(80)
    StarterRating(2)
    WallCollisionDetection(1)
    FloorCollision(1)
    EnableCollision(1)
    UseSlashHitspark(1)
    AutoHitStopSending(1)
    IgnorePauses(3)

    def upon_44():
        IgnorePauses(0)
    HitsPerCall(1, 0, 0, 1, 0, 1, 1, 1)
    sendToLabelUpon(54, 9)
    Unknown23091(1)
    DespawnEAEffect('hbef_crow')
    RunLoopUpon(17, 120)
    sendToLabelUpon(17, 9)

@Subroutine
def Drive_Bunshin_Break():
    clearUponHandler(54)
    clearUponHandler(32)
    XImpulseAcceleration(5)
    YAccel(5)
    setGravity(0)
    AlphaValue(255)
    NoDamageAction(1)
    AttackOff()
    EnableCollision(0)
    CameraFollowTarget(0, 0)
    ObjectUpon(3, 41)

@State
def AN_NmlAtk5D_Bunshin():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        PushbackX(19800)
        AirPushbackX(10000)
        AirPushbackY(24000)
        Hitstun(24)
        AirUntechableTime(30)
        AlphaValue(0)

        def upon_FRAME_STEP():
            if SLOT_51:
                if (SLOT_19 <= 320000):
                    clearUponHandler(3)
                    sendToLabel(0)
    sprite('hb203_06', 3)
    ConstantAlphaModifier(50)
    AddX(50000)
    physicsXImpulse(50000)
    CreateObject('hbef_D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddY(192000)
    ApplyFunctionsToSelf()
    sprite('hb203_07', 3)
    SLOT_51 = 1
    sprite('hb203_06', 3)
    sprite('hb203_07', 3)
    label(0)
    sprite('hb203_08', 3)
    CommonSE('010_swing_sword_1')
    clearUponHandler(3)
    XImpulseAcceleration(80)
    sprite('hb203_09', 3)
    XImpulseAcceleration(10)
    CreateObject('hbef_203_slash', 100)
    ObjectUpon(3, 32)
    sprite('hb203_10', 3)
    sprite('hb203_11', 5)
    EndMomentum(1)
    sprite('hb203_11', 15)
    clearUponHandler(54)
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    clearUponHandler(3)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def AN_NmlAtk6D_Bunshin():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb203_03', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb203_04', 3)
    sprite('hb203_05', 3)
    label(0)
    sprite('hb203_02', 3)
    sprite('hb203_03', 3)
    sprite('hb203_04', 3)
    sprite('hb203_05', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def AN_NmlAtk2D_Bunshin():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackP1(70)
        BonusProration(110)
        GroundedHitstunAnimation(13)
        AirPushbackX(7000)
        AirPushbackY(38000)
        AirUntechableTime(48)
        YImpulseBeforeWallbounce(1600)
        AttackDirection(1)
        FatalCounter(1)
        AlphaValue(0)
    sprite('hb234_06', 2)
    EnableCollision(0)
    NoDamageAction(1)
    Visibility(1)
    sprite('hb234_06', 10)
    if (SLOT_19 < 1000000):
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(-50000)
    else:
        AddX(1000000)
        AbsoluteY(0)
    label(0)
    sprite('hb234_07', 2)
    Flip()
    EndMomentum(1)
    SetXCollisionFromOrigin(80)
    SetYCollisionFromOrigin(80)
    PushCollisionHeightLow(80000)
    EnableCollision(1)
    clearUponHandler(3)
    sendToLabelUpon(2, 1)
    sprite('hb234_13', 4)
    physicsXImpulse(3000)
    physicsYImpulse(18000)
    setGravity(2000)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    Visibility(0)
    SetXCollisionFromOrigin(100)
    CreateObject('hbef_234_shadow_b', 100)
    sprite('hb234_13', 4)
    NoDamageAction(0)
    sprite('hb234_14', 3)
    CommonSE('009_swing_rapier_1')
    sprite('hb234_15', 3)
    SetXCollisionFromOrigin(-1)
    CreateObject('hbef_234_slash', 100)
    sprite('hb234_16', 2)
    sprite('hb234_17', 2)
    sprite('hb234_18', 32767)
    label(1)
    sprite('hb234_19', 2)
    clearUponHandler(2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    EnableCollision(0)
    clearUponHandler(54)
    NoDamageAction(1)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    ApplyFunctionsToObjects(1)
    Flip()
    AddY(-100000)
    AddX(-16000)
    ApplyFunctionsToSelf()
    sprite('hb234_20', 2)
    sprite('hb234_21', 20)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    clearUponHandler(2)
    clearUponHandler(3)

@State
def AN_NmlAtk3D_Bunshin():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb234_07', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    label(0)
    sprite('hb234_06', 3)
    sprite('hb234_07', 3)
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir5D_Bunshin():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackP1(80)
        AirPushbackX(10000)
        AirPushbackY(26000)
        AirUntechableTime(36)
        Wallbounce(1)
        WallbounceReboundTime(20)
        AirHitstunAfterWallbounce(30)
        NonCornerWallbounce(1)
        AlphaValue(0)
    sprite('hb253_05', 4)
    ConstantAlphaModifier(50)
    AddX(50000)
    physicsXImpulse(40000)
    CreateObject('hbef_D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddY(192000)
    ApplyFunctionsToSelf()
    sprite('hb253_06', 3)
    sprite('hb253_07', 2)
    CommonSE('010_swing_sword_1')
    sprite('hb253_08', 3)
    CreateObject('hbef_253_slash', 100)
    XImpulseAcceleration(30)
    sprite('hb253_09', 3)
    sprite('hb253_10', 3)
    sprite('hb253_11', 3)
    sprite('hb253_12', 10)
    XImpulseAcceleration(5)
    clearUponHandler(54)
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir6D_Bunshin():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb253_02', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb253_03', 3)
    sprite('hb253_04', 3)
    label(0)
    sprite('hb253_02', 3)
    sprite('hb253_03', 3)
    sprite('hb253_04', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir2D_Bunshin():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackP1(80)
        AirPushbackY(-40000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(40)
        PushbackX(1000)
        GroundedHitstunAnimation(11)
        HardKnockdown(1)
        SetZVal(-500)
        LandingHeight(-10000)
        FloorCollision(0)

        def upon_LANDING():
            clearUponHandler(2)
            EndMomentum(1)
        AlphaValue(0)
        if (SLOT_25 < 110000):
            EnableCollision(0)
    sprite('hb254_05', 4)
    physicsXImpulse(26400)
    physicsYImpulse(-36000)
    ConstantAlphaModifier(70)
    CreateObject('hbef_Air2D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddX(60000)
    AddY(100000)
    ApplyFunctionsToSelf()
    sprite('hb254_06', 3)
    sprite('hb254_07', 2)
    CommonSE('010_swing_sword_1')
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('hb254_08', 3)
    EnableCollision(1)
    CreateObject('hbef_254_slash', 100)
    sprite('hb254_09', 3)
    sprite('hb254_10', 3)
    sprite('hb254_11', 3)
    sprite('hb254_12', 20)
    EndMomentum(1)
    clearUponHandler(54)
    EnableCollision(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    loopRest()
    ExitState()
    label(1)
    sprite('hb024_00', 3)
    EndMomentum(1)
    EnableCollision(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(3)
    sprite('hb024_01', 3)
    sprite('hb024_02', 3)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir3D_Bunshin():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        SetZVal(500)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb254_02', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb254_03', 3)
    sprite('hb254_04', 3)
    label(0)
    sprite('hb254_02', 3)
    sprite('hb254_03', 3)
    sprite('hb254_04', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtk5D_Bunshin_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackLevel_(4)
        Damage(900)
        PushbackX(19800)
        AirPushbackX(10000)
        AirPushbackY(24000)
        Hitstun(24)
        AirUntechableTime(30)
        AlphaValue(0)

        def upon_FRAME_STEP():
            if SLOT_51:
                if (SLOT_19 <= 320000):
                    clearUponHandler(3)
                    sendToLabel(0)
    sprite('hb203_06', 3)
    ConstantAlphaModifier(50)
    AddX(50000)
    physicsXImpulse(55000)
    CreateObject('hbef_D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddY(192000)
    ApplyFunctionsToSelf()
    sprite('hb203_07', 3)
    SLOT_51 = 1
    sprite('hb203_06', 3)
    sprite('hb203_07', 3)
    label(0)
    sprite('hb203_08', 2)
    CommonSE('010_swing_sword_1')
    clearUponHandler(3)
    XImpulseAcceleration(80)
    sprite('hb203_09', 3)
    XImpulseAcceleration(10)
    CreateObject('hbef_203_slash', 100)
    ObjectUpon(3, 32)
    sprite('hb203_10', 3)
    sprite('hb203_11', 5)
    EndMomentum(1)
    sprite('hb203_11', 15)
    XImpulseAcceleration(5)
    clearUponHandler(54)
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    clearUponHandler(3)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def AN_NmlAtk6D_Bunshin_OD():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb203_04', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb203_05', 3)
    sprite('hb203_02', 3)
    label(0)
    sprite('hb203_03', 3)
    sprite('hb203_04', 3)
    sprite('hb203_05', 3)
    sprite('hb203_02', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def AN_NmlAtk2D_Bunshin_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackLevel_(4)
        Damage(900)
        AttackP1(70)
        BonusProration(110)
        GroundedHitstunAnimation(13)
        AirPushbackX(7000)
        AirPushbackY(38000)
        AirUntechableTime(48)
        YImpulseBeforeWallbounce(1600)
        AttackDirection(1)
        FatalCounter(1)
        AlphaValue(0)
    sprite('hb234_06', 2)
    EnableCollision(0)
    NoDamageAction(1)
    Visibility(1)
    sprite('hb234_06', 1)
    if (SLOT_19 < 1000000):
        TeleportToObject(22)
        AbsoluteY(0)
        AddX(-50000)
    else:
        AddX(1000000)
        AbsoluteY(0)
    label(0)
    sprite('hb234_07', 2)
    Flip()
    EndMomentum(1)
    SetXCollisionFromOrigin(80)
    SetYCollisionFromOrigin(80)
    PushCollisionHeightLow(80000)
    EnableCollision(1)
    clearUponHandler(3)
    sendToLabelUpon(2, 1)
    sprite('hb234_13', 2)
    physicsXImpulse(3000)
    physicsYImpulse(18000)
    setGravity(2400)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    Visibility(0)
    SetXCollisionFromOrigin(100)
    CreateObject('hbef_234_shadow_b', 100)
    sprite('hb234_13', 2)
    NoDamageAction(0)
    sprite('hb234_14', 1)
    CommonSE('009_swing_rapier_1')
    sprite('hb234_15', 3)
    SetXCollisionFromOrigin(-1)
    CreateObject('hbef_234_slash', 100)
    sprite('hb234_16', 2)
    sprite('hb234_17', 2)
    sprite('hb234_18', 32767)
    label(1)
    sprite('hb234_19', 2)
    clearUponHandler(2)
    EndMomentum(1)
    LandingEffects(100, 1, 1)
    EnableCollision(0)
    clearUponHandler(54)
    NoDamageAction(1)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    ApplyFunctionsToObjects(1)
    Flip()
    AddY(-100000)
    AddX(-16000)
    ApplyFunctionsToSelf()
    sprite('hb234_20', 2)
    sprite('hb234_21', 20)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    clearUponHandler(2)
    clearUponHandler(3)

@State
def AN_NmlAtk3D_Bunshin_OD():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(1)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
            NoDamageAction(1)
            EnableCollision(0)
            EnableAfterimage(0)
            callSubroutine('Bunshin_Black')
            callSubroutine('Bunshin_Alpha')
            CreateObject('hbef_crow', 100)
            ApplyFunctionsToObjects(1)
            Flip()
            AddY(-65000)
            ApplyFunctionsToSelf()
    sprite('hb234_07', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    sprite('hb234_06', 3)
    sprite('hb234_07', 3)
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    sprite('hb234_06', 3)
    sprite('hb234_07', 3)
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    sprite('hb234_06', 3)
    sprite('hb234_07', 3)
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    sprite('hb234_06', 3)
    sprite('hb234_07', 3)
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    sprite('hb234_06', 3)
    sprite('hb234_07', 3)
    sprite('hb234_08', 3)
    sprite('hb234_09', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb234_06', 2)
    sprite('hb234_07', 2)
    sprite('hb234_08', 2)
    sprite('hb234_09', 2)
    sprite('hb234_06', 2)
    sprite('hb234_07', 2)
    sprite('hb234_08', 2)
    sprite('hb234_09', 2)
    sprite('hb234_10', 3)
    sprite('hb234_11', 3)
    sprite('hb234_12', 3)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir5D_Bunshin_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackLevel_(4)
        AttackP1(80)
        Damage(900)
        AirPushbackX(40000)
        AirPushbackY(26000)
        AirHitstunAnimation(12)
        AirUntechableTime(36)
        GroundedHitstunAnimation(1)
        Wallbounce(1)
        WallbounceReboundTime(20)
        AirHitstunAfterWallbounce(50)
        AlphaValue(0)
    sprite('hb253_05', 2)
    ConstantAlphaModifier(50)
    AddX(50000)
    physicsXImpulse(50000)
    CreateObject('hbef_D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddY(192000)
    ApplyFunctionsToSelf()
    sprite('hb253_06', 3)
    sprite('hb253_07', 2)
    CommonSE('010_swing_sword_1')
    sprite('hb253_08', 3)
    CreateObject('hbef_253_slash', 100)
    XImpulseAcceleration(30)
    sprite('hb253_09', 3)
    sprite('hb253_10', 3)
    sprite('hb253_11', 3)
    sprite('hb253_12', 10)
    XImpulseAcceleration(5)
    clearUponHandler(54)
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir6D_Bunshin_OD():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb253_02', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb253_03', 3)
    sprite('hb253_04', 3)
    label(0)
    sprite('hb253_02', 3)
    sprite('hb253_03', 3)
    sprite('hb253_04', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir2D_Bunshin_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        callSubroutine('Drive_Bunshin_Init')
        AttackLevel_(4)
        AttackP1(80)
        Damage(900)
        AirPushbackY(-40000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(40)
        PushbackX(1000)
        GroundedHitstunAnimation(11)
        HardKnockdown(1)
        SetZVal(-500)
        LandingHeight(-10000)
        FloorCollision(0)

        def upon_LANDING():
            clearUponHandler(2)
            EndMomentum(1)
        AlphaValue(0)
        if (SLOT_25 < 110000):
            EnableCollision(0)
    sprite('hb254_05', 4)
    physicsXImpulse(26400)
    physicsYImpulse(-36000)
    ConstantAlphaModifier(70)
    CreateObject('hbef_Air2D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddX(60000)
    AddY(100000)
    ApplyFunctionsToSelf()
    sprite('hb254_06', 3)
    sprite('hb254_07', 2)
    CommonSE('010_swing_sword_1')
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('hb254_08', 3)
    EnableCollision(1)
    CreateObject('hbef_254_slash', 100)
    sprite('hb254_09', 3)
    setGravity(1800)
    sprite('hb254_10', 3)
    sprite('hb254_11', 20)
    EndMomentum(1)
    clearUponHandler(54)
    EnableCollision(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    loopRest()
    ExitState()
    label(1)
    sprite('hb024_00', 3)
    EndMomentum(1)
    EnableCollision(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(3)
    sprite('hb024_01', 3)
    sprite('hb024_02', 3)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def AN_NmlAtkAir3D_Bunshin_OD():

    def upon_IMMEDIATE():
        callSubroutine('Drive_Bunshin_Init')
        PreventSelfPush(1)
        SetZVal(500)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)

        def upon_32():
            sendToLabel(9)
            clearUponHandler(32)
            CameraFollowTarget(0, 0)
    sprite('hb254_02', 3)
    callSubroutine('Bunshin_Zanzou')
    sprite('hb254_03', 3)
    sprite('hb254_04', 3)
    label(0)
    sprite('hb254_02', 3)
    sprite('hb254_03', 3)
    sprite('hb254_04', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def hbef_313_smoke():

    def upon_IMMEDIATE():
        AbsoluteY(500000)
        DeviationX(-64000, 64000)
    sprite('null', 1)
    CreateParticle('hbef_313smoke', 100)
    CreateObject('hbef_313_shot', 100)

@State
def hbef_313_shot():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        RenderLayer(1)
        AttackDefaults_Projectile()
        FloorCollision(1)
        AttackLevel_(1)
        Damage(200)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP2(100)
        SingleProration(1)
        MinimumDamage(100)
        AirPushbackX(6000)
        AirPushbackY(-50000)
        HardKnockdown(30)
        Hitstop(0)
        AirUntechableTime(60)
        StarterRating(2)
        SpecialCancel(0)
        AttackDirection(3)
        UseSlashHitspark(1)
        IgnoreBurst(1)
        sendToLabelUpon(12, 0)
    sprite('vr_hb313_00', 20)
    physicsYImpulse(-64000)
    LinkParticle('hbef_313shot')
    label(0)
    sprite('keep', 1)
    EndMomentum(1)
    clearUponHandler(10)
    EndAttack()

@State
def __313_AttackEffect():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        DeviationX(-128000, 128000)
        DeviationY(0, 128000)
    sprite('null', 1)
    ParticleSize(700)
    CallCustomizableParticle('ef_hitlz', 103)
    CommonSE('101_hit_slash_0')

@State
def ThrowExe_Bunshin_a():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        AddX(180000)
        WallCollisionDetection(1)
        RemoveOnCallStateEnd(3)

        def upon_56():
            clearUponHandler(56)
            NoDamageAction(1)
            EndMomentum(1)
            AttackOff()
            sendToLabel(0)
    sprite('hb203_06', 3)
    ColorForTransition(3355443200)
    ColorTransition(4294967295, 10)
    physicsXImpulse(24000)
    CreateParticle('hbef_311feather', 100)
    sprite('hb203_07', 3)
    sprite('hb311_05', 6)
    XImpulseAcceleration(20)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 20)
    ConstantAlphaModifier(-20)

@State
def ThrowExe_Bunshin_b():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
    sprite('hb311_04', 20)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def hbef_311_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('hbef311_slash', '')
        BlendMode_Add()
    sprite('null', 3)
    sprite('null', 4)

@State
def AirThrowExe_Bunshin_a():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        AddX(-110000)
    sprite('hb321_00', 3)
    physicsXImpulse(30000)
    StartMultihit()

@State
def AirThrowExe_Bunshin_b():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        AddX(-110000)
    sprite('hb320_02', 20)
    StartMultihit()
    ConstantAlphaModifier(-20)

@State
def hbef_321_slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        SetZVal(-1000)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(0)
        AlphaValue(245)
        AddX(-128000)
        AddY(64000)
        Size(800)
    sprite('vr_hb321_00', 3)
    sprite('vr_hb321_01', 3)
    sprite('vr_hb321_02', 3)
    sprite('vr_hb321_03', 3)

@State
def hbef_312_slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        SetZVal(-1000)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(240)
        PaletteColor1(241)
        PaletteColor3(242)
        PaletteColor4(1)
        AlphaValue(245)
    sprite('vr_hb312_00', 4)
    sprite('vr_hb312_01', 4)
    sprite('vr_hb312_02', 4)

@State
def AntiAir_Bunshin_a():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        FloorCollision(1)
        HitsPerCall(1, 0, 0, 1, 0, 1, 1, 1)
        sendToLabelUpon(54, 0)
        Unknown23091(1)
        NoDamageAction(1)
        NoAttackDuringAction(1)
        Visibility(1)
        IgnorePauses(3)
        Unknown4022(3)
    sprite('hb411_03', 2)
    physicsXImpulse(2000)
    physicsYImpulse(15000)
    setGravity(1000)
    sprite('hb411_04', 2)
    YAccel(90)
    sprite('hb411_05', 2)
    YAccel(90)
    sprite('hb411_06', 2)
    sprite('hb411_07', 3)
    Visibility(0)
    sprite('hb411_07', 20)
    XImpulseAcceleration(5)
    YAccel(5)
    setGravity(0)
    NoDamageAction(1)
    clearUponHandler(54)
    CreateObject('hbef_crow', 100)
    ApplyFunctionsToObjects(1)
    AddY(96000)
    ApplyFunctionsToSelf()
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 20)
    clearUponHandler(54)
    XImpulseAcceleration(20)
    YAccel(20)
    setGravity(0)
    AlphaValue(255)
    AttackOff()
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def hbef_411_slash_3d():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef411_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AlphaValue(192)
        AddY(310000)
        AddX(37000)
    sprite('null', 10)
    sprite('null', 2)
    E0EAEffectPosition(0)

@State
def hbef_411_slash_pt():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddY(272000)
    sprite('null', 10)
    PaletteIndex(1)
    ParticleColorFromPalette(224, 224, 224)
    CallPrivateEffect('hbef_411slash')
    sprite('null', 10)
    E0EAEffectPosition(0)

@State
def hbef_400_dash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(100000)
        AddY(-5000)
    label(0)
    sprite('null', 2)
    CallCustomizableParticle('hbef_400_dash', 100)
    gotoLabel(0)

@State
def hbef_400_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef400_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 3)
    ConstantRedModifier(-25)
    ConstantGreenModifier(-25)
    sprite('null', 7)
    ConstantAlphaModifier(-36)

@State
def hbef_400_damage():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    CreateParticle('hbef_400damage01', 100)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 242, 242)
    CallCustomizableParticle('hbef_400damage', 100)

@State
def hbef_401_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef401_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 5)
    ConstantRedModifier(-17)
    ConstantGreenModifier(-17)
    PaletteIndex(1)
    ParticleColorFromPalette(240, 242, 242)
    CallCustomizableParticle('hbef_401slash', 100)
    sprite('null', 15)
    ConstantAlphaModifier(-17)

@State
def Assault_Dash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 5)
    CallCustomizableParticle('hbef_400', 100)
    gotoLabel(0)

@State
def Assault_D_Bunshin():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        HitsPerCall(1, 0, 0, 1, 0, 1, 1, 1)
        sendToLabelUpon(54, 0)
        Unknown23091(1)
    sprite('hb400_03', 5)
    clearUponHandler(54)
    XImpulseAcceleration(80)
    CommonSE('005_swing_grap_2_0')
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    sprite('hb400_04', 3)
    StartMultihit()
    SkidEffects(100, 1, 0)
    XImpulseAcceleration(25)
    sprite('hb400_05', 3)
    sprite('hb400_05', 20)
    EndMomentum(1)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 20)
    clearUponHandler(54)
    EndMomentum(1)
    AlphaValue(255)
    NoDamageAction(1)
    AttackOff()
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def hbef_402_kick():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(191)
        AddY(128048)
        AddX(48000)
    sprite('vr_hb402_00', 3)
    sprite('vr_hb402_01', 4)
    E0EAEffectPosition(0)
    sprite('vr_hb402_02', 3)

@State
def hbef_403_kick():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(191)
        AddY(0)
    sprite('vr_hb403_00', 3)
    sprite('vr_hb403_01', 2)
    sprite('vr_hb403_02', 5)

@State
def BunshinAssault_Bunshin():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        HitsPerCall(1, 0, 0, 1, 0, 1, 1, 1)
        sendToLabelUpon(54, 0)
        Unknown23091(1)
    sprite('hb402_02', 3)
    callSubroutine('Bunshin_Zanzou')
    physicsXImpulse(-10000)
    physicsYImpulse(18000)
    setGravity(1600)
    sprite('hb402_03', 3)
    StartMultihit()
    sprite('hb402_04', 3)
    sprite('hb402_05', 3)
    sprite('hb402_06', 20)
    EndMomentum(1)
    ConstantAlphaModifier(-20)
    EnableAfterimage(0)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 20)
    clearUponHandler(54)
    EndMomentum(1)
    AlphaValue(255)
    NoDamageAction(1)
    AttackOff()
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def BunshinAssault_A_Bunshin():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        HitsPerCall(1, 0, 0, 1, 0, 1, 1, 1)
        sendToLabelUpon(54, 0)
        Unknown23091(1)
        AlphaValue(0)

        def upon_32():
            clearUponHandler(54)
            EnableCollision(0)
    sprite('hb403_00', 2)
    ConstantAlphaModifier(70)
    physicsXImpulse(28000)
    sprite('hb403_01', 2)
    sprite('hb403_02', 2)
    sprite('hb403_03', 2)
    sprite('hb403_01', 2)
    EnableCollision(1)
    sprite('hb403_02', 2)
    sprite('hb403_03', 2)
    sprite('hb403_01', 2)
    sprite('hb403_04', 3)
    sprite('hb403_05', 1)
    sprite('hb403_05', 3)
    clearUponHandler(54)
    clearUponHandler(32)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    EnableCollision(0)
    sprite('hb403_06', 3)
    sprite('hb403_07', 2)
    sprite('hb403_08', 2)
    sprite('hb403_09', 3)
    StartMultihit()
    sprite('hb403_10', 2)
    XImpulseAcceleration(30)
    sprite('hb403_11', 2)
    sprite('hb403_12', 2)
    XImpulseAcceleration(30)
    StartMultihit()
    sprite('hb234_19', 3)
    sprite('hb234_20', 3)
    EndMomentum(1)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 20)
    callSubroutine('Drive_Bunshin_Break')
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def BunshinAssault_A_BunshinF():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        NoDamageAction(1)
        RemoveOnCallStateEnd(3)
        AlphaValue(0)

        def upon_32():
            AlphaValue(255)
            SetActionMark(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)
    sprite('hb402_07', 2)
    physicsXImpulse(28000)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('hb402_08', 2)
    sprite('hb402_09', 2)
    sprite('hb402_07', 2)
    sprite('hb402_08', 2)
    CameraFollowTarget(0, 0)
    sprite('hb402_09', 2)
    sprite('hb402_07', 2)
    sprite('hb402_08', 2)
    sprite('hb402_10', 1)
    sprite('hb402_11', 1)
    sprite('hb402_12', 2)
    sprite('hb402_13', 2)
    if SLOT_2:
        callSubroutine('Bunshin_Black')
        callSubroutine('Bunshin_Alpha')
        CreateObject('hbef_crow', 100)
        PassbackAddActionMarkToFunction('BunshinAssault_A', 32)
    sprite('hb402_14', 2)
    sprite('hb402_15', 1)
    sprite('hb402_16', 10)
    StartMultihit()
    EndMomentum(1)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    clearUponHandler(54)
    EndMomentum(1)
    AlphaValue(255)
    NoDamageAction(1)
    AttackOff()
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def BunshinAssault_B_Bunshin():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        HitsPerCall(1, 0, 0, 1, 0, 1, 1, 1)
        sendToLabelUpon(54, 0)
        Unknown23091(1)
        AlphaValue(0)

        def upon_32():
            clearUponHandler(54)
            EnableCollision(0)
    sprite('hb402_07', 2)
    ConstantAlphaModifier(70)
    physicsXImpulse(28000)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('hb402_08', 2)
    sprite('hb402_09', 2)
    sprite('hb402_07', 2)
    sprite('hb402_08', 2)
    EnableCollision(1)
    sprite('hb402_09', 2)
    sprite('hb402_07', 2)
    sprite('hb402_08', 2)
    sprite('hb402_10', 1)
    sprite('hb402_11', 1)
    sprite('hb402_12', 2)
    sprite('hb402_13', 2)
    clearUponHandler(54)
    clearUponHandler(32)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    EnableCollision(0)
    sprite('hb402_14', 2)
    sprite('hb402_15', 1)
    sprite('hb402_16', 20)
    StartMultihit()
    EndMomentum(1)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 20)
    clearUponHandler(54)
    EndMomentum(1)
    AlphaValue(255)
    NoDamageAction(1)
    AttackOff()
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def BunshinAssault_B_BunshinF():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        NoDamageAction(1)
        RemoveOnCallStateEnd(3)
        AlphaValue(0)

        def upon_32():
            AlphaValue(255)
            SetActionMark(1)
        CameraFollowTarget(23, 22)

        def upon_STATE_END():
            CameraFollowTarget(0, 0)
    sprite('hb403_00', 2)
    physicsXImpulse(28000)
    sprite('hb403_01', 2)
    sprite('hb403_02', 2)
    sprite('hb403_03', 2)
    sprite('hb403_01', 2)
    CameraFollowTarget(0, 0)
    sprite('hb403_02', 2)
    sprite('hb403_03', 2)
    sprite('hb403_01', 2)
    sprite('hb403_04', 3)
    sprite('hb403_05', 1)
    sprite('hb403_05', 3)
    if SLOT_2:
        callSubroutine('Bunshin_Black')
        callSubroutine('Bunshin_Alpha')
        CreateObject('hbef_crow', 100)
    sprite('hb403_06', 3)
    if SLOT_2:
        PassbackAddActionMarkToFunction('BunshinAssault_B', 32)
    sprite('hb403_07', 2)
    sprite('hb403_08', 2)
    sprite('hb403_09', 10)
    StartMultihit()
    EndMomentum(1)
    loopRest()
    ExitState()
    label(9)
    sprite('keep', 20)
    clearUponHandler(54)
    EndMomentum(1)
    AlphaValue(255)
    NoDamageAction(1)
    AttackOff()
    EnableCollision(0)
    CreateObject('hbef_crow', 100)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')

@State
def FrontJump_Testdummy():

    def upon_IMMEDIATE():
        NoDamageAction(1)
    sprite('hb024_00', 3)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('hb024_01', 3)
    sprite('hb024_02', 20)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    ApplyFunctionsToObjects(1)
    AddY(-70000)
    AddX(15000)
    ApplyFunctionsToSelf()

@State
def hbef_405_kick():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(13000)
        AddY(-52000)
    sprite('null', 2)
    CreateParticle('hbef_405kick', 100)
    CreateParticle('hbef_405feather', 100)
    sprite('null', 2)

@State
def Derive_A_Dummy():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(500)
        AttackP1(80)
        AttackP2(100)
        AirPushbackY(-40000)
        PushbackX(12000)
        AttackDirection(3)
        UseSlashHitspark(1)
        FloorCollision(1)
        StarterRating(2)
        SameMoveProration(1)
        VoodooDamageMultiplier(2)
        CancelIfPlayerHit(3)
        NoAttackDuringAction(1)

        def upon_32():
            RotationAngle(30000)
            HitboxMovement(70000, -120000)

        def upon_33():
            RotationAngle(5000)
            HitboxMovement(70000, -95000)

        def upon_34():
            RotationAngle(-15000)
            HitboxMovement(70000, -75000)

        def upon_ON_HIT_OR_BLOCK():
            NoAttackDuringAction(1)
    sprite('vr_hb407_00', 7)
    Visibility(1)
    sprite('vr_hb407_00', 1)
    EndMomentum(1)
    sprite('vr_hb407_01', 15)
    Visibility(0)
    AbsoluteY(0)
    CreateParticle('hbef_407stuck', 0)
    sprite('keep', 20)
    ConstantAlphaModifier(-25)

@State
def Derive_A_Dummy_kg():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(500)
        AttackP1(80)
        AirPushbackY(-40000)
        PushbackX(12000)
        AttackDirection(3)
        UseSlashHitspark(1)
        FloorCollision(1)
        StarterRating(2)
        SameMoveProration(1)
        VoodooDamageMultiplier(2)
        NoAttackDuringAction(1)

        def upon_32():
            RotationAngle(30000)
            HitboxMovement(70000, -120000)

        def upon_33():
            RotationAngle(5000)
            HitboxMovement(70000, -95000)

        def upon_34():
            RotationAngle(-15000)
            HitboxMovement(70000, -75000)

        def upon_ON_HIT_OR_BLOCK():
            NoAttackDuringAction(1)
    sprite('vr_hb407_00ex', 7)
    Visibility(1)
    sprite('vr_hb407_00ex', 1)
    EndMomentum(1)
    sprite('vr_hb407_01ex', 15)
    Visibility(0)
    AbsoluteY(0)
    CreateParticle('hbef_407stuck', 0)
    sprite('keep', 20)
    ConstantAlphaModifier(-25)

@State
def Derive_A_Attack():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(1)
        Damage(500)
        Hitstun(14)
        AttackP1(80)
        AirPushbackY(-40000)
        PushbackX(12000)
        AttackDirection(3)
        UseSlashHitspark(1)
        FloorCollision(1)
        StarterRating(2)
        SameMoveProration(1)
        VoodooDamageMultiplier(3)
        CancelIfPlayerHit(3)
        AbsoluteY(0)
    sprite('hb407_AtkDummy2', 3)

@State
def Derive_C_Bunshin():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
    sprite('hb409_03', 2)
    StartMultihit()
    sprite('hb409_04', 2)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    sprite('hb409_04', 20)
    ConstantAlphaModifier(-30)

@State
def hbef_408_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(191)
        AddY(64000)
    sprite('vr_hb408_00', 3)
    sprite('vr_hb408_01', 3)
    sprite('vr_hb408_02', 3)

@State
def hbef_409_crow():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        E0EAEffectPosition(22)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetScaleX(900)
        AddY(192000)
        AddX(-64000)
    sprite('vr_hb409_00', 30)
    AlphaValue(150)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    AfterimageInterval(3)
    AfterimageCount(2)
    AfterimageColor_1(150, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    CreateObject('hbef_409_jump', 1)
    CreateObject('hbef_409_jump', 0)
    sprite('vr_hb409_00', 8)
    CreateObject('hbef_409_change', 103)
    ConstantAlphaModifier(-32)

@State
def hbef_409_jump():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)
    sprite('null', 3)
    CreateParticle('hbef_409jump', 100)

@State
def hbef_409_feather():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_r', 100)

@State
def hbef_409_feather2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)
    sprite('null', 3)
    CreateParticle('hbef_409feather_l', 100)

@State
def hbef_409_change():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 1)
    CreateParticle('hbef_409change', 100)

@State
def hbef_409_atemi():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        LinkParticle('hbef_409atemi')
    sprite('null', 15)
    CreateParticle('hbef_409atemi_feather', -1)

@State
def Derive_D_Bunshin():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        NoDamageAction(1)
    sprite('hb410_01', 2)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    sprite('hb410_02', 2)
    sprite('hb410_03', 2)
    sprite('hb410_01', 2)
    sprite('hb410_02', 2)
    sprite('hb410_03', 2)
    sprite('hb410_01', 2)
    sprite('hb410_02', 2)
    sprite('hb410_03', 2)
    sprite('hb410_01', 2)
    sprite('hb410_02', 2)
    sprite('hb410_03', 2)

@State
def hbef_410_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef410_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(128000)
        Size(1075)
        AlphaValue(191)
        sendToLabelUpon(32, 0)
        LinkParticle('hbef_410slash')
    label(1)
    sprite('null', 4)
    CreateObject('hbef_410_smoke', 100)
    sprite('null', 4)
    CreateObject('hbef_410_smoke', 100)
    CreateParticle('hbef_410slash+', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 10)
    CreateObject('hbef_410_smoke', 100)
    ConstantAlphaModifier(-64)
    ConstantRedModifier(-64)
    ConstantGreenModifier(-32)
    SetScaleSpeed(50)
    E0EAEffectPosition(0)

@State
def hbef_410_slash_Air():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef410_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(128000)
        Size(1075)
        AlphaValue(191)
        sendToLabelUpon(32, 0)
        LinkParticle('hbef_410slash')
    label(1)
    sprite('null', 4)
    sprite('null', 4)
    CreateParticle('hbef_410slash+', 100)
    gotoLabel(1)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-64)
    ConstantRedModifier(-64)
    ConstantGreenModifier(-32)
    SetScaleSpeed(50)
    E0EAEffectPosition(0)

@State
def hbef_410_smoke():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AbsoluteY(0)
    sprite('null', 1)
    CreateParticle('hbef_410smoke', 100)

@State
def hbef_430_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vr_hb430_00', 3)
    CreateParticle('hbef_430fall_b', 100)
    sprite('vr_hb430_01', 3)

@State
def hbef_430_fall():

    def upon_IMMEDIATE():
        Eff3DEffect('hbef430_tornado', '')
        FaceSpawnLocation()
        BlendMode_Sub()
        AlphaValue(129)
    sprite('null', 60)
    ScreenShake(30000, 30000)
    CreateParticle('hbef_430fall', 100)
    SetScaleSpeedY(-16)
    SetScaleXPerFrame(75)
    ConstantAlphaModifier(-4)

@State
def hbef_430_fall_OD():

    def upon_IMMEDIATE():
        Eff3DEffect('hbef430_tornado', '')
        FaceSpawnLocation()
        BlendMode_Sub()
        AlphaValue(129)
    sprite('null', 60)
    ScreenShake(30000, 30000)
    CreateParticle('hbef_430fall_od', 100)
    SetScaleSpeedY(-16)
    SetScaleXPerFrame(75)
    ConstantAlphaModifier(-4)

@State
def hbef_430_fall_OD_add():

    def upon_IMMEDIATE():
        Eff3DEffect('hbef430_tornado', '')
        FaceSpawnLocation()
        BlendMode_Sub()
        AlphaValue(129)
    sprite('null', 60)
    ScreenShake(50000, 50000)
    SetScaleSpeedY(-16)
    SetScaleXPerFrame(75)
    ConstantAlphaModifier(-4)

@State
def hbef_431_shot():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        RemoveOnContact(2)
        PaletteIndex(0)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(3)
        AfterimageCount(3)
        AfterimageColor_1(255, 191, 191, 255)
        AfterimageColor_2(0, 191, 191, 255)
        sendToLabelUpon(32, 0)
    sprite('vr_hb431_00', 3)
    PrivateSE('hbse_07')
    sprite('vr_hb431_01', 3)
    PrivateSE('hbse_07')
    sprite('vr_hb431_00', 3)
    sprite('vr_hb431_01', 3)
    sprite('vr_hb431_00', 3)
    sprite('vr_hb431_01', 3)
    EnableAfterimage(0)
    label(1)
    sprite('vr_hb431_00', 3)
    sprite('vr_hb431_01', 3)
    gotoLabel(1)
    label(0)
    sprite('vr_hb431_00', 3)
    EnableAfterimage(0)
    ColorTransition(4278190080, 2)
    sprite('vr_hb431_01', 3)
    sprite('vr_hb431_00', 3)
    ConstantAlphaModifier(-12)
    sprite('vr_hb431_01', 3)
    gotoLabel(1)

@State
def UltimateAssault2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AttackP2(100)
        UseSlashHitspark(1)
        Hitstun(30)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        StarterRating(2)
        CancelIfPlayerHit(3)
        HitboxMovement(65000, 0)

        def upon_ON_HIT_OR_BLOCK():
            NoAttackDuringAction(1)

        def upon_OPPONENT_HIT():
            sendToLabel(0)
            DefeatOpponentBehavior(1)
            Hitstun(500)
            PushbackX(0)
            ObjectUpon(3, 33)

        def upon_45():
            if Unknown2065(23):
                clearUponHandler(45)
                ObjectUpon(2, 40)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hb407_AtkDummy', 5)
    Visibility(1)
    CreateObject('hbef_431_shot', 100)
    sprite('hb407_AtkDummy', 5)
    sprite('hb407_AtkDummy', 5)
    sprite('hb407_AtkDummy', 20)
    XImpulseAcceleration(20)
    ConstantAlphaModifier(-20)
    NoAttackDuringAction(1)
    PassbackAddActionMarkToFunction('hbef_431_shot', 32)
    CreateObject('hbef_crow', 100)
    ApplyFunctionsToObjects(1)
    AddY(-192000)
    ApplyFunctionsToSelf()
    sprite('hb407_AtkDummy', 10)
    ObjectUpon(3, 32)
    EndMomentum(1)
    loopRest()
    ExitState()
    label(0)
    sprite('keep', 10)
    XImpulseAcceleration(5)
    EndAttack()
    clearUponHandler(54)
    clearUponHandler(10)
    ConstantAlphaModifier(-50)
    CreateObject('hbef_crow', 100)
    ApplyFunctionsToObjects(1)
    AddY(-192000)
    ApplyFunctionsToSelf()
    sprite('keep', 20)
    EndMomentum(1)

@State
def hbef_431_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef431_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 9)

@State
def hbef_431_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef431_slash2', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(200000)
    sprite('null', 4)

@State
def hbef_431_slash3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef431_slash3', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 32)
    ConstantRedModifier(-8)
    ConstantGreenModifier(-8)
    sprite('null', 10)
    ConstantAlphaModifier(-16)

@State
def hbef_431_rolling():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef410_slash', '')
        FaceSpawnLocation()
        LinkParticle('hbef_410slash')
        BlendMode_Add()
        AddY(128000)
        Size(1075)
        AlphaValue(191)
        sendToLabelUpon(32, 0)
    sprite('null', 60)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-64)
    ConstantRedModifier(-64)
    ConstantGreenModifier(-32)
    SetScaleSpeed(50)
    E0EAEffectPosition(0)

@State
def hbef_431_rolling_dash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 4)
    CreateParticle('hbef_431rolling', 100)
    gotoLabel(0)

@State
def hbef_431_slash4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('hbef431_slash4', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(150000)
        AddX(-190000)
        SetScaleX(1500)
    sprite('null', 15)
    sprite('null', 15)
    ConstantRedModifier(-17)
    ConstantGreenModifier(-17)
    ConstantAlphaModifier(-17)

@State
def hbef_431_slash_bg():
    sprite('null', 1)
    AddY(-75000)
    ParticleRotationAngle(110000)
    ParticleLayer(11)
    CallCustomizableParticle('hbef_431slash_bg', 103)

@State
def hbef_431_slash_bg2():
    sprite('null', 1)
    AddY(-100000)
    ParticleRotationAngle(300000)
    ParticleLayer(11)
    CallCustomizableParticle('hbef_431slash_bg', 103)

@State
def hbef_431_slash_bg3():
    sprite('null', 1)
    AddY(-50000)
    ParticleRotationAngle(250000)
    ParticleLayer(11)
    CallCustomizableParticle('hbef_431slash_bg', 103)

@State
def hbef_431_slash_bg4():
    sprite('null', 1)
    AddY(-50000)
    ParticleRotationAngle(90000)
    ParticleLayer(11)
    CallCustomizableParticle('hbef_431slash_bg2', 103)

@State
def hbef_431_hit():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        ParticleLayer(13)
        CallPrivateEffect('hbef_431hit')
        sendToLabelUpon(32, 0)
    sprite('null', 1)
    Size(500)
    sprite('null', 32767)
    Size(1000)
    label(0)
    sprite('null', 1)
    ParticleLayer(13)
    CallCustomizableParticle('nbef_431end', -1)

@State
def __431_AttackEffect():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        DeviationX(-120000, 120000)
        DeviationY(180000, 240000)
    sprite('null', 10)
    if random_(2, 0, 50):
        CommonSE('101_hit_slash_1')
    else:
        CommonSE('101_hit_slash_2')
    ScreenShake(0, 5000)

@State
def __431_AttackDummy():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        TeleportToObject(22)
        AttackLevel_(5)
        Damage(900)
        AttackP2(84)
        SingleProration(1)
        Hitstop(1)
        GroundedHitstunAnimation(2)
        Crumple(100)
        Stagger(35)
        CHStagger(35)
        HardKnockdown(15)
        PushbackX(0)
        DefeatOpponentBehavior(1)
        AirUntechableTime(60)
        UseSlashHitspark(1)

        def upon_OPPONENT_HIT():
            CommonSE('103_hit_counter_slash_0')
            ScreenShake(0, 8000)
        CHStateIfCHStart(2)
        HitAnywhere(1)
        AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hb431_AtkDummy', 10)
    sprite('hb431_AtkDummy', 1)
    RefreshMultihit()
    AddCombo(3)
    PassbackAddActionMarkToFunction('hbef_431_hit', 32)
    sprite('hb431_AtkDummy', 1)
    AddCombo(4)
    sprite('hb431_AtkDummy', 1)
    RefreshMultihit()
    AddCombo(3)
    sprite('hb431_AtkDummy', 1)
    AddCombo(4)
    sprite('hb431_AtkDummy', 1)
    ObjectUpon(3, 32)
    RefreshMultihit()
    Damage(2400)
    if SLOT_137:
        DamageMultiplier(80)
    DefeatOpponentBehavior(0)
    AddCombo(3)

@State
def UltimateAssault2_Bunshin0():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        NoDamageAction(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
    sprite('hb431_06', 3)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    sprite('hb431_06', 3)
    ConstantAlphaModifier(-12)
    sprite('hb431_07', 3)
    sprite('hb431_08', 3)
    sprite('hb431_06', 3)
    sprite('hb431_07', 3)
    sprite('hb431_08', 3)
    sprite('hb431_06', 3)
    sprite('hb431_07', 3)
    sprite('hb431_08', 3)

@State
def UltimateAssault2_Bunshin1():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        NoDamageAction(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
    sprite('hb431_14', 5)
    physicsXImpulse(2000)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    sprite('hb431_14', 20)
    ConstantAlphaModifier(-12)

@State
def UltimateAssault2_Bunshin2():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        NoDamageAction(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
    sprite('hb431_20', 5)
    physicsXImpulse(-2000)
    physicsYImpulse(-2000)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)
    sprite('hb431_20', 20)
    ConstantAlphaModifier(-12)

@State
def hbef_431_hit_OD():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        ParticleLayer(13)
        CallPrivateEffect('hbef_431hit_od')
        sendToLabelUpon(32, 0)
    sprite('null', 1)
    Size(500)
    sprite('null', 32767)
    Size(1000)
    label(0)
    sprite('null', 12)
    sprite('null', 1)
    ParticleLayer(13)
    CallCustomizableParticle('nbef_431end_od', -1)

@State
def hbef_431_odbg():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(60)
    label(0)
    sprite('null', 2)
    ParticleLayer(12)
    CallCustomizableParticle('hbef_431odbg', 103)
    gotoLabel(0)

@State
def hbef_431_slash_od():
    sprite('null', 1)
    AddY(175000)
    ParticleRotationAngle(90000)
    ParticleLayer(11)
    CallCustomizableParticle('hbef_431slash_bg', 103)
    CreateParticle('hbef_431hit_add', 103)

@State
def hbef_431_slash_od2():
    sprite('null', 1)
    AddY(125000)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('hbef_431slash_bg', 103)
    CreateParticle('hbef_431hit_add', 103)

@State
def __431_AttackEffect_OD():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        DeviationX(-120000, 120000)
        DeviationY(180000, 240000)
    sprite('null', 10)
    CommonSE('103_hit_counter_slash_0')
    CommonSE('101_hit_slash_2')
    ScreenShake(0, 12000)

@State
def __431_AttackDummy_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        TeleportToObject(22)
        AttackLevel_(5)
        Damage(570)
        AttackP2(84)
        SingleProration(1)
        Hitstop(1)
        GroundedHitstunAnimation(2)
        Crumple(100)
        Stagger(35)
        CHStagger(35)
        HardKnockdown(15)
        PushbackX(0)
        HitsparkSize(900)
        DefeatOpponentBehavior(1)
        AttackType(4)
        AirUntechableTime(60)
        UseSlashHitspark(1)

        def upon_OPPONENT_HIT():
            ScreenShake(0, 8000)
            AddCombo(2)
        CHStateIfCHStart(2)
        HitAnywhere(1)
        AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('hb431_AtkDummy', 10)
    sprite('hb431_AtkDummy', 4)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 4)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 4)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 3)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 3)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 2)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 2)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 1)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 1)
    RefreshMultihit()
    sprite('hb431_AtkDummy', 1)
    PassbackAddActionMarkToFunction('hbef_431_hit_OD', 32)
    ObjectUpon(3, 32)
    DefeatOpponentBehavior(0)
    RefreshMultihit()

@State
def UltimateAssault2_OD_Bunshin():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        EnableCollision(0)
        AlphaValue(0)
        DespawnEAEffect('hbef_crow')

        def upon_FRAME_STEP():
            if (SLOT_19 < 80000):
                CreateObject('431_AttackEffect_OD', 103)
    sprite('hb203_06', 2)
    callSubroutine('Zanzou_Ranbu')
    ForceFaceSprite()
    EndMomentum(1)
    TeleportToObject(22)
    AddX(-480000)
    physicsXImpulse(50000)
    CreateObject('hbef_D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddY(192000)
    ApplyFunctionsToSelf()
    sprite('hb203_07', 2)
    sprite('hb203_08', 2)
    CommonSE('010_swing_sword_1')
    sprite('hb203_09', 3)
    CreateObject('hbef_203_slash', 100)
    CreateObject('hbef_431_slash_od', 103)
    sprite('hb203_10', 3)
    sprite('hb203_11', 5)
    XImpulseAcceleration(75)
    sprite('hb203_12', 10)
    XImpulseAcceleration(25)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@State
def UltimateAssault2_OD_Bunshin1():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        EnableCollision(0)
        AlphaValue(0)
        DespawnEAEffect('hbef_crow')

        def upon_FRAME_STEP():
            if (SLOT_19 < 80000):
                CreateObject('431_AttackEffect_OD', 103)
    sprite('hb203_06', 2)
    callSubroutine('Zanzou_Ranbu')
    Flip()
    EndMomentum(1)
    TeleportToObject(22)
    AddX(-480000)
    physicsXImpulse(50000)
    CreateObject('hbef_D_feather', 100)
    ApplyFunctionsToObjects(1)
    AddY(192000)
    ApplyFunctionsToSelf()
    sprite('hb203_07', 2)
    sprite('hb203_08', 2)
    CommonSE('010_swing_sword_1')
    sprite('hb203_09', 3)
    CreateObject('hbef_203_slash', 100)
    CreateObject('hbef_431_slash_od2', 103)
    sprite('hb203_10', 3)
    sprite('hb203_11', 5)
    XImpulseAcceleration(75)
    sprite('hb203_12', 10)
    XImpulseAcceleration(25)
    callSubroutine('Bunshin_Black')
    callSubroutine('Bunshin_Alpha')
    CreateObject('hbef_crow', 100)

@Subroutine
def Zanzou_Ranbu():
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(42)
    ColorTransition(4294967295, 6)

@State
def hbef_440_kick():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('hbef440_kick', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(190000)
        AddX(112000)
    sprite('null', 10)

@State
def hbef_440_kick2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('hbef440_kick', '')
        FaceSpawnLocation()
        BlendMode_Add()
        AddY(98000)
        AddX(30000)
        Size(1225)
    sprite('null', 10)

@State
def hbef_440_kickBG():

    def upon_IMMEDIATE():
        AbsoluteY(0)
        AddY(-100000)
        AddX(90000)
    sprite('null', 1)
    CallCustomizableParticle('hbef_440upper', -1)

@State
def hbef_440_slash():

    def upon_IMMEDIATE():
        Eff3DEffect('hbef440_slash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 20)
    Size(1200)
    SetScaleSpeed(40)
    CreateParticle('hbef_440slash', -1)

@State
def hbef_440_slash2():

    def upon_IMMEDIATE():
        Eff3DEffect('hbef440_slash2', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 15)
    AddRotationPerFrame(-22500)
    Size(1250)

@State
def hbef_440_wing():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(0)
    sprite('vr_hb440_00', 10)
    CreateObject('hbef_440_slash2', -1)
    CreateParticle('hbef_440wing', -1)
    AddRotationPerFrame(-15000)
    AlphaValue(64)
    ConstantAlphaModifier(64)
    Size(1240)
    SetScaleSpeed(10)
    sprite('vr_hb440_00', 16)
    ConstantAlphaModifier(-16)

@State
def hbef_450_bg():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('hbef_450bg')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 60)
    ConstantAlphaModifier(-4)

@State
def hbef_450_lead():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        PaletteIndex(0)
        BlendMode_Normal()
        sendToLabelUpon(32, 0)
    sprite('vr_hb450_00', 6)
    sprite('vr_hb450_01', 6)
    sprite('vr_hb450_10', 10)
    CreateObject('hbef_450_circle', 100)
    sprite('vr_hb450_10', 10)
    ColorTransition(4278190080, 10)
    sprite('vr_hb450_10', 1)
    CreateObject('hbef_450_lead_c', 100)

@State
def hbef_450_lead_c():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(208)
        PaletteColor1(208)
        PaletteColor3(208)
        SetCustomPaletteAlpha(-400)
    sprite('vr_hb450_20', 60)

@State
def hbef_450_circle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        AddY(16000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Size(1250)
    ParticleLayer(11)
    CallPrivateEffect('hbef_450circle')
    CreateObject('hbef_450_cicle_wave', 100)
    sprite('null', 10)
    CreateObject('hbef_450_cicle_wave', 100)
    sprite('null', 10)
    CreateObject('hbef_450_cicle_wave', 100)
    sprite('null', 60)
    label(0)
    sprite('null', 25)
    ConstantAlphaModifier(-10)

@State
def hbef_450_cicle_wave():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        Eff3DEffect('hbef450_circle', '')
        FaceSpawnLocation()
        BlendMode_Sub()
    sprite('null', 8)
    SetScaleSpeed(50)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    sprite('null', 32)
    ConstantAlphaModifier(-8)

@State
def hbef_450_splash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
    sprite('null', 30)
    CreateParticle('hbef_450crow', 100)
    label(0)
    sprite('null', 30)
    CreateParticle('hbef_450splash', 100)
    gotoLabel(0)

@State
def hbef_450_crows():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 160)
    CallPrivateEffect('hbef_450crows')
    CreateObject('Fade_Out', 100)

@State
def Fade_Out():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        FaceRight()
        ScreenPosition(1)
        SetPosXByScreenPer(0)
        SetPosYByScreenPer(50)
        ForceBloomMaskOn(1)
        BlendMode_Normal()
        PaletteIndex(1)
        RenderLayer(1)
        Size(20000)
    sprite('vr_screen_black', 15)
    AlphaValue(0)
    sprite('vr_screen_black', 32767)
    ConstantAlphaModifier(4)

@State
def Fade_Up():
    sprite('null', 100)
    CreateObject('Fade_Up_Sub', -1)
    CreateObject('Fade_Up_Sub', -1)
    ObjectUpon(1, 32)
    CreateObject('Fade_Up_Sub', -1)
    ObjectUpon(1, 33)

@State
def Fade_Up_Sub():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        FaceRight()
        BlendMode_Normal()
        RenderLayer(1)
        XPositionRelativeFacing(640000)
        AbsoluteY(-2000000)
        ScreenPosition(1)
        ColorForTransition(4278190080)
        Size(2500)
        SetScaleY(5500)
        physicsYImpulse(75000)

        def upon_32():
            AddX(426666)

        def upon_33():
            AddX(-426666)
    sprite('vr_screen_fade', 100)

@State
def Screen_Black():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        ForceBloomMaskOn(1)
        BlendMode_Normal()
        PaletteIndex(1)
        RenderLayer(1)
        Size(20000)
    sprite('vr_screen_black', 32767)

@State
def Fade_In():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(0)
        SetPosYByScreenPer(50)
        ForceBloomMaskOn(1)
        BlendMode_Normal()
        PaletteIndex(1)
        RenderLayer(1)
        Size(20000)
    sprite('vr_screen_black', 40)
    AlphaValue(255)
    ConstantAlphaModifier(-6)

@State
def hbef_enemy_black():

    def upon_FRAME_STEP():
        ApplyFunctionsToObjects(22)
        ColorForTransition(4282400832)
        ApplyFunctionsToSelf()
    sprite('null', 32767)

@State
def hbef_450_ground():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        LinkParticle('hbef_450ground')
        AddY(-16000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 32)
    ConstantAlphaModifier(-8)

@State
def hbef_450_mist():

    def upon_IMMEDIATE():
        FaceLeft()
        ScreenPosition(1)
        BlendMode_Normal()
        Eff3DEffect('hbef450_mist', '')
        FaceSpawnLocation()
        Size(1300)
        BlendMode_Add()
        BlueColorValue(184)
        sendToLabelUpon(32, 0)
        SetActionMark(0)

        def upon_33():
            clearUponHandler(33)
            SetActionMark(1)

        def upon_48():
            if (not SLOT_2):
                SetPosXByScreenPer(50)
    sprite('null', 32767)
    label(0)
    sprite('null', 4)
    ConstantAlphaModifier(-64)

@State
def AstralHeat_ExclamationControl():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AddY(480000)
    sprite('null', 10)
    CreateParticle('ef_girdmiss_m', 0)

@State
def BG_Black():

    def upon_IMMEDIATE():
        Flip()
        ForceBloomMaskOn(1)
        BlendMode_Normal()
        PaletteIndex(1)
        ScreenPosition(1)
        XPositionRelativeFacing(-640000)
        AbsoluteY(0)
        RenderLayer(2)
        Size(20000)
    sprite('vr_screen_black', 60)
    AlphaValue(0)
    ConstantAlphaModifier(6)

@State
def hbef_450_cross():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        SetPosYByScreenPer(50)
    sprite('null', 32767)
    AddY(-56000)
    ScreenShake(15000, 15000)
    FaceLeft()
    RenderLayer(3)
    LinkParticle('hbef_450cross')

@State
def hbef_450_EnemyWhite():
    label(0)
    sprite('null', 1)
    ApplyFunctionsToObjects(22)
    StopCharacterFlash1(-1)
    ApplyFunctionsToSelf()
    gotoLabel(0)

@State
def hbef_450_crash():

    def upon_IMMEDIATE():
        RenderLayer(2)
        FaceLeft()
        TeleportToObject(22)
        ScreenPosition(1)
        SetPosYByScreenPer(50)
    sprite('null', 90)
    CreateParticle('hbef_450crash', 100)
    LinkParticle('hbef_450blood')
    sprite('null', 16)
    ConstantAlphaModifier(-16)

@State
def Astralheat_Bunshin0():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        EnableCollision(0)
        NoDamageAction(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        SetZVal(500)
    sprite('hb030_01ex', 10)
    AddX(150000)
    physicsXImpulse(1000)
    callSubroutine('AH_Bunshin_black')
    AlphaValue(0)
    ConstantAlphaModifier(12)
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    AfterimageColor_1(64, 0, 0, 0)
    AfterimageColor_2(0, 0, 0, 0)
    AfterimageCount(5)
    AfterimageInterval(3)
    sprite('hb030_02ex', 10)
    sprite('hb030_03ex', 10)
    sprite('hb030_03ex', 10)
    ConstantAlphaModifier(-8)
    sprite('hb030_04ex', 10)
    sprite('hb030_05ex', 9)
    physicsXImpulse(1000)
    sprite('hb030_06ex', 9)
    sprite('hb030_07ex', 9)
    sprite('hb030_08ex', 9)

@State
def Astralheat_Bunshin1():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirPushbackX(30000)
        AirPushbackY(15000)
        Hitstun(30)
        AirUntechableTime(30)
        UseSlashHitspark(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        AddX(-260000)
        HitAnywhere(1)
    sprite('hb213_09', 3)
    physicsXImpulse(40000)
    physicsYImpulse(30000)
    CommonSE('010_swing_sword_1')
    callSubroutine('AH_Bunshin')
    callSubroutine('AH_Bunshin_Zanzoh')
    sprite('hb213_10', 3)
    ScreenShake(4000, 4000)
    ColorForTransition(4294967295)
    DespawnEAEffect('hbef_enemy_black')
    CreateObject('hbef_213_slash2', 100)
    ApplyFunctionsToObjects(22)
    ParticleRotationAngle(45000)
    CallCustomizableParticle('hbef_450slash', 103)
    ApplyFunctionsToSelf()
    sprite('hb213_11', 3)
    callSubroutine('AH_Bunshin_black')
    callSubroutine('AH_Bunshin_end')
    CreateObject('hbef_enemy_black', 100)
    sprite('hb213_12', 4)
    sprite('hb213_12', 20)

@State
def Astralheat_Bunshin2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirPushbackX(30000)
        AirPushbackY(15000)
        Hitstun(30)
        AirUntechableTime(30)
        UseSlashHitspark(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(180)
        Crumple(180)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        AddX(320000)
        HitAnywhere(1)
    sprite('hb311_05', 3)
    callSubroutine('AH_Bunshin')
    callSubroutine('AH_Bunshin_Zanzoh')
    sprite('hb311_06', 3)
    sprite('hb311_07', 2)
    sprite('hb234_15', 3)
    physicsXImpulse(-60000)
    physicsYImpulse(40000)
    ScreenShake(4000, 4000)
    ColorForTransition(4294967295)
    DespawnEAEffect('hbef_enemy_black')
    CreateObject('hbef_234_slash', 100)
    ApplyFunctionsToObjects(22)
    ParticleRotationAngle(45000)
    CallCustomizableParticle('hbef_450slash', 103)
    ApplyFunctionsToSelf()
    sprite('hb234_16', 4)
    callSubroutine('AH_Bunshin_black')
    callSubroutine('AH_Bunshin_end')
    CreateObject('hbef_enemy_black', 100)
    sprite('hb234_17', 4)
    sprite('hb234_18', 20)

@State
def Astralheat_Bunshin3():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(-80000)
        AirUntechableTime(120)
        UseSlashHitspark(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        GroundBounce(1)
        BouncePercentage(35)
        HardKnockdown(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        AddY(250000)
        FloorCollision(1)
        HitAnywhere(1)
    sprite('hb251_07', 6)
    physicsYImpulse(6000)
    callSubroutine('AH_Bunshin')
    callSubroutine('AH_Bunshin_Zanzoh')
    sprite('hb251_08', 3)
    sprite('hb251_09', 3)
    physicsYImpulse(-40000)
    CommonSE('010_swing_sword_1')
    sprite('hb251_10', 2)
    ScreenShake(4000, 4000)
    ColorForTransition(4294967295)
    DespawnEAEffect('hbef_enemy_black')
    CreateObject('hbef_251_slash2', 100)
    ApplyFunctionsToObjects(22)
    ParticleRotationAngle(180000)
    CallCustomizableParticle('hbef_450slash', 103)
    ApplyFunctionsToSelf()
    sprite('hb251_11', 2)
    callSubroutine('AH_Bunshin_black')
    callSubroutine('AH_Bunshin_end')
    CreateObject('hbef_enemy_black', 100)
    sprite('hb251_12', 2)
    YAccel(10)
    sprite('hb251_13', 20)

@State
def Astralheat_Bunshin4():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirPushbackX(80000)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(999)
        UseSlashHitspark(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        GroundBounce(1)
        HardKnockdown(1)
        WallbounceReboundTime(10)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        AddY(60000)
        SetPosXByScreenPer(5)
        ForceFaceSprite()
        HitAnywhere(1)
    sprite('hb253_10', 3)
    setGravity(0)
    callSubroutine('AH_Bunshin')
    callSubroutine('AH_Bunshin_Zanzoh')
    sprite('hb253_11', 3)
    sprite('hb253_12', 3)
    sprite('hb253_13', 3)
    sprite('hb253_05', 1)
    physicsXImpulse(60000)
    sprite('hb253_06', 2)
    sprite('hb253_07', 1)
    CommonSE('010_swing_sword_1')
    sprite('hb253_08', 3)
    PassbackAddActionMarkToFunction('hbef_450_ground', 32)
    PassbackAddActionMarkToFunction('hbef_450_mist', 32)
    ScreenShake(4000, 4000)
    XImpulseAcceleration(30)
    ColorForTransition(4294967295)
    DespawnEAEffect('hbef_enemy_black')
    CreateObject('hbef_253_slash', 100)
    ApplyFunctionsToObjects(22)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('hbef_450slash', 103)
    ApplyFunctionsToSelf()
    sprite('hb253_09', 3)
    callSubroutine('AH_Bunshin_black')
    callSubroutine('AH_Bunshin_end')
    CreateObject('hbef_enemy_black', 100)
    sprite('hb253_10', 3)
    sprite('hb253_11', 4)

@State
def Astralheat_Bunshin5():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        AirUntechableTime(999)
        Hitstop(6)
        EnemyHitstopAddition(60, 60, 60)
        UseSlashHitspark(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        HitAnywhere(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        AddX(360000)
        AddY(50000)
        EnableAfterimage(1)
        AfterimageCount(8)
        AfterimageInterval(3)
        sendToLabelUpon(2, 1)
        FloorCollision(1)
        AttackOff()
    sprite('hb601_01', 3)
    Visibility(1)
    setGravity(0)
    sprite('hb601_01ex03', 3)
    sprite('hb601_01ex02', 3)
    sprite('hb601_01ex01', 3)
    sprite('hb601_01', 3)
    sprite('hb601_01ex03', 3)
    Visibility(0)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('hb601_01ex02', 3)
    sprite('hb601_01ex01', 3)
    sprite('hb601_01', 3)
    sprite('hb601_01ex03', 3)
    sprite('hb601_01ex02', 3)
    sprite('hb601_01ex01', 3)
    sprite('hb601_01', 3)
    sprite('hb450_17', 10)
    sprite('hb450_18', 10)
    sprite('hb450_19', 10)
    sprite('hb450_20', 2)
    physicsXImpulse(-100000)
    physicsYImpulse(-50000)
    sprite('hb450_20ex', 6)
    RefreshMultihit()
    AddCombo(1)
    CreateObject('hbef_450_cross', 100)
    ApplyFunctionsToObjects(22)
    StopCharacterFlash1(-1)
    ApplyFunctionsToSelf()
    StopCharacterFlash1(-1)
    label(1)
    sprite('hb450_21', 8)
    EndMomentum(1)
    AbsoluteY(8000)
    ApplyFunctionsToObjects(22)
    StopCharacterFlash1(-1)
    ApplyFunctionsToSelf()
    sprite('hb450_22', 52)
    StartMultihit()
    CreateObject('ScreenSlashMain', 0)
    PrivateSE('hbse_07')
    sprite('hb450_22', 45)
    Visibility(1)
    RefreshMultihit()
    AirHitstunAnimation(1)
    DespawnEAEffect('hbef_450_cross')
    DespawnEAEffect('ScreenSlashMain')
    DespawnEAEffect('Astralheat_Bunshin6')
    ScreenShake(30000, 30000)
    CreateObject('hbef_450_crash', 100)
    ApplyFunctionsToObjects(22)
    StopCharacterFlash1(-16777216)
    ApplyFunctionsToSelf()
    SetBackground(3)
    FinishBG(1)
    PrivateSE('hbse_09')
    sprite('hb450_22', 30)
    Voiceline('hb293')
    RefreshMultihit()
    DisableOppPushCollision(0)
    HitAnywhere(1)
    Hitstop(0)
    YImpulseBeforeWallbounce(0)
    Damage(30000)
    DefeatOpponentBehavior(3)

    def upon_OPPONENT_HIT():
        ApplyFunctionsToObjects(22)
        Visibility(1)
        AlphaValue(0)
        ApplyFunctionsToSelf()

@State
def Astralheat_Bunshin6():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        AirUntechableTime(999)
        Hitstop(6)
        EnemyHitstopAddition(120, 120, 120)
        UseSlashHitspark(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        HitAnywhere(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        TeleportToObject(22)
        AddX(-360000)
        AddY(50000)
        EnableAfterimage(1)
        AfterimageCount(8)
        AfterimageInterval(3)
        Flip()
        sendToLabelUpon(2, 1)
        FloorCollision(1)

        def upon_32():
            StopCharacterFlash1(-1)
        NoAttackDuringAction(1)
    sprite('hb601_01', 3)
    Visibility(1)
    setGravity(0)
    sprite('hb601_01ex03', 3)
    sprite('hb601_01ex02', 3)
    sprite('hb601_01ex01', 3)
    sprite('hb601_01', 3)
    sprite('hb601_01ex03', 3)
    Visibility(0)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('hb601_01ex02', 3)
    sprite('hb601_01ex01', 3)
    sprite('hb601_01', 3)
    sprite('hb601_01ex03', 3)
    sprite('hb601_01ex02', 3)
    sprite('hb601_01ex01', 3)
    sprite('hb601_01', 3)
    sprite('hb450_17', 10)
    sprite('hb450_18', 10)
    sprite('hb450_19', 10)
    sprite('hb450_20', 2)
    StartMultihit()
    physicsXImpulse(-100000)
    physicsYImpulse(-50000)
    sprite('hb450_20ex', 6)
    StartMultihit()
    StopCharacterFlash1(-1)
    EndMomentum(1)
    sprite('hb450_20ex', 6)
    StartMultihit()
    physicsXImpulse(-100000)
    physicsYImpulse(-50000)
    label(1)
    sprite('hb450_21', 8)
    EndMomentum(1)
    AbsoluteY(8000)
    sprite('hb450_22', 52)
    sprite('hb450_22', 45)
    Visibility(1)
    StartMultihit()
    sprite('hb450_22', 30)
    StartMultihit()

@State
def AstralHeat_CameraControl00():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        CameraControlEnable(1)
        CameraFast(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        CameraNoCeiling(1)
        RenderLayer(1)
        Visibility(1)
        TeleportToObject(22)
        AbsoluteY(51200000)
        physicsYImpulse(-100000)
    sprite('null', 100)
    CreateObject('Fade_In', 103)
    sprite('null', 50)
    CreateObject('Fade_Up', 100)

@State
def AstralHeat_CameraControl01():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RemoveOnCallStateEnd(2)
        CameraControlEnable(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraNoScreenCollision(1)
        RenderLayer(1)
        TeleportToObject(22)
        AddY(-50000)
        Visibility(1)
    sprite('null', 60)
    EndMomentum(1)

@State
def Astralheat_EnemyControl():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        sendToLabelUpon(32, 10)
    sprite('null', 1)
    SetActionMark(4)
    ApplyFunctionsToObjects(22)
    EnableAfterimage(1)
    AfterimageCount(5)
    AfterimageInterval(2)
    XImpulseAcceleration(0)
    YAccel(0)
    setGravity(1400)
    ApplyFunctionsToSelf()
    label(1)
    sprite('null', 3)
    AddActionMark(-1)
    ApplyFunctionsToObjects(22)
    EndSprite(1)
    ApplyFunctionsToSelf()
    sprite('null', 1)
    ApplyFunctionsToObjects(22)
    EndSprite(0)
    ApplyFunctionsToSelf()
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    sprite('null', 1)
    SetActionMark(4)
    ApplyFunctionsToObjects(22)
    XImpulseAcceleration(5)
    YAccel(5)
    setGravity(20)
    ApplyFunctionsToSelf()
    label(2)
    sprite('null', 5)
    AddActionMark(-1)
    ApplyFunctionsToObjects(22)
    EndSprite(1)
    ApplyFunctionsToSelf()
    sprite('null', 1)
    ApplyFunctionsToObjects(22)
    EndSprite(0)
    ApplyFunctionsToSelf()
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('null', 32767)
    clearUponHandler(32)
    ApplyFunctionsToObjects(22)
    EndSprite(1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    ApplyFunctionsToSelf()
    loopRest()

@Subroutine
def AH_Bunshin():
    ColorForTransition(4278190080)
    ColorTransition(4284769380, 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)

@Subroutine
def AH_Bunshin_end():
    ColorTransition(4278190080, 9)
    ConstantAlphaModifier(-28)

@Subroutine
def AH_Bunshin_Zanzoh():
    EnableAfterimage(1)
    AfterimageBlendMode(1)
    AfterimageColor_1(255, 100, 100, 100)
    AfterimageColor_2(0, 0, 0, 0)
    AfterimageCount(5)
    AfterimageInterval(1)

@Subroutine
def AH_Bunshin_black():
    ColorForTransition(4282400832)

@State
def ScreenSlashMain():
    sprite('null', 32767)
    CreateObject('ScreenSlashWhite', 0)
    CreateObject('ScreenSlashLeft', 0)
    CreateObject('ScreenSlashRight', 0)
    CreateObject('ScreenSlashTop', 0)
    CreateObject('ScreenSlashUnder', 0)
    loopRest()

@State
def ScreenSlashWhite():
    sprite('vr_screen_white', 32767)
    BlendMode_Normal()
    PaletteIndex(1)
    SetZVal(500)
    RemoveOnCallStateEnd(2)
    FaceLeft()
    RenderLayer(3)
    ScreenPosition(1)
    XPositionRelativeFacingAbsolute(640000)
    AbsoluteY(-384000)
    Size(4000)
    ColorForTransition(4294967295)
    loopRest()

@State
def ScreenSlashRight():
    sprite('vr_screen_slashR', 20)
    RemoveOnCallStateEnd(2)
    FaceLeft()
    Unknown3079(1)
    RenderLayer(3)
    ScreenPosition(1)
    XPositionRelativeFacingAbsolute(640000)
    AbsoluteY(-384000)
    SetScaleX(1250)
    SetScaleY(750)
    sprite('vr_screen_slashR', 10)
    physicsYImpulse(-1500)
    physicsXImpulse(-2500)
    sprite('vr_screen_slashR', 10)
    physicsYImpulse(-2000)
    physicsXImpulse(-3500)
    sprite('vr_screen_slashR', 32767)
    EndMomentum(1)
    loopRest()

@State
def ScreenSlashLeft():
    sprite('vr_screen_slashL', 20)
    RemoveOnCallStateEnd(2)
    FaceLeft()
    Unknown3079(1)
    RenderLayer(3)
    ScreenPosition(1)
    XPositionRelativeFacingAbsolute(640000)
    AbsoluteY(-384000)
    SetScaleX(1250)
    SetScaleY(750)
    sprite('vr_screen_slashL', 10)
    physicsYImpulse(1500)
    physicsXImpulse(2500)
    sprite('vr_screen_slashL', 10)
    physicsYImpulse(-500)
    physicsXImpulse(1000)
    sprite('vr_screen_slashL', 32767)
    EndMomentum(1)
    loopRest()

@State
def ScreenSlashTop():
    sprite('vr_screen_slashT', 20)
    CreateObject('ScreenOverTop', 0)
    RemoveOnCallStateEnd(2)
    FaceLeft()
    Unknown3079(1)
    RenderLayer(3)
    ScreenPosition(1)
    XPositionRelativeFacingAbsolute(640000)
    AbsoluteY(-384000)
    SetScaleX(1200)
    SetScaleY(750)
    sprite('vr_screen_slashT', 10)
    physicsYImpulse(-1500)
    physicsXImpulse(-2500)
    sprite('vr_screen_slashT', 10)
    physicsYImpulse(-500)
    physicsXImpulse(-1000)
    sprite('vr_screen_slashT', 32767)
    EndMomentum(1)
    loopRest()

@State
def ScreenSlashUnder():
    sprite('vr_screen_slashU', 20)
    CreateObject('ScreenOverUnder', 0)
    RemoveOnCallStateEnd(2)
    FaceLeft()
    Unknown3079(1)
    RenderLayer(3)
    ScreenPosition(1)
    XPositionRelativeFacingAbsolute(640000)
    AbsoluteY(-384000)
    SetScaleX(1200)
    SetScaleY(750)
    sprite('vr_screen_slashU', 10)
    physicsYImpulse(1500)
    physicsXImpulse(2500)
    sprite('vr_screen_slashU', 10)
    EndMomentum(1)
    sprite('vr_screen_slashU', 32767)
    EndMomentum(1)
    loopRest()

@State
def ScreenOverTop():
    sprite('vr_screen_over_t', 32767)
    FaceLeft()
    E0EAEffectPosition(2)
    RemoveOnCallStateEnd(2)
    RenderLayer(3)
    BlendMode_Normal()
    PaletteIndex(1)
    ScreenPosition(1)
    AddY(384000)
    SetScaleX(960)
    loopRest()

@State
def ScreenOverUnder():
    sprite('vr_screen_over_u', 32767)
    FaceLeft()
    E0EAEffectPosition(2)
    RemoveOnCallStateEnd(2)
    RenderLayer(3)
    BlendMode_Normal()
    PaletteIndex(1)
    ScreenPosition(1)
    AddY(-384000)
    SetScaleX(960)
    loopRest()

@State
def hbef_600_feather():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 1)
    CreateParticle('hbef_600feather', 100)
    gotoLabel(0)

@State
def hbef_600_feather2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 1)
    CreateParticle('hbef_600feather2', 100)

@State
def hbef_611_shadow():

    def upon_IMMEDIATE():
        AddX(96000)
        ForceBloomMaskOn(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(208)
        PaletteColor1(208)
        PaletteColor3(208)
        PaletteColor4(1)
        SetCustomPaletteAlpha(-1000)
    sprite('vr_hb611_00', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)
    sprite('vr_hb611_00', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)
    sprite('vr_hb611_00', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)

@State
def hbef_615_hibana():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AddY(-5000)
        AddX(-1000)
    sprite('null', 1)
    CreateParticle('hbef_615hibana', 100)

@State
def hbef_615_smoke():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AddY(-5000)
        AddX(-1000)
    sprite('null', 1)
    CreateParticle('hbef_615smoke', 100)

@State
def hbef_615_lead():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Flip()
        PaletteIndex(0)
        BlendMode_Normal()
        AddX(0)
        AddY(-128000)
        Rotation(5000)
        AddRotationPerFrame(-500)
    sprite('vr_hb615_00', 6)
    sprite('vr_hb615_00', 60)
    physicsXImpulse(-1000)
    physicsYImpulse(-5000)
    ConstantAlphaModifier(-20)

@State
def hbef_615_lead2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(0)
        BlendMode_Normal()
        AddX(0)
        AddY(-128000)
        Rotation(0)
    sprite('vr_hb615_00', 6)
    sprite('vr_hb615_00', 60)
    physicsXImpulse(-1000)
    physicsYImpulse(-5000)
    AddRotationPerFrame(-300)
    ConstantAlphaModifier(-20)

@State
def AmAstralDamage_karasu():

    def upon_IMMEDIATE():
        AddX(-60000)
        AddY(120000)
    label(0)
    sprite('hb901_01', 7)
    physicsYImpulse(-800)
    sprite('hb901_02', 4)
    physicsYImpulse(-400)
    sprite('hb901_03', 4)
    physicsYImpulse(800)
    sprite('hb901_04', 5)
    physicsYImpulse(400)
    loopRest()
    gotoLabel(0)

@State
def Kunai_Event():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        FloorCollision(1)
        CancelIfPlayerHit(3)
        NoAttackDuringAction(1)
        AddY(200000)

        def upon_32():
            RotationAngle(-30000)
            HitboxMovement(60000, -60000)

        def upon_33():
            RotationAngle(-20000)
            HitboxMovement(60000, -70000)

        def upon_34():
            RotationAngle(-10000)
            HitboxMovement(60000, -80000)

        def upon_ON_HIT_OR_BLOCK():
            NoAttackDuringAction(1)
        sendToLabelUpon(2, 0)
    sprite('vr_hb407_00', 60)
    label(0)
    sprite('vr_hb407_01', 10)
    CreateParticle('hbef_407stuck', 0)
    EndMomentum(1)
    EndAttack()
    clearUponHandler(54)
    clearUponHandler(10)
    clearUponHandler(3)
    sprite('keep', 20)
    ConstantAlphaModifier(-25)

@State
def hbef_611_shadow_Event():

    def upon_IMMEDIATE():
        ForceBloomMaskOn(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(208)
        PaletteColor1(208)
        PaletteColor3(208)
        PaletteColor4(1)
        SetCustomPaletteAlpha(-1000)
    sprite('vr_hb611_00', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)
    sprite('vr_hb611_00', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)
    sprite('vr_hb611_00', 6)
    sprite('vr_hb611_01', 6)
    sprite('vr_hb611_02', 6)

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
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Act3Event_BNvsHB00shadow():

    def upon_IMMEDIATE():
        ForceBloomMaskOn(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(208)
        PaletteColor1(208)
        PaletteColor3(208)
        PaletteColor4(1)
        SetCustomPaletteAlpha(-1000)
        AlphaValue(10)
    sprite('hb603_00', 6)
    ConstantAlphaModifier(10)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)

@State
def Act3Event_BNvsHB01shadow():

    def upon_IMMEDIATE():
        ForceBloomMaskOn(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(208)
        PaletteColor1(208)
        PaletteColor3(208)
        PaletteColor4(1)
        SetCustomPaletteAlpha(-1000)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)
    sprite('hb603_00', 6)