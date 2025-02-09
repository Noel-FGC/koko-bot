@State
def EMB_TK():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_TK.DIG', 'ef_emb_TK_motion_000.mmot')
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
def EMB_TK_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_TK.DIG', 'ef_emb_TK_motion_000.mmot')
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
def EMB_TK_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        SetPosXByScreenPer(50)
        AbsoluteY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_TK.DIG', 'ef_emb_TK_motion_000.mmot')
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
def EventCKRun():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        physicsXImpulse(-7200)
        ContinueState(600)
    label(0)
    sprite('ctk450_25', 7)
    sprite('ctk450_26', 7)
    sprite('ctk450_27', 7)
    sprite('ctk450_28', 7)
    loopRest()
    gotoLabel(0)

@State
def EventBN():
    sprite('bn000_11', 7)
    PaletteIndex(7)
    CreateParticle('bnef_throw_smoke', 0)
    CreateParticle('bnef_throw_leaf', 0)
    CommonSE('019_cloth_c')
    label(0)
    sprite('bn000_00', 7)
    sprite('bn000_01', 7)
    sprite('bn000_02', 7)
    sprite('bn000_03', 7)
    sprite('bn000_04', 7)
    sprite('bn000_05', 7)
    sprite('bn000_06', 7)
    sprite('bn000_07', 7)
    sprite('bn000_08', 7)
    sprite('bn000_09', 7)
    sprite('bn000_11', 7)
    loopRest()
    gotoLabel(0)

@State
def bn_shot():

    def upon_IMMEDIATE():
        PaletteIndex(7)
        CollideWithWall(1)
        ContinueState(360)
        Size(1250)
        RotationAngle(45000)
        physicsXImpulse(30000)
        physicsYImpulse(-30000)
        sendToLabelUpon(2, 1)
    sprite('vrbnef406_009', 4)
    CommonSE('000_airdash_1')
    label(0)
    sprite('vrbnef406_008', 4)
    sprite('vrbnef406_009', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CommonSE('105_guard_slash_0')
    CreateObject('bn_shot_reflect', -1)
    loopRest()

@State
def bn_shot_reflect():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        PaletteIndex(7)
        Size(1250)
        BlendMode_Normal()
    sprite('null', 2)
    sprite('vrbnef406_001', 60)
    AlphaValue(255)
    ConstantAlphaModifier(-4)
    AddRotationPerFrame(15000)
    physicsYImpulse(20000)
    physicsXImpulse(5000)
    setGravity(2000)
    CreateParticle('bnef_kugi_hit', -1)

@State
def tkef_throw():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    ParticleFacing(0)
    CallCustomizableParticle('tkef_throw', -1)

@State
def tkef061():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
    sprite('vrtkef061_00', 2)

@State
def tkef_hit_low():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    ParticleFacing(2)
    CallCustomizableParticle('tkef_hit_low', -1)
    PrivateSE('tkse_03')

@State
def tkef_hit_high():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    ParticleFacing(2)
    CallCustomizableParticle('tkef_hit_high', -1)
    PrivateSE('tkse_03')

@State
def tkef_hit_sp():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    ParticleFacing(2)
    CallCustomizableParticle('tkef_hit_sp', -1)

@State
def tkef_slash():

    def upon_IMMEDIATE():
        pass
    sprite('vrtkef_slash_dummy', -1)
    ParticleDeviation(15000, 75000)
    CallCustomizableParticle('tkef_hit_slash', 0)
    PrivateSE('tkse_08')

@State
def tkef_highslash():

    def upon_IMMEDIATE():
        pass
    sprite('vrtkef_slash_dummy', -1)
    ParticleDeviation(15000, 75000)
    CallCustomizableParticle('tkef_hit_highslash', 0)
    PrivateSE('tkse_09')

@State
def tkef202():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-100)
        SetScaleX(1000)
        SetScaleY(1000)
        RotationAngle(5000)
    sprite('vrtkef202_00', 1)
    sprite('vrtkef202_01', 1)
    sprite('vrtkef202_02', 2)
    RemoveOnCallStateEnd(0)
    sprite('vrtkef202_03', 3)
    sprite('vrtkef202_04', 3)
    sprite('vrtkef202_05', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef202b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-100)
        SetScaleX(1000)
        SetScaleY(1000)
        RotationAngle(0)
    sprite('vrtkef202_00', 1)
    sprite('vrtkef202_01', 1)
    sprite('vrtkef202_02', 2)
    RemoveOnCallStateEnd(0)
    sprite('vrtkef202_03', 3)
    sprite('vrtkef202_04', 3)
    sprite('vrtkef202_05', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef202c():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-100)
        SetScaleX(1000)
        SetScaleY(1000)
        RotationAngle(-5000)
    sprite('vrtkef202_00', 1)
    sprite('vrtkef202_01', 1)
    sprite('vrtkef202_02', 2)
    RemoveOnCallStateEnd(0)
    sprite('vrtkef202_03', 3)
    sprite('vrtkef202_04', 3)
    sprite('vrtkef202_05', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef232():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        AddY(50000)
        AddX(250000)
    CreateParticle('tkef_hit_slash_low', 0)
    sprite('vrtkef232_00', 5)
    sprite('vrtkef232_01', 5)
    RemoveOnCallStateEnd(0)
    sprite('vrtkef232_02', 5)
    sprite('vrtkef232_03', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef252():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleX(750)
        SetScaleY(750)
        AddY(-42000)
    sprite('vrtkef252_00', 3)
    sprite('vrtkef252_01', 3)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    SetZVal(500)
    sprite('vrtkef252_02', 3)
    sprite('vrtkef252_03', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef252b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleX(875)
        SetScaleY(750)
        AddY(-42000)
    sprite('vrtkef252_00', 3)
    sprite('vrtkef252_01', 3)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    SetZVal(500)
    sprite('vrtkef252_02', 3)
    sprite('vrtkef252_03', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef252c():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ForceShadowOff(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleX(750)
        SetScaleY(750)
        RotationAngle(0)
        AddY(-42000)
    sprite('vrtkef252_00', 3)
    sprite('vrtkef252_01', 3)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    SetZVal(500)
    sprite('vrtkef252_02', 3)
    sprite('vrtkef252_03', 12)
    AlphaValue(250)
    ConstantAlphaModifier(-22)

@State
def tkef203a():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddX(120000)
        AddY(256000)
        BlendMode_Add()
    sprite('vrtkef203_a00', 3)
    sprite('vrtkef203_a01', 4)
    sprite('vrtkef203_a02', 25)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-10)

@State
def tkef203b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddX(140000)
        AddY(200000)
        BlendMode_Add()
    sprite('vrtkef203_b00', 3)
    sprite('vrtkef203_b01', 4)
    sprite('vrtkef203_b02', 25)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-10)

@State
def tkef213():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddY(300000)
        AddX(200000)
        BlendMode_Add()
    sprite('vrtkef213_00', 2)
    sprite('vrtkef213_01', 2)
    sprite('vrtkef213_02', 4)
    sprite('vrtkef213_03', 42)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-6)

@State
def tkef213_2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddY(300000)
        AddX(100000)
        BlendMode_Add()
    sprite('vrtkef213_10', 4)
    sprite('vrtkef213_11', 4)
    sprite('vrtkef213_12', 42)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-6)

@State
def tkef253a():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddY(160000)
        AddX(64000)
        BlendMode_Add()
    sprite('vrtkef253_00', 2)
    sprite('vrtkef253_01', 2)
    sprite('vrtkef253_02', 25)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-10)

@State
def tkef253b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddY(160000)
        AddX(64000)
        BlendMode_Add()
    sprite('vrtkef253_10', 2)
    sprite('vrtkef253_11', 2)
    sprite('vrtkef253_12', 25)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-10)

@State
def tkef416a():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddY(140000)
        AddX(280000)
        BlendMode_Add()
    sprite('vrtkef416_00', 2)
    sprite('vrtkef416_01', 2)
    sprite('vrtkef416_02', 2)
    sprite('vrtkef416_03', 25)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-10)

@State
def tkef416b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        ForceShadowOff(1)
        PaletteIndex(2)
        AddY(140000)
        AddX(280000)
        BlendMode_Add()
    sprite('vrtkef416_10', 1)
    sprite('vrtkef416_11', 1)
    sprite('vrtkef416_12', 2)
    sprite('vrtkef416_13', 25)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(250)
    ConstantAlphaModifier(-10)

@Subroutine
def tk_shot_Init():
    AttackDefaults_SpecialProjectile()
    AttackLevel_(1)
    Damage(500)
    AttackP1(90)
    AttackP2(80)
    SameMoveProration(10)
    StarterRating(1)
    DamageEffect(2, 'tkef_hit_sp')
    if SLOT_137:
        DamageMultiplier(80)
    ForceShadowOff(1)
    Size(1000)
    PaletteIndex(1)
    CollideWithWall(1)
    ContinueState(450)

@State
def tk_shot_A():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        HeatGainMultiplier(500)
        PaletteIndex(0)
        AddRotationPerFrame(20000)
        physicsXImpulse(20000)
        physicsYImpulse(28000)
        setGravity(1200)

        def upon_ON_HIT_OR_BLOCK():
            YSpeed(22500)
            XSpeed(-10000)
            setGravity(2400)
            SetScaleSpeed(20)
    sprite('vrtkef412_30', 32767)

@State
def tk_shot_A2():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        GroundedHitstunAnimation(9)
        Hitstop(0)
        AirUntechableTime(30)
        AddRotationPerFrame(200)
        physicsXImpulse(20000)
        physicsYImpulse(28000)
        setGravity(1200)
        sendToLabelUpon(10, 1)
    label(0)
    sprite('vrtkef412_21', 1)
    CreateObject('BombHibana', 0)
    CreateParticle('tkef_412a_bomsmoke', 0)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(10)
    sprite('vrtkef412_21', 1)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    CreateParticle('tkef_expl', 0)
    sprite('vrtkef412_21', 1)
    RefreshMultihit()

@State
def BombHibana():

    def upon_IMMEDIATE():
        LinkParticle('tkef_412a_bomsparks')
        E0EAEffectPosition(2)
    sprite('null', 10)

@State
def tk_shot_A3():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        Hitstop(0)
        AddRotationPerFrame(15000)
        physicsXImpulse(20000)
        physicsYImpulse(28000)
        setGravity(1200)
        sendToLabelUpon(10, 1)
    sprite('vrtkef412_20', 32767)
    loopRest()
    label(1)
    clearUponHandler(10)
    sprite('vrtkef412_20', 20)
    AddRotationPerFrame(25000)
    physicsYImpulse(36000)
    physicsXImpulse(2200)
    setGravity(1800)
    sendToLabelUpon(10, 2)
    sprite('vrtkef412_20', 32767)
    RefreshMultihit()
    loopRest()
    label(2)
    clearUponHandler(10)
    sprite('vrtkef412_20', 32767)
    YSpeed(22500)
    XSpeed(1200)
    loopRest()

@State
def tk_shot_A4():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        EnableAfterimage(1)
        AddRotationPerFrame(30000)
        physicsXImpulse(20000)
        physicsYImpulse(28000)
        setGravity(1200)

        def upon_ON_HIT_OR_BLOCK():
            EnableAfterimage(0)
            YSpeed(22500)
            XSpeed(-10000)
            setGravity(2400)
            SetScaleSpeed(20)
    sprite('vrtkef412_22', 32767)

@State
def tk_shot_B():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        EnableAfterimage(1)
        AddRotationPerFrame(45000)
        physicsXImpulse(48000)
        physicsYImpulse(3000)
        setGravity(400)

        def upon_ON_HIT_OR_BLOCK():
            EnableAfterimage(0)
            YSpeed(30000)
            XSpeed(-10000)
            setGravity(2400)
    sprite('vrtkef412_00', 32767)

@State
def tk_shot_B2():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        EnableAfterimage(1)
        CollideWithWall(0)
        ScreenCollision(1)
        AddRotationPerFrame(75000)
        physicsXImpulse(48000)
        physicsYImpulse(3000)
        setGravity(400)
        sendToLabelUpon(7, 1)
        sendToLabelUpon(10, 2)
        if CharacterIDCheck('ta'):
            clearUponHandler(7)
            ScreenCollision(0)
    sprite('vrtkef412_01', 32767)
    loopRest()
    label(1)
    clearUponHandler(7)
    sprite('null', 120)
    CancelIfPlayerHit(3)
    ScreenCollision(0)
    XPositionRelativeFacing(-2000000)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('vrtkef412_01', 32767)
    physicsXImpulse(48000)
    loopRest()
    label(2)
    clearUponHandler(7)
    clearUponHandler(10)
    sprite('vrtkef412_01', 32767)
    EnableAfterimage(0)
    YSpeed(30000)
    XSpeed(-10000)
    setGravity(2400)
    CollideWithWall(1)
    ScreenCollision(0)
    loopRest()

@State
def tk_shot_B3():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        Hitstop(18)
        CHGroundedHitstunAnimation(2)
        EnableAfterimage(1)
        AddRotationPerFrame(22500)
        physicsXImpulse(48000)
        physicsYImpulse(3000)
        setGravity(400)

        def upon_ON_HIT_OR_BLOCK():
            EnableAfterimage(0)
            YSpeed(30000)
            XSpeed(-10000)
            setGravity(2400)
    sprite('vrtkef412_02', 32767)

@State
def tk_shot_C():

    def upon_IMMEDIATE():
        callSubroutine('tk_shot_Init')
        AirPushbackY(15000)
        physicsXImpulse(2000)
        physicsYImpulse(18000)
        setGravity(1600)
        FloorCollision(1)
        AttackOff()

        def upon_5():
            if (SLOT_2 == 0):
                YAccel(-50)
                CreateParticle('tkef_412c_ballbound', 0)
                CommonSE('209_down_normal_0')
                RefreshMultihit()
                XImpulseAcceleration(300)
            if (SLOT_2 == 1):
                YAccel(-50)
                CommonSE('209_down_normal_0')
            if (SLOT_2 == 2):
                physicsYImpulse(0)
                CommonSE('209_down_normal_0')
            AddActionMark(1)
            RefreshMultihit()
        SLOT_59 = 2

        def upon_32():
            SLOT_59 = 3

        def upon_ON_HIT_OR_BLOCK():
            setGravity(1600)
            physicsYImpulse(9000)
            SLOT_59 = (SLOT_59 + (-1))
            if (SLOT_59 == 0):
                FloorCollision(0)
                clearUponHandler(5)

        def upon_44():
            AttackOff()
            FloorCollision(0)
            clearUponHandler(5)
        SetPrivateValue(0, 1)

        def upon_STATE_END():
            SetPrivateValue(0, 0)

        def upon_FRAME_STEP():
            if (SLOT_22 > 2000000):
                DeleteObject(23)
            if (SLOT_22 < (-2000000)):
                DeleteObject(23)
            if (SLOT_23 < (-2000000)):
                DeleteObject(23)
        if CharacterIDCheck('ta'):
            clearUponHandler(3)

            def upon_FRAME_STEP():
                if (SLOT_22 > 5500000):
                    DeleteObject(23)
                if (SLOT_22 < (-5500000)):
                    DeleteObject(23)
                if (SLOT_23 < (-2000000)):
                    DeleteObject(23)
    sprite('vrtkef412_10_dummy', 32767)
    CreateObject('tk_shot_C_roll', 0)
    CreateObject('tk_shot_C_shadow', 0)

@State
def tk_shot_C_roll():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(0)
        Size(1000)
        PaletteIndex(1)
        CollideWithWall(1)
        ForceShadowOff(1)
        E0EAEffect('cmn_judgment', 65535)
        ApplyFunctionsToObjects(1)
        AbsoluteY(80000)
        ApplyFunctionsToSelf()
        AddRotationPerFrame(7500)
    sprite('vrtkef412_10', 32767)

@State
def tk_shot_C_shadow():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Sub()
    sprite('vrtkef412_11', 32767)

@State
def GuardCrash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        FaceLeft()
    sprite('null', 30)
    LinkParticle('tkef_guardcrash')

@State
def chocho():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        AbsoluteY(300000)
        XPositionRelativeFacing(1800000)
        BlendMode_Normal()
        EnableAfterimage(1)

        def upon_FRAME_STEP():
            RandSpeedX(-1000, 1000)
            RandSpeedY(-1000, 1000)
            XImpulseAcceleration(90)
            YAccel(90)

        def upon_32():
            YSpeed(25000)
            XSpeed(-15000)
    label(1)
    PaletteIndex(1)
    sprite('vr_chocho00', 4)
    CreateParticle('tkef_butterfly_powder', -1)
    loopRest()
    sprite('vr_chocho01', 4)
    CreateParticle('tkef_butterfly_powder', -1)
    loopRest()
    sprite('vr_chocho02', 4)
    CreateParticle('tkef_butterfly_powder', -1)
    loopRest()
    gotoLabel(1)

@State
def denchu():

    def upon_IMMEDIATE():
        ForceShadowOff(1)
        ForceBloomMaskOn(1)
        PaletteIndex(1)
    sprite('vr_denchu', 32767)
    XPositionRelativeFacing(1800000)
    SetZVal(500)

@State
def tk600HandX():
    sprite('vrtk600_hand', 4)
    ForceShadowOff(1)
    RenderLayer(1)
    RotationAngle(90000)
    SetZVal(-500)
    XPositionRelativeFacing(-820000)
    AbsoluteY(680000)
    physicsXImpulse(50000)
    sprite('vrtk600_hand', 90)
    physicsXImpulse(0)
    sprite('vrtk600_hand', 4)
    physicsXImpulse(-50000)

@State
def tk600HandY():
    sprite('vrtk600_hand', 4)
    ForceShadowOff(1)
    RenderLayer(1)
    SetZVal(-500)
    XPositionRelativeFacing(-220000)
    AbsoluteY(-360000)
    physicsYImpulse(50000)
    sprite('vrtk600_hand', 90)
    physicsYImpulse(0)
    sprite('vrtk600_hand', 4)
    physicsYImpulse(-50000)

@State
def tk600Eye():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ForceShadowOff(1)
    label(0)
    sprite('vrtk600_eye', 30)
    RotationAngle(45000)
    Size(1000)
    sprite('vrtk600_eye', 4)
    SetScaleSpeedY(10)
    sprite('vrtk600_eye', 9)
    PrivateSE('tkse_07')
    SetScaleX(1200)
    SetScaleY(100)
    SetScaleSpeed(0)
    sprite('vrtk600_eye', 2)
    SetScaleSpeedY(10)
    Size(1000)
    sprite('vrtk600_eye', 9)
    PrivateSE('tkse_07')
    SetScaleX(1200)
    SetScaleY(100)
    SetScaleSpeed(0)
    sprite('vrtk600_eye', 40)
    Size(1000)
    loopRest()
    gotoLabel(0)

@State
def tk600Mouth():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ForceShadowOff(1)
    label(0)
    sprite('vrtk600_mouth', 20)
    SetScaleSpeed(5)
    sprite('vrtk600_mouth', 20)
    SetScaleSpeed(-5)
    loopRest()
    gotoLabel(0)

@State
def tk600Face():
    sprite('null', 4)
    RenderLayer(1)
    CreateObject('tk600HandX', -1)
    CreateObject('tk600HandY', -1)
    ScreenShake(20000, 20000)
    CommonSE('211_down_steal_0')
    ForceShadowOff(1)
    sprite('vrtk600_face', 4)
    SetZVal(-500)
    CreateObject('tk600Eye', 0)
    CreateObject('tk600Eye', 1)
    CreateObject('tk600Mouth', 2)
    XPositionRelativeFacing(-1000000)
    AbsoluteY(380000)
    physicsXImpulse(200000)
    PrivateSE('tkse_06')
    PrivateSE('tkse_06')
    sprite('vrtk600_face', 40)
    physicsXImpulse(0)
    ParticleLayer(1)
    CallCustomizableParticle('tkef_breath', 2)
    sprite('vrtk600_face', 40)
    ParticleLayer(1)
    CallCustomizableParticle('tkef_breath', 2)
    sprite('vrtk600_face', 16)
    physicsXImpulse(-80000)

@State
def vrtkef430_upR():

    def upon_IMMEDIATE():
        SetScaleX(2000)
        SetScaleY(2000)
        RotationAngle(120000)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrtkef430_00', 12)
    sprite('vrtkef430_01', 4)
    sprite('vrtkef430_02', 4)
    sprite('vrtkef430_03', 4)

@State
def vrtkef430_downR():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        SetScaleX(2000)
        SetScaleY(2000)
        RotationAngle(45000)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrtkef430_00', 12)
    sprite('vrtkef430_01', 4)
    sprite('vrtkef430_02', 4)
    sprite('vrtkef430_03', 4)

@State
def vrtkef430_upL():

    def upon_IMMEDIATE():
        SetScaleX(2000)
        SetScaleY(2000)
        RotationAngle(-120000)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrtkef430_00', 12)
    sprite('vrtkef430_01', 4)
    sprite('vrtkef430_02', 4)
    sprite('vrtkef430_03', 4)

@State
def vrtkef430_downL():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        SetScaleX(2000)
        SetScaleY(2000)
        RotationAngle(-45000)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrtkef430_00', 12)
    sprite('vrtkef430_01', 4)
    sprite('vrtkef430_02', 4)
    sprite('vrtkef430_03', 4)

@State
def vrtkef431_00():
    PaletteIndex(1)
    SetScaleX(1000)
    SetScaleY(1000)
    SetZVal(-500)
    sprite('vrtkef431_00', 60)

@State
def vrtkef431_01():
    sprite('vrtkef431_01', 15)
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    RotationAngle(25000)
    SetZVal(-500)
    PrivateSE('tkse_03')
    sprite('vrtkef431_01', 10)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrtkef431_01', 8)
    physicsXImpulse(-10000)
    physicsYImpulse(-10000)

@State
def vrtkef431_02():
    sprite('vrtkef431_02', 12)
    AddRotationPerFrame(5000)
    physicsXImpulse(-35000)
    physicsYImpulse(25000)
    SetZVal(-500)
    PrivateSE('tkse_03')
    sprite('vrtkef431_02', 12)
    physicsXImpulse(35000)
    physicsYImpulse(-25000)

@State
def vrtkef431_03():
    sprite('vrtkef431_03', 10)
    physicsYImpulse(30000)
    SetZVal(-500)
    PrivateSE('tkse_03')
    sprite('vrtkef431_03', 10)
    physicsYImpulse(0)
    sprite('vrtkef431_03', 8)
    physicsYImpulse(-30000)

@State
def vrtkef431_04():
    sprite('vrtkef431_04', 8)
    physicsXImpulse(50000)
    SetZVal(-500)
    PrivateSE('tkse_03')
    sprite('vrtkef431_04', 10)
    physicsXImpulse(0)
    sprite('vrtkef431_04', 8)
    physicsXImpulse(-50000)

@State
def BunshinAtkObj():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        CopyAttackValues(2)
        DamageMultiplier(50)
        AttackP2(100)
        SameMoveProration(-1)
        PassByArmor(1)
        GuardCrush(0, 1)
        DefeatOpponentBehavior(1)
        Visibility(1)
    sprite('vrdmy_bunshin_atk', 17)
    StartMultihit()
    sprite('vrdmy_bunshin_atk', 3)

@State
def AstWhite():
    sprite('vr_white', 20)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(255)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-15)

@State
def AST_TkAttack():
    sprite('null', 12)
    XPositionRelativeFacing(560000)
    AbsoluteY(-150000)
    CreateObject('AST_TkAttackA', -1)
    sprite('null', 12)
    XPositionRelativeFacing(0)
    AbsoluteY(500000)
    CreateObject('AST_TkAttackB', -1)
    sprite('null', 12)
    XPositionRelativeFacing(-560000)
    AbsoluteY(-150000)
    CreateObject('AST_TkAttackC', -1)
    sprite('null', 12)
    XPositionRelativeFacing(560000)
    AbsoluteY(340000)
    CreateObject('AST_TkAttackD', -1)
    sprite('null', 12)
    XPositionRelativeFacing(-560000)
    AbsoluteY(340000)
    CreateObject('AST_TkAttackE', -1)
    sprite('null', 12)
    XPositionRelativeFacing(560000)
    AbsoluteY(-100000)
    CreateObject('AST_CtkAttackA', -1)
    sprite('null', 12)
    XPositionRelativeFacing(0)
    AbsoluteY(550000)
    CreateObject('AST_CtkAttackB', -1)
    sprite('null', 12)
    XPositionRelativeFacing(-560000)
    AbsoluteY(-100000)
    CreateObject('AST_CtkAttackC', -1)
    sprite('null', 12)
    XPositionRelativeFacing(560000)
    AbsoluteY(500000)
    CreateObject('AST_CtkAttackD', -1)
    sprite('null', 14)
    XPositionRelativeFacing(-560000)
    AbsoluteY(500000)
    CreateObject('AST_CtkAttackE', -1)
    sprite('null', 19)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    CreateObject('AST_CtkAttackLast', -1)
    sprite('null', 19)

@State
def AST_TkAttackA():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(100)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AttackDirection(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(30000)
        DamageFromStateOnly('AST_TkAttackB')
        EnableAfterimage(1)
    sprite('tk450_08', 3)
    sprite('tk450_09', 3)
    Voiceline('tk297')
    sprite('tk450_10', 15)
    sprite('null', 30)

@State
def AST_TkAttackB():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(100)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirPushbackX(-50000)
        AirPushbackY(-30000)
        OppPositionOnHit(2, 0, 300000)
        DamageFromStateOnly('AST_TkAttackC')
        EnableAfterimage(1)
    sprite('tk450_11', 3)
    sprite('tk450_12', 3)
    Voiceline('tk298')
    sprite('tk450_13', 15)
    sprite('null', 30)

@State
def AST_TkAttackC():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(100)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        YImpulseBeforeWallbounce(1600)
        AirPushbackX(100000)
        AirPushbackY(40000)
        DamageFromStateOnly('AST_TkAttackD')
        EnableAfterimage(1)
    sprite('tk450_14', 3)
    sprite('tk450_15', 3)
    Voiceline('tk295')
    sprite('tk450_16', 15)
    sprite('null', 30)

@State
def AST_TkAttackD():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(100)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirPushbackX(-95000)
        AirPushbackY(10000)
        DamageFromStateOnly('AST_TkAttackE')
        EnableAfterimage(1)
    sprite('tk450_17', 3)
    sprite('tk450_18', 3)
    Voiceline('tk296')
    sprite('tk450_19', 15)
    sprite('null', 30)

@State
def AST_TkAttackE():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(100)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirPushbackX(100000)
        AirPushbackY(-32000)
        DamageFromStateOnly('AST_CtkAttackA')
        EnableAfterimage(1)
    sprite('tk450_20', 4)
    sprite('tk450_21', 3)
    Voiceline('tk297')
    sprite('tk450_22', 15)
    sprite('null', 30)

@State
def AST_CtkAttackA():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(10)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(-50000)
        AirPushbackY(30000)
        DamageFromStateOnly('AST_CtkAttackB')
        EnableAfterimage(1)
    sprite('ctk450_00', 3)
    sprite('ctk450_01', 5)
    sprite('ctk450_02', 15)
    sprite('null', 30)

@State
def AST_CtkAttackB():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(10)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirPushbackX(-60000)
        AirPushbackY(-28000)
        OppPositionOnHit(2, 0, 260000)
        DamageFromStateOnly('AST_CtkAttackC')
        EnableAfterimage(1)
    sprite('ctk450_03', 4)
    sprite('ctk450_04', 4)
    sprite('ctk450_05', 15)
    sprite('null', 30)

@State
def AST_CtkAttackC():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(10)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        Floorslide(30)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(110000)
        AirPushbackY(50000)
        DamageFromStateOnly('AST_CtkAttackD')
        EnableAfterimage(1)
    sprite('ctk450_06', 2)
    sprite('ctk450_07', 4)
    sprite('ctk450_08', 15)
    sprite('null', 30)

@State
def AST_CtkAttackD():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(10)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AttackDirection(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(110000)
        AirPushbackY(2000)
        DamageFromStateOnly('AST_CtkAttackE')
        EnableAfterimage(1)
    sprite('ctk450_09', 2)
    sprite('ctk450_10', 5)
    sprite('ctk450_11', 15)
    sprite('null', 30)

@State
def AST_CtkAttackE():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(10)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirPushbackX(38000)
        AirPushbackY(-20000)
        DamageFromStateOnly('AST_CtkAttackLast')
        EnableAfterimage(1)
    sprite('ctk450_12', 2)
    sprite('ctk450_13', 5)
    sprite('ctk450_14', 15)
    sprite('null', 30)

@State
def AST_CtkAttackLast():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(1)
        Damage(20)
        MinimumDamage(100)
        DamageEffect(2, 'tkef_hit_high')
        AirUntechableTime(400)
        HardKnockdown(3)
        Hitstop(3)
        YImpulseBeforeWallbounce(1600)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(108000)
        YImpulseBeforeWallbounce(1600)
        OppPositionOnHit(2, 0, 100000)
        DamageFromStateOnly('AstralHeat2')
    sprite('ctk450_15', 3)
    sprite('ctk450_16', 6)
    AddCombo(1)
    sprite('ctk450_17', 15)
    sprite('ctk450_17', 15)
    Visibility(1)
    CreateObject('ctk_run1', 0)
    CreateObject('ctk_run2', 1)

@State
def tkef450_jyubei():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        ForceShadowOff(1)
        SetZVal(-100)
        ContinueState(200)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(4)
        AfterimageMask_1(0, 255, 0, 128)
        AfterimageMask_2(0, 128, 0, 255)
        AfterimageSize_1(1010)
        AfterimageSize_2(1100)
        XPositionRelativeFacing(640000)
        AbsoluteY(440000)
        XSpeed(-280000)
        YSpeed(-5000)
    sprite('vrtkef450_00', 2)
    sprite('vrtkef450_01', 2)
    EndMomentum(1)
    sprite('vrtkef450_02', 2)
    sprite('vrtkef450_00', 2)
    sprite('vrtkef450_01', 2)
    sprite('vrtkef450_02', 2)
    sprite('vrtkef450_00', 2)
    sprite('vrtkef450_01', 2)
    sprite('vrtkef450_02', 2)
    sprite('vrtkef450_00', 2)
    sprite('vrtkef450_01', 2)
    sprite('vrtkef450_02', 2)
    sprite('vrtkef450_00', 2)
    sprite('vrtkef450_01', 2)
    sprite('vrtkef450_02', 2)
    sprite('vrtkef450_00', 1)
    XSpeed(-40000)
    YSpeed(-10000)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)
    sprite('vrtkef450_00', 1)
    sprite('vrtkef450_01', 1)
    sprite('vrtkef450_02', 1)

@State
def tkef450_tora():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        ForceShadowOff(1)
        SetZVal(-100)
        ContinueState(200)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(4)
        AfterimageMask_1(0, 255, 0, 128)
        AfterimageMask_2(0, 128, 0, 255)
        AfterimageSize_1(1010)
        AfterimageSize_2(1100)
        XPositionRelativeFacing(740000)
        AbsoluteY(240000)
        XSpeed(-280000)
        YSpeed(-5000)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    EndMomentum(1)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t13ex00', 2)
    sprite('tk432_t12ex00', 2)
    sprite('tk432_t12ex00', 1)
    XSpeed(-40000)
    YSpeed(-30000)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)
    sprite('tk432_t13ex00', 1)
    sprite('tk432_t12ex00', 1)

@State
def tkef450_jyubei_win():

    def upon_IMMEDIATE():
        SetZVal(100)
        XPositionRelativeFacing(-690000)
        AbsoluteY(0)
        physicsXImpulse(3000)
    sprite('vrtkef450_03', 16)
    sprite('vrtkef450_03', 60)
    physicsXImpulse(0)
    sprite('vrtkef450_03', 60)
    physicsXImpulse(-6000)

@State
def ctk_run1():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        ContinueState(240)
        CollideWithWall(1)
        physicsXImpulse(-16000)
    label(0)
    sprite('ctk450_21', 3)
    sprite('ctk450_22', 3)
    sprite('ctk450_23', 3)
    sprite('ctk450_24', 3)
    loopRest()
    gotoLabel(0)

@State
def ctk_run2():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        Flip()
        ContinueState(240)
        CollideWithWall(1)
        physicsXImpulse(-16000)
    label(0)
    sprite('ctk450_21', 3)
    sprite('ctk450_22', 3)
    sprite('ctk450_23', 3)
    sprite('ctk450_24', 3)
    loopRest()
    gotoLabel(0)

@State
def tkef450_?():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        FaceLeft()
    sprite('vrtkef450_10', 5)
    Size(500)
    SetScaleSpeed(100)
    sprite('vrtkef450_10', 13)
    Size(1000)
    SetScaleSpeed(0)

@State
def LookAtMeAstStart():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        CameraControlEnable(1)
    sprite('null', 60)

@State
def LookAtMe():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        RemoveOnCallStateEnd(2)
    sprite('null', 32767)
    CameraControlEnable(1)

@State
def UltimateAirRushAttackTao():

    def upon_IMMEDIATE():
        pass
    sprite('null', 45)
    CreateObject('UltimateAirRushAttackTaoJ8D', -1)
    sprite('null', 25)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    sprite('null', 10)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    sprite('null', 8)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    sprite('null', 6)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 32)
    sprite('null', 4)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    sprite('null', 4)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    sprite('null', 20)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    sprite('null', 1)
    ObjectUpon(3, 32)

@State
def UltimateAirRushAttackODTao():

    def upon_IMMEDIATE():
        pass
    sprite('null', 45)
    CreateObject('UltimateAirRushAttackTaoJ8D', -1)
    ObjectUpon(1, 35)
    sprite('null', 25)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 25)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 15)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 10)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 8)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 8)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 6)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 6)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 4)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 4)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 3)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 3)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 3)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 2)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 2)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 2)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 2)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 2)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ5D', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 1)
    CreateObject('UltimateAirRushAttackTaoJ2D', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 35)
    sprite('null', 1)
    ObjectUpon(3, 32)

@Subroutine
def UltimateAirRushAttackTaoInit():
    AttackLevel_(3)
    Damage(160)
    AttackP2(100)
    AirPushbackY(2500)
    AirPushbackX(0)
    YImpulseBeforeWallbounce(100)
    AirUntechableTime(60)
    Hitstop(1)
    DamageEffect(2, 'tkef_highslash')
    CHStateIfCHStart(3)
    DefeatOpponentBehavior(1)
    OnlyHitPlayer(1)
    PassByArmor(1)
    VoodooDamageMultiplier(2)
    MinimumDamage(15)
    CopyFromRightToLeft(23, 2, 2, 3, 2, 66)
    if SLOT_2:
        SLOT_78 = 70
    NoDamageAction(1)
    EndMomentum(1)
    EnableAfterimage(1)
    AfterimageBlendMode(0)

@State
def UltimateAirRushAttackTaoJ8D():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        callSubroutine('UltimateAirRushAttackTaoInit')
        AlphaValue(0)

        def upon_35():
            AttackType(4)
            Damage(100)
            if SLOT_137:
                DamageMultiplier(80)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('tk400_01', 10)
    sprite('tk400_01', 5)
    ConstantAlphaModifier(51)
    TeleportToObject(22)
    AddX(-400000)
    AddY(-800000)
    sprite('tk400_01', 2)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    physicsYImpulse(9000)
    SmartRandomVoiceline('tk260', 100, 'tk261', 100, '', 0, '', 0)
    sprite('tk400_02', 2)
    sprite('tk401_00', 2)
    XSpeed(70000)
    physicsYImpulse(120000)
    PrivateSE('tkse_01')
    sprite('tk401_01', 4)
    AirDashEffects(1)
    sprite('tk401_02', 4)

@State
def UltimateAirRushAttackTaoJ5D():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        callSubroutine('UltimateAirRushAttackTaoInit')

        def upon_32():
            TeleportToObject(22)
            AddX(-1000000)
            ForceFaceSprite()

        def upon_33():
            TeleportToObject(22)
            AddX(1000000)
            ForceFaceSprite()

        def upon_35():
            AttackType(4)
            Damage(100)
            if SLOT_137:
                DamageMultiplier(80)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('tk400_01', 1)
    sprite('tk400_03', 1)
    XSpeed(140000)
    physicsYImpulse(0)
    PrivateSE('tkse_01')
    SmartRandomVoiceline('tk260', 100, 'tk261', 100, '', 0, '', 0)
    sprite('tk400_07', 3)
    RefreshMultihit()
    AirDashEffects(1)
    sprite('tk400_08', 3)
    sprite('tk400_07', 3)
    sprite('tk400_08', 3)

@State
def UltimateAirRushAttackTaoJ2D():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        callSubroutine('UltimateAirRushAttackTaoInit')

        def upon_32():
            TeleportToObject(22)
            AddX(-450000)
            AddY(700000)
            ForceFaceSprite()

        def upon_33():
            TeleportToObject(22)
            AddX(450000)
            AddY(700000)
            ForceFaceSprite()

        def upon_35():
            AttackType(4)
            Damage(100)
            if SLOT_137:
                DamageMultiplier(80)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('tk404_00', 1)
    sprite('tk404_04', 1)
    PrivateSE('tkse_01')
    XSpeed(40000)
    physicsYImpulse(-80000)
    SmartRandomVoiceline('tk260', 100, 'tk261', 100, '', 0, '', 0)
    sprite('tk404_05', 3)
    RefreshMultihit()
    AirDashEffects(1)
    sprite('tk404_06', 3)
    sprite('tk404_07', 3)
    sprite('tk404_05', 3)
    sprite('tk404_06', 3)

@State
def UltimateAirRushTorakaka():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        EndMomentum(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        SetZVal(500)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(3)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(4)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(5)

        def upon_36():
            clearUponHandler(36)
            sendToLabel(6)
    sprite('tk432_t00', 1)
    AddX(-50000)
    AddY(75000)
    sprite('tk400_01', 2)
    sprite('tk400_02', 2)
    sprite('tk401_00', 2)
    sprite('tk432_t01', 2)
    AirDashEffects(1)
    sprite('tk432_t02', 4)
    label(0)
    sprite('tk432_t01', 4)
    sprite('tk432_t02', 4)
    gotoLabel(0)
    label(1)
    sprite('tk432_t03', 2)
    AddX(120000)
    AddY(-100000)
    sprite('tk432_t04', 2)
    sprite('tk432_t05', 2)
    sprite('tk432_t06', 2)
    sprite('tk432_t07', 2)
    sprite('tk432_t08', 2)
    sprite('tk432_t05', 2)
    sprite('tk432_t06', 2)
    sprite('tk432_t07', 2)
    sprite('tk432_t08', 2)
    sprite('tk432_t05', 2)
    sprite('tk432_t06', 2)
    sprite('tk432_t07', 2)
    sprite('tk432_t08', 2)
    sprite('tk432_t09', 6)
    sprite('tk432_t10', 10)
    sprite('tk432_t11', 3)
    label(2)
    sprite('tk432_t12', 3)
    sprite('tk432_t13', 3)
    gotoLabel(2)
    label(3)
    sprite('tk432_t14', 3)
    sprite('tk432_t15', 3)
    gotoLabel(3)
    label(4)
    sprite('tk432_t16', 2)
    sprite('tk432_t17', 2)
    sprite('tk432_t18', 2)
    sprite('tk432_t19', 32767)
    label(5)
    sprite('tk432_t20', 2)
    sprite('tk432_t21', 2)
    sprite('tk432_t22', 2)
    sprite('tk432_t23', 2)
    sprite('tk432_t24', 2)
    sprite('tk432_t25', 32767)
    label(6)
    sprite('tk432_t26', 3)
    AddY(25000)
    LandingEffects(100, 1, 1)
    sprite('tk432_t27', 3)
    sprite('tk432_t28', 3)
    sprite('tk432_t29', 3)
    sprite('tk432_t30', 3)
    sprite('tk432_t31', 3)
    sprite('tk432_t32', 2)
    sprite('tk432_t33', 5)
    physicsYImpulse(11400)
    EndYPhysicsImpulse()
    JumpEffects(3, 100)
    sprite('tk432_t33', 4)
    physicsYImpulse(0)
    setGravity(200)
    sprite('tk432_t00', 2)
    AirDashEffects(1)
    XSpeed(20000)
    physicsYImpulse(45000)
    PrivateSE('tkse_01')
    sprite('tk432_t01', 2)
    sprite('tk432_t02', 2)
    sprite('tk432_t00', 2)
    sprite('tk432_t01', 2)
    sprite('tk432_t02', 2)

@Subroutine
def Func_BurstDD():
    ContinueState(300)
    if SLOT_7:
        physicsXImpulse(25000)
        Flip()
    else:
        physicsXImpulse(-25000)
    SetZVal(100)
    AddY(-12500)

    def upon_32():
        SetZVal(-500)
        AddY(-12500)

    def upon_33():
        SetZVal(-100)
        AddY(4166)

    def upon_34():
        SetZVal(100)
        AddY(20833)
    Unknown61(0, 1, 0, 4, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_2 = SLOT_0
    if (SLOT_2 <= 1):
        sendToLabel(1)
    if (SLOT_2 == 2):
        SLOT_51 = 1
        sendToLabel(2)
    if (SLOT_2 == 3):
        SLOT_52 = 1
        sendToLabel(3)
    if (SLOT_2 >= 4):
        sendToLabel(4)
    RunLoopUpon(17, 30)

    def upon_17():
        CollideWithWall(1)

@State
def BurstDD_ChibiMatome():

    def upon_IMMEDIATE():
        SetActionMark(5)
        if SLOT_7:
            SetPosXByScreenPer(-50)
        else:
            SetPosXByScreenPer(150)
    sprite('null', 1)
    CreateObject('BurstDD_Chibi1st', -1)
    label(0)
    sprite('null', 3)
    AddActionMark(-1)
    CreateObject('BurstDD_Chibi', -1)
    ObjectUpon(1, 33)
    sprite('null', 3)
    CreateObject('BurstDD_Chibi', -1)
    ObjectUpon(1, 34)
    sprite('null', 3)
    CreateObject('BurstDD_Chibi', -1)
    ObjectUpon(1, 32)
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('null', 1)
    sprite('null', 100)
    CreateObject('BurstDD_ChibiLast', -1)

@State
def BurstDD_Chibi1st():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(440)
        AttackP2(100)
        Hitstun(40)
        AirUntechableTime(400)
        Hitstop(0)
        EnemyHitstopAddition(-1, -1, -1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(-10000)
        DamageFromStateOnly('BurstDD_Chibi1st')
        DefeatOpponentBehavior(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        CHStateIfCHStart(3)
        PassByArmor(1)
        CopyFromRightToLeft(23, 2, 2, 3, 2, 66)
        if SLOT_2:
            SLOT_78 = 70

        def upon_45():
            CopyFromRightToLeft(23, 2, 51, 3, 2, 22)
            if SLOT_38:
                PrivateFunction(1, 2, 51, 2, 22, 2, 52)
            else:
                PrivateFunction(1, 2, 22, 2, 51, 2, 52)
            if (SLOT_52 <= 100000):
                ObjectUpon(3, 32)
                clearUponHandler(45)

        def upon_OPPONENT_HIT():
            clearUponHandler(12)
            SetActionMark(26)

            def upon_FRAME_STEP():
                if (not SLOT_2):
                    clearUponHandler(3)
                    RefreshMultihit()
                    Damage(0)
                    HitsparkSize(0)
                    HitAnywhere(1)
                    AirPushbackX(-25000)
                    AirPushbackY(-1)
                    YImpulseBeforeWallbounce(0)
                    if SLOT_5:
                        DamageFromStateOnly('BurstDD_BokosukaSP')
                    else:
                        DamageFromStateOnly('BurstDD_Bokosuka')
                    if SLOT_51:
                        GroundedHitstunAnimation(17)
                        AirHitstunAnimation(17)
                    if SLOT_52:
                        GroundedHitstunAnimation(9)
                        AirHitstunAnimation(9)
                else:
                    AddActionMark(-1)
        callSubroutine('Func_BurstDD')
    label(1)
    sprite('vrctk440_00', 2)
    LandingEffects(100, 1, 1)
    sprite('vrctk440_01', 2)
    sprite('vrctk440_02', 2)
    sprite('vrctk440_03', 2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('vrctk440_04', 2)
    LandingEffects(100, 1, 1)
    sprite('vrctk440_05', 2)
    sprite('vrctk440_06', 2)
    sprite('vrctk440_07', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('vrctk440_08', 2)
    LandingEffects(100, 1, 1)
    sprite('vrctk440_09', 2)
    sprite('vrctk440_10', 2)
    sprite('vrctk440_11', 2)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('vrctk440_12', 2)
    LandingEffects(100, 1, 1)
    sprite('vrctk440_13', 2)
    sprite('vrctk440_14', 2)
    sprite('vrctk440_15', 2)
    loopRest()
    gotoLabel(4)

@State
def BurstDD_Chibi():

    def upon_IMMEDIATE():
        callSubroutine('Func_BurstDD')
    label(1)
    sprite('vrctk440_00', 2)
    LandingEffects(100, 1, 0)
    PrivateSE('tkse_07')
    sprite('vrctk440_01', 2)
    sprite('vrctk440_02', 2)
    sprite('vrctk440_03', 2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('vrctk440_04', 2)
    LandingEffects(100, 1, 0)
    sprite('vrctk440_05', 2)
    sprite('vrctk440_06', 2)
    sprite('vrctk440_07', 2)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('vrctk440_08', 2)
    LandingEffects(100, 1, 0)
    sprite('vrctk440_09', 2)
    sprite('vrctk440_10', 2)
    sprite('vrctk440_11', 2)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('vrctk440_12', 2)
    LandingEffects(100, 1, 0)
    sprite('vrctk440_13', 2)
    sprite('vrctk440_14', 2)
    sprite('vrctk440_15', 2)
    loopRest()
    gotoLabel(4)

@State
def BurstDD_ChibiLast():

    def upon_IMMEDIATE():
        ContinueState(300)
        if SLOT_7:
            physicsXImpulse(16000)
            Flip()
        else:
            physicsXImpulse(-16000)
        SetZVal(100)
        AddY(-12500)
        RunLoopUpon(17, 120)

        def upon_17():
            CollideWithWall(1)
    label(1)
    sprite('ctk450_25', 5)
    LandingEffects(100, 1, 1)
    sprite('ctk450_26', 5)
    sprite('ctk450_27', 5)
    sprite('ctk450_28', 5)
    loopRest()
    gotoLabel(1)

@State
def BurstDD_Bokosuka():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(40)
        AttackP2(100)
        AirHitstunAnimation(6)
        GroundedHitstunAnimation(6)
        Hitstun(200)
        AirUntechableTime(200)
        PushbackX(0)
        Hitstop(3)
        HitsparkSize(0)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDD_Bokosuka')
        DefeatOpponentBehavior(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        CHStateIfCHStart(3)
        CopyFromRightToLeft(23, 2, 2, 3, 2, 66)
        if SLOT_2:
            SLOT_78 = 70
        ApplyFunctionsToObjects(22)
        TeleportToObject(22)
        AddX(900000)
        AbsoluteY(300000)
        ApplyFunctionsToSelf()
        Visibility(1)
        TeleportToObject(22)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 51)
        SetActionMark(6)
    label(0)
    sprite('vrctk440_00', 1)
    RefreshMultihit()
    ScreenShake(3000, 3000)
    CreateObject('tkef_440smoke', -1)
    CreateObject('tkef_440RandomItem', -1)
    sprite('vrctk440_00', 1)
    RefreshMultihit()
    ScreenShake(6000, 0)
    sprite('vrctk440_00', 1)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(0, 6000)
    if SLOT_2:
        _gotolabel(0)
    loopRest()
    sprite('vrctk440_00', 30)
    CreateObject('tkef_440smoke', -1)
    CreateObject('tkef_440RandomItem', -1)
    sprite('vrctk440_00', 10)
    RefreshMultihit()
    Damage(1200)
    AttackType(4)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackY(1000)
    AirPushbackX(48000)
    Floorslide(40)
    Hitstop(20)
    DefeatOpponentBehavior(0)
    ScreenShake(50000, 50000)

@State
def BurstDD_BokosukaSP():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(60)
        AttackP2(100)
        AirHitstunAnimation(6)
        GroundedHitstunAnimation(6)
        Hitstun(200)
        AirUntechableTime(200)
        PushbackX(0)
        Hitstop(2)
        HardKnockdown(100)
        HitsparkSize(0)
        HitAnywhere(1)
        DamageFromStateOnly('BurstDD_BokosukaSP')
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        CHStateIfCHStart(3)
        CopyFromRightToLeft(23, 2, 2, 3, 2, 66)
        if SLOT_2:
            SLOT_78 = 70
        ApplyFunctionsToObjects(22)
        TeleportToObject(22)
        AddX(900000)
        AbsoluteY(300000)
        AlphaMultiplier(0)
        ApplyFunctionsToSelf()
        Visibility(1)
        TeleportToObject(22)
        SetActionMark(6)
    label(0)
    sprite('vrctk440_00', 1)
    RefreshMultihit()
    ScreenShake(3000, 3000)
    CreateObject('tkef_440smoke', -1)
    CreateObject('tkef_440RandomItem', -1)
    sprite('vrctk440_00', 1)
    RefreshMultihit()
    ScreenShake(6000, 0)
    sprite('vrctk440_00', 1)
    RefreshMultihit()
    AddActionMark(-1)
    ScreenShake(0, 6000)
    if SLOT_2:
        _gotolabel(0)
    loopRest()
    sprite('vrctk440_00', 30)
    CreateObject('tkef_440smoke', -1)
    CreateObject('tkef_440RandomItem', -1)
    sprite('vrctk440_00', 55)
    CreateObject('tkef_440CatGot', -1)
    RefreshMultihit()
    Damage(1200)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackY(50000)
    AirPushbackX(22000)
    ScreenShake(50000, 50000)
    sprite('vrctk440_00', 30)
    RefreshMultihit()
    AirPushbackY(-100000)
    AirPushbackX(0)
    ObjectUpon(3, 33)
    sprite('ctk440_16', 3)
    TeleportToObject(22)
    SetZVal(-501)
    Visibility(0)
    if (SLOT_25 <= 600000):
        Flip()
    physicsYImpulse(30000)
    setGravity(1800)

    def upon_4():
        clearUponHandler(4)
        physicsXImpulse(10000)
        sendToLabel(1)

    def upon_LANDING():
        CollideWithWall(1)
        Flip()
        EndMomentum(1)
        physicsXImpulse(-15000)
        sendToLabel(2)
    ScreenShake(0, 10000)
    PassbackAddActionMarkToFunction('tkef_440CatGot', 32)
    sprite('ctk440_17', 3)
    RefreshMultihit()
    AttackType(4)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackY(46000)
    AirPushbackX(1000)
    ResetGravity()
    Hitstop(8)
    HardKnockdownReset()
    OppPositionOnHit(3, 0, 150000)
    DefeatOpponentBehavior(0)
    ApplyFunctionsToObjects(22)
    AlphaValue(255)
    ApplyFunctionsToSelf()
    sprite('ctk440_18', 10)
    label(1)
    sprite('ctk450_19ex01', 3)
    sprite('ctk450_20ex01', 3)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ctk450_21', 3)
    XImpulseAcceleration(110)
    PrivateSE('tkse_07')
    sprite('ctk450_22', 3)
    sprite('ctk450_23', 3)
    sprite('ctk450_24', 3)
    loopRest()
    gotoLabel(2)

@State
def tkef_440smoke():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AbsoluteY(0)
        CallCustomizableParticle('tkef_431smoke02', -1)

@State
def tkef_440CatGot():

    def upon_IMMEDIATE():
        PaletteIndex(4)
        AddX(1157000)
        AddY(400000)
        FaceRight()
        WallCollisionDetection(1)
        SetZVal(-500)
        sendToLabelUpon(32, 10)

        def upon_LANDING():
            sendToLabel(0)
            YAccel(-40)
            AltKnockdownEffects(100, 1, 1)
            ScreenShake(4000, 20000)
    sprite('null', 40)
    sprite('vrtkef440_00', 2)
    EnableAfterimage(1)
    physicsYImpulse(-30000)
    setGravity(5000)
    sprite('vrtkef440_00', 32767)
    label(0)
    sprite('vrtkef440_00', 32767)

    def upon_LANDING():
        EndMomentum(1)
        AltKnockdownEffects(100, 1, 1)
        ScreenShake(2000, 10000)
    label(10)
    sprite('vrtkef440_01', 6)
    ParticleSize(1100)
    CallCustomizableParticle('tkef_hit_sp', 0)
    sprite('vrtkef440_02', 6)
    sprite('vrtkef440_03', 6)
    ConstantAlphaModifier(-26)
    sprite('vrtkef440_04', 4)

@State
def tkef_440RandomItem():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        SLOT_51 = (SLOT_51 + SLOT_22)
        SLOT_52 = (SLOT_52 + SLOT_23)
        if SLOT_39:
            DeviationX(-10000, -30000)
        else:
            DeviationX(10000, 30000)
        DeviationY(20000, 50000)
        PrivateFunction(1, 2, 22, 2, 51, 2, 12)
        PrivateFunction(1, 2, 23, 2, 52, 2, 13)
        setGravity(2000)
        AddRotationPerFrame(15000)
        TeleportToObject(22)
        AddY(-100000)

        def upon_LANDING():
            YAccel(-60)
            XImpulseAcceleration(50)
            sendToLabel(100)
        Unknown61(0, 1, 0, 44, 0, 0, 0, 9999, 0, 9999, 0, 9999)
        SLOT_2 = SLOT_0
        if (SLOT_2 == 1):
            sendToLabel(1)
        if (SLOT_2 == 2):
            sendToLabel(2)
        if (SLOT_2 == 3):
            sendToLabel(3)
        if (SLOT_2 == 4):
            sendToLabel(4)
        if (SLOT_2 == 5):
            sendToLabel(5)
        if (SLOT_2 == 6):
            sendToLabel(6)
        if (SLOT_2 == 7):
            sendToLabel(7)
        if (SLOT_2 == 8):
            sendToLabel(8)
        if (SLOT_2 == 9):
            sendToLabel(9)
        if (SLOT_2 == 10):
            sendToLabel(10)
        if (SLOT_2 == 11):
            sendToLabel(11)
        if (SLOT_2 == 12):
            sendToLabel(12)
        if (SLOT_2 == 13):
            sendToLabel(13)
        if (SLOT_2 == 14):
            sendToLabel(14)
        if (SLOT_2 == 15):
            sendToLabel(15)
        if (SLOT_2 == 16):
            sendToLabel(16)
        if (SLOT_2 == 17):
            sendToLabel(17)
        if (SLOT_2 == 18):
            sendToLabel(18)
        if (SLOT_2 == 19):
            sendToLabel(19)
        if (SLOT_2 == 20):
            sendToLabel(20)
        if (SLOT_2 == 21):
            sendToLabel(21)
        if (SLOT_2 == 22):
            sendToLabel(22)
        if (SLOT_2 == 23):
            sendToLabel(23)
        if (SLOT_2 == 24):
            sendToLabel(24)
        if (SLOT_2 == 25):
            sendToLabel(25)
        if (SLOT_2 == 26):
            sendToLabel(26)
        if (SLOT_2 == 27):
            sendToLabel(27)
        if (SLOT_2 == 28):
            sendToLabel(28)
        if (SLOT_2 == 29):
            sendToLabel(29)
        if (SLOT_2 == 30):
            sendToLabel(30)
        if (SLOT_2 == 31):
            sendToLabel(31)
        if (SLOT_2 == 32):
            sendToLabel(32)
        if (SLOT_2 == 33):
            sendToLabel(33)
        if (SLOT_2 == 34):
            sendToLabel(34)
        if (SLOT_2 == 35):
            sendToLabel(35)
        if (SLOT_2 == 36):
            sendToLabel(36)
        if (SLOT_2 == 37):
            sendToLabel(37)
        if (SLOT_2 == 38):
            sendToLabel(38)
        if (SLOT_2 == 39):
            sendToLabel(39)
        if (SLOT_2 == 40):
            sendToLabel(40)
        if (SLOT_2 == 41):
            sendToLabel(41)
        if (SLOT_2 == 42):
            sendToLabel(42)
        if (SLOT_2 == 43):
            sendToLabel(43)
        if (SLOT_2 == 44):
            sendToLabel(44)
    sprite('null', 32767)
    label(1)
    sprite('vrtkef412_30', 32767)
    PaletteIndex(0)
    label(2)
    sprite('vrtkef412_21', 32767)
    label(3)
    sprite('vrtkef412_20', 32767)
    label(4)
    sprite('vrtkef412_22', 32767)
    label(5)
    sprite('vrtkef412_00', 32767)
    label(6)
    sprite('vrtkef412_01', 32767)
    label(7)
    sprite('vrtkef412_02', 32767)
    label(8)
    sprite('vrtkef412_10', 32767)
    label(9)
    sprite('vrtkef417_rg', 32767)
    label(10)
    sprite('vrtkef417_jn', 32767)
    label(11)
    sprite('vrtkef417_no', 32767)
    label(12)
    sprite('vrtkef417_rc', 32767)
    label(13)
    sprite('vrtkef417_tk', 32767)
    label(14)
    sprite('vrtkef417_tg', 32767)
    label(15)
    sprite('vrtkef417_ar', 32767)
    label(16)
    sprite('vrtkef417_lc', 32767)
    label(17)
    sprite('vrtkef417_bn', 32767)
    label(18)
    sprite('vrtkef417_ca', 32767)
    label(19)
    sprite('vrtkef417_ha', 32767)
    label(20)
    sprite('vrtkef417_ny', 32767)
    label(21)
    sprite('vrtkef417_tb', 32767)
    label(22)
    sprite('vrtkef417_hz', 32767)
    label(23)
    sprite('vrtkef417_mu', 32767)
    label(24)
    sprite('vrtkef417_mk', 32767)
    label(25)
    sprite('vrtkef417_vh', 32767)
    label(26)
    sprite('vrtkef417_pt', 32767)
    label(27)
    sprite('vrtkef417_rl', 32767)
    label(28)
    sprite('vrtkef417_iz', 32767)
    label(29)
    sprite('vrtkef417_am', 32767)
    label(30)
    sprite('vrtkef417_bl', 32767)
    label(31)
    sprite('vrtkef417_az', 32767)
    label(32)
    sprite('vrtkef417_kg', 32767)
    label(33)
    sprite('vrtkef417_kk', 32767)
    label(34)
    sprite('vrtkef417_tm', 32767)
    label(35)
    sprite('vrtkef417_ce', 32767)
    label(36)
    sprite('vrtkef417_rm', 32767)
    label(37)
    sprite('vrtkef417_hb', 32767)
    label(38)
    sprite('vrtkef417_nt', 32767)
    label(39)
    sprite('vrtkef417_ph', 32767)
    label(40)
    sprite('vrtkef417_mi', 32767)
    label(41)
    sprite('vrtkef417_su', 32767)
    label(42)
    sprite('vrtkef417_es', 32767)
    label(43)
    sprite('vrtkef417_ma', 32767)
    label(44)
    sprite('vrtkef417_ma2', 32767)
    label(100)
    sprite('keep', 20)
    ConstantAlphaModifier(-15)

@Subroutine
def FoodInit():
    AttackDefaults_SpecialProjectile()
    PaletteIndex(1)
    TeleportToObject(22)
    physicsYImpulse(10000)
    setGravity(2200)
    ContinueState(90)
    RunLoopUpon(17, 70)

    def upon_17():
        ConstantAlphaModifier(-10)
    sendToLabelUpon(2, 10)
    sendToLabelUpon(32, 100)

@State
def RushPlusFood_RG():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_rg', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_JN():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_jn', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_NO():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_no', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_RC():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_rc', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_TK():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_tk', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_TG():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_tg', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_AR():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_ar', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_LC():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_lc', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_BN():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_bn', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_CA():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_ca', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_HA():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_ha', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_NY():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_ny', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_TB():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_tb', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_HZ():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_hz', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_MU():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_mu', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_MK():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_mk', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_VH():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_vh', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_PT():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_pt', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_RL():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_rl', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_IZ():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_iz', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_AM():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_am', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_BL():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_bl', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_AZ():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_az', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_KG():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_kg', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_KK():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_kk', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_TM():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_tm', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_CE():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_ce', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_RM():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_rm', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_HB():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_hb', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_NT():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_nt', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_PH():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_ph', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_MI():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_mi', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_SU():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_su', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_ES():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_es', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 32)

@State
def RushPlusFood_MA():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    random_(2, 0, 20)
    if SLOT_0:
        _gotolabel(1)
    sprite('vrtkef417_ma', 32767)
    label(1)
    sprite('vrtkef417_ma2', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def RushPlusFood_JB():

    def upon_IMMEDIATE():
        callSubroutine('FoodInit')
    sprite('vrtkef417_jb', 32767)
    label(10)
    sprite('keep', 1)
    setGravity(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    clearUponHandler(2)
    sprite('keep', 32767)
    label(100)
    sprite('null', 1)
    clearUponHandler(32)
    ObjectUpon(3, 33)

@State
def EventAR():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    sprite('ar232_05', 6)
    Flip()
    XPositionRelativeFacing(-900000)
    sprite('ar232_06', 6)
    physicsXImpulse(20000)
    sprite('ar232_05', 6)
    CommonSE('203_walk_water_2')
    sprite('ar232_06', 6)
    CommonSE('203_walk_water_0')
    CommonSE('203_walk_water_1')
    sprite('ar232_07', 6)
    sprite('ar232_08', 6)
    sprite('ar232_09', 6)
    CommonSE('203_walk_water_0')
    sprite('ar232_10', 6)
    CommonSE('203_walk_water_2')
    sprite('ar232_06', 6)
    CommonSE('203_walk_water_0')
    CommonSE('203_walk_water_1')
    sprite('ar232_07', 6)
    sprite('ar232_08', 6)
    sprite('ar232_09', 6)
    CommonSE('203_walk_water_0')
    sprite('ar232_10', 6)
    CommonSE('203_walk_water_2')
    sprite('ar232_06', 6)
    CommonSE('203_walk_water_0')
    CommonSE('203_walk_water_1')
    sprite('ar232_07', 6)
    sprite('ar232_08', 6)
    sprite('ar232_09', 6)
    CommonSE('203_walk_water_0')
    sprite('ar232_10', 6)
    loopRest()

@State
def Act2Event_Kemuri():

    def upon_IMMEDIATE():
        TeleportToObject(3)
        AddY(100000)
    sprite('null', 1)
    ParticleSize(1000)
    CallCustomizableParticle('tkef_431smoke02', -1)
    loopRest()

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
    ScreenShake(0, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Eventtk450_?():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        FaceLeft()
        RemoveOnCallStateEnd(3)
    sprite('vrtkef450_10', 5)
    Size(500)
    SetScaleSpeed(100)
    AddX(-70000)
    AddY(182000)
    sprite('vrtkef450_10', 160)
    Size(1000)
    SetScaleSpeed(0)

@State
def Act3Event_Cam():

    def upon_IMMEDIATE():
        CameraControlEnable(1)

        def upon_FRAME_STEP():
            if SLOT_38:
                if (SLOT_22 <= 0):
                    XPositionRelativeFacing(0)
                    EndMomentum(1)
                    CameraControlEnable(0)
                    sendToLabel(0)
                    clearUponHandler(3)
            elif (SLOT_22 >= 0):
                XPositionRelativeFacing(0)
                EndMomentum(1)
                CameraControlEnable(0)
                sendToLabel(0)
                clearUponHandler(3)
    sprite('null', 600)
    AddInertia(15000)
    label(0)
    sprite('null', 5)

@State
def Act3Event_Damage():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AddY(150000)
    sprite('null', 10)
    CreateParticle('tkef_hit_high', 103)
    PrivateSE('tkse_03')

@State
def Act3Event_Black():

    def upon_IMMEDIATE():
        ColorForTransition(4278190080)
        RenderLayer(3)
        BlendMode_Off()
        ScreenPosition(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        Size(20000)
        AlphaValue(0)
        sendToLabelUpon(32, 0)
    sprite('vr_white', 20)
    ConstantAlphaModifier(12)
    sprite('vr_white', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    label(0)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-5)
    sprite('vr_white', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)