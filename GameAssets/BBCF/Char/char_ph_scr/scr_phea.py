@Subroutine
def RedOnlyAirStatus():
    AirUntechableTime(25)
    AirPushbackX(10000)
    AirPushbackY(17000)

@Subroutine
def BlueOnlyAirStatus():
    AirPushbackX(2500)
    AirPushbackY(2500)

@Subroutine
def ShotDeleteZone():
    CancelIfPlayerHit(3)
    RemoveOnCallStateEnd(3)
    E0EAEffectPosition(3)
    IgnorePauses(3)
    GuardPoint_(1)
    setInvincible(1)
    SpecificInvincibility(0, 0, 0, 1, 0)
    GuardpointHitstop(0, 0)
    PretendNoGuardPointIfFail(1)
    SetActionMark(1)

    def upon_FRAME_STEP():
        if (not SLOT_30):

            def upon_GUARDPOINT_ACTIVATION():
                if SLOT_2:
                    ObjectUpon(3, 32)

@State
def ShotDefCol():

    def upon_IMMEDIATE():
        callSubroutine('ShotDeleteZone')
        SetScaleX(1800)
        SetScaleY(2700)
        AddX(150000)
        AddY(150000)
    sprite('null', 2)
    sprite('ph_shotdefcol', 9)

@State
def EMB_PH():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        RenderLayer(5)
        Eff3DEffect('ef_emb_ph.DIG', '')
        AddY(315000)
        Size(1300)
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
def EMB_PH_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        Visibility(1)
        RenderLayer(5)
        Eff3DEffect('ef_emb_ph.DIG', '')
        AddY(315000)
        Size(1300)
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
def EMB_PH_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        Eff3DEffect('ef_emb_ph.DIG', '')
        AddY(315000)
        Size(1300)
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
def ph333_arm():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(2)
        IgnorePauses(2)
        RenderLayer(8)
    sprite('ph333_cutin00', 3)
    CreateObject('ph333_arm_eff_L', 0)
    CreateObject('ph333_arm_eff_R', 1)
    sprite('ph333_cutin01', 20)
    sprite('ph333_cutin02', 3)
    CreateObject('ph333_arm_eff2_L', 0)
    CreateObject('ph333_arm_eff2_R', 1)
    sprite('ph333_cutin03', 32767)
    ParticleLayer(9)
    CallCustomizableParticle('phef_333arm_fire3', 2)
    ParticleLayer(9)
    CallCustomizableParticle('phef_333arm_fire3', 3)

@State
def ph333_arm_eff_L():

    def upon_IMMEDIATE():
        Flip()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        ParticleLayer(6)
        CallPrivateEffect('phef_333arm_circle')
    label(0)
    sprite('null', 3)
    ParticleLayer(9)
    CallCustomizableParticle('phef_333arm_fire', 100)
    gotoLabel(0)

@State
def ph333_arm_eff_R():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        ParticleLayer(6)
        CallPrivateEffect('phef_333arm_circle')
    label(0)
    sprite('null', 3)
    ParticleLayer(9)
    CallCustomizableParticle('phef_333arm_fire', 100)
    gotoLabel(0)

@State
def ph333_arm_eff2_L():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        RenderLayer(7)
        LinkParticle('phef_333arm')
    sprite('null', 60)
    ParticleLayer(9)
    CallCustomizableParticle('phef_333arm_fire2', 100)

@State
def ph333_arm_eff2_R():

    def upon_IMMEDIATE():
        Flip()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        RenderLayer(7)
        LinkParticle('phef_333arm')
    sprite('null', 60)
    ParticleLayer(9)
    CallCustomizableParticle('phef_333arm_fire2', 100)

@State
def phef_340_fire():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
        AddX(-32000)
        AddY(8000)
    sprite('vr_ph340_07', 3)
    CreateParticle('phef_340fire_ground', 0)
    sprite('vr_ph340_08', 4)
    ParticleSize(1250)
    CallCustomizableParticle('phef_340fire', 0)
    ParticleSize(1000)
    CallCustomizableParticle('phef_340fire', 1)
    sprite('vr_ph340_10', 2)
    ParticleSize(750)
    CallCustomizableParticle('phef_340fire', 0)
    ParticleSize(500)
    CallCustomizableParticle('phef_340fire', 1)
    sprite('vr_ph340_11', 2)
    ParticleSize(250)
    CallCustomizableParticle('phef_340fire', 0)
    CreateParticle('phef_340fire_add', 1)
    sprite('vr_ph340_12', 2)
    sprite('vr_ph340_13', 4)
    sprite('vr_ph340_14', 4)
    sprite('vr_ph340_15', 4)

@State
def phef_600_bg():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(3)
        BlendMode_Normal()
        SetScaleX(20000)
        SetScaleY(20000)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        RenderLayer(15)
        SetZVal(10000)
    sprite('vr_screen_black', 30)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('vr_screen_black', 60)
    AlphaValue(95)
    ConstantAlphaModifier(0)
    sprite('vr_screen_black', 30)
    ConstantAlphaModifier(-3)

@State
def phef_600_Fire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(100000)
    sprite('null', 1)
    CreateParticle('phef_600bigen', 100)

@State
def phef_600_Fire2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def phef_600_FireWall():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('pheff600_firewall', '')
        FaceSpawnLocation()
        AddX(100000)
        BlendMode_Add()
        LinkParticle('phef_600ground')
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_1')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_1')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_1')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 16)
    ConstantAlphaModifier(-16)
    CreateObject('phef_600_Fire_End', -1)

@State
def phef_600_Fire_End():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    CreateParticle('phef_600fire_end', -1)

@State
def phef_600_HatFire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
        RenderLayer(6)
    sprite('phef600_01', 6)
    sprite('phef600_02', 6)
    sprite('phef600_03', 6)
    sprite('phef600_04', 6)
    sprite('phef600_05', 6)
    sprite('phef600_06', 6)

@State
def phef_600_Hat():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
    sprite('phef600_hat', 2)
    AlphaValue(127)
    sprite('phef600_hat', 2)
    AlphaValue(191)
    sprite('phef600_hat', 2)
    AlphaValue(255)

@State
def phef_602_Fire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(-20000)
    sprite('null', 1)
    CreateParticle('phef_600bigen', 100)

@State
def phef_602_Fire2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
        AddX(-80000)
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def phef_602_FireWall():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('pheff600_firewall', '')
        FaceSpawnLocation()
        AddX(-20000)
        BlendMode_Add()
        LinkParticle('phef_600ground')
        SetScaleX(1500)
    sprite('null', 6)
    CommonSE('019_quake_0')
    AlphaValue(0)
    ConstantAlphaModifier(32)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CommonSE('019_quake_1')
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CommonSE('019_quake_0')
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CommonSE('019_quake_1')
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CommonSE('019_quake_0')
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CommonSE('019_quake_1')
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CommonSE('019_quake_0')
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 16)
    ConstantAlphaModifier(-16)
    CreateObject('phef_602_Fire_End', -1)

@State
def phef_602_Fire_End():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(-20000)
    sprite('null', 1)
    CreateParticle('phef_600fire_end', -1)

@State
def ph001Eff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('pheff001_fire00', '')
        Size(450)
        AlphaValue(180)
        AddY(275000)
        AddX(-65000)
        FaceRight()
        LinkParticle('phef001_hinoko')
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    label(0)
    sprite('null', 25)
    physicsYImpulse(300)
    ConstantAlphaModifier(0)
    SetScaleSpeed(-2)
    sprite('null', 5)
    SetScaleSpeed(-1)
    physicsYImpulse(150)
    sprite('null', 25)
    physicsYImpulse(-300)
    SetScaleSpeed(2)
    sprite('null', 5)
    SetScaleSpeed(1)
    physicsYImpulse(-150)
    gotoLabel(0)

@State
def ph032FireEff():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(2)
        BlendMode_Add()
        AddX(50000)
    sprite('vr_ph32_00', 3)
    CreateObject('ph032FireEffSub', -1)
    CreateParticle('phef_dash_aura', 0)
    CreateParticle('phef_dash_aura', 1)
    CreateParticle('phef_dash_aura', 2)
    CreateParticle('phef_dash_aura', 3)
    CreateParticle('phef_dash_aura', 4)
    CreateParticle('phef_dash_aura', 5)
    CreateParticle('phef_dash_aura', 6)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    ConstantAlphaModifier(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph032FireEffSub():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(0)
    sprite('vr_ph32_10', 3)
    ColorTransition(0, 16)
    sprite('vr_ph32_11', 3)
    sprite('vr_ph32_12', 3)
    sprite('vr_ph32_13', 3)
    ConstantAlphaModifier(-25)
    sprite('vr_ph32_14', 3)
    sprite('vr_ph32_15', 3)

@State
def ph032FireEff2():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(2)
        BlendMode_Add()
        AddX(50000)
    sprite('vr_ph32_00', 3)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    ConstantAlphaModifier(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph035FireEff():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vr_ph35_00', 3)
    CreateObject('ph035FireEffSub', -1)
    CreateParticle('phef_dash_aura', 0)
    CreateParticle('phef_dash_aura', 1)
    CreateParticle('phef_dash_aura', 2)
    CreateParticle('phef_dash_aura', 3)
    CreateParticle('phef_dash_aura', 4)
    CreateParticle('phef_dash_aura', 5)
    CreateParticle('phef_dash_aura', 6)
    sprite('vr_ph35_01', 3)
    sprite('vr_ph35_02', 3)
    sprite('vr_ph35_04', 3)
    sprite('vr_ph35_05', 2)
    sprite('vr_ph35_06', 2)
    sprite('vr_ph35_07', 2)

@State
def ph035FireEffSub():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(0)
    sprite('vr_ph035_10', 3)
    ColorTransition(0, 16)
    sprite('vr_ph035_11', 3)
    sprite('vr_ph035_12', 3)
    ConstantAlphaModifier(-25)
    sprite('vr_ph035_13', 3)
    sprite('vr_ph035_14', 3)

@State
def ph035FireEff2():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vr_ph35_00', 3)
    sprite('vr_ph35_02', 3)
    sprite('vr_ph35_05', 3)
    ConstantAlphaModifier(-25)
    sprite('vr_ph35_06', 3)
    sprite('vr_ph35_07', 3)

@State
def phStocEff_Master1():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(0)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(1)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 10)
    label(0)
    sprite('null', 32767)
    CreateObject('phStocEff_blue', -1)
    RegisterObject(4, 1)
    ObjectUpon(4, 33)
    label(1)
    sprite('null', 32767)
    CreateObject('phStocEff_green', -1)
    RegisterObject(4, 1)
    ObjectUpon(4, 33)
    label(2)
    sprite('null', 32767)
    CreateObject('phStocEff_red', -1)
    RegisterObject(4, 1)
    ObjectUpon(4, 33)
    label(100)
    sprite('null', 10)
    ObjectUpon(4, 32)
    ExitState()
    label(200)
    sprite('null', 10)
    ObjectUpon(4, 41)
    ExitState()

@State
def phStocEff_Master2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(0)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(1)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 10)
    label(0)
    sprite('null', 3)
    sprite('null', 32767)
    CreateObject('phStocEff_blue', -1)
    RegisterObject(5, 1)
    ObjectUpon(5, 34)
    label(1)
    sprite('null', 3)
    sprite('null', 32767)
    CreateObject('phStocEff_green', -1)
    RegisterObject(5, 1)
    ObjectUpon(5, 34)
    label(2)
    sprite('null', 3)
    sprite('null', 32767)
    CreateObject('phStocEff_red', -1)
    RegisterObject(5, 1)
    ObjectUpon(5, 34)
    label(100)
    sprite('null', 10)
    ObjectUpon(5, 32)
    ExitState()
    label(200)
    sprite('null', 10)
    ObjectUpon(5, 41)
    ExitState()

@State
def phStocEff_Master3():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(0)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(1)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 10)
    label(0)
    sprite('null', 6)
    sprite('null', 32767)
    CreateObject('phStocEff_blue', -1)
    RegisterObject(6, 1)
    ObjectUpon(6, 35)
    label(1)
    sprite('null', 6)
    sprite('null', 32767)
    CreateObject('phStocEff_green', -1)
    RegisterObject(6, 1)
    ObjectUpon(6, 35)
    label(2)
    sprite('null', 6)
    sprite('null', 32767)
    CreateObject('phStocEff_red', -1)
    RegisterObject(6, 1)
    ObjectUpon(6, 35)
    label(100)
    sprite('null', 10)
    ObjectUpon(6, 32)
    ExitState()
    label(200)
    sprite('null', 10)
    ObjectUpon(6, 41)
    ExitState()

@State
def phStocEff_red():

    def upon_IMMEDIATE():
        Visibility(1)
        Size(650)
        BlendMode_Normal()
        RemoveOnContact(3)
        E0EAEffectDirection(3)
        IgnoreScreenfreeze(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_41():
            EndObject()

        def upon_33():
            SLOT_51 = 1

        def upon_34():
            SLOT_52 = 1

        def upon_35():
            SLOT_53 = 1

        def upon_16():
            if SLOT_51:
                PrivateFunction3(3, 0, 100000, 90, 1)
            if SLOT_52:
                PrivateFunction3(3, -25000, 50000, 90, 1)
            if SLOT_53:
                PrivateFunction3(3, -50000, 0, 90, 1)
    sprite('null', 1)
    sprite('null', 5)
    Eff3DEffect('pheff_stoc00', '')
    sprite('null', 32767)
    Eff3DEffect('pheff_stoc01', '')
    label(1)
    sprite('null', 6)
    sprite('null', 4)
    RemoveOnContact(0)
    Eff3DEffect('pheff_stoc02', '')
    ConstantAlphaModifier(-51)

@State
def phStocEff_blue():

    def upon_IMMEDIATE():
        Visibility(1)
        Size(650)
        BlendMode_Normal()
        RemoveOnContact(3)
        E0EAEffectDirection(3)
        IgnoreScreenfreeze(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_41():
            EndObject()

        def upon_33():
            SLOT_51 = 1

        def upon_34():
            SLOT_52 = 1

        def upon_35():
            SLOT_53 = 1

        def upon_16():
            if SLOT_51:
                PrivateFunction3(3, 0, 100000, 90, 1)
            if SLOT_52:
                PrivateFunction3(3, -25000, 50000, 90, 1)
            if SLOT_53:
                PrivateFunction3(3, -50000, 0, 90, 1)
    sprite('null', 1)
    sprite('null', 5)
    Eff3DEffect('pheff_Bstoc00', '')
    sprite('null', 32767)
    Eff3DEffect('pheff_Bstoc01', '')
    label(1)
    sprite('null', 6)
    sprite('null', 4)
    RemoveOnContact(0)
    Eff3DEffect('pheff_Bstoc02', '')
    ConstantAlphaModifier(-51)

@State
def phStocEff_green():

    def upon_IMMEDIATE():
        Visibility(1)
        Size(650)
        BlendMode_Normal()
        RemoveOnContact(3)
        E0EAEffectDirection(3)
        IgnoreScreenfreeze(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_41():
            EndObject()

        def upon_33():
            SLOT_51 = 1

        def upon_34():
            SLOT_52 = 1

        def upon_35():
            SLOT_53 = 1

        def upon_16():
            if SLOT_51:
                PrivateFunction3(3, 0, 100000, 90, 1)
            if SLOT_52:
                PrivateFunction3(3, -25000, 50000, 90, 1)
            if SLOT_53:
                PrivateFunction3(3, -50000, 0, 90, 1)
    sprite('null', 1)
    sprite('null', 5)
    Eff3DEffect('pheff_Gstoc00', '')
    sprite('null', 32767)
    Eff3DEffect('pheff_Gstoc01', '')
    label(1)
    sprite('null', 6)
    sprite('null', 4)
    RemoveOnContact(0)
    Eff3DEffect('pheff_Gstoc02', '')
    ConstantAlphaModifier(-51)

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
def phCmnFireEff():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        Eff3DEffect('phCmneff_fire00', '')
        BlendMode_Normal()
    sprite('null', 7)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def phCmnWaterEff():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 10)
    SetScaleSpeed(1)
    CreateParticle('phefcmn_fallwater', -1)
    ConstantAlphaModifier(-8)
    sprite('null', 6)
    SetScaleSpeed(15)

@State
def phCmnWaterEff2():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Size(550)
        Eff3DEffect('phCmneff_water01', '')
    sprite('null', 10)
    CreateParticle('phefcmn_fallwater', -1)
    sprite('null', 6)
    SetScaleSpeed(15)

@State
def ph200_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ph200eff_00.DIG', '')
        AddY(300000)
        AddX(100000)
        SetScaleX(1400)
        SetScaleY(950)
        BlendMode_Normal()
        Rotation(20000)
        E0EAEffectPosition(2)
    sprite('null', 3)
    sprite('null', 3)
    E0EAEffectPosition(0)
    sprite('null', 16)
    CreateObject('ph200_effSub', -1)

@State
def ph200_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(20000)
    sprite('vr_ph200effpos_00', 2)
    CreateParticle('phefcmn_fallwater', 0)
    sprite('vr_ph200effpos_00', 2)
    CreateParticle('phefcmn_fallwater', 1)
    sprite('vr_ph200effpos_00', 2)
    CreateParticle('phefcmn_fallwater', 2)

@State
def ph201_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ph201eff_00.DIG', '')
        AddY(270000)
        AddX(100000)
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 3)
    Size(700)
    sprite('null', 9)
    E0EAEffectPosition(0)
    CreateObject('ph201_effSub', -1)
    Size(850)
    sprite('null', 4)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def ph201_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(75000)
        AddY(-50000)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 3)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 4)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 5)

@State
def ph202_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('ph202eff_00.DIG', '')
        AddY(210000)
        AddX(205000)
        SetScaleX(700)
        SetScaleY(600)
        E0EAEffectPosition(2)
    sprite('null', 3)
    CreateParticle('phef202_patchin', -1)
    CommonSE('015_blaze_0')
    sprite('null', 3)
    E0EAEffectPosition(0)
    sprite('null', 5)
    CreateParticle('phef202_hinoko', -1)
    CreateObject('ph202_effSub', -1)

@State
def ph202_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(20000)
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 0)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(700)
    AddY(-25000)
    ApplyFunctionsToSelf()
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 1)
    ApplyFunctionsToObjects(1)
    SetScaleX(900)
    SetScaleY(-700)
    AddY(32500)
    ApplyFunctionsToSelf()
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 2)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(700)
    AddY(-22000)
    ApplyFunctionsToSelf()

@State
def ph210_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ph210eff_00.DIG', '')
        AddY(324000)
        AddX(-40000)
        Size(900)
        RotationAngle(-15000)
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 3)
    CreateObject('ph210_effSub', -1)
    sprite('null', 11)
    E0EAEffectPosition(0)
    sprite('null', 8)

@State
def ph210_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('vr_ph210effpos_00', 1)
    CreateParticle('phefcmn_fallwater', 0)
    sprite('vr_ph210effpos_00', 1)
    CreateParticle('phefcmn_fallwater', 1)
    sprite('vr_ph210effpos_00', 1)
    CreateParticle('phefcmn_fallwater', 2)
    sprite('vr_ph210effpos_00', 1)
    CreateParticle('phefcmn_fallwater', 3)
    sprite('vr_ph210effpos_00', 1)
    CreateParticle('phefcmn_fallwater', 4)

@State
def ph211_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddY(308000)
        AddX(50000)
        BlendMode_Normal()
        RotationAngle(-30000)
        SetScaleY(-1000)
        SetScaleX(1000)
        E0EAEffectPosition(2)
    sprite('vr_ph254_00', 1)
    CreateParticle('phef201_kira', 0)
    CreateParticle('phef201_kira', 1)
    CreateParticle('phef201_kira', 2)
    CreateParticle('phef201_kira', 3)
    CreateParticle('phef201_kira', 4)
    CreateParticle('phef201_kira', 5)
    CreateParticle('phef201_kira', 6)
    sprite('vr_ph254_00', 3)
    AddScaleX(300)
    AddScaleY(-300)
    sprite('vr_ph254_01', 2)
    sprite('vr_ph254_01', 2)
    E0EAEffectPosition(0)
    sprite('vr_ph254_02', 4)
    ConstantAlphaModifier(-22)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph212_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('ph202eff_00.DIG', '')
        AddY(330000)
        AddX(175000)
        SetScaleX(900)
        SetScaleY(750)
        RotationAngle(-14500)
        E0EAEffectPosition(2)
    sprite('null', 3)
    CreateParticle('phef202_patchin', -1)
    CommonSE('015_blaze_0')
    sprite('null', 3)
    E0EAEffectPosition(0)
    sprite('null', 5)
    CreateParticle('phef202_hinoko', -1)
    CreateObject('ph212_effSub', -1)

@State
def ph212_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('vr_ph212effpos_00', 2)
    CreateObject('phCmnFireEff', 0)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(800)
    AddY(-60000)
    ApplyFunctionsToSelf()
    sprite('vr_ph212effpos_00', 2)
    CreateObject('phCmnFireEff', 1)
    ApplyFunctionsToObjects(1)
    Size(800)
    SetScaleY(-700)
    AddX(40000)
    RotationAngle(7500)
    ApplyFunctionsToSelf()
    sprite('vr_ph212effpos_00', 2)
    CreateObject('phCmnFireEff', 2)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(900)
    AddX(-100000)
    AddY(-100000)
    ApplyFunctionsToSelf()

@State
def ph214_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        AddY(130000)
        AddX(135000)
        Size(1100)
        RandAddRotation(-25000, 25000)
        E0EAEffectPosition(2)
    sprite('vr_ph214_00', 3)
    IgnoreFinishStop(1)
    sprite('vr_ph214_01', 3)
    E0EAEffectPosition(0)
    IgnoreFinishStop(0)
    sprite('vr_ph214_02', 4)
    sprite('vr_ph214_03', 3)
    ConstantAlphaModifier(-15)
    sprite('vr_ph214_04', 2)
    sprite('vr_ph214_05', 2)
    CreateParticle('phefcmn_fallwater', -1)

@State
def ph215_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddX(300000)
        AddY(-25000)
        Size(1150)
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('vr_ph215_00', 2)
    sprite('vr_ph215_01', 2)
    sprite('vr_ph215_02', 2)
    sprite('vr_ph215_03', 3)
    sprite('vr_ph215_04', 3)
    E0EAEffectPosition(0)
    sprite('vr_ph215_05', 3)
    sprite('vr_ph215_06', 3)
    CreateParticle('phef201_kira', 0)
    CreateParticle('phef201_kira', 1)
    CreateParticle('phef201_kira', 2)
    sprite('vr_ph215_07', 3)

@State
def ph216_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddY(130000)
        AddX(135000)
        SetScaleX(1400)
        SetScaleY(1200)
        BlendMode_Add()
        PaletteIndex(2)
        RenderLayer(1)
        E0EAEffectPosition(2)
    sprite('vr_ph216_00', 4)
    CreateObject('ph216_effBG', -1)
    CommonSE('015_blaze_0')
    sprite('vr_ph216_01', 4)
    CreateParticle('phef216_smoke', -1)
    E0EAEffectPosition(0)
    sprite('vr_ph216_02', 3)
    sprite('vr_ph216_03', 3)
    sprite('vr_ph216_04', 2)
    sprite('vr_ph216_05', 2)

@State
def ph216_effBG():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Size(2000)
    sprite('vr_ph216bloom_00', 15)
    sprite('vr_ph216bloom_00', 10)
    ConstantAlphaModifier(-26)

@State
def ph230_eff():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('ph230eff_00.DIG', '')
        AddX(20000)
        AddY(50000)
        BlendMode_Normal()
        SetScaleY(700)
        SetScaleX(600)
        RotationAngle(15000)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
    sprite('vr_ph202effpos_00', 4)
    CreateParticle('phef230_sibuki', -1)
    sprite('vr_ph202effpos_00', 2)
    E0EAEffectPosition(0)
    AddScale(50)
    sprite('vr_ph202effpos_00', 2)
    CreateParticle('phef230_sibuki', -1)
    AddScale(50)
    sprite('vr_ph202effpos_00', 16)

@State
def ph231_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ph201eff_00.DIG', '')
        AddX(120000)
        AddY(150000)
        RotationAngle(10000)
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 3)
    Size(400)
    sprite('null', 3)
    CreateObject('ph231_effSub', -1)
    Size(550)
    sprite('null', 6)
    E0EAEffectPosition(0)
    sprite('null', 4)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def ph231_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(75000)
        AddY(-50000)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 3)

@Subroutine
def MagicInit():
    AttackDefaults_SpecialProjectile()
    CancelIfPlayerHit(3)

@State
def ph232_eff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        AddX(-100000)
        AddY(-50000)
        E0EAEffectPosition(2)
    sprite('vr_ph235_00', 4)
    CommonSE('015_blaze_0')
    CreateParticle('phef_232_burn', 0)
    sprite('vr_ph235_01', 4)
    E0EAEffectPosition(0)
    CreateParticle('phef235fire', -1)
    sprite('vr_ph235_02', 4)
    sprite('vr_ph235_03', 4)
    sprite('vr_ph235_04', 4)

@State
def ph235_eff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        AddX(275000)
        AddY(-10000)
        Size(1900)
        Flip()
        E0EAEffectPosition(2)
    sprite('vr_ph235_10', 4)
    CommonSE('015_blaze_0')
    CreateParticle('phef232_sub', 0)
    CreateParticle('phef232_sub', 1)
    CreateParticle('phef232_sub', 2)
    CreateParticle('phef232_sub', 3)
    CreateParticle('phef232_sub', 4)
    CreateParticle('phef232_sub', 5)
    CreateParticle('phef232_sub', 6)
    sprite('vr_ph235_11', 4)
    E0EAEffectPosition(0)
    sprite('vr_ph235_12', 4)
    sprite('vr_ph235_13', 4)
    sprite('vr_ph235_14', 4)
    sprite('vr_ph235_15', 4)
    sprite('vr_ph235_16', 4)

@State
def ph250_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ph250eff_00.DIG', '')
        AddY(217000)
        AddX(75000)
        Size(850)
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 3)
    sprite('null', 19)
    CreateObject('ph250_effSub', -1)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)

@State
def ph250_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(20000)
        AddY(100000)
    sprite('vr_ph200effpos_00', 2)
    CreateObject('phCmnWaterEff', 0)
    ApplyFunctionsToObjects(1)
    Size(450)
    AddY(-25000)
    Rotation(-5000)
    ApplyFunctionsToSelf()
    sprite('vr_ph200effpos_00', 2)
    CreateObject('phCmnWaterEff', 1)
    ApplyFunctionsToObjects(1)
    SetScaleX(550)
    SetScaleY(-750)
    AddY(40000)
    ApplyFunctionsToSelf()

@State
def ph251_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddY(289800)
        AddX(20000)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('vr_ph254_00', 2)
    CreateParticle('phef201_kira', 0)
    CreateParticle('phef201_kira', 1)
    CreateParticle('phef201_kira', 2)
    CreateParticle('phef201_kira', 3)
    CreateParticle('phef201_kira', 4)
    CreateParticle('phef201_kira', 5)
    CreateParticle('phef201_kira', 6)
    SetScaleSpeed(3)
    sprite('vr_ph254_00', 1)
    sprite('vr_ph254_00', 1)
    AddScale(300)
    sprite('vr_ph254_01', 3)
    sprite('vr_ph254_02', 3)
    ConstantAlphaModifier(-22)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph251_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(75000)
        AddY(-50000)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    CreateParticle('phef201_kira', 3)

@State
def ph252_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('ph202eff_00.DIG', '')
        AddY(270000)
        AddX(175000)
        SetScaleX(600)
        SetScaleY(700)
        E0EAEffectPosition(2)
    sprite('null', 3)
    RemoveOnCallStateEnd(2)
    CreateParticle('phef202_patchin', -1)
    CommonSE('015_blaze_0')
    sprite('null', 3)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('null', 5)
    CreateParticle('phef202_hinoko', -1)
    CreateObject('ph252_effSub', -1)

@State
def ph252_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(20000)
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 0)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(600)
    AddY(-25000)
    ApplyFunctionsToSelf()
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 1)
    ApplyFunctionsToObjects(1)
    SetScaleX(800)
    SetScaleY(-600)
    AddY(32500)
    ApplyFunctionsToSelf()
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 2)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(600)
    AddY(-22000)
    AddX(-22000)
    ApplyFunctionsToSelf()

@State
def ph253_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ph253eff_00.DIG', '')
        AddY(270000)
        AddX(-90000)
        BlendMode_Normal()
        AddX(100000)
        AddY(50000)
        Rotation(-20000)
        E0EAEffectPosition(2)
    sprite('null', 3)
    CreateObject('ph253_effSub', -1)
    sprite('null', 12)
    E0EAEffectPosition(0)

@State
def ph253_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddY(-100000)
    sprite('vr_ph200effpos_00', 2)
    CreateParticle('phefcmn_fallwater', 0)
    CreateParticle('phefcmn_fallwater', 1)
    CreateParticle('phefcmn_fallwater', 2)

@State
def ph254_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddY(250000)
        AddX(100000)
        BlendMode_Normal()
        RotationAngle(60000)
        Size(950)
        E0EAEffectPosition(2)
    sprite('vr_ph254_00', 3)
    CreateParticle('phef201_kira', 0)
    CreateParticle('phef201_kira', 1)
    CreateParticle('phef201_kira', 2)
    CreateParticle('phef201_kira', 3)
    CreateParticle('phef201_kira', 4)
    CreateParticle('phef201_kira', 5)
    CreateParticle('phef201_kira', 6)
    SetScaleSpeed(3)
    sprite('vr_ph254_01', 3)
    sprite('vr_ph254_02', 3)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-22)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph255_eff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('ph202eff_00.DIG', '')
        AddY(210000)
        AddX(125000)
        SetScaleX(700)
        SetScaleY(800)
        RotationAngle(40000)
        E0EAEffectPosition(2)
    sprite('null', 3)
    CreateParticle('phef202_patchin', -1)
    CommonSE('015_blaze_0')
    sprite('null', 3)
    E0EAEffectPosition(0)
    sprite('null', 5)
    CreateParticle('phef202_hinoko', -1)
    CreateObject('ph255_effSub', -1)

@State
def ph255_effSub():

    def upon_IMMEDIATE():
        Visibility(1)
        AddX(20000)
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 0)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(700)
    AddY(-100000)
    RotationAngle(-40000)
    ApplyFunctionsToSelf()
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 1)
    ApplyFunctionsToObjects(1)
    SetScaleX(700)
    SetScaleY(-700)
    RotationAngle(20000)
    AddX(-50000)
    AddY(-140000)
    ApplyFunctionsToSelf()
    sprite('vr_ph202effpos_00', 3)
    CreateObject('phCmnFireEff', 2)
    ApplyFunctionsToObjects(1)
    Flip()
    Size(800)
    AddY(-300000)
    AddX(100000)
    RotationAngle(-40000)
    ApplyFunctionsToSelf()

@State
def DriveAtk_NNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleY(4000)
        AddX(250000)
        AddY(200000)
        AttackLevel_(3)
        Damage(750)
        AttackP1(90)
        BonusProration(110)
        UseSlashHitspark(1)
        HitsparkSize(700)
        AirUntechableTime(35)
        AirPushbackX(15000)
        AirPushbackY(6000)
        CHGroundedHitstunAnimation(2)
        CHStagger(45)
        CHCrumple(35)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 0):
                AutoHitStopSending(1)
            ObjectUpon(3, 32)
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_NNN', -1)
    SetScaleX(7500)
    AddX(-120000)
    sprite('vr_ph_magictest', 2)
    SetScaleX(15000)
    AddX(120000)

@State
def Eff_NNN():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddX(-300000)
        AddY(70000)
        Size(1000)
    sprite('vr_ph5d_00', 2)
    physicsXImpulse(32000)
    CreateObject('Eff_NNNsub', -1)
    PrivateSE('phse_04')
    sprite('vr_ph5d_00', 1)
    physicsXImpulse(1000)
    CreateParticle('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_01', 2)
    CreateParticle('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_02', 2)
    CreateParticle('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_03', 2)
    physicsXImpulse(-1000)
    CreateParticle('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_04', 2)
    CreateParticle('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_05', 2)
    CreateParticle('phef_nnn_nokosi', 0)

@State
def Eff_NNNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RenderLayer(1)
    sprite('null', 60)
    LinkParticle('phef_nnn')
    CreateObject('Eff_NNNsub2', -1)

@State
def Eff_NNNsub2():

    def upon_IMMEDIATE():
        Eff3DEffect('phef_nnn00', '')
        BlendMode_Normal()
        RenderLayer(1)
        AlphaValue(200)
    sprite('null', 8)
    sprite('null', 2)
    ConstantAlphaModifier(-26)
    SetScaleX(600)
    SetScaleY(900)
    sprite('null', 2)
    SetScaleX(450)
    SetScaleY(700)
    sprite('null', 5)

@State
def DriveAtk_RNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6000)
        SetScaleY(11000)
        if (SLOT_19 < 400000):
            Unknown1008()
            TeleportToObject(22)
            NoVerticalTracking()
        else:
            AddX(400000)
        AddY(75000)
        AttackLevel_(3)
        Damage(900)
        AttackP2(69)
        AirPushbackX(2000)
        AirPushbackY(43000)
        AirUntechableTime(38)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        FatalCounter(1)
        WallCollisionDetection(1)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 256):
                AutoHitStopSending(1)

        def upon_32():
            Damage(1080)
            AttackP2(79)

        def upon_33():
            callSubroutine('RedOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_RNN', -1)

@State
def Eff_RNN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_rnn00', '')
        Size(1200)
        AddY(50000)
        WallCollisionDetection(1)
    sprite('null', 8)
    CreateObject('Eff_RNNsub', -1)
    CommonSE('016_explode_0')
    sprite('null', 3)
    AddScaleY(50)
    sprite('null', 3)
    AddScaleY(50)
    sprite('null', 8)
    AddScaleY(50)
    BlendMode_Add()
    CreateObject('Eff_RNNsub2', -1)

@State
def Eff_RNNsub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Eff3DEffect('pheff_rnn01', '')
        Size(1200)
    sprite('null', 16)
    ConstantAlphaModifier(-10)

@State
def Eff_RNNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Size(800)
    sprite('null', 60)
    LinkParticle('phef_rnn_mc')

@State
def DriveAtk_GNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(20000)
        SetScaleY(2500)
        AddX(650000)
        AddY(210000)
        AttackLevel_(3)
        Damage(700)
        AttackP2(69)
        SingleProration(1)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Floorslide(40)
        GroundedHitstunAnimation(9)
        AirUntechableTime(25)
        EnemyHitstopAddition(0, 0, 0)
        HitsparkSize(500)
        UseSlashHitspark(1)
        PushbackX(39800)
        VoodooDamageMultiplier(3)
        Visibility(1)

        def upon_32():
            Damage(840)
            AttackP2(79)

        def upon_33():
            AirPushbackX(50000)
            AirPushbackY(15000)
            AirHitstunAfterWallbounce(28)
            Wallbounce(1)
            WallbounceReboundTime(25)
            FloorslideReset()
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 16):
                AutoHitStopSending(1)
    sprite('vr_ph_magictest', 1)
    CreateObject('Eff_GNN', -1)
    CreateObject('Eff_GNN', -1)
    ObjectUpon(1, 32)
    CreateObject('Eff_GNN', -1)
    ObjectUpon(1, 33)
    CommonSE('011_spin_0')
    CommonSE('011_spin_0')
    CommonSE('011_spin_1')
    PrivateSE('phse_01')
    SetScaleX(15000)
    AddX(-400000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    SetScaleX(25000)
    AddX(160000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    SetScaleX(40000)
    AddX(240000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def DriveAtk_GNN_PU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(40000)
        SetScaleY(2500)
        AddX(650000)
        AddY(210000)
        AttackLevel_(3)
        Damage(350)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Floorslide(40)
        AirUntechableTime(25)
        AttackP2(96)
        GroundedHitstunAnimation(9)
        EnemyHitstopAddition(0, 0, 0)
        YImpulseBeforeWallbounce(1800)
        PushbackX(39800)
        Hitstop(3)
        HitsparkSize(500)
        UseSlashHitspark(1)
        VoodooDamageMultiplier(3)
        Visibility(1)

        def upon_33():
            AirPushbackX(50000)
            AirPushbackY(15000)
            AirHitstunAfterWallbounce(28)
            Wallbounce(1)
            WallbounceReboundTime(25)
            FloorslideReset()
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 16):
                AutoHitStopSending(1)
    sprite('vr_ph_magictest', 1)
    CreateObject('Eff_GNN', -1)
    CreateObject('Eff_GNN', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 34)
    CreateObject('Eff_GNN', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 34)
    CommonSE('011_spin_0')
    CommonSE('011_spin_0')
    CommonSE('011_spin_1')
    PrivateSE('phse_01')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def Eff_GNN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_gnn00', '')
        AddX(-500000)
        AddY(40000)
        Size(700)
        AddScaleY(-200)

        def upon_32():
            AlphaValue(0)
            SetActionMark(3)
            AddX(350000)

        def upon_33():
            AlphaValue(0)
            SetActionMark(6)
            AddX(700000)

        def upon_34():
            AlphaValue(255)

        def upon_FRAME_STEP():
            if SLOT_2:
                AddActionMark(-1)
                if (not SLOT_2):
                    AlphaValue(255)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('phef_gnn_moya02', -1)
    if (not SLOT_2):
        CreateParticle('phef_gnn_mc', -1)
    CreateObject('Eff_GNNsub', -1)
    sprite('null', 2)
    CreateObject('Eff_GNNsub', -1)
    ApplyFunctionsToObjects(1)
    AddX(200000)
    ApplyFunctionsToSelf()
    sprite('null', 12)
    ExitState()

@State
def Eff_GNNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_gnn01', '')
    sprite('null', 8)
    SetScaleSpeed(15)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def DriveAtk_BNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(14500)
        SetScaleY(4000)
        AddX(330000)
        AddY(180000)
        AttackLevel_(3)
        Damage(800)
        AttackP2(69)
        AirPushbackX(100)
        AirPushbackY(28000)
        Hitstop(6)
        EnemyHitstopAddition(5, 5, 7)
        FreezeCount(1)
        FreezeTime(36)
        ChipPercentage(40)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 1):
                AutoHitStopSending(1)

        def upon_32():
            Damage(960)
            AttackP2(79)

        def upon_33():
            callSubroutine('BlueOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_BNN', -1)

@State
def Eff_BNN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bnn00', '')
        Size(1000)
        AddX(-100000)
        AddY(35000)
    sprite('null', 5)
    CreateObject('Eff_BNNsub', -1)
    sprite('null', 4)
    AddScale(100)
    sprite('null', 3)
    AddScale(-50)
    AlphaValue(200)
    sprite('null', 3)
    AddScale(-50)
    AlphaValue(100)
    CreateParticle('phef_bnn_moya', -1)

@State
def Eff_BNNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bnn01', '')
        Size(750)
        CreateParticle('phef_bnn_mc', -1)
    sprite('null', 5)
    CommonSE('017_freeze_1')
    AddScale(200)
    sprite('null', 5)
    AddScale(200)
    sprite('null', 2)
    AddScale(-200)
    sprite('null', 2)
    CommonSE('018_ice_break_1')
    AddScale(-200)

@State
def DriveAtk_RRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6000)
        SetScaleY(13000)
        if (SLOT_19 < 400000):
            Unknown1008()
            TeleportToObject(22)
            NoVerticalTracking()
        else:
            AddX(400000)
        AddY(75000)
        AttackLevel_(4)
        Damage(1200)
        AttackP2(72)
        AirPushbackX(1000)
        AirPushbackY(43000)
        AirUntechableTime(38)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        FatalCounter(1)
        WallCollisionDetection(1)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 512):
                AutoHitStopSending(1)

        def upon_32():
            Damage(1440)
            AttackP2(82)

        def upon_33():
            callSubroutine('RedOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_RRN', -1)

@State
def Eff_RRN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_rnn00', '')
        Size(1350)
        AddY(50000)
        WallCollisionDetection(1)
    sprite('null', 8)
    CreateObject('Eff_RNNsub', -1)
    CreateObject('Eff_RRNsub2Mato', -1)
    CommonSE('016_explode_1')
    sprite('null', 3)
    AddScaleY(50)
    sprite('null', 3)
    AddScaleY(50)
    sprite('null', 8)
    AddScaleY(50)
    BlendMode_Add()
    CreateObject('Eff_RRNsub', -1)

@State
def Eff_RRNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Eff3DEffect('pheff_rnn01', '')
        Size(1350)
    sprite('null', 16)
    ConstantAlphaModifier(-10)

@State
def Eff_RRNsub2Mato():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 4)
    CreateParticle('phef_rrn_bg', -1)
    CreateObject('Eff_RRNsub2', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(25500)
    ApplyFunctionsToSelf()
    sprite('null', 4)
    CreateObject('Eff_RRNsub2', -1)
    ApplyFunctionsToObjects(1)
    AddY(100000)
    AddScale(-125)
    Flip()
    RotationAngle(-25500)
    ApplyFunctionsToSelf()
    sprite('null', 4)
    CreateObject('Eff_RRNsub2', -1)
    ApplyFunctionsToObjects(1)
    AddY(200000)
    AddScale(-125)
    RotationAngle(25500)
    ApplyFunctionsToSelf()

@State
def Eff_RRNsub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_rrn00', '')
        Size(1450)
        AlphaValue(255)
    sprite('null', 15)
    SetScaleSpeed(20)
    sprite('null', 4)
    ConstantAlphaModifier(-51)

@State
def DriveAtk_GGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(40000)
        SetScaleY(2500)
        AddX(650000)
        AddY(210000)
        AttackLevel_(4)
        Damage(500)
        AttackP2(72)
        SingleProration(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Floorslide(40)
        AirUntechableTime(25)
        Hitstop(4)
        EnemyHitstopAddition(0, 0, 0)
        HitsparkSize(500)
        UseSlashHitspark(1)
        PushbackX(60800)
        VoodooDamageMultiplier(3)
        Visibility(1)

        def upon_32():
            SetActionMark(1)
            AttackP2(82)

        def upon_33():
            AirPushbackX(55000)
            AirPushbackY(12500)
            AirHitstunAfterWallbounce(28)
            Wallbounce(1)
            WallbounceReboundTime(22)
            FloorslideReset()
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 32):
                AutoHitStopSending(1)
    sprite('vr_ph_magictest', 1)
    Damage(500)
    if SLOT_2:
        Damage(600)
    RefreshMultihit()
    CreateObject('Eff_GGN', -1)
    CreateObject('Eff_GGN', -1)
    ObjectUpon(1, 32)
    CreateObject('Eff_GGN', -1)
    ObjectUpon(1, 33)
    CommonSE('011_spin_2')
    CommonSE('011_spin_2')
    CommonSE('006_swing_blade_2')
    CommonSE('022_magiccircle_b')
    SetScaleX(15000)
    AddX(-400000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Damage(800)
    if SLOT_2:
        Damage(960)
    RefreshMultihit()
    SetScaleX(25000)
    AddX(160000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    SetScaleX(40000)
    AddX(240000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def DriveAtk_GGN_PU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(40000)
        SetScaleY(2500)
        AddX(650000)
        AddY(210000)
        AttackLevel_(4)
        Damage(250)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Floorslide(40)
        AirUntechableTime(25)
        AttackP2(97)
        YImpulseBeforeWallbounce(1800)
        PushbackX(37500)
        Hitstop(2)
        EnemyHitstopAddition(0, 0, 0)
        HitsparkSize(500)
        UseSlashHitspark(1)
        PushbackX(60800)
        VoodooDamageMultiplier(3)
        Visibility(1)

        def upon_33():
            AirPushbackX(50000)
            AirPushbackY(12500)
            AirHitstunAfterWallbounce(28)
            Wallbounce(1)
            WallbounceReboundTime(22)
            FloorslideReset()
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 32):
                AutoHitStopSending(1)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    CreateObject('Eff_GGN', -1)
    CreateObject('Eff_GGN', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 34)
    CreateObject('Eff_GGN', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 34)
    CommonSE('011_spin_2')
    CommonSE('011_spin_2')
    CommonSE('006_swing_blade_2')
    CommonSE('022_magiccircle_b')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def Eff_GGN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_ggn00', '')
        AddX(-500000)
        AddY(40000)
        Size(700)
        AddScaleY(-150)
        RotationAngle(2000)

        def upon_32():
            AlphaValue(0)
            SetActionMark(3)
            AddX(350000)

        def upon_33():
            AlphaValue(0)
            SetActionMark(6)
            AddX(700000)

        def upon_34():
            AlphaValue(255)

        def upon_FRAME_STEP():
            if SLOT_2:
                AddActionMark(-1)
                if (not SLOT_2):
                    AlphaValue(255)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('phef_ggn_moya02', -1)
    if (not SLOT_2):
        CreateObject('Eff_GNNmc', -1)
    CreateObject('Eff_GGNsub', -1)
    sprite('null', 2)
    CreateObject('Eff_GGNsub', -1)
    ApplyFunctionsToObjects(1)
    AddX(200000)
    ApplyFunctionsToSelf()
    sprite('null', 12)
    ExitState()

@State
def Eff_GGNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_gnn01', '')
    sprite('null', 8)
    SetScaleSpeed(30)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def Eff_GNNmc():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef_gnn_mc')
    sprite('null', 20)

@State
def DriveAtk_BBN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(16000)
        SetScaleY(4000)
        AddX(305000)
        AddY(180000)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(72)
        AirPushbackX(100)
        AirPushbackY(28000)
        Hitstop(7)
        EnemyHitstopAddition(5, 5, 10)
        FreezeCount(1)
        FreezeTime(36)
        ChipPercentage(40)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 2):
                AutoHitStopSending(1)

        def upon_32():
            Damage(1200)
            AttackP2(82)

        def upon_33():
            callSubroutine('BlueOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_BBN', -1)

@State
def Eff_BBN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bbn00', '')
        Size(1000)
        AddScaleX(100)
        AddX(-125000)
        AddY(25000)
    sprite('null', 5)
    CreateObject('Eff_BNNsub', -1)
    ApplyFunctionsToObjects(1)
    AddScale(150)
    ApplyFunctionsToSelf()
    CommonSE('017_freeze_1')
    sprite('null', 4)
    AddScale(100)
    sprite('null', 3)
    AddScale(-50)
    AlphaValue(200)
    sprite('null', 3)
    AddScale(-50)
    AlphaValue(100)
    BlendMode_Add()
    CreateParticle('phef_bbb', -1)
    CommonSE('018_ice_break_1')

@State
def DriveAtk_BGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        E0EAEffectDirection(3)
        RemoveOnContact(3)
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AirUntechableTime(30)
        AirPushbackY(12000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        DistanceCheck(150000, -150000, 300000, -300000)
        StarterRating(2)
        AddY(300000)
        AddX(100000)
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        ParticleLayer(7)
        CallPrivateEffect('phef_bgn_00')
        RenderLayer(8)
        PaletteIndex(0)
        Size(1000)
        BlendMode_Normal()
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 2)

        def upon_FRAME_STEP():
            if (not CopyFromRightToLeft(23, 2, 0, 3, 2, 23)):
                if Unknown68(1, 0, 0, 0, 0):
                    PrivateFunction3(3, 120000, 0, 20, 1)
                else:
                    PrivateFunction3(3, 120000, 80000, 20, 1)
            else:
                CopyFromRightToLeft(23, 2, 0, 3, 2, 13)
                if (not (0 >= SLOT_0)):
                    PrivateFunction3(3, 120000, -80000, 20, 1)
                else:
                    PrivateFunction3(3, 120000, 0, 20, 1)
        RunLoopUpon(17, 180)

        def upon_17():
            sendToLabel(1)

        def upon_32():
            sendToLabel(1)
    sprite('vr_ph', 4)
    StartMultihit()
    setGravity(-200)
    PrivateSE('phse_04')
    ConstantAlphaModifier(51)
    CreateObject('Eff_BGNeye', -1)
    RegisterObject(4, 1)
    label(0)
    sprite('vr_ph', 30)
    PerGravity(-100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ph', 10)
    EndMomentum(1)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(54)
    clearUponHandler(32)
    EndAttack()
    ConstantAlphaModifier(-26)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_bgn_end', -1)
    ExitState()
    label(2)
    sprite('vr_ph', 10)
    EndMomentum(1)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(54)
    clearUponHandler(32)
    EndAttack()
    ConstantAlphaModifier(-26)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CreateParticle('phef216_smoke', -1)

@State
def DriveDef_BGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Visibility(1)
        E0EAEffectDirection(2)

        def upon_35():
            clearUponHandler(32)
            clearUponHandler(35)
            clearUponHandler(14)
            sendToLabel(2)

        def upon_PLAYER_HIT():
            clearUponHandler(32)
            clearUponHandler(35)
            clearUponHandler(14)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(35)
            clearUponHandler(14)
            sendToLabel(1)

        def upon_33():
            setInvincible(0)
            ObjectUpon(4, 34)

        def upon_34():
            setInvincible(1)
            ObjectUpon(4, 35)

        def upon_STATE_END():
            SLOT_8 = 0
        NoDamageAction(1)
        NoAttackDuringAction(1)
        Unknown23142(1)
        SetScaleX(7000)
        SetScaleY(14000)

        def upon_FRAME_STEP():
            if (not CopyFromRightToLeft(23, 2, 0, 3, 2, 23)):
                PrivateFunction3(3, 0, -250000, 100, 1)
            else:
                CopyFromRightToLeft(23, 2, 0, 3, 2, 13)
                if (not (0 >= SLOT_0)):
                    PrivateFunction3(3, 0, -180000, 100, 1)
                else:
                    PrivateFunction3(3, 0, -250000, 100, 1)
    sprite('null', 13)
    AlphaValue(128)
    InvincibleState(1)
    CreateObject('Eff_BGN', -1)
    RegisterObject(4, 1)
    sprite('vr_ph_magictestEx01', 600)
    SLOT_8 = 180
    label(1)
    sprite('vr_ph_magictestEx01', 8)
    ObjectUpon(4, 32)
    sprite('null', 10)
    SLOT_8 = 0
    ExitState()
    label(2)
    sprite('null', 10)
    ObjectUpon(4, 33)
    SLOT_8 = 0
    ExitState()

@State
def Eff_BGN():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        ParticleLayer(7)
        CallPrivateEffect('phef_bgn_00')
        RenderLayer(8)
        AddY(300000)
        AddX(100000)
        RemoveOnContact(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        PaletteIndex(0)
        Size(1000)
        BlendMode_Normal()
        AlphaValue(0)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)

        def upon_34():
            AlphaValue(255)
            ConstantAlphaModifier(0)
            RemoveOnContact(3)
            ObjectUpon(4, 32)

        def upon_35():
            AlphaValue(0)
            ConstantAlphaModifier(0)
            RemoveOnContact(0)
            ObjectUpon(4, 33)

        def upon_FRAME_STEP():
            PrivateFunction3(3, 100000, 80000, 50, 1)
    sprite('null', 5)
    sprite('null', 5)
    PrivateSE('phse_04')
    sprite('vr_ph', 4)
    ConstantAlphaModifier(51)
    CreateObject('Eff_BGNeye', -1)
    RegisterObject(4, 1)
    label(0)
    sprite('vr_ph', 20)
    physicsYImpulse(-1500)
    sprite('vr_ph', 10)
    physicsYImpulse(-750)
    sprite('vr_ph', 5)
    physicsYImpulse(-375)
    sprite('vr_ph', 20)
    physicsYImpulse(1500)
    sprite('vr_ph', 10)
    physicsYImpulse(750)
    sprite('vr_ph', 5)
    physicsYImpulse(375)
    gotoLabel(0)
    label(1)
    sprite('vr_ph', 10)
    ConstantAlphaModifier(-26)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_bgn_end', -1)
    ExitState()
    label(2)
    sprite('vr_ph', 10)
    ConstantAlphaModifier(-26)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_bgn_end', -1)
    CreateParticle('phef_bgn_guard', -1)
    ExitState()

@State
def Eff_BGNeye():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(2)
        E0EAEffectObjectZ(3)
        ParticleColorFromPalette(1, 1, 1)
        ParticleLayer(9)
        CallPrivateEffect('phef_bgn_00b')
        RemoveOnContact(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
    label(0)
    sprite('null', 32767)
    AlphaValue(255)
    loopRest()
    label(1)
    sprite('null', 32767)
    AlphaValue(0)
    loopRest()

@State
def DriveAtk_BRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6000)
        SetScaleY(6000)
        AddX(200000)
        AddY(150000)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(82)
        BonusProration(110)
        Hitstop(0)
        ProjectileLevel(1)
        EnemyHitstopAddition(10, 10, 15)
        AirPushbackX(2500)
        AirPushbackY(20000)
        AirUntechableTime(100)
        AttackP1(80)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        CollideWithWall(1)
        Visibility(1)
        StarterRating(2)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 1)

        def upon_32():
            clearUponHandler(10)
            clearUponHandler(32)
            SetActionMark(0)
            sendToLabel(1)
    sprite('vr_ph_magictest', 14)
    SetActionMark(18)
    CreateObject('Eff_BRN', -1)
    PrivateSE('phse_04')
    CreateParticle('phef_rbn_mc', -1)
    label(0)
    sprite('vr_ph_magictest', 13)
    RefreshMultihit()
    CreateObject('Eff_BRN', -1)
    AddX(120000)
    if (SLOT_2 <= 12):
        AddX(-20000)
    if (SLOT_2 <= 9):
        AddX(-20000)
    if (SLOT_2 <= 6):
        AddX(-20000)
    sprite('vr_ph_magictest', 1)
    if SLOT_2:
        AddActionMark(-1)
        sendToLabel(0)
    label(1)
    sprite('null', 10)
    clearUponHandler(54)
    clearUponHandler(32)

@State
def Eff_BRN():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Eff3DEffect('pheff_brn00', '')
        LinkParticle('phef_brn_00')
        AddY(75000)
    sprite('null', 2)
    AlphaValue(255)
    CreateParticle('phef_brn_00a2', -1)
    CreateObject('Eff_BRNsub', -1)
    CommonSE('014_electric_sl')
    sprite('null', 2)
    RandAddRotation(-90000, 90000)
    AlphaValue(255)
    CreateObject('Eff_BRNsub', -1)
    sprite('null', 2)
    CreateObject('Eff_BRNsub', -1)
    sprite('null', 2)
    RandAddRotation(-90000, 90000)
    sprite('null', 2)
    sprite('null', 2)
    BlendMode_Add()
    Size(1075)
    RandAddRotation(-90000, 90000)
    sprite('null', 2)
    sprite('null', 3)
    Size(1100)

@State
def Eff_BRNsub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('pheff_brn01', '')
        Size(750)
        RandAddScale(-50, 250)
        RandAddRotation(-360000, 360000)
    sprite('null', 2)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(128)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(128)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(128)

@State
def DriveAtk_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6500)
        SetScaleY(13000)
        AddY(75000)
        AttackLevel_(4)
        Damage(700)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Floorslide(19)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        PassByArmor(1)
        StarterRating(2)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(11)
            ObjectUpon(2, 34)
    sprite('vr_ph_magictest', 5)

@State
def DriveReAtk_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        E0EAEffectPosition(2)
        SetScaleX(4000)
        SetScaleY(13000)
        AddX(0)
        AddY(75000)
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirPushbackX(40000)
        AirPushbackY(25000)
        AirHitstunAfterWallbounce(40)
        WallbounceReboundTime(0)
        Wallbounce(1)
        Hitstop(6)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AttackP1(80)
        HardKnockdown(1)
        StarterRating(2)
        Visibility(1)

        def upon_32():
            clearUponHandler(32)
            EndAttack()
    sprite('null', 1)
    sprite('vr_ph_magictest', 15)

@State
def DriveDef_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Visibility(1)
        CancelIfPlayerHit(0)
        AddX(100000)
        setInvincible(1)
        ArmorHealth(3000)
        GuardPoint_(1)
        SpecificInvincibility(0, 0, 0, 1, 0)
        BurstInvincibility(0)
        FloorCollision(1)
        WallCollisionDetection(1)
        EnableCollision(1)
        SetXCollisionFromOrigin(105)
        PushCollisionHeightLow(-100000)

        def upon_40():
            TurnAround()
            CommonSE('100_hit_grap_2')
            CreateParticle('ef_hitmd', 0)
            physicsXImpulse(100000)
            CreateObject('DriveReAtk_GRN', -1)
            IgnorePauses(3)

            def upon_FRAME_STEP():
                XImpulseAcceleration(90)

        def upon_41():
            TurnAround()
            CommonSE('100_hit_grap_2')
            CreateParticle('ef_hitmd', 0)
            physicsXImpulse(-50000)
            CreateObject('DriveReAtk_GRN', -1)

        def upon_44():
            clearUponHandler(44)
            sendToLabel(1)

        def upon_34():
            AddX(50000)
            EnableCollision(0)
            SLOT_51 = 10

            def upon_FRAME_STEP():
                SLOT_51 = (SLOT_51 + (-1))
                if (SLOT_51 <= 0):
                    EnableCollision(1)

        def upon_32():
            EnableCollision(0)
            sendToLabel(1)
        CurrentHP(1)

        def upon_PLAYER_HIT():
            EnableCollision(0)
            sendToLabel(1)
        SetActionMark(0)

        def upon_GUARDPOINT_ACTIVATION():
            ObjectUpon(3, 40)
            CopyFromRightToLeft(23, 2, 0, 22, 2, 38)
            if op(15, 2, 0, 2, 38):
                if (SLOT_2 == 0):
                    sendToLabel(2)
                if (SLOT_2 == 1):
                    sendToLabel(3)
                if (SLOT_2 == 2):
                    sendToLabel(4)
                AddActionMark(1)
                if (SLOT_2 >= 3):
                    SetActionMark(0)
        NoAttackDuringAction(1)
    sprite('null', 1)
    CreateObject('DriveAtk_GRN', -1)
    CreateObject('Eff_GRN', -1)
    RegisterObject(4, 1)
    PrivateSE('phse_04')
    sprite('phdrivecol_grn', 10)
    AlphaValue(128)
    physicsXImpulse(20000)
    sprite('phdrivecol_grn', 10)
    XImpulseAcceleration(60)
    sprite('phdrivecol_grn', 10)
    XImpulseAcceleration(60)
    sprite('phdrivecol_grn', 10)
    XImpulseAcceleration(60)
    sprite('phdrivecol_grn', 10)
    XImpulseAcceleration(60)
    sprite('phdrivecol_grn', 10)
    XImpulseAcceleration(60)
    label(0)
    sprite('phdrivecol_grn', 300)
    XImpulseAcceleration(60)
    label(1)
    sprite('null', 10)
    clearUponHandler(42)
    clearUponHandler(14)
    clearUponHandler(44)
    clearUponHandler(32)
    clearUponHandler(40)
    clearUponHandler(41)
    PassbackAddActionMarkToFunction('DriveReAtk_GRN', 32)
    ObjectUpon(4, 32)
    ExitState()
    label(2)
    sprite('phdrivecol_grn', 30)
    CreateObject('DriveDef_GRN_ATK', 0)
    CreateObject('Eff_GRNatk', -1)
    sendToLabel(0)
    ExitState()
    label(3)
    sprite('phdrivecol_grn', 30)
    CreateObject('DriveDef_GRN_ATK', 1)
    CreateObject('Eff_GRNatk', -1)
    sendToLabel(0)
    ExitState()
    label(4)
    sprite('phdrivecol_grn', 30)
    CreateObject('DriveDef_GRN_ATK', 2)
    CreateObject('Eff_GRNatk', -1)
    sendToLabel(0)
    ExitState()

@State
def DriveDef_GRN_ATK():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(4000)
        SetScaleY(2000)
        AttackLevel_(3)
        Damage(650)
        ProjectileLevel(2)
        UseSlashHitspark(1)
        Hitstop(3)
        PassByArmor(1)
        HitsparkSize(300)
        EnemyHitstopAddition(8, 8, 10)
        AttackP1(50)
        AttackP2(94)
        SameMoveProration(-1)
        GroundedHitstunAnimation(2)
        StarterRating(2)
        BlendMode_Normal()
        Eff3DEffect('pheff_grn02', '')
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Visibility(1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    PassbackAddActionMarkToFunction('Eff_GRNmc', 32)
    CreateObject('Eff_GRNmc', -1)
    sprite('vr_ph_magictest', 30)
    physicsXImpulse(120000)
    CreateObject('Eff_GRNnokosi', -1)

@State
def Eff_GRN():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_grn00', '')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Size(500)
        AlphaValue(0)
        AddY(200000)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    CallCustomizableParticle('phef_rnn_start', -1)
    CreateObject('Eff_GRNsub', -1)
    SetScaleX(0)
    SetScaleXPerFrame(100)
    ConstantAlphaModifier(51)
    gotoLabel(0)
    label(0)
    sprite('null', 20)
    SetScaleXPerFrame(0)
    physicsYImpulse(400)
    ConstantAlphaModifier(-2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_rnn_jizoku', -1)
    sprite('null', 10)
    physicsYImpulse(200)
    sprite('null', 20)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_rnn_jizoku', -1)
    ConstantAlphaModifier(2)
    physicsYImpulse(-400)
    sprite('null', 10)
    physicsYImpulse(-200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_rnn_end', -1)
    ConstantAlphaModifier(-51)
    SetScaleXPerFrame(-60)
    SetScaleSpeedY(60)
    loopRest()

@State
def Eff_GRNsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_grn01', '')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        RemoveOnContact(2)
        E0EAEffectScale(2)
    sprite('null', 32767)

@State
def Eff_GRNatk():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Eff3DEffect('pheff_grn01', '')
        Size(650)
        AddY(200000)
    sprite('null', 5)
    SetScaleSpeedY(7)
    SetScaleXPerFrame(15)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def Eff_GRNmc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_grn_atk00')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 55)
    label(1)
    sprite('null', 5)

@State
def Eff_GRNnokosi():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(2)
    label(0)
    sprite('null', 2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_grn_nokosi', -1)
    gotoLabel(0)

@State
def DriveAtk_RRR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6000)
        SetScaleY(15000)
        if (SLOT_19 < 400000):
            Unknown1008()
            TeleportToObject(22)
            NoVerticalTracking()
        else:
            AddX(400000)
        AddY(75000)
        AttackLevel_(5)
        Damage(1500)
        AttackP2(74)
        AirPushbackX(0)
        AirPushbackY(43000)
        AirUntechableTime(38)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        FatalCounter(1)
        WallCollisionDetection(1)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 768):
                AutoHitStopSending(1)

        def upon_32():
            Damage(1800)
            AttackP2(84)

        def upon_33():
            callSubroutine('RedOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_RRR', -1)

@State
def Eff_RRR():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_rrr01', '')
        SetScaleY(1750)
        SetScaleX(1500)
        AddY(50000)
        WallCollisionDetection(1)
    sprite('null', 8)
    CreateObject('Eff_RNNsub', -1)
    CreateObject('Eff_RRRsub2Mato', -1)
    CommonSE('016_explode_2')
    ScreenShake(5000, 5000)
    sprite('null', 3)
    AddScaleY(25)
    sprite('null', 3)
    AddScaleY(25)
    sprite('null', 8)
    AddScaleY(25)
    BlendMode_Add()
    CreateObject('Eff_RRRsub', -1)

@State
def Eff_RRRsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Eff3DEffect('pheff_rnn01', '')
        Size(1350)
    sprite('null', 16)
    ConstantAlphaModifier(-10)

@State
def Eff_RRRsub2Mato():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
    sprite('null', 6)
    CreateParticle('phef_rrr_bg', -1)
    CreateObject('Eff_RRRsub2', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(25500)
    ApplyFunctionsToSelf()
    sprite('null', 6)
    CreateObject('Eff_RRRsub2', -1)
    ApplyFunctionsToObjects(1)
    AddY(100000)
    AddScale(-125)
    Flip()
    RotationAngle(-25500)
    ApplyFunctionsToSelf()
    sprite('null', 6)
    CreateObject('Eff_RRRsub2', -1)
    ApplyFunctionsToObjects(1)
    AddY(200000)
    AddScale(100)
    RotationAngle(25500)
    ApplyFunctionsToSelf()
    sprite('null', 12)

@State
def Eff_RRRsub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Eff3DEffect('pheff_rrr00', '')
        Size(1450)
        AlphaValue(255)
    sprite('null', 14)
    SetScaleSpeed(20)
    sprite('null', 4)
    ConstantAlphaModifier(-51)

@State
def Wind_Herald():

    def upon_IMMEDIATE():
        AddY(260000)
        SetScaleX(700)
        LinkParticle('phef_g_yotyou')
    sprite('null', 7)
    sprite('null', 4)
    ConstantAlphaModifier(-51)

@State
def DriveAtk_GGG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(40000)
        SetScaleY(2500)
        AddX(650000)
        AddY(210000)
        AttackLevel_(5)
        Damage(500)
        AttackP2(74)
        SingleProration(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Floorslide(40)
        AirUntechableTime(25)
        Hitstop(2)
        EnemyHitstopAddition(0, 0, 0)
        HitsparkSize(500)
        UseSlashHitspark(1)
        PushbackX(79800)
        VoodooDamageMultiplier(3)
        Visibility(1)

        def upon_32():
            SetActionMark(1)
            AttackP2(84)

        def upon_33():
            AirPushbackX(60000)
            AirPushbackY(8000)
            AirHitstunAfterWallbounce(28)
            Wallbounce(1)
            WallbounceReboundTime(20)
            FloorslideReset()
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 48):
                AutoHitStopSending(1)
    sprite('vr_ph_magictest', 1)
    Damage(350)
    if SLOT_2:
        Damage(420)
    RefreshMultihit()
    CreateObject('Eff_GGG', -1)
    CreateObject('Eff_GGG', -1)
    ObjectUpon(1, 32)
    CreateObject('Eff_GGG', -1)
    ObjectUpon(1, 33)
    PrivateSE('phse_03')
    ScreenShake(5000, 5000)
    SetScaleX(15000)
    AddX(-400000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Damage(600)
    if SLOT_2:
        Damage(720)
    RefreshMultihit()
    SetScaleX(25000)
    AddX(160000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Damage(1000)
    if SLOT_2:
        Damage(1200)
    RefreshMultihit()
    SetScaleX(40000)
    AddX(240000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def DriveAtk_GGG_PU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(40000)
        SetScaleY(2500)
        AddX(650000)
        AddY(210000)
        AttackLevel_(5)
        Damage(210)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Floorslide(40)
        AirUntechableTime(25)
        Hitstop(1)
        AttackP2(98)
        YImpulseBeforeWallbounce(1800)
        PushbackX(59900)
        EnemyHitstopAddition(0, 0, 0)
        HitsparkSize(500)
        UseSlashHitspark(1)
        PushbackX(79800)
        VoodooDamageMultiplier(3)
        Visibility(1)

        def upon_33():
            AirPushbackX(45000)
            AirPushbackY(8000)
            AirHitstunAfterWallbounce(28)
            Wallbounce(1)
            WallbounceReboundTime(20)
            FloorslideReset()
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 48):
                AutoHitStopSending(1)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    CreateObject('Eff_GGG', -1)
    CreateObject('Eff_GGG', -1)
    ObjectUpon(1, 32)
    ObjectUpon(1, 34)
    CreateObject('Eff_GGG', -1)
    ObjectUpon(1, 33)
    ObjectUpon(1, 34)
    PrivateSE('phse_03')
    ScreenShake(5000, 5000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    ExitState()

@State
def Eff_GGG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_ggg00', '')
        AddX(-500000)
        AddY(40000)
        Size(750)
        AddScaleY(-300)
        RotationAngle(2000)

        def upon_32():
            AlphaValue(0)
            SetActionMark(3)
            AddX(350000)

        def upon_33():
            AlphaValue(0)
            SetActionMark(6)
            AddX(700000)

        def upon_34():
            AlphaValue(255)

        def upon_FRAME_STEP():
            if SLOT_2:
                AddActionMark(-1)
                if (not SLOT_2):
                    AlphaValue(255)
    sprite('null', 1)
    sprite('null', 1)
    if (not SLOT_2):
        CreateObject('Eff_GNNmc', -1)
    CreateParticle('phef_ggg_moya03', -1)
    CreateObject('Eff_GGGsub', -1)
    AddScaleY(50)
    sprite('null', 2)
    CreateObject('Eff_GGGsub', -1)
    ApplyFunctionsToObjects(1)
    AddX(200000)
    ApplyFunctionsToSelf()
    AddScaleY(-50)
    sprite('null', 2)
    AddScaleY(50)
    sprite('null', 2)
    AddScaleY(-50)
    sprite('null', 2)
    AddScaleY(50)
    sprite('null', 1)
    sprite('null', 5)
    ExitState()

@State
def Eff_GGGsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_gnn01', '')
    sprite('null', 8)
    SetScaleSpeed(45)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def DriveAtk_BBB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(17500)
        SetScaleY(5000)
        AddX(280000)
        AddY(170000)
        AttackLevel_(5)
        Damage(1250)
        AttackP2(74)
        AirPushbackX(100)
        AirPushbackY(28000)
        Hitstop(8)
        EnemyHitstopAddition(5, 5, 13)
        FreezeCount(1)
        FreezeTime(36)
        ChipPercentage(40)
        Visibility(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AutoHitStopSending(0)
            CopyFromRightToLeft(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 3):
                AutoHitStopSending(1)

        def upon_32():
            Damage(1500)
            AttackP2(84)

        def upon_33():
            callSubroutine('BlueOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_BBB', -1)

@State
def Eff_BBB():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bbb00', '')
        Size(675)
        AddX(-100000)
        AddY(70000)
    sprite('null', 4)
    CreateObject('Eff_BNNsub', -1)
    ApplyFunctionsToObjects(1)
    AddScale(225)
    ApplyFunctionsToSelf()
    CommonSE('017_freeze_0')
    CommonSE('017_freeze_0')
    sprite('null', 4)
    AddScale(100)
    sprite('null', 3)
    AddScale(-50)
    AlphaValue(200)
    CreateParticle('phef_bbb', -1)
    CommonSE('018_ice_break_0')
    CommonSE('018_ice_break_0')
    sprite('null', 4)
    AddScale(-50)
    SetScaleSpeed(7)
    ConstantAlphaModifier(-51)

@State
def DriveAtk_RRB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6000)
        SetScaleY(10000)
        AddY(375000)
        WallCollisionDetection(1)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
        if SLOT_51:
            if (SLOT_19 > 300000):
                if (SLOT_19 < 650000):
                    Unknown1008()
                    TeleportToObject(22)
                    NoVerticalTracking()
                else:
                    AddX(650000)
            else:
                AddX(300000)
        elif (SLOT_19 > 100000):
            if (SLOT_19 < 650000):
                Unknown1008()
                TeleportToObject(22)
                NoVerticalTracking()
            else:
                AddX(650000)
        else:
            AddX(100000)
        AttackLevel_(5)
        Damage(1050)
        AirPushbackX(1500)
        AirPushbackY(50000)
        Hitstop(3)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP1(100)
        AttackP2(79)
        AirPushbackX(3500)
        AirPushbackY(-60000)
        PushbackX(19950)
        StarterRating(2)
        HitOverhead(2)
        GroundBounce(1)
        BouncePercentage(30)
        AirUntechableTime(60)
        Visibility(1)
        FloorCollision(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(2)
            sendToLabel(2)
    sprite('vr_ph_magictest', 17)
    CreateObject('phEff_RRB', -1)
    RegisterObject(4, 1)
    PrivateSE('phse_04')
    CommonSE('019_quake_1')
    StartMultihit()
    physicsYImpulse(5000)
    setGravity(500)
    sprite('vr_ph_magictest', 32767)
    physicsYImpulse(-150000)
    label(1)
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    AirHitstunAnimation(9)
    AirPushbackX(5000)
    AirPushbackY(20000)
    AirUntechableTime(30)
    Blockstun(11)
    EnemyHitstopAddition(0, 7, 15)
    GroundBounceReset()
    PushbackX(19800)
    HitOverhead(0)
    ObjectUpon(4, 32)
    CreateObject('Eff_RRNsub2', -1)
    ApplyFunctionsToObjects(1)
    AddY(180000)
    Rotation(25000)
    AddScale(500)
    ApplyFunctionsToSelf()
    StartMultihit()
    CommonSE('016_explode_2')
    sprite('vr_ph_magictest', 5)
    CreateObject('Eff_RRNsub2', -1)
    ApplyFunctionsToObjects(1)
    AddY(60000)
    Rotation(15000)
    SetScaleSpeed(30)
    ApplyFunctionsToSelf()
    ExitState()
    label(2)
    sprite('null', 10)
    ConstantAlphaModifier(-23)
    ExitState()

@State
def phEff_RRB():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(100000)
        Size(1150)
        sendToLabelUpon(32, 1)
    sprite('vr_phrrb_01', 2)
    CreateObject('phEff_RRBSub', -1)
    sprite('vr_phrrb_02', 2)
    sprite('vr_phrrb_03', 2)
    sprite('vr_phrrb_04', 2)
    LinkParticle('phef_rrb_jizoku')
    sprite('vr_phrrb_05', 2)
    sprite('vr_phrrb_00', 4)
    label(0)
    sprite('vr_phrrb_00', 2)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageSize_1(1200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_phrrb_00', 3)
    SetScaleSpeed(30)
    sprite('null', 10)
    CreateParticle('phef_rrb_end', -1)
    ConstantAlphaModifier(-26)
    ScreenShake(10000, 10000)
    loopRest()

@State
def phEff_RRBSub():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
    sprite('null', 30)
    LinkParticle('phef_rrb_start')

@State
def DriveAtk_RRG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Visibility(1)
        SetScaleX(2500)
        SetScaleY(2500)
        AddX(100000)
        AddY(300000)
        OnlyHitIfHitstun(1)
        AttackOff()
        FloorCollision(1)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(2)

        def upon_4():
            clearUponHandler(4)
            AttackLevel_(3)
            Damage(100)
            AttackP1(90)
            AirPushbackY(-20000)
            AirUntechableTime(60)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            OnlyHitIfHitstun(0)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(7500)
    physicsYImpulse(10000)
    EndYPhysicsImpulse()
    CreateObject('phEff_RRGseed', -1)
    PrivateSE('phse_04')
    label(0)
    sprite('vr_ph_magictest', 32767)
    label(1)
    sprite('vr_ph_magictest', 10)
    AttackLevel_(5)
    Damage(900)
    HitLow(2)
    AirPushbackX(20000)
    AirPushbackY(-20000)
    AttackP2(84)
    Hitstop(0)
    PushbackX(19950)
    EnemyHitstopAddition(6, 6, 8)
    Floorslide(17)

    def upon_OPPONENT_HIT_OR_BLOCK():
        AddActionMark(1)

    def upon_FRAME_STEP():
        if (SLOT_2 >= 1):
            HitLow(0)
    DespawnEAEffect('phEff_RRGseed')
    CreateParticle('phef_rrb_umore', -1)
    SetScaleXPerFrame(500)
    SetScaleSpeedY(150)
    StartMultihit()
    EndMomentum(1)
    ForceFaceSprite()
    CommonSE('012_stab_deep')
    sprite('vr_ph_magictest', 15)
    CreateObject('phEff_RRGmoguri', -1)
    SetScaleX(7500)
    SetScaleY(4000)
    SetScaleXPerFrame(0)
    SetScaleSpeedY(0)
    StartMultihit()
    physicsXImpulse(1000)
    CommonSE('019_quake_1')
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    Stagger(40)
    Crumple(30)
    ForceFaceSprite()
    physicsXImpulse(45000)
    CreateObject('phEff_RRG', -1)
    CommonSE('005_swing_grap_2_2')
    PrivateSE('phse_05')
    sprite('vr_ph_magictest', 13)
    StartMultihit()
    XImpulseAcceleration(5)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()
    ForceFaceSprite()
    PushbackX(50000)
    GroundedHitstunAnimation(9)
    AirPushbackX(20000)
    Floorslide(12)
    HardKnockdown(20)
    physicsXImpulse(45000)
    CreateObject('phEff_RRG', -1)
    CommonSE('005_swing_grap_2_2')
    PrivateSE('phse_05')
    sprite('vr_ph_magictest', 20)
    StartMultihit()
    XImpulseAcceleration(5)
    ExitState()
    label(2)
    sprite('null', 10)
    ConstantAlphaModifier(-23)
    ExitState()

@State
def phEff_RRG():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(1000)
        Flip()
        LinkParticle('phef_rrb_kusa')
    sprite('null', 7)
    Eff3DEffect('pheff_rrg_start', '')
    ScreenShake(4000, 4000)
    CreateParticle('phef_rrb_kusa', -1)
    CreateObject('phEff_RRG_moya', -1)
    sprite('null', 10)
    Eff3DEffect('pheff_rrg_jizoku', '')
    sprite('null', 5)
    E0EAEffectPosition(0)
    sprite('null', 40)
    AlphaValue(0)
    CreateObject('phEff_RRGend', -1)
    PassbackAddActionMarkToFunction('phEff_RRG_moya', 32)

@State
def phEff_RRG_moya():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(1000)
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_rrg_moya')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('phef_rrg_tb', -1)

@State
def phEff_RRGseed():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(2)
        Size(1200)
        AddRotationPerFrame(1250)
        RenderLayer(8)
        ParticleLayer(7)
        CallPrivateEffect('phef_rrb_seed')
        EnableAfterimage(1)
    sprite('vr_phrrg_00', 10)
    AddRotationPerFrame(1250)
    sprite('vr_phrrg_00', 10)
    AddRotationPerFrame(625)
    sprite('vr_phrrg_00', 32767)
    AddRotationPerFrame(416)

@State
def phEff_RRGend():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1200)
    sprite('null', 15)
    CreateParticle('phef_rrb_kusa', -1)
    Eff3DEffect('pheff_rrg_end', '')

@State
def phEff_RRGmoguri():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 4)
    CreateParticle('phef_rrb_umore2', -1)
    gotoLabel(0)

@State
def DriveAtk_GGR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        CancelIfPlayerHit(3)
        Size(200)
        AddX(150000)
        AddY(225000)
        WallCollisionDetection(1)
        NoAttackDuringAction(1)
        Visibility(1)
        BlendMode_Normal()
        Eff3DEffect('pheff_ggr00', '')
        FaceSpawnLocation()
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_ggr_jizoku')
        SetActionMark(0)

        def upon_FRAME_STEP():
            if SLOT_2:
                YAccel(95)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(0)
    sprite('null', 10)
    CreateParticle('phef_ggr_mc', -1)
    AlphaValue(0)
    ConstantAlphaModifier(28)
    SetScaleSpeed(30)
    PrivateSE('phse_04')
    physicsXImpulse(5000)
    physicsYImpulse(5000)
    sprite('null', 10)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    sprite('null', 5)
    SetActionMark(1)
    XImpulseAcceleration(1200)
    YAccel(1800)
    sprite('null', 2)
    SetActionMark(0)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('null', 2)
    XImpulseAcceleration(40)
    YAccel(40)
    sprite('null', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SetScaleSpeed(100)
    sprite('null', 70)
    clearUponHandler(3)

    def upon_FRAME_STEP():
        CopyFromRightToLeft(23, 2, 52, 22, 2, 22)
        PrivateFunction(1, 2, 22, 2, 52, 2, 52)
        if SLOT_38:
            PrivateFunction(3, 2, 52, 0, 60, 2, 12)
        else:
            PrivateFunction(3, 2, 52, 0, -60, 2, 12)
    CreateObject('phEff_GGRYotyouMC', -1)
    SetScaleSpeed(0)
    sprite('null', 5)
    clearUponHandler(3)
    XImpulseAcceleration(80)
    CreateObject('phEff_GGRatk', -1)
    sprite('null', 5)
    XImpulseAcceleration(80)
    sprite('null', 5)
    XImpulseAcceleration(80)
    sprite('null', 5)
    XImpulseAcceleration(80)
    sprite('null', 5)
    XImpulseAcceleration(80)
    sprite('null', 5)
    physicsXImpulse(0)
    sprite('null', 3)
    PassbackAddActionMarkToFunction('phEff_GGRYotyouMC', 32)
    CreateObject('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    CreateObject('DriveAtk_GGR_LL', -1)
    sprite('null', 60)
    PassbackAddActionMarkToFunction('phEff_GGRatk', 32)
    PassbackAddActionMarkToFunction('phEff_GGRYotyouMC', 33)
    ConstantAlphaModifier(-25)
    ExitState()
    label(0)
    sprite('null', 15)
    PassbackAddActionMarkToFunction('phEff_GGRatk', 32)
    ConstantAlphaModifier(-15)
    ExitState()

@State
def DriveAtk_GGR_PreAtk():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(4000)
        SetScaleY(4000)
        AttackLevel_(2)
        Damage(300)
        AirPushbackX(15000)
        AirPushbackY(40000)
        AirUntechableTime(53)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        OnlyHitIfHitstun(1)
        Visibility(1)

        def upon_FRAME_STEP():
            PrivateFunction3(2, 10000, -10000, 100, 1)
    sprite('vr_ph_magictest', 10)

@State
def phEff_GGRatk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(200)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('pheff_ggr01', '')
        FaceSpawnLocation()

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    physicsYImpulse(-16000)
    SetScaleSpeed(20)
    CommonSE('016_explode_0')
    CommonSE('019_quake_1')
    sprite('null', 100)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    physicsYImpulse(0)
    SetScaleSpeed(0)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CallPrivateEffect('phef_ggr_ray')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-23)
    loopRest()

@State
def phEff_GGRtama():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RenderLayer(8)
        ParticleLayer(7)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_ggr_tamacolor')
        SetScaleX(1000)
    sprite('vr_phbbr_00', 2)
    AddY(150000)
    label(0)
    sprite('vr_phbbr_00', 2)
    CreateObject('Eff_GGRfire', -1)
    sprite('vr_phbbr_01', 2)
    sprite('vr_phbbr_02', 2)
    CreateObject('Eff_GGRfire2', -1)
    sprite('vr_phbbr_03', 2)
    gotoLabel(0)

@State
def Eff_GGRfire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectRotation(2)
        Eff3DEffect('pheff_ggrAtk00', '')
        SetScaleY(500)
        SetScaleX(600)
        RandAddScale(-100, 100)
    sprite('null', 3)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def Eff_GGRfire2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectRotation(2)
        Eff3DEffect('pheff_ggrAtk00', '')
        SetScaleY(500)
        SetScaleX(-600)
        RandAddScaleX(0, 200)
    sprite('null', 3)
    sprite('null', 5)
    RandAddScale(-100, 100)

@State
def phEff_GGRgshock():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Size(400)
        BlendMode_Add()
        PaletteIndex(2)
        RenderLayer(1)
        RandAddRotation(-360000, 360000)
        DeviationY(50000, 100000)
        DeviationX(-25000, 25000)
        RandAddScale(0, 300)
    sprite('vr_ph216_00', 2)
    SetScaleSpeed(30)
    sprite('vr_ph216_01', 2)
    sprite('vr_ph216_02', 2)
    sprite('vr_ph216_03', 2)
    sprite('vr_ph216_04', 2)
    sprite('vr_ph216_05', 5)

@Subroutine
def DriveAtk_GGR_Init():
    AttackLevel_(3)
    Damage(400)
    AirHitstunAnimation(10)
    AttackP1(80)
    AttackP2(94)
    AirUntechableTime(25)
    AirPushbackX(0)
    AirPushbackY(12000)
    Hitstop(0)
    EnemyHitstopAddition(2, 2, 4)
    PushbackX(0)
    HitsparkSize(300)
    PassByArmor(1)
    StarterRating(2)
    VoodooDamageMultiplier(2)

@State
def DriveAtk_GGR_C():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        SetScaleX(1500)
        SetScaleY(1500)
        AddY(-100000)
        Visibility(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    CommonSE('015_blaze_0')
    CreateObject('phEff_GGRtama', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(90000)
    ApplyFunctionsToSelf()
    physicsYImpulse(-60000)
    label(1)
    sprite('null', 1)
    CommonSE('016_explode_1')
    CreateObject('phEff_GGRgshock', -1)
    CreateParticle('phef_ggr_gshock', -1)
    EndMomentum(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    ExitState()

@State
def DriveAtk_GGR_L():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        AddX(-25000)
        AddY(-100000)
        SetScaleX(1500)
        SetScaleY(1500)
        Visibility(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(-11000)
    physicsYImpulse(-60000)
    CreateObject('phEff_GGRtama', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(90000)
    ApplyFunctionsToSelf()
    label(1)
    sprite('null', 1)
    CreateObject('phEff_GGRgshock', -1)
    CreateParticle('phef_ggr_gshock', -1)
    EndMomentum(1)
    ScreenShake(1000, 1000)
    loopRest()
    label(2)
    sprite('null', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    ExitState()

@State
def DriveAtk_GGR_LL():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        AddX(-50000)
        AddY(-100000)
        SetScaleX(1500)
        SetScaleY(1500)
        Visibility(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(-22000)
    physicsYImpulse(-60000)
    CreateObject('phEff_GGRtama', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(100000)
    ApplyFunctionsToSelf()
    label(1)
    sprite('null', 1)
    CreateObject('phEff_GGRgshock', -1)
    CreateParticle('phef_ggr_gshock', -1)
    EndMomentum(1)
    ScreenShake(1000, 1000)
    loopRest()
    label(2)
    sprite('null', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    ExitState()

@State
def DriveAtk_GGR_R():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        AddX(25000)
        AddY(-100000)
        SetScaleX(1500)
        SetScaleY(1500)
        Visibility(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(11000)
    physicsYImpulse(-60000)
    CreateObject('phEff_GGRtama', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(85000)
    ApplyFunctionsToSelf()
    label(1)
    sprite('null', 1)
    CreateObject('phEff_GGRgshock', -1)
    CreateParticle('phef_ggr_gshock', -1)
    EndMomentum(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    ExitState()

@State
def DriveAtk_GGR_RR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        AddX(50000)
        AddY(-100000)
        SetScaleX(1500)
        SetScaleY(1500)
        Visibility(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(22000)
    physicsYImpulse(-60000)
    CreateObject('phEff_GGRtama', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(75000)
    ApplyFunctionsToSelf()
    label(1)
    sprite('null', 1)
    CreateObject('phEff_GGRgshock', -1)
    CreateParticle('phef_ggr_gshock', -1)
    EndMomentum(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    ExitState()

@State
def phEff_GGRYotyouMC():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        RenderLayer(5)
        Eff3DEffect('pheff_ggr00_yotyou', '')
        TeleportToObject(2)
        AbsoluteY(0)
        SetScaleX(900)
        SetScaleY(600)
        AlphaValue(160)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        CopyFromRightToLeft(23, 2, 51, 2, 2, 23)
        PrivateFunction(3, 2, 51, 0, 800, 2, 104)
        if (SLOT_104 > 2000):
            SLOT_104 = 2000

        def upon_FRAME_STEP():
            TeleportToObject(2)
            AbsoluteY(0)
    sprite('null', 32767)
    CreateObject('phEff_GGRYotyouMCcolor', -1)
    CreateObject('phEff_GGRYotyouMCcore', -1)
    label(0)
    sprite('null', 32767)
    PassbackAddActionMarkToFunction('phEff_GGRYotyouMCcolor', 32)
    label(1)
    sprite('null', 5)
    PassbackAddActionMarkToFunction('phEff_GGRYotyouMCcore', 32)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def phEff_GGRYotyouMCcore():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('phef_rgg_yotei_mc')
        SetScaleX(900)
        SetScaleY(600)
        sendToLabelUpon(32, 0)

        def upon_FRAME_STEP():
            TeleportToObject(2)
            AbsoluteY(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    SetScaleSpeed(80)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def phEff_GGRYotyouMCcolor():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_rgg_yotei_color')
        Size(700)
        sendToLabelUpon(32, 0)

        def upon_FRAME_STEP():
            TeleportToObject(2)
            AbsoluteY(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def DriveDef_GGB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Visibility(1)
        E0EAEffectPosition(2)

        def upon_PLAYER_HIT():
            clearUponHandler(32)
            clearUponHandler(14)
            ObjectUpon(2, 32)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(14)
            NoDamageAction(1)
            sendToLabel(1)
    sprite('phdrivecol_ggb', 300)
    label(1)
    sprite('null', 10)

@State
def DriveAtk_GGB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(4000)
        SetScaleY(4000)
        AddX(150000)
        AddY(125000)
        WallCollisionDetection(1)
        FloorCollision(1)
        Visibility(1)
        AttackLevel_(3)
        Hitstop(0)
        Damage(300)
        ProjectileLevel(3)
        AirHitstunAnimation(18)
        AirUntechableTime(19)
        AirPushbackX(15000)
        AirPushbackY(10000)
        YImpulseBeforeWallbounce(1000)
        OnlyHitIfHitstun(1)
        EndAttack()
        SetActionMark(0)

        def upon_FRAME_STEP():
            XImpulseAcceleration(95)
            YAccel(95)
            if SLOT_2:
                if SLOT_51:
                    SetAcceleration(0)
                    SetActionMark(0)
                    sendToLabel(1)
                if (not SLOT_51):
                    if CheckInput(0x93):
                        YSpeed(1500)
                    if CheckInput(0x45):
                        YSpeed(-1500)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(3)
            clearUponHandler(54)
            sendToLabel(0)

        def upon_33():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(54)
            SLOT_51 = 1

        def upon_34():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(54)
            SLOT_51 = 1
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(3)
            clearUponHandler(54)
            sendToLabel(0)
    sprite('vr_ph_magictest', 3)
    physicsXImpulse(60000)
    SetAcceleration(1000)
    PrivateSE('phse_04')
    CreateObject('DriveDef_GGB', -1)
    CreateObject('Eff_GGB', -1)
    RegisterObject(4, 1)
    SetActionMark(1)
    sprite('vr_ph_magictest', 3)
    XImpulseAcceleration(50)
    sprite('vr_ph_magictest', 3)
    XImpulseAcceleration(50)
    sprite('vr_ph_magictest', 60)
    EndAttack()
    label(1)
    sprite('vr_ph_magictest', 15)
    XImpulseAcceleration(50)
    sprite('vr_ph_magictest', 5)
    EndMomentum(1)
    ObjectUpon(4, 34)
    PassbackAddActionMarkToFunction('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(3)
    ObjectUpon(4, 32)
    sprite('vr_ph_magictest', 60)
    CreateObject('DriveAtk_GGB_ATKMaster', -1)
    CommonSE('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()
    label(2)
    sprite('vr_ph_magictest', 40)
    EndMomentum(1)
    sprite('vr_ph_magictest', 20)
    ObjectUpon(4, 34)
    PassbackAddActionMarkToFunction('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(3)
    ObjectUpon(4, 32)
    sprite('vr_ph_magictest', 60)
    CreateObject('DriveAtk_GGB_ATKMaster', -1)
    CommonSE('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()
    label(0)
    sprite('null', 11)
    physicsXImpulse(0)
    physicsYImpulse(0)
    PassbackAddActionMarkToFunction('DriveDef_GGB', 32)
    ObjectUpon(4, 33)
    ConstantAlphaModifier(-25)
    ExitState()

@State
def DriveAtk_GGB_ATKMaster():

    def upon_IMMEDIATE():
        SetActionMark(6)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 3)
    CreateObject('Eff_GGBatk', -1)
    RegisterObject(4, 1)
    CreateObject('DriveAtk_GGB_ATKU', -1)
    RegisterObject(5, 1)
    CreateObject('DriveAtk_GGB_ATKH', -1)
    RegisterObject(6, 1)
    ObjectUpon(5, 33)
    ObjectUpon(6, 33)
    label(0)
    sprite('null', 2)
    ObjectUpon(5, 33)
    ObjectUpon(6, 33)
    sprite('null', 1)
    if (SLOT_2 == 0):
        sendToLabel(1)
    else:
        AddActionMark(-1)
        sendToLabel(0)
    label(1)
    sprite('null', 10)
    ObjectUpon(4, 32)
    ObjectUpon(5, 32)
    ObjectUpon(6, 32)

@Subroutine
def DriveAtk_GGB_Init():
    AttackLevel_(3)
    Damage(250)
    ChipPercentage(15)
    AttackDirection(1)
    Hitstop(0)
    EnemyHitstopAddition(0, 10, 10)
    HitsparkSize(200)
    UseSlashHitspark(1)
    AttackP2(92)
    VoodooDamageMultiplier(2)
    PassByArmor(1)
    PushbackX(39900)
    StarterRating(2)
    AirPushbackX(60000)
    AirPushbackY(35000)
    AirUntechableTime(30)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    Wallbounce(1)
    WallbounceReboundTime(10)
    AirHitstunAfterWallbounce(60)

@State
def DriveAtk_GGB_ATKU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(120000)
        SetScaleY(1000)
        AddY(25000)
        callSubroutine('DriveAtk_GGB_Init')
        Visibility(1)

        def upon_OPPONENT_HIT():
            Damage(300)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        AttackOff()
    sprite('null', 10)
    label(1)
    sprite('vr_ph_magictest', 4)
    RefreshMultihit()
    sprite('null', 60)
    label(0)
    sprite('null', 5)

@State
def DriveAtk_GGB_ATKH():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(1000)
        SetScaleY(100000)
        AddY(-600000)
        callSubroutine('DriveAtk_GGB_Init')
        Visibility(1)

        def upon_OPPONENT_HIT():
            Damage(400)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    label(1)
    sprite('vr_ph_magictest', 4)
    RefreshMultihit()
    sprite('null', 60)
    label(0)
    sprite('null', 5)

@State
def Eff_GGB():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('pheff_ggb01', '')
        FaceSpawnLocation()
        Size(1100)
        AddY(50000)
        LinkParticle('phef_ggb_add')
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(34, 100)
        AlphaValue(0)
        ConstantAlphaModifier(63)
    label(0)
    sprite('null', 2)
    Size(1100)
    CreateObject('Eff_GGBMoya', -1)
    sprite('null', 2)
    Size(1000)
    sprite('null', 2)
    Size(1100)
    sprite('null', 2)
    Size(1000)
    CommonSE('014_electric_s')
    gotoLabel(0)
    label(100)
    clearUponHandler(34)
    sprite('null', 5)
    AlphaValue(255)
    ConstantAlphaModifier(-23)
    Size(1000)
    SetScaleSpeed(-90)
    PassbackAddActionMarkToFunction('Eff_GGBMoya', 32)
    sprite('null', 5)
    CreateObject('Eff_GGBPre', -1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    Size(0)
    SetScaleSpeed(0)
    label(1)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 7)
    ScreenShake(20000, 20000)
    AlphaValue(255)
    Size(1000)
    SetScaleSpeed(200)
    CreateParticle('phef_ggb_start', -1)
    PassbackAddActionMarkToFunction('Eff_GGBMoya', 32)
    loopRest()
    label(2)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 10)
    AlphaValue(255)
    ConstantAlphaModifier(-23)
    PassbackAddActionMarkToFunction('Eff_GGBMoya', 32)
    loopRest()

@State
def Eff_GGBPre():

    def upon_IMMEDIATE():
        Size(250)
        LinkParticle('phef_ggb_end')
    sprite('null', 60)

@State
def Eff_DriveMagicCircle():

    def upon_IMMEDIATE():
        LinkParticle('phef_magicAir_mc')

        def upon_FRAME_STEP():
            PrivateFunction3(3, -50000, -200000, 100, 1)
    sprite('null', 20)

@State
def Eff_GGBMoya():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        sendToLabelUpon(32, 1)
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_rrb_moya')
        Size(700)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    SetScaleSpeed(-25)
    ConstantAlphaModifier(-31)

@State
def Eff_GGBatk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('pheff_ggb00', '')
        FaceSpawnLocation()
        AddY(50000)
        sendToLabelUpon(32, 1)
        LinkParticle('phef_ggb_jizoku')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    Size(1300)
    ScreenShake(1000, 1000)
    sprite('null', 2)
    Size(1250)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    SetScaleSpeed(-25)
    CreateParticle('phef_ggb_end', -1)
    loopRest()

@State
def DriveAtk_BBR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        BlendMode_Normal()
        CancelIfPlayerHit(2)
        Size(550)
        AlphaValue(0)
        LinkParticle('phef_rrb_add')
        AddX(150000)
        AddY(200000)
        Visibility(1)
        NoAttackDuringAction(1)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(1)
    sprite('null', 10)
    physicsXImpulse(2000)
    CreateObject('Eff_BBRSub', -1)
    CreateObject('ParticleMaster_BBR', -1)
    Eff3DEffect('pheff_bbr00', '')
    AlphaValue(0)
    ConstantAlphaModifier(51)
    PrivateSE('phse_04')
    sprite('null', 20)
    sprite('null', 4)
    XImpulseAcceleration(2500)
    AlphaValue(255)
    ConstantAlphaModifier(-63)
    CommonSE('000_airdash_0')
    sprite('null', 20)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    sprite('null', 5)
    TeleportToObject(22)
    AddY(200000)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('null', 4)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    physicsXImpulse(-60000)
    physicsYImpulse(50000)
    sprite('null', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    XImpulseAcceleration(10)
    YAccel(10)
    sprite('null', 6)
    XImpulseAcceleration(10)
    YAccel(10)
    sprite('null', 2)
    XImpulseAcceleration(0)
    YAccel(0)
    Eff3DEffect('pheff_bbr01', '')
    sprite('null', 3)
    CreateObject('DriveAtk_BBR_ATK', -1)
    ObjectUpon(1, 32)
    physicsXImpulse(-8000)
    physicsYImpulse(8000)
    sprite('null', 3)
    XImpulseAcceleration(25)
    YAccel(25)
    sprite('null', 3)
    XImpulseAcceleration(25)
    YAccel(25)
    sprite('null', 6)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('null', 6)
    physicsXImpulse(5000)
    physicsYImpulse(-1500)
    Eff3DEffect('pheff_bbr00', '')
    sprite('null', 4)
    XImpulseAcceleration(2500)
    YAccel(2500)
    AlphaValue(255)
    ConstantAlphaModifier(-63)
    CommonSE('000_airdash_0')
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('null', 5)
    TeleportToObject(22)
    AddY(200000)
    sprite('null', 4)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    physicsXImpulse(80000)
    sprite('null', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    XImpulseAcceleration(5)
    YAccel(5)
    ForceFaceSprite()
    sprite('null', 6)
    XImpulseAcceleration(5)
    YAccel(5)
    sprite('null', 2)
    XImpulseAcceleration(0)
    YAccel(0)
    RotationAngle(15000)
    Eff3DEffect('pheff_bbr01', '')
    sprite('null', 3)
    CreateObject('DriveAtk_BBR_ATK', -1)
    ObjectUpon(1, 33)
    physicsXImpulse(-8000)
    sprite('null', 3)
    XImpulseAcceleration(25)
    sprite('null', 3)
    XImpulseAcceleration(25)
    sprite('null', 6)
    XImpulseAcceleration(0)
    sprite('null', 6)
    physicsXImpulse(6000)
    Eff3DEffect('pheff_bbr00', '')
    sprite('null', 4)
    RotationAngle(0)
    XImpulseAcceleration(2500)
    YAccel(2500)
    AlphaValue(255)
    ConstantAlphaModifier(-63)
    CommonSE('000_airdash_0')
    sprite('null', 10)
    ConstantAlphaModifier(-63)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    XImpulseAcceleration(0)
    YAccel(0)
    sprite('null', 5)
    TeleportToObject(22)
    AddX(-30000)
    AddY(200000)
    sprite('null', 4)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    physicsYImpulse(75000)
    sprite('null', 6)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    XImpulseAcceleration(5)
    YAccel(5)
    sprite('null', 6)
    XImpulseAcceleration(5)
    YAccel(5)
    sprite('null', 2)
    XImpulseAcceleration(0)
    YAccel(0)
    ForceFaceSprite()
    sprite('null', 3)
    Eff3DEffect('pheff_bbr01', '')
    RotationAngle(35000)
    CreateObject('DriveAtk_BBR_ATK', -1)
    ObjectUpon(1, 34)
    physicsYImpulse(8000)
    sprite('null', 5)
    YAccel(25)
    sprite('null', 5)
    YAccel(25)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 5)
    Eff3DEffect('pheff_bbr00', '')
    physicsXImpulse(-20000)
    physicsYImpulse(2000)
    sprite('null', 5)
    XImpulseAcceleration(50)
    YAccel(50)
    sprite('null', 5)
    physicsYImpulse(-5000)
    sprite('null', 5)
    XImpulseAcceleration(50)
    YAccel(200)
    sprite('null', 5)
    physicsXImpulse(10000)
    YAccel(200)
    sprite('null', 8)
    RotationAngle(0)
    XImpulseAcceleration(1500)
    YAccel(150)
    AlphaValue(255)
    ConstantAlphaModifier(-15)
    CommonSE('000_airdash_0')
    sprite('null', 30)
    AlphaValue(0)
    ConstantAlphaModifier(0)
    ExitState()
    label(1)
    sprite('null', 10)
    Eff3DEffect('pheff_bbr00', '')
    XImpulseAcceleration(0)
    YAccel(0)
    ConstantAlphaModifier(-28)

@State
def DriveAtk_BBR_PreAtk():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(4000)
        SetScaleY(4000)
        AttackLevel_(2)
        Damage(300)
        AirPushbackX(20000)
        AirPushbackY(10000)
        AirUntechableTime(26)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        OnlyHitIfHitstun(1)
        Visibility(1)

        def upon_FRAME_STEP():
            PrivateFunction3(2, -20000, -40000, 100, 1)
    sprite('vr_ph_magictest', 10)

@State
def ParticleMaster_BBR():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 4)
    CreateParticle('phef_rrb_tb', -1)
    gotoLabel(0)

@State
def DriveAtk_BBR_ATK():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(1500)
        SetScaleY(1500)
        AttackLevel_(2)
        AttackP1(80)
        AirPushbackX(250)
        AirPushbackY(25000)
        AirUntechableTime(20)
        EnemyHitstopAddition(0, 10, 11)
        UsePunchHitspark(1)
        HitsparkSize(500)
        VoodooDamageMultiplier(2)
        StarterRating(2)
        Visibility(1)
        CollideWithWall(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            EndAttack()

        def upon_32():
            RotationAngle(45000)
            physicsXImpulse(60000)
            physicsYImpulse(-60000)

        def upon_33():
            physicsXImpulse(60000)

        def upon_34():
            AirPushbackX(0)
            AirPushbackY(-40000)
            AttackDirection(3)
            GroundBounce(1)
            BouncePercentage(25)
            RotationAngle(90000)
            physicsYImpulse(-60000)
    sprite('vr_ph_magictest', 120)
    CreateObject('Eff_BBRmc', -1)
    CreateObject('Eff_BBRAtk', -1)
    PrivateSE('phse_07')
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-23)

@State
def Eff_BBRSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(2)
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_rrb_moya')
    sprite('null', 32767)

@State
def Eff_BBRAtk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(2)
        E0EAEffectRotation(2)
        PaletteIndex(3)
        RenderLayer(8)
        ParticleLayer(7)
        CallPrivateEffect('phef_rrbatk_add')
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        Size(1000)
    label(0)
    sprite('vr_phbbr_00', 2)
    CreateParticle('phef_rrbatk_bgnokosi', -1)
    CreateParticle('phef_rrbatk_tb', -1)
    CreateParticle('phef_rrbatk_tb2', -1)
    CreateObject('Eff_BBRBlack', -1)
    sprite('vr_phbbr_01', 2)
    CreateParticle('phef_rrbatk_bgnokosi', -1)
    sprite('vr_phbbr_02', 2)
    CreateParticle('phef_rrbatk_bgnokosi', -1)
    CreateParticle('phef_rrbatk_tb', -1)
    CreateParticle('phef_rrbatk_tb2', -1)
    CreateObject('Eff_BBRBlack', -1)
    sprite('vr_phbbr_03', 2)
    CreateParticle('phef_rrbatk_bgnokosi', -1)
    gotoLabel(0)

@State
def Eff_BBRBlack():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectRotation(2)
        Eff3DEffect('pheff_bbrAtk', '')
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def Eff_BBRmc():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectRotation(2)
        LinkParticle('phef_bbr_entermc')
    sprite('null', 30)

@State
def DriveAtk_BBG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(10000)
        SetScaleY(150000)
        Unknown1008()
        TeleportToObject(22)
        NoVerticalTracking()
        AttackLevel_(3)
        Damage(0)
        AttackP1(50)
        AttackP2(100)
        AirHitstunAnimation(11)
        AirPushbackY(-50000)
        Hitstop(0)
        AirUntechableTime(60)
        HardKnockdown(25)
        PreventGroundedHit(1)
        Unknown11104(1)
        OnlyHitPlayer(1)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        DistanceCheck(200000, -200000, 2000000, -2000000)
        CounterHitSetting(1)
        StarterRating(0)
        Unknown12055(1)
        AttackOff()
        Visibility(1)
        WallCollisionDetection(1)
        SetActionMark(1)

        def upon_FRAME_STEP():
            if (SLOT_135 > 0):
                SetActionMark(0)
                AttackOff()
            if SLOT_2:
                CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
                if (SLOT_51 == 0):
                    AttackOff()
                elif (SLOT_51 > 80000):
                    if (SLOT_135 == 0):
                        RefreshMultihit()
            else:
                CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
                if (SLOT_51 == 0):
                    if (SLOT_135 == 0):
                        SetActionMark(1)
            if SLOT_52:
                if (SLOT_19 < 350000):
                    SLOT_53 = (SLOT_53 + 1)
                    if (SLOT_53 > 150):
                        SLOT_52 = 0
                        SLOT_53 = 0
                        sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(33)
            TeleportToObject(3)
            AddX(300000)
    sprite('null', 1)
    sprite('null', 105)
    CreateObject('Eff_BBGmc', -1)
    RegisterObject(4, 1)
    PrivateSE('phse_06')
    sprite('null', 8)
    SLOT_52 = 1
    CreateObject('SoundMaster_BBG', -1)
    PreventOppJump(1)
    ScreenShake(10000, 10000)
    CreateObject('Eff_BBGct', -1)
    RegisterObject(5, 1)
    CreateObject('Eff_BBG', -1)
    RegisterObject(6, 1)
    CreateObject('Eff_BBG', -1)
    RegisterObject(7, 1)
    ApplyFunctionsToObjects(6)
    AddX(250000)
    ApplyFunctionsToSelf()
    ApplyFunctionsToObjects(7)
    AddX(-250000)
    Flip()
    ApplyFunctionsToSelf()
    sprite('vr_ph_magictest', 300)
    label(1)
    sprite('vr_ph_magictest', 30)
    clearUponHandler(3)
    EndAttack()
    ObjectUpon(4, 32)
    ObjectUpon(5, 32)
    ObjectUpon(6, 32)
    ObjectUpon(7, 32)
    PreventOppJump(0)

@State
def SoundMaster_BBG():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
    label(0)
    sprite('null', 50)
    CommonSE('022_magiccircle_c')
    gotoLabel(0)

@State
def Eff_BBG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bbg00', '')
        RemoveOnCallStateEnd(2)
        SetScaleX(180)
        SetScaleY(700)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        AbsoluteY(0)
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(13)
    label(0)
    sprite('null', 20)
    ConstantAlphaModifier(-4)
    physicsXImpulse(0)
    SetScaleXPerFrame(-1)
    sprite('null', 20)
    ConstantAlphaModifier(4)
    SetScaleXPerFrame(1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()

@State
def Eff_BBGct():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bbg01', '')
        RemoveOnCallStateEnd(2)
        SetScaleX(650)
        SetScaleY(750)
        AbsoluteY(0)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    CreateObject('Eff_BBGcore', -1)
    RegisterObject(4, 1)
    AlphaValue(0)
    ConstantAlphaModifier(45)
    label(0)
    sprite('null', 25)
    ConstantAlphaModifier(-5)
    CreateParticle('phef_bbg_jizoku', -1)
    sprite('null', 25)
    ConstantAlphaModifier(5)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    ObjectUpon(4, 32)
    loopRest()

@State
def Eff_BBGcore():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ParticleLayer(2)
        CallPrivateEffect('phef_bbr_core')
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
        Size(550)
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    physicsYImpulse(15000)
    sprite('null', 4)
    physicsYImpulse(7500)
    CreateObject('Eff_BBGcoresub', -1)
    ApplyFunctionsToObjects(1)
    RenderLayer(2)
    ApplyFunctionsToSelf()
    physicsYImpulse(3750)
    CreateObject('Eff_BBGcoresub', -1)
    ApplyFunctionsToObjects(1)
    RenderLayer(2)
    ApplyFunctionsToSelf()
    label(0)
    sprite('null', 4)
    physicsYImpulse(-1500)
    CreateObject('Eff_BBGcoresub', -1)
    ApplyFunctionsToObjects(1)
    RenderLayer(2)
    ApplyFunctionsToSelf()
    sprite('null', 4)
    physicsYImpulse(1500)
    CreateObject('Eff_BBGcoresub', -1)
    ApplyFunctionsToObjects(1)
    RenderLayer(2)
    ApplyFunctionsToSelf()
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    ConstantAlphaModifier(-17)
    physicsYImpulse(-15000)
    loopRest()

@State
def Eff_BBGcoresub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('pheff_brn01', '')
        Size(750)
        RandAddScale(-50, 250)
        RandAddRotation(-360000, 360000)
    sprite('null', 2)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(64)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(64)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(64)

@State
def Eff_BBGmc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('phef_bbr_core_mc')
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 5)
    SetScaleSpeed(60)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()

@State
def DriveAtk_BGR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Size(20000)
        AttackLevel_(5)
        Damage(1500)
        AttackP1(80)
        AttackP2(74)
        MinimumDamage(20)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(100000)
        AirUntechableTime(180)
        Hitstop(2)
        EnemyHitstopAddition(0, 0, 1)
        DamageFromStateOnly('DriveAtk_BGR')
        HitAnywhere(1)
        ChipPercentage(35)
        AttackDirection(3)
        IgnoreBurst(1)
        StarterRating(2)
        FaceRight()
        GuardCrush(100, 1)
        SetActionMark(481)
        Visibility(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 10)
    PrivateSE('phse_04')
    CreateObject('Eff_BGRcount', -1)
    RegisterObject(4, 1)
    sprite('null', 600)
    sprite('null', 64)
    TeleportToObject(22)
    ObjectUpon(4, 32)
    DistortionSettings(60, -1, 2)
    CreateObject('Eff_BGRCamera', -1)
    CreateObject('Eff_BGRstart', -1)
    CreateObject('Eff_BGRbg', -1)
    RegisterObject(5, 1)
    sprite('vr_ph_magictest', 1)
    ObjectUpon(4, 33)
    CreateObject('Eff_BGRmato', -1)
    ScreenShake(0, 20000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    GuardCrush(0, 0)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    DamageFromStateOnly('')
    sprite('vr_ph_magictest', 25)
    EndAttack()
    sprite('vr_ph_magictest', 10)
    ObjectUpon(5, 32)
    ExitState()
    label(1)
    sprite('null', 10)
    ObjectUpon(4, 33)
    ObjectUpon(5, 32)

@State
def Eff_BGRcount():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Size(50)
        RenderLayer(6)
        TeleportToObject(22)
        AddY(240000)

        def upon_FRAME_STEP():
            PrivateFunction3(22, 0, 50000, 50, 1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('vr_phbgr_00', 10)
    CommonSE('022_magiccircle_b')
    CreateObject('Eff_BGRhari', -1)
    SetScaleSpeed(75)
    sprite('vr_phbgr_00', 78)
    Size(800)
    SetScaleSpeed(0)
    sprite('vr_phbgr_00', 138)
    CreateObject('Eff_BGRcountSub1', 2)
    RegisterObject(4, 1)
    sprite('vr_phbgr_00', 162)
    CreateObject('Eff_BGRcountSub2', 3)
    RegisterObject(5, 1)
    sprite('vr_phbgr_00', 138)
    CreateObject('Eff_BGRcountSub3', 1)
    RegisterObject(6, 1)
    sprite('vr_phbgr_00', 1)
    CreateObject('Eff_BGRcountSub4', 0)
    RegisterObject(7, 1)
    sprite('vr_phbgr_00', 32767)
    label(0)
    sprite('vr_phbgr_00', 32767)
    clearUponHandler(3)
    Size(1300)
    TeleportToObject(22)
    AddY(200000)
    ObjectUpon(4, 32)
    ObjectUpon(5, 32)
    ObjectUpon(6, 32)
    ObjectUpon(7, 32)
    label(1)
    sprite('null', 1)

@State
def Eff_BGRhari():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1200)
        RenderLayer(8)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('vr_phbgr_01', 10)
    AlphaValue(0)
    ConstantAlphaModifier(28)
    sprite('vr_phbgr_01', 32767)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    AddRotationPerFrame(600)

@Subroutine
def CountDownFrameInit():
    E0EAEffectPosition(2)
    RemoveOnCallStateEnd(2)
    CancelIfPlayerHit(3)
    BlendMode_Normal()
    ParticleLayer(7)
    CommonSE('015_blaze_0')

@State
def Eff_BGRcountSub1():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        CallPrivateEffect('phef_bgr_count1')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(20)
    physicsXImpulse(3000)
    physicsYImpulse(3000)
    sprite('null', 32767)
    SetScaleSpeed(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub2():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        CallPrivateEffect('phef_bgr_count2')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(20)
    physicsXImpulse(3000)
    physicsYImpulse(-3000)
    sprite('null', 32767)
    SetScaleSpeed(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub3():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        LinkParticle('phef_bgr_count3')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(20)
    physicsXImpulse(-3000)
    physicsYImpulse(-3000)
    sprite('null', 32767)
    SetScaleSpeed(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub4():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        CallPrivateEffect('phef_bgr_count4')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(20)
    physicsXImpulse(-3000)
    physicsYImpulse(3000)
    sprite('null', 32767)
    SetScaleSpeed(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRCamera():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
    sprite('null', 30)
    CameraPosition(1250)
    CameraControlEnable(1)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    sprite('null', 30)
    CameraControlEnable(0)
    sprite('null', 32767)
    AddY(300000)
    CameraPosition(1000)

@State
def Eff_BGRstart():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bgr_start', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        DeviationY(-10000, 10000)
        IgnoreScreenfreeze(1)
    sprite('null', 60)
    CreateParticle('phef_ggr_start', -1)
    sprite('null', 5)
    physicsYImpulse(-1000)
    SetScaleSpeedY(50)

@State
def Eff_BGRmato():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        AbsoluteY(0)
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    CommonSE('013_thunder_0')
    CommonSE('016_explode_2')
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(300000)
    ApplyFunctionsToSelf()
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(-300000)
    ApplyFunctionsToSelf()
    CommonSE('013_thunder_0')
    CommonSE('016_explode_2')
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(-600000)
    ApplyFunctionsToSelf()
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(600000)
    ApplyFunctionsToSelf()
    CommonSE('013_thunder_0')
    CommonSE('016_explode_2')
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(300000)
    ApplyFunctionsToSelf()
    CommonSE('013_thunder_0')
    CommonSE('016_explode_2')
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(-300000)
    ApplyFunctionsToSelf()
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(-600000)
    ApplyFunctionsToSelf()
    CommonSE('013_thunder_0')
    CommonSE('016_explode_2')
    sprite('null', 3)
    CreateObject('Eff_BGRatk', -1)
    ApplyFunctionsToObjects(1)
    AddX(600000)
    ApplyFunctionsToSelf()

@State
def Eff_BGRatk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bgr_water00', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        SetScaleX(300)
        SetScaleY(800)
        DeviationY(-10000, 10000)
    sprite('null', 10)
    ScreenShake(2500, 2500)
    sprite('null', 10)
    SetScaleXPerFrame(-13)
    CreateParticle('phef_bgr_atk_end', -1)
    CreateObject('Eff_BGRatkEnd', -1)

@State
def Eff_BGRatkEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bgr_water01', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        SetScaleX(300)
        SetScaleY(800)
        DeviationY(-5000, 5000)
    sprite('null', 30)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def Eff_BGRbg():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_bgr_bg', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
        AddY(600000)
        Size(600)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def ph320SmokeEff():

    def upon_IMMEDIATE():
        LinkParticle('phef321_smoke')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        SetScaleSpeed(5)
        RandAddScaleX(150, 300)
        RandAddScaleY(0, 300)
        AlphaValue(175)
    sprite('vr_phcmn_10', 6)
    sprite('vr_phcmn_11', 6)
    sprite('vr_phcmn_12', 6)
    sprite('vr_phcmn_13', 5)
    ConstantAlphaModifier(-7)
    sprite('vr_phcmn_14', 4)
    sprite('vr_phcmn_15', 4)

@State
def ph320SmokeEff2():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RandAddScaleX(150, 300)
        RandAddScaleY(0, 300)
        AlphaValue(175)
    sprite('null', 12)
    sprite('vr_phcmn_10', 6)
    LinkParticle('phef321_smoke')
    SetScaleSpeed(5)
    sprite('vr_phcmn_11', 6)
    sprite('vr_phcmn_12', 6)
    sprite('vr_phcmn_13', 5)
    ConstantAlphaModifier(-7)
    sprite('vr_phcmn_14', 4)
    sprite('vr_phcmn_15', 4)

@State
def ph320BombEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
    sprite('null', 4)
    Eff3DEffect('pheff431_bomb00', '')
    CreateParticle('phef_400_bom', -1)
    Size(750)
    ScreenShake(10000, 10000)
    sprite('null', 3)
    AlphaValue(0)
    Size(1800)
    Eff3DEffect('pheffcmn_bomb00', '')
    CreateObject('ph320BombEff2', -1)
    sprite('null', 7)
    AlphaValue(255)
    CreateParticle('phef_400_bom', -1)
    CreateParticle('phef321_shock', -1)
    CreateObject('ph320BombEff_Circle', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def ph320BombEff2():

    def upon_IMMEDIATE():
        PaletteIndex(3)
    sprite('vr_ph400_07', 2)
    Size(1300)
    sprite('vr_ph400_08', 2)
    sprite('vr_ph400_09', 2)
    SetScaleSpeed(20)
    sprite('vr_ph400_06', 2)

@State
def ph320BombEff_Circle():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Eff3DEffect('pheff450_AddCircle', '')
        Size(650)
    sprite('null', 5)
    SetScaleSpeed(300)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def pheff_400():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 1)
    sprite('vr_ph400_00', 2)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    CreateParticle('phef400_nokosi', 0)
    CreateObject('pheff_400Fire', 0)
    CreateParticle('phef400_nokosi', 1)
    CreateObject('pheff_400Fire', 1)
    CreateParticle('phef400_nokosi', 2)
    CreateObject('pheff_400Fire', 2)
    CreateParticle('phef400_nokosi', 3)
    label(0)
    sprite('vr_ph400_00', 2)
    CreateParticle('phef400_nokosi', 0)
    CreateParticle('phef400_nokosi', 1)
    CreateParticle('phef400_nokosi', 2)
    CreateParticle('phef400_nokosi', 3)
    sprite('vr_ph400_01', 2)
    CreateParticle('phef400_nokosi', 0)
    CreateParticle('phef400_nokosi', 1)
    CreateParticle('phef400_nokosi', 2)
    CreateParticle('phef400_nokosi', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ph400_00', 2)
    PassbackAddActionMarkToFunction('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 4)
    sprite('vr_ph400_03', 4)
    sprite('vr_ph400_04', 2)
    Size(1000)
    EnableAfterimage(0)
    sprite('vr_ph400_04', 2)
    Size(1500)
    AddX(-40000)
    AddY(-50000)
    E0EAEffectPosition(0)
    sprite('vr_ph400_05', 7)
    Size(1150)
    AddY(50000)
    AddY(200000)
    AddX(40000)
    ScreenShake(10000, 10000)
    SetScaleSpeed(15)
    CreateObject('pheff_400sub', 0)
    CreateParticle('phef_400_bom', 1)
    CreateParticle('phef_400_blm', 1)
    CreateParticle('phef_400_bom_ground', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    sprite('vr_ph400_09', 3)
    CreateObject('pheff_400sub3', 0)
    sprite('vr_ph400_06', 5)
    CreateObject('phEff400_corebom', 0)
    ConstantAlphaModifier(-51)

@State
def pheff_400Fire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ph400eff_jizoku00', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RandAddScaleX(-50, 200)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(13)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    SetScaleSpeedY(-30)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def pheff_400sub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ph240eff_00', '')
        SetScaleY(450)
        SetScaleX(600)
        IgnoreScreenfreeze(1)
    sprite('null', 19)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def phEff400_corebom():

    def upon_IMMEDIATE():
        Size(1300)
        BlendMode_Add()
        PaletteIndex(2)
        RenderLayer(1)
    sprite('vr_ph216_03', 4)
    SetScaleSpeed(15)
    sprite('vr_ph216_04', 4)
    sprite('vr_ph216_05', 4)

@State
def pheff_400Air():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 1)

        def upon_33():
            clearUponHandler(33)
            RotationAngle(22500)

        def upon_34():
            clearUponHandler(34)
            RotationAngle(-22500)

        def upon_35():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(35)
            RotationAngle(0)
    sprite('vr_ph400_00', 2)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    CreateParticle('phef400_nokosi', 0)
    CreateObject('pheff_400Fire', 0)
    CreateParticle('phef400_nokosi', 1)
    CreateObject('pheff_400Fire', 1)
    CreateParticle('phef400_nokosi', 2)
    CreateObject('pheff_400Fire', 2)
    CreateParticle('phef400_nokosi', 3)
    label(0)
    sprite('vr_ph400_00', 2)
    CreateParticle('phef400_nokosi', 0)
    CreateParticle('phef400_nokosi', 1)
    CreateParticle('phef400_nokosi', 2)
    CreateParticle('phef400_nokosi', 3)
    sprite('vr_ph400_01', 2)
    CreateParticle('phef400_nokosi', 0)
    CreateParticle('phef400_nokosi', 1)
    CreateParticle('phef400_nokosi', 2)
    CreateParticle('phef400_nokosi', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ph400_00', 2)
    PassbackAddActionMarkToFunction('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 4)
    sprite('vr_ph400_03', 4)
    sprite('vr_ph400_04', 2)
    EnableAfterimage(0)
    sprite('vr_ph400_04', 2)
    RotationAngle(0)
    Size(1500)
    AddX(-40000)
    AddY(-50000)
    E0EAEffectPosition(0)
    sprite('vr_ph400_05', 7)
    Size(1150)
    AddX(40000)
    AddY(50000)
    AddY(200000)
    ScreenShake(10000, 10000)
    SetScaleSpeed(15)
    CreateObject('pheff_400sub2', 1)
    CreateParticle('phef_400_bom', 1)
    CreateParticle('phef_400_blm', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    CreateParticle('phef321_shock2', -1)
    sprite('vr_ph400_09', 3)
    sprite('vr_ph400_06', 5)
    CreateObject('pheff_400sub3', 0)
    CreateObject('phEff400_corebom', 0)
    ConstantAlphaModifier(-51)

@State
def pheff_400sub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ph240eff_01', '')
        Size(300)
        AddX(25000)
        AlphaValue(200)
    sprite('null', 23)
    SetScaleSpeed(4)

@State
def pheff_400sub3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ph240eff_02', '')
        AddY(-100000)
        Size(500)
        IgnoreScreenfreeze(1)
    sprite('null', 13)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def MidAssault_Atk():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        SetScaleX(6000)
        SetScaleY(15000)
        AddY(80000)
        if (SLOT_19 > 550000):
            Unknown1008()
            TeleportToObject(22)
            NoVerticalTracking()
        else:
            AddX(550000)
        WallCollisionDetection(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        AttackLevel_(5)
        Damage(1500)
        AirPushbackX(1500)
        AirPushbackY(-80000)
        AirUntechableTime(35)
        HitAirUnblockable(3)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        StarterRating(2)
        HardKnockdown(10)
        AttackP1(90)
        AttackP2(84)
        SameMoveProration(10)
        UseFireHitspark(1)
        FatalCounter(1)
        HitAirUnblockable(0)
        Visibility(1)
        if SLOT_137:
            DamageMultiplier(80)
        CHGroundBounce(1)
        CHBouncePercentage(50)
        CHHardKnockdown(0)

        def upon_32():
            Blockstun(25)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            Damage(1625)

        def upon_OPPONENT_HIT():
            ObjectUpon(3, 32)
    sprite('null', 10)
    label(0)
    sprite('null', 4)
    CreateObject('Eff_402', -1)
    CommonSE('016_explode_1')
    sprite('vr_ph_magictest', 5)
    KnockdownEffects(104, 1, 1)
    ExitState()
    label(1)
    sprite('null', 4)
    SetScaleX(7200)
    SetScaleY(14400)
    CreateObject('Eff_402_G', -1)
    CommonSE('016_explode_2')
    sprite('vr_ph_magictest', 5)
    KnockdownEffects(104, 1, 1)
    ExitState()

@State
def Eff_402():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        PaletteIndex(5)
        LinkParticle('phef402_mc')
        AddY(-60000)
        FaceLeft()
    sprite('ph402_cutin_a', 2)
    sprite('ph402_cutin_b', 1)
    BlendMode_Normal()
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    CreateObject('Eff_402Fire', -1)
    sprite('ph402_cutin', 15)
    IgnorePauses(0)
    CreateParticle('phef_402_end_g', -1)
    sprite('ph402_cutin', 2)
    ConstantAlphaModifier(-26)
    CreateParticle('phef402_end_sita', -1)
    CreateParticle('phef402_end', 0)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 1)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 2)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 3)

@State
def Eff_402Fire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        AlphaValue(160)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        PaletteIndex(2)
        RenderLayer(3)
        LinkParticle('phef402_sub')
    sprite('vr_ph402_00', 3)
    Size(1200)
    sprite('vr_ph402_00', 3)
    IgnorePauses(0)
    sprite('vr_ph402_01', 3)
    sprite('vr_ph402_02', 3)
    sprite('vr_ph402_03', 3)
    AlphaValue(255)
    Size(1200)
    sprite('vr_ph402_04', 3)
    Size(1100)
    sprite('vr_ph402_05', 5)
    Size(1000)
    ConstantAlphaModifier(-51)

@State
def Eff_402_G():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(5)
        LinkParticle('phef402_mc')
        AddY(-60000)
        FaceLeft()
        AddScale(150)
    sprite('ph402_cutin_a', 2)
    sprite('ph402_cutin_b', 1)
    BlendMode_Normal()
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    CreateObject('Eff_402Fire_G', -1)
    sprite('ph402_cutin', 15)
    RemoveOnCallStateEnd(0)
    IgnorePauses(0)
    CreateParticle('phef_402_end_g', -1)
    sprite('ph402_cutin', 2)
    ConstantAlphaModifier(-26)
    CreateParticle('phef402_end_sita', -1)
    CreateParticle('phef402_end', 0)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 1)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 2)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 3)

@State
def Eff_402Fire_G():

    def upon_IMMEDIATE():
        BlendMode_Add()
        AlphaValue(160)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(2)
        RenderLayer(3)
        LinkParticle('phef402_sub')
    sprite('vr_ph402_00', 3)
    Size(1400)
    sprite('vr_ph402_00', 3)
    RemoveOnCallStateEnd(0)
    IgnorePauses(0)
    sprite('vr_ph402_01', 3)
    sprite('vr_ph402_02', 3)
    sprite('vr_ph402_03', 3)
    AlphaValue(255)
    sprite('vr_ph402_04', 3)
    Size(1300)
    sprite('vr_ph402_05', 5)
    Size(1200)
    ConstantAlphaModifier(-51)

@State
def Eff_402Fire_PL():

    def upon_IMMEDIATE():
        BlendMode_Add()
        AlphaValue(255)
        PaletteIndex(2)
        RenderLayer(3)
        Size(2000)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
    sprite('vr_ph402_10', 3)
    LinkParticle('phef402_mcadd_g')
    sprite('vr_ph402_10', 3)
    Size(1700)
    sprite('vr_ph402_11', 3)
    sprite('vr_ph402_12', 3)
    sprite('vr_ph402_13', 3)

@State
def Eff_401():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(5)
        RenderLayer(13)
        AddX(-140000)
        BlendMode_Normal()
        AlphaValue(0)
        AttackLevel_(4)
        Damage(1100)
        AirPushbackY(44000)
        AirUntechableTime(35)
        AirPushbackX(25000)
        AirPushbackY(50000)
        CHAirPushbackX(50000)
        CHAirPushbackY(40000)
        CHWallbounce(1)
        CHWallbounceReboundTime(35)
        CHAirHitstunAfterWallbounce(60)
        CHWallstick(1)
        CHWallstickDuration(30)
        HitAirUnblockable(3)
        GroundedHitstunAnimation(9)
        AttackP1(90)
        AttackP2(82)
        SameMoveProration(10)
        UseFireHitspark(1)
        StarterRating(0)
        if SLOT_137:
            DamageMultiplier(80)

        def upon_OPPONENT_HIT():
            ObjectUpon(3, 32)
    sprite('null', 3)
    CreateObject('Eff_401Fire', -1)
    sprite('null', 3)
    sprite('ph401_cutin', 6)
    AlphaValue(255)
    sprite('ph401_cutin', 3)
    EndAttack()
    IgnorePauses(0)
    E0EAEffectPosition(0)
    sprite('ph401_cutin', 10)
    ConstantAlphaModifier(-51)

@State
def Eff_401Fire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        PaletteIndex(2)
        RenderLayer(14)
        Size(1300)
        AddX(35000)
        LinkParticle('phef401_sub')
    sprite('vr_ph401_00', 3)
    sprite('vr_ph401_01', 3)
    AddX(22500)
    sprite('vr_ph401_02', 5)
    AddX(22500)
    sprite('vr_ph401_03', 3)
    IgnorePauses(0)
    sprite('vr_ph401_04', 3)
    sprite('vr_ph401_05', 3)
    CreateParticle('phef401_hinoko', -1)
    sprite('vr_ph401_06', 3)
    CreateParticle('phef402_end', 0)
    CreateParticle('phef402_end', 1)
    CreateParticle('phef402_end', 2)
    CreateParticle('phef402_end', 3)
    CreateParticle('phef402_end', 4)
    sprite('vr_ph401_07', 3)
    sprite('null', 10)

@State
def Eff_401_G():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(5)
        RenderLayer(13)
        AddX(-140000)
        BlendMode_Normal()
        AlphaValue(0)
        Size(1000)
    sprite('null', 3)
    CreateObject('Eff_401Fire_G', -1)
    sprite('null', 3)
    sprite('ph401_cutin', 5)
    AlphaValue(255)
    sprite('ph401_cutin', 3)
    IgnorePauses(0)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    sprite('ph401_cutin', 10)
    ConstantAlphaModifier(-51)

@State
def Eff_401Fire_G():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        PaletteIndex(2)
        RenderLayer(14)
        Size(2000)
        AddX(35000)
        LinkParticle('phef401_sub')
    sprite('vr_ph401_00', 3)
    sprite('vr_ph401_01', 3)
    AddX(37500)
    sprite('vr_ph401_02', 5)
    AddX(37500)
    sprite('vr_ph401_03', 3)
    IgnorePauses(0)
    sprite('vr_ph401_04', 3)
    sprite('vr_ph401_05', 3)
    CreateParticle('phef401_hinoko', -1)
    sprite('vr_ph401_06', 3)
    CreateParticle('phef402_end', 0)
    CreateParticle('phef402_end', 1)
    CreateParticle('phef402_end', 2)
    CreateParticle('phef402_end', 3)
    CreateParticle('phef402_end', 4)
    sprite('vr_ph401_07', 3)
    sprite('null', 10)

@State
def Eff_MagicConv():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('phef403_flash')
    sprite('null', 60)

@State
def pheff_BufWaterMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)

        def upon_16():
            PrivateFunction3(3, 0, 1000, 100, 1)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    CreateObject('pheff_BufWater', -1)
    sprite('null', 2)
    CreateObject('pheff_BufWater', -1)
    ApplyFunctionsToObjects(1)
    Flip()
    ApplyFunctionsToSelf()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('pheff_BufWater', 32)

@State
def pheff_BufWater():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(4)
        Size(600)
        RandAddScale(-100, 400)
        DeviationX(-130000, 130000)
        DeviationY(-125000, 60000)
        AlphaValue(200)
        RenderLayer(11)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_buffw00', 5)
    SetScaleSpeedY(40)
    SetScaleXPerFrame(20)
    sprite('vrpheff_buffw01', 2)
    sprite('vrpheff_buffw02', 3)
    LinkParticle('pheff404_sub2')
    E0EAEffectPosition(0)
    sprite('vrpheff_buffw03', 3)
    sprite('vrpheff_buffw04', 3)
    ConstantAlphaModifier(-22)
    sprite('vrpheff_buffw05', 2)
    sprite('vrpheff_buffw06', 2)
    sprite('vrpheff_buffw07', 2)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    ConstantAlphaModifier(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def pheff_BufFireMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)

        def upon_16():
            PrivateFunction3(3, 0, 1000, 100, 1)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    CreateObject('pheff_BufFire', -1)
    sprite('null', 2)
    CreateObject('pheff_BufFire', -1)
    ApplyFunctionsToObjects(1)
    Flip()
    ApplyFunctionsToSelf()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('pheff_BufFire', 32)

@State
def pheff_BufFire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        EnableAfterimage(1)
        AfterimageCount(2)
        PaletteIndex(4)
        AlphaValue(200)
        Size(825)
        RandAddScale(-100, 400)
        RandAddScaleX(0, 200)
        DeviationX(-130000, 130000)
        DeviationY(-125000, 60000)
        RenderLayer(11)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_bufff00', 3)
    sprite('vrpheff_bufff01', 3)
    sprite('vrpheff_bufff02', 3)
    E0EAEffectPosition(0)
    LinkParticle('pheff404_sub')
    sprite('vrpheff_bufff03', 3)
    sprite('vrpheff_bufff04', 3)
    ConstantAlphaModifier(-16)
    sprite('vrpheff_bufff05', 3)
    sprite('vrpheff_bufff06', 3)
    sprite('vrpheff_bufff07', 3)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    ConstantAlphaModifier(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def pheff_BufWindMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)

        def upon_16():
            PrivateFunction3(3, 0, 1000, 100, 1)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 3)
    CreateObject('pheff_BufWind', -1)
    sprite('null', 3)
    CreateObject('pheff_BufWind', -1)
    ApplyFunctionsToObjects(1)
    Flip()
    ApplyFunctionsToSelf()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('pheff_BufWind', 32)

@State
def pheff_BufWind():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(4)
        AlphaValue(200)
        Size(800)
        RandAddScale(-100, 400)
        DeviationX(-130000, 130000)
        DeviationY(-125000, 60000)
        EnableAfterimage(1)
        AfterimageCount(2)
        RenderLayer(11)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_buffk00', 3)
    SetScaleSpeedY(35)
    SetScaleXPerFrame(-7)
    sprite('vrpheff_buffk01', 3)
    sprite('vrpheff_buffk02', 3)
    E0EAEffectPosition(0)
    LinkParticle('pheff404_sub3')
    physicsYImpulse(1500)
    sprite('vrpheff_buffk03', 3)
    sprite('vrpheff_buffk04', 3)
    ConstantAlphaModifier(-16)
    sprite('vrpheff_buffk05', 3)
    sprite('vrpheff_buffk06', 3)
    sprite('vrpheff_buffk07', 3)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    ConstantAlphaModifier(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def Eff_BuffAtkR():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        AddY(200000)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('null', 7)
    sprite('null', 24)
    CreateObject('Eff_BuffAtkRSub', -1)

@State
def Eff_BuffAtkRSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(3)
        Eff3DEffect('pheff_buffatk00', '')
        LinkParticle('pheff_buffatkR')
        Size(500)
    sprite('null', 9)
    IgnoreFinishStop(1)
    sprite('null', 10)
    IgnoreFinishStop(0)
    sprite('null', 4)
    SetScaleSpeed(10)

@State
def Eff_BuffAtkB():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        AddY(200000)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('null', 7)
    sprite('null', 24)
    CreateObject('Eff_BuffAtkBSub', -1)

@State
def Eff_BuffAtkBSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(3)
        Eff3DEffect('pheff_buffatk01', '')
        LinkParticle('pheff_buffatkB')
        Size(500)
    sprite('null', 9)
    IgnoreFinishStop(1)
    sprite('null', 10)
    IgnoreFinishStop(0)
    sprite('null', 4)
    SetScaleSpeed(10)

@State
def Eff_BuffAtkG():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        AddY(200000)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
    sprite('null', 7)
    sprite('null', 24)
    CreateObject('Eff_BuffAtkGSub', -1)

@State
def Eff_BuffAtkGSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(3)
        Eff3DEffect('pheff_buffatk02', '')
        LinkParticle('pheff_buffatkG')
        Size(500)
    sprite('null', 9)
    IgnoreFinishStop(1)
    sprite('null', 10)
    IgnoreFinishStop(0)
    sprite('null', 4)
    SetScaleSpeed(10)

@State
def UltimateShotAtk1st():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(3500)
        AddX(850000)
        AddY(180000)
        AttackLevel_(3)
        Damage(400)
        MinimumDamage(10)
        AttackP1(90)
        AttackP2(79)
        SingleProration(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        Hitstun(30)
        AirPushbackX(15000)
        AirPushbackY(4000)
        GroundBounce(1)
        BouncePercentage(85)
        Hitstop(0)
        EnemyHitstopAddition(3, 3, 5)
        HitsparkSize(500)
        UseSlashHitspark(1)
        StarterRating(2)
        Visibility(1)

        def upon_FRAME_STEP():
            if Unknown2065(23):
                clearUponHandler(3)
                ObjectUpon(3, 41)
    sprite('vr_ph_magictest', 8)
    CreateObject('Eff_430_Beam00', -1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('null', 1)
    PassbackAddActionMarkToFunction('Eff_430_Beam00', 32)

@State
def Eff_430_cap():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        EnableAfterimage(1)
    sprite('vr_ph430_cap', 6)
    sprite('vr_ph430_cap', 5)
    physicsYImpulse(30000)
    physicsXImpulse(-7500)
    AddRotationPerFrame(3000)
    sprite('vr_ph430_cap', 5)
    ConstantAlphaModifier(-51)

@State
def Eff_430_capFire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        AddY(20000)
        IgnoreScreenfreeze(1)
    sprite('vr_ph430_00', 4)
    sprite('vr_ph430_01', 4)
    sprite('vr_ph430_02', 4)
    sprite('vr_ph430_03', 4)
    sprite('vr_ph430_04', 4)
    sprite('vr_ph430_06', 4)
    sprite('vr_ph430_07', 4)

@State
def Eff_430_Beam00():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        Eff3DEffect('ph430eff_00', '')
        AddX(-800000)
        AddY(45000)
        LinkParticle('phef430_mc')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    AddScaleY(-75)
    CommonSE('014_electric_ll')
    PrivateSE('phse_11')
    sprite('null', 2)
    AddScaleY(75)
    CommonSE('014_electric_l')
    PrivateSE('phse_11')
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('phef430_beamend_00', -1)
    CreateObject('Eff_430_Beam01', -1)

@State
def Eff_430_Beam01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ph430eff_01', '')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 3)
    sprite('null', 3)
    AddScaleY(25)
    sprite('null', 3)
    AddScaleY(25)
    sprite('null', 3)
    AddScaleY(25)
    sprite('null', 4)

@State
def Eff_430_hinoNemoto():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff430od_00', '')
        LinkParticle('phef430_hngate')
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Size(1400)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 3)
    sprite('null', 6)
    ConstantAlphaModifier(-42)

@State
def Eff_430_hinoEnter():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff430od_01', '')
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('null', 5)
    Size(1200)
    sprite('null', 5)
    Size(1700)
    sprite('null', 5)
    ConstantAlphaModifier(-17)
    sprite('null', 4)
    CreateObject('Eff_430_hinoEnterEnd', -1)

@State
def Eff_430_hinoEnterEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff430od_02', '')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(1000)
        AddX(300000)
        physicsXImpulse(7500)
    sprite('null', 20)
    SetScaleSpeed(30)

@State
def Eff_430_TameEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff430odbeam_00', '')
        LinkParticle('phef430_beamtame')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        AddY(240000)
        AddX(380000)
        Size(60)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    SetScaleSpeed(300)
    sprite('null', 5)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 1)
    AddScale(200)
    ScreenShake(2500, 2500)
    sprite('null', 1)
    AddScale(-100)
    sprite('null', 1)
    AddScale(200)
    sprite('null', 1)
    AddScale(-100)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(10000, 10000)
    Size(1000)
    AlphaValue(0)

@State
def Eff_430_HinoBeamEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Visibility(1)
        Eff3DEffect('pheff430odbeam_01', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Size(1000)
        AddScaleY(1200)
        AddX(-650000)
        AddY(250000)
        sendToLabelUpon(32, 1)
    sprite('vr_ph430_effpos', 5)
    SetScaleSpeedY(80)
    SetScaleY(120)
    CommonSE('016_explode_2')
    sprite('vr_ph430_effpos', 5)
    PrivateSE('phse_02')
    sprite('vr_ph430_effpos', 5)
    SetScaleSpeedY(10)
    sprite('vr_ph430_effpos', 5)
    SetScaleSpeedY(0)
    CreateParticle('phef_430_shock', 0)
    CreateParticle('phef_430_shock', 2)
    label(0)
    sprite('vr_ph430_effpos', 1)
    AddScaleX(-50)
    AddScaleY(50)
    CreateParticle('phef_430_shock', 0)
    CreateParticle('phef_430_shock', 2)
    PrivateSE('phse_02')
    sprite('vr_ph430_effpos', 1)
    AddScaleY(-50)
    AddScaleX(50)
    sprite('vr_ph430_effpos', 1)
    AddScaleX(-50)
    AddScaleY(50)
    sprite('vr_ph430_effpos', 1)
    AddScaleY(-50)
    AddScaleX(50)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('Eff_430_HinoBeamEffEnd', -1)

@State
def Eff_430_HinoBeamEffEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff430odbeam_02', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    Eff3DEffect('pheff430odbeam_02', '')
    sprite('vr_ph430odbeam_expos', 1)
    Visibility(1)
    CreateParticle('phef430_beamend', 0)
    CreateParticle('phef430_beamend', 1)
    CreateParticle('phef430_beamend', 2)
    CreateParticle('phef430_beamend', 3)
    CreateParticle('phef430_beamend', 4)
    CreateParticle('phef430_beamend', 5)

@State
def UltimateShotAtk2nd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(7000)
        AddX(850000)
        AddY(130000)
        AttackLevel_(4)
        Damage(325)
        MinimumDamage(20)
        AttackP1(90)
        AttackP2(82)
        SingleProration(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        Hitstun(30)
        AirPushbackX(35000)
        AirPushbackY(4500)
        Wallbounce(1)
        WallbounceReboundTime(55)
        AirHitstunAfterWallbounce(60)
        Hitstop(0)
        EnemyHitstopAddition(3, 3, 5)
        HitsparkSize(500)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        StarterRating(2)
        Visibility(1)
    sprite('vr_ph_magictest', 7)
    CreateObject('Eff_430_Beam00', -1)
    ApplyFunctionsToObjects(1)
    AddScale(150)
    AddY(30000)
    ApplyFunctionsToSelf()
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('null', 1)
    PassbackAddActionMarkToFunction('Eff_430_Beam00', 32)

@State
def UltimateShotAtk1stOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(3500)
        AddX(850000)
        AddY(180000)
        AttackLevel_(3)
        AttackType(4)
        Damage(400)
        MinimumDamage(10)
        AttackP1(90)
        AttackP2(79)
        SingleProration(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        Hitstun(30)
        AirPushbackX(15000)
        AirPushbackY(4000)
        GroundBounce(1)
        BouncePercentage(85)
        Hitstop(0)
        EnemyHitstopAddition(3, 3, 5)
        HitsparkSize(500)
        UseSlashHitspark(1)
        StarterRating(2)
        Visibility(1)

        def upon_FRAME_STEP():
            if Unknown2065(23):
                clearUponHandler(3)
                ObjectUpon(3, 41)
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    CreateObject('Eff_430_Beam00', -1)
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    PassbackAddActionMarkToFunction('Eff_430_Beam00', 32)

@State
def UltimateShotAtk2ndOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(7000)
        AddX(850000)
        AddY(130000)
        AttackLevel_(4)
        AttackType(4)
        Damage(325)
        MinimumDamage(20)
        AttackP1(90)
        AttackP2(82)
        SingleProration(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        Hitstun(30)
        AirPushbackX(35000)
        AirPushbackY(4500)
        Wallbounce(1)
        WallbounceReboundTime(55)
        AirHitstunAfterWallbounce(60)
        Hitstop(0)
        EnemyHitstopAddition(3, 3, 5)
        HitsparkSize(500)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        StarterRating(2)
        Visibility(1)
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    CreateObject('Eff_430_Beam00', -1)
    ApplyFunctionsToObjects(1)
    AddScale(150)
    AddY(30000)
    ApplyFunctionsToSelf()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()

    def upon_OPPONENT_HIT():
        ObjectUpon(3, 32)
    PassbackAddActionMarkToFunction('Eff_430_Beam00', 32)

@State
def UltimateShotAtk3rdOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(20000)
        AddX(850000)
        AddY(140000)
        AttackLevel_(5)
        AttackType(4)
        Damage(200)
        MinimumDamage(20)
        AttackP1(90)
        AttackP2(84)
        SingleProration(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        Hitstun(60)
        AirPushbackX(40000)
        AirPushbackY(15000)
        Hitstop(0)
        EnemyHitstopAddition(4, 4, 6)
        HitsparkSize(500)
        UseFireHitspark(1)
        CHStateIfCHStart(3)
        StarterRating(2)
        Visibility(1)
    sprite('vr_ph_magictest', 5)
    CreateObject('Eff_430_HinoBeamEff', -1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('null', 10)
    PassbackAddActionMarkToFunction('Eff_430_HinoBeamEff', 32)
    PassbackAddActionMarkToFunction('UltimateShotHinokagutsuchi', 32)

@State
def UltimateShotODCamera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)

        def upon_FRAME_STEP():
            TeleportToObject(3)
            SLOT_51 = SLOT_19
            SLOT_51 = (SLOT_51 / 2)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 22)
            CopyFromRightToLeft(23, 2, 53, 22, 2, 22)
            if (SLOT_52 < SLOT_53):
                SLOT_22 = (SLOT_22 + SLOT_51)
            elif (SLOT_52 > SLOT_53):
                SLOT_22 = (SLOT_22 - SLOT_51)
            else:
                pass
            SLOT_22 = (SLOT_22 + 50000)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 120)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    label(1)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)

@State
def UltimateShotHinokagutsuchi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RenderLayer(11)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('ph430cutin_00', 15)
    AlphaValue(0)
    CreateObject('Eff_430_hinoEnter', 0)
    sprite('ph430cutin_00', 27)
    ConstantAlphaModifier(51)
    ScreenShake(10000, 10000)
    CreateObject('Eff_430_hinoNemoto', 0)
    CreateParticle('phef430_end', 1)
    CreateParticle('phef430_end', 2)
    CreateParticle('phef430_end', 3)
    CreateParticle('phef430_end', 4)
    CreateParticle('phef430_end', 5)
    CreateParticle('phef430_end', 6)
    CreateObject('Eff_430_TameEff', -1)
    sprite('ph430cutin_01', 3)
    ColorForTransition(4290032820)
    sprite('ph430cutin_02', 3)
    ColorForTransition(4288716960)
    sprite('ph430cutin_03', 3)
    ColorForTransition(4284769380)
    CreateObject('UltimateShotAtk3rdOD', -1)
    PassbackAddActionMarkToFunction('Eff_430_TameEff', 32)
    SetInertia(-20000)
    sprite('ph430cutin_03', 300)
    label(1)
    sprite('ph430cutin_02', 3)
    ConstantAlphaModifier(-31)
    sprite('ph430cutin_01', 3)
    PassbackAddActionMarkToFunction('Eff_430_hinoNemoto', 32)
    sprite('ph430cutin_00', 3)
    CreateParticle('phef402_end', 1)
    CreateParticle('phef402_end', 2)
    CreateParticle('phef402_end', 3)
    CreateParticle('phef402_end', 4)
    CreateParticle('phef402_end', 5)
    CreateParticle('phef402_end', 6)
    sprite('null', 2)

@Subroutine
def UltimateLock_Atk1stInit():
    AttackLevel_(3)
    Damage(250)
    MinimumDamage(20)
    Hitstop(3)
    HitsparkSize(500)
    NoAttackOffset(1)
    EnemyHitstopAddition(60, 60, 60)
    AttackP2(79)
    SingleProration(1)
    UseFireHitspark(1)
    OppPositionOnHit(1, 0, 50000)
    DefeatOpponentBehavior(1)
    CHStateIfCHStart(3)
    StarterRating(2)
    if SLOT_137:
        DamageMultiplier(80)
    DamageEffect(5, '')

@State
def Eff_432_AtkFire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        Flip()
        SetScaleX(900)
        SetScaleY(1200)
        AddY(-25000)
    sprite('vr_ph432_00', 6)
    CreateObject('Eff_432_AtkFireSub', -1)
    sprite('vr_ph432_01', 6)
    sprite('vr_ph432_02', 5)
    sprite('vr_ph432_03', 4)
    sprite('vr_ph432_04', 4)
    sprite('vr_ph432_05', 2)

@State
def Eff_432_AtkFireSub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        SetScaleX(-700)
        SetScaleY(700)
    sprite('vr_ph432_00', 4)
    sprite('vr_ph432_01', 4)
    sprite('vr_ph432_02', 4)
    sprite('vr_ph432_03', 4)
    sprite('vr_ph432_04', 4)
    sprite('vr_ph432_05', 4)

@State
def UltimateLock_Atk1stLv1():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateLock_Atk1stLv1Exe', 3, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SetScaleX(10000)
        SetScaleY(15000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    RefreshMultihit()
    CreateObject('Eff_432_yariLv1', -1)

@State
def Eff_432_yariLv1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari00', '')
        IgnoreScreenfreeze(1)
        Size(1750)
    sprite('null', 20)
    CreateObject('Eff_432_Boya', -1)
    sprite('null', 50)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    PassbackAddActionMarkToFunction('Eff_432_Boya', 32)

@State
def Eff_432_Boya():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 8)
    CreateParticle('phef432_fire00', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def UltimateLock_Atk1stLv1Exe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        SetScaleX(10000)
        SetScaleY(25000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    AttackOff()
    ApplyFunctionsToObjects(22)
    AbsoluteY(50000)
    ApplyFunctionsToSelf()
    sprite('vr_ph_magictest', 3)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk1stLv2():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateLock_Atk1stLv2Exe', 3, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SetScaleX(10000)
        SetScaleY(15000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CreateObject('Eff_432_yariLv2', -1)

@State
def Eff_432_yariLv2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari00', '')
        IgnoreScreenfreeze(1)
        Size(1750)
    sprite('null', 5)
    sprite('null', 45)
    CreateObject('Eff_432_yariLv2sub', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    PassbackAddActionMarkToFunction('Eff_432_yariLv2sub', 32)

@State
def Eff_432_yariLv2sub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari04', '')
        IgnoreScreenfreeze(1)
        SetScaleX(1200)
        SetScaleY(1400)
        AddY(-20000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 8)
    CreateParticle('phef432_fire00', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeedY(80)

@State
def UltimateLock_Atk1stLv2Exe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        SetScaleX(10000)
        SetScaleY(25000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    AttackOff()
    ApplyFunctionsToObjects(22)
    AbsoluteY(50000)
    ApplyFunctionsToSelf()
    CommonSE('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    RefreshMultihit()
    CommonSE('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('015_blaze_0')

@State
def UltimateLock_Atk1stLv3():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('UltimateLock_Atk1stLv3Exe', 3, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        SetScaleX(10000)
        SetScaleY(15000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CreateObject('Eff_432_yari', -1)

@State
def Eff_432_yari():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari00', '')
        IgnoreScreenfreeze(1)
        Size(1750)
    sprite('null', 4)
    CreateObject('Eff_432_Boya', -1)
    CreateObject('Eff_432_yari_sub2', -1)
    CreateObject('Eff_432_yari_sub1', -1)
    ApplyFunctionsToObjects(1)
    AddY(50000)
    ApplyFunctionsToSelf()
    sprite('null', 4)
    CreateObject('Eff_432_yari_sub1', -1)
    ApplyFunctionsToObjects(1)
    AddY(250000)
    AddScale(-300)
    ApplyFunctionsToSelf()
    sprite('null', 4)
    CreateObject('Eff_432_yari_sub1', -1)
    ApplyFunctionsToObjects(1)
    AddY(435000)
    AddScale(-600)
    ApplyFunctionsToSelf()
    sprite('null', 14)
    CreateObject('Eff_432_yari_sub1', -1)
    ApplyFunctionsToObjects(1)
    AddY(640000)
    AddScale(-900)
    ApplyFunctionsToSelf()
    sprite('null', 50)
    PassbackAddActionMarkToFunction('Eff_432_yari_sub2', 32)
    PassbackAddActionMarkToFunction('Eff_432_yari_sub1', 32)
    sprite('null', 10)
    PassbackAddActionMarkToFunction('Eff_432_Boya', 32)
    ConstantAlphaModifier(-26)

@State
def Eff_432_yari_sub1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari01', '')
        IgnoreScreenfreeze(1)
        Size(4000)
        AddX(50000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(-120)

@State
def Eff_432_yari_sub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari02', '')
        IgnoreScreenfreeze(1)
        SetScaleX(500)
        SetScaleY(2000)
        AddX(50000)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    ScreenShake(15000, 15000)
    SetScaleXPerFrame(300)
    sprite('null', 32767)
    SetScaleXPerFrame(0)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(-120)
    sprite('null', 5)
    CreateObject('Eff_432_yari_sub3', -1)

@State
def Eff_432_yari_sub3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('pheff432_yari03', '')
        IgnoreScreenfreeze(1)
        Size(2000)
    sprite('null', 15)

@State
def UltimateLock_Atk1stLv3Exe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        SetScaleX(10000)
        SetScaleY(25000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    AttackOff()
    ApplyFunctionsToObjects(22)
    AbsoluteY(50000)
    ApplyFunctionsToSelf()
    PrivateSE('phse_02')
    sprite('vr_ph_magictest', 3)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    RefreshMultihit()
    CommonSE('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    PrivateSE('phse_02')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    PrivateSE('phse_02')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    CommonSE('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk1stLv3Exe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        SetScaleX(10000)
        SetScaleY(25000)
        TeleportToObject(22)
        AbsoluteY(0)
        Visibility(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    AttackOff()
    ApplyFunctionsToObjects(22)
    AbsoluteY(50000)
    ApplyFunctionsToSelf()
    sprite('vr_ph_magictest', 3)
    OppThrowAnimation(24, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@Subroutine
def UltimateLock_Atk2ndInit():
    MinimumDamage(10)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirUntechableTime(60)
    Hitstun(60)
    AirPushbackX(45000)
    AirPushbackY(15000)
    HitsparkSize(400)
    CHStateIfCHStart(3)
    Wallbounce(1)
    WallbounceReboundTime(0)
    Hitstop(1)
    EnemyHitstopAddition(10, 10, 10)
    HitsparkSize(500)
    UseFireHitspark(1)
    StarterRating(2)

@Subroutine
def UltimateLock_Atk2ndODInit():
    MinimumDamage(10)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(60)
    Hitstun(60)
    AirPushbackX(7500)
    AirPushbackY(30000)
    DefeatOpponentBehavior(1)
    HitsparkSize(400)
    Wallbounce(1)
    WallbounceReboundTime(0)
    Hitstop(1)
    EnemyHitstopAddition(10, 10, 10)
    HitsparkSize(500)
    UseFireHitspark(1)
    StarterRating(2)

@State
def UltimateLock_Atk2ndLv1():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(12000)
        AddX(850000)
        AddY(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
            MinimumDamage(8)
        AttackLevel_(2)
        Damage(1250)
        MinimumDamage(8)
        if SLOT_137:
            DamageMultiplier(80)
        AttackOff()
        Visibility(1)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash_SS', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2_SS', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash3_SS', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash_SS', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2_SS', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()

@State
def Eff_432_mgSlash_SS():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_slash00', '')
        LinkParticle('phef432_aura')
        IgnoreScreenfreeze(1)
        Size(1000)
        AddX(-1100000)
        DeviationX(0, 100000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    CreateParticle('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2_SS():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        LinkParticle('phef432_aura')
        IgnoreScreenfreeze(1)
        Size(1000)
        AddX(-900000)
        AddY(150000)
        DeviationX(0, 100000)
        DeviationY(-50000, 50000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    CreateParticle('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3_SS():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(1000)
        AddX(-900000)
        AddY(-100000)
        DeviationX(0, 100000)
        DeviationY(-50000, 50000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    CreateParticle('phef432_hinoko00', -1)

@State
def UltimateLock_Atk2ndLv2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(12000)
        AddX(850000)
        AddY(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(3)
        Damage(1050)
        if SLOT_137:
            DamageMultiplier(80)
        AttackOff()
        Visibility(1)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash_S', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 5)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2_S', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 5)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash3_S', -1)
    PrivateSE('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def Eff_432_mgSlash_S():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(2000)
        AddX(-1100000)
        DeviationX(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    CreateParticle('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2_S():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(1700)
        AddX(-900000)
        AddY(150000)
        DeviationX(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    CreateParticle('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3_S():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(1700)
        AddX(-900000)
        AddY(-100000)
        DeviationX(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    CreateParticle('phef432_hinoko00', -1)

@State
def UltimateLock_Atk2ndLv3():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(12000)
        AddX(850000)
        AddY(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(4)
        Damage(630)
        if SLOT_137:
            DamageMultiplier(80)
        AttackOff()
        Visibility(1)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash3_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash3_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk2ndLv4():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        SetScaleX(45000)
        SetScaleY(12000)
        AddX(850000)
        AddY(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(5)
        Damage(550)
        if SLOT_137:
            DamageMultiplier(80)
        AttackOff()
        Visibility(1)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash3', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash2', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash3', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 8)
    sprite('null', 2)
    CreateObject('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()

@State
def Eff_432_mgSlash():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(2200)
        AddX(-1100000)
        DeviationX(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    CallCustomizableParticle('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(1700)
        AddX(-900000)
        AddY(300000)
        Rotation(15000)
        DeviationX(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    ParticleRotationAngle(15000)
    CallCustomizableParticle('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('phef432_aura')
        Eff3DEffect('pheff432_slash00', '')
        IgnoreScreenfreeze(1)
        Size(1700)
        AddX(-900000)
        AddY(-300000)
        Rotation(-15000)
        DeviationX(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    ParticleRotationAngle(15000)
    CallCustomizableParticle('phef432_hinoko00', -1)

@State
def UltimateLock_AtkODAdd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        Size(20000)
        AttackLevel_(5)
        Damage(250)
        AttackType(4)
        MinimumDamage(20)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(25000)
        AirUntechableTime(120)
        Hitstop(1)
        EnemyHitstopAddition(25, 25, 25)
        SingleProration(1)
        DamageEffect(5, '')
        CHStateIfCHStart(3)
        if SLOT_137:
            DamageMultiplier(80)
        Visibility(1)
    sprite('vr_ph_magictest', 1)
    TeleportToObject(22)
    AbsoluteY(0)
    CreateObject('Eff_BGRmato', -1)
    ScreenShake(0, 20000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 10)
    StartMultihit()
    ExitState()

@State
def UltimateChargeATK():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1500)
        AttackP2(84)
        AirUntechableTime(60)
        AirPushbackX(500)
        AirPushbackY(41000)
        MinimumDamage(30)
        GroundedHitstunAnimation(10)
        AttackP1(70)
        UseFireHitspark(1)
        StarterRating(0)
        EnemyHitstopAddition(0, -12, -12)
        if SLOT_31:
            Damage(2000)
        SetScaleX(11000)
        SetScaleY(11000)
        AddX(150000)
        AddY(100000)
        Visibility(1)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()

@State
def UltimateChargeODATK():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1500)
        AttackP2(84)
        AirUntechableTime(60)
        AirPushbackX(500)
        AirPushbackY(41000)
        MinimumDamage(30)
        GroundedHitstunAnimation(10)
        AttackP1(70)
        UseFireHitspark(1)
        StarterRating(0)
        EnemyHitstopAddition(0, -12, -12)
        AttackType(4)
        if SLOT_31:
            Damage(2000)
        SetScaleX(11000)
        SetScaleY(11000)
        AddX(150000)
        AddY(100000)
        Visibility(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(12)
            PassbackAddActionMarkToFunction('UltimateChargeOD', 32)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()

@State
def UltimateChargeODAddAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(500)
        AttackP2(96)
        AttackType(4)
        AirUntechableTime(60)
        AirPushbackX(25000)
        AirPushbackY(38000)
        MinimumDamage(10)
        GroundedHitstunAnimation(9)
        AttackP1(70)
        UseFireHitspark(1)
        CHStateIfCHStart(3)
        StarterRating(2)
        SetScaleX(11000)
        SetScaleY(11000)
        Visibility(1)
    sprite('null', 17)
    sprite('vr_ph_magictest', 3)
    TeleportToObject(22)
    AddX(50000)
    ForceFaceSprite()
    CreateObject('UltimateChargeODAddAtk_Bomb', -1)
    RefreshMultihit()
    sprite('null', 5)
    sprite('vr_ph_magictest', 3)
    TeleportToObject(22)
    AddX(50000)
    ForceFaceSprite()
    CreateObject('UltimateChargeODAddAtk_Bomb', -1)
    RefreshMultihit()
    sprite('null', 3)
    sprite('vr_ph_magictest', 3)
    TeleportToObject(22)
    AddX(80000)
    ForceFaceSprite()
    CreateObject('UltimateChargeODAddAtk_Bomb', -1)
    RefreshMultihit()
    AirHitstunAnimation(18)
    AirPushbackX(500)
    sprite('null', 30)

@State
def UltimateChargeODAddAtk_Bomb():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        CancelIfPlayerHit(3)
        IgnoreFinishStop(1)
        Size(800)
    sprite('vr_ph400_04', 2)
    sprite('vr_ph400_05', 3)
    AddY(200000)
    ScreenShake(10000, 10000)
    SetScaleSpeed(15)
    CreateObject('pheff_400sub2', 1)
    ApplyFunctionsToObjects(1)
    IgnoreFinishStop(1)
    RandAddRotation(-40000, 40000)
    ApplyFunctionsToSelf()
    CreateParticle('phef_400_bom', 1)
    CreateParticle('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    CreateParticle('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    CreateObject('ph320BombEff_Circle', -1)
    ApplyFunctionsToObjects(1)
    IgnoreFinishStop(1)
    RandAddRotation(20000, 30000)
    AddScale(-600)
    ApplyFunctionsToSelf()
    CreateObject('phEff400_corebom', 0)
    ConstantAlphaModifier(-51)

@State
def Eff_431_obi():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('pheff431_obi00', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Size(2700)
        AddY(-10000)
        AddX(-38000)
    sprite('null', 6)
    Eff3DEffect('pheff431_obi00', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi01', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi02', '')
    sprite('null', 8)
    Eff3DEffect('pheff431_obi03', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi04', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi05', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi06', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi07', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi08', '')
    sprite('null', 6)
    Eff3DEffect('pheff431_obi09', '')
    ConstantAlphaModifier(-18)
    sprite('null', 6)
    Eff3DEffect('pheff431_obi10', '')

@State
def Eff_431_mc():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('pheff431_mc00', '')
        AlphaValue(160)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Size(1500)
        AddY(250000)
        AddX(-38000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    SetScaleSpeed(150)
    ConstantAlphaModifier(-26)
    physicsXImpulse(42500)

@State
def Eff_431_mc_sub1():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff431_mc01', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Size(3000)
        AddY(250000)
        AddX(-38000)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(-200)
    physicsXImpulse(42500)

@State
def Eff_431_BomBall():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Eff3DEffect('pheff431_tameball00', '')
        LinkParticle('pheff431_tameball')
        RemoveOnCallStateEnd(2)
        AddY(280000)
        AddX(100000)
        SetScaleX(1400)
        SetScaleY(1200)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 10)
    AlphaValue(0)
    SetScaleSpeed(-75)
    ConstantAlphaModifier(26)
    label(0)
    sprite('null', 5)
    physicsXImpulse(10000)
    SetScaleSpeed(5)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(1)
    sprite('null', 5)
    physicsXImpulse(-5000)
    SetScaleSpeed(10)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(2)
    sprite('null', 1)
    AddX(22500)
    AddY(-10000)
    AddScaleX(200)
    AddScaleY(300)
    sprite('null', 1)
    AddScaleX(200)
    AddScaleY(300)
    AddX(10000)
    AddY(-10000)
    sprite('null', 1)
    AddScaleX(200)
    AddScaleY(300)
    AddX(10000)
    AddY(-10000)

@State
def Eff_431_bomb():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff431_bomb00', '')
        LinkParticle('phef431_blm')
        RemoveOnCallStateEnd(2)
        AddY(200000)
        AddX(100000)
        Size(600)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    AddScale(200)
    AddY(25000)
    sprite('null', 2)
    AddY(25000)
    sprite('null', 1)
    CreateObject('ph320BombEff_Circle', -1)
    CreateObject('Eff_431_bombEnd', -1)
    AddScale(100)
    AddY(25000)
    ConstantAlphaModifier(-51)
    CreateParticle('phef_400_bom', -1)
    CreateParticle('phef_400_blm', -1)
    sprite('null', 10)
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddY(-105000)
    AddScale(900)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddY(-205000)
    AddX(200000)
    AddScale(550)
    Rotation(20000)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddY(-205000)
    AddX(-200000)
    AddScale(550)
    Rotation(-20000)
    ApplyFunctionsToSelf()

@State
def Eff_431_bombEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff431_bomb01', '')
        IgnoreScreenfreeze(1)
        Size(250)
        AddY(-260000)
    sprite('null', 14)
    CreateParticle('phef_402_end_g', -1)
    sprite('null', 9)
    CreateParticle('pheff431_gsmoke_pos', -1)
    ConstantAlphaModifier(-26)

@State
def AstralHeatAtk():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        SetScaleX(8000)
        SetScaleY(10000)
        AttackLevel_(3)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Stagger(810)
        Crumple(800)
        AirUntechableTime(600)
        UseSlashHitspark(1)
        PushbackX(0)
        OppPositionOnHit(1, 0, 0)
        DefeatOpponentBehavior(1)
        AttackDirection(0)
        Visibility(1)

        def upon_OPPONENT_HIT():
            ObjectUpon(3, 32)
    sprite('vr_ph_magictest', 8)
    if (SLOT_19 > 450000):
        TeleportToObject(22)
        AbsoluteY(0)
    else:
        AddX(500000)
    CreateParticle('phef450_ahatk', -1)
    CommonSE('022_magiccircle_c')
    CommonSE('014_electric_ll')

@State
def AstralHeatAtk2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        SetScaleX(8000)
        SetScaleY(10000)
        AttackLevel_(5)
        Damage(5000)
        MinimumDamage(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(600)
        UseSlashHitspark(1)
        PushbackX(0)
        OppPositionOnHit(1, 0, 0)
        AttackDirection(0)
        Visibility(1)
    sprite('vr_ph_magictest', 3)
    TeleportToObject(22)
    AbsoluteY(0)

@State
def AstralHeatLastAtk():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        SetScaleX(8000)
        SetScaleY(8000)
        AttackLevel_(5)
        Damage(30000)
        MinimumDamage(100)
        DefeatOpponentBehavior(3)
        AirPushbackY(-50000)
        GroundedHitstunAnimation(11)
        TeleportToObject(22)
    sprite('vr_ph_magictest', 5)

@State
def Eff_450_EyeBurning():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(2)
    label(0)
    sprite('vr_ph450_00', 3)
    sprite('vr_ph450_01', 3)
    sprite('vr_ph450_02', 3)
    sprite('vr_ph450_03', 3)
    sprite('vr_ph450_04', 3)
    gotoLabel(0)

@State
def Eff_450_Terepo():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
    sprite('vr_ph450_10', 6)
    sprite('vr_ph450_11', 3)
    sprite('vr_ph450_12', 3)
    CreateParticle('phef450_terepo', -1)
    sprite('vr_ph450_12', 10)
    physicsYImpulse(25000)
    SetScaleSpeedY(2400)
    CreateObject('Eff_450_circle', -1)
    CreateObject('Eff_450_circle2', -1)

@State
def Eff_450_circle():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Eff3DEffect('pheff450_AddCircle', '')
        AddY(300000)
    sprite('null', 5)
    SetScaleSpeed(300)
    sprite('null', 5)
    ConstantAlphaModifier(-51)

@State
def Eff_450_circle2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Eff3DEffect('pheff450_AddCircle', '')
    sprite('null', 5)
    SetScaleSpeed(300)
    ConstantAlphaModifier(-51)

@State
def AstralHeat_Hibi():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    Size(1350)
sprite('vr_ph450_20', 4)
RenderLayer(2)
sprite('vr_ph450_21', 4)
RenderLayer(0)
sprite('vr_ph450_22', 4)
ScreenShake(10000, 10000)
sprite('vr_ph450_22', 4)
ScreenShake(10000, 10000)
CreateParticle('phef450_groundray', 0)
CreateParticle('phef450_groundsmoke_R', 5)
CreateParticle('phef450_groundsmoke_L', 6)
sprite('vr_ph450_22', 4)
ScreenShake(10000, 10000)
CreateParticle('phef450_groundray', 1)
CreateParticle('phef450_groundray', 2)
CreateParticle('phef450_groundsmoke_R', 5)
CreateParticle('phef450_groundsmoke_L', 6)
sprite('vr_ph450_22', 10)
ScreenShake(10000, 10000)
CreateParticle('phef450_groundray', 3)
CreateParticle('phef450_groundray', 4)
CreateParticle('phef450_groundsmoke_R', 5)
CreateParticle('phef450_groundsmoke_L', 6)
sprite('vr_ph450_22', 4)
ScreenShake(10000, 10000)
CreateParticle('phef450_groundray', 0)
CreateParticle('phef450_groundsmoke_R', 5)
CreateParticle('phef450_groundsmoke_L', 6)
sprite('vr_ph450_22', 4)
ScreenShake(10000, 10000)
CreateParticle('phef450_groundray', 1)
CreateParticle('phef450_groundray', 2)
CreateParticle('phef450_groundsmoke_R', 5)
CreateParticle('phef450_groundsmoke_L', 6)
sprite('null', 8)
CreateParticle('phef_450_groundstone', -1)
endState()

@State
def AstralHeat_Hinokagutsuchi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        AbsoluteY(0)
        PaletteIndex(5)
        AddX(-25000)
    sprite('null', 40)
    CreateObject('AstralHeat_Hibi', -1)
    CommonSE('019_quake_1')
    sprite('ph450_cutin00', 10)
    ScreenShake(80000, 80000)
    CommonSE('019_quake_1')
    CommonSE('016_explode_2')
    CreateObject('AstralHeatEff_SetugouFire', 0)
    CreateObject('AstralHeatEff_SetugouFire', 1)
    CreateObject('AstralHeatEff_SetugouFire', 2)
    CreateObject('AstralHeatEff_SetugouFire', 3)
    CreateObject('AstralHeatEff_SetugouFire', 4)
    sprite('ph450_cutin01', 6)
    CommonSE('019_quake_0')
    sprite('ph450_cutin02', 6)
    CommonSE('019_quake_0')
    sprite('ph450_cutin03', 6)
    CommonSE('019_quake_1')
    sprite('ph450_cutin04', 6)
    ScreenShake(20000, 20000)
    CommonSE('019_quake_1')
    ApplyFunctionsToObjects(22)
    Visibility(1)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin05', 6)
    CommonSE('019_quake_1')
    sprite('ph450_cutin06', 6)
    sprite('ph450_cutin07', 6)
    sprite('ph450_cutin08', 6)
    sprite('ph450_cutin09', 6)
    sprite('ph450_cutin10', 6)
    CreateObject('AstralHeatEff_HinoAdd', -1)
    CommonSE('016_explode_1')
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_2')
    sprite('ph450_cutin10', 1)
    CreateObject('AstralHeatEff_DelFire', 0)
    CommonSE('019_quake_1')
    sprite('ph450_cutin10', 1)
    CreateObject('AstralHeatEff_DelFire2', 1)
    sprite('ph450_cutin10', 1)
    CreateObject('AstralHeatEff_DelFire', 2)
    CommonSE('019_quake_0')
    sprite('ph450_cutin10', 1)
    sprite('ph450_cutin10', 1)
    CommonSE('015_blaze_2')
    CommonSE('019_quake_1')
    sprite('ph450_cutin10', 1)
    sprite('ph450_cutin10', 10)
    ConstantAlphaModifier(-26)
    CommonSE('019_quake_0')
    sprite('ph450_cutin10', 10)
    CreateObject('AstralHeatEff_Rougoku', -1)
    Visibility(1)
    ApplyFunctionsToObjects(22)
    Visibility(0)
    ApplyFunctionsToSelf()
    CommonSE('019_quake_1')
    CommonSE('015_blaze_2')
    sprite('ph450_cutin10', 2)
    CreateObject('AstralHeatEff_DelFire', 0)
    sprite('ph450_cutin10', 2)
    CreateObject('AstralHeatEff_DelFire2', 1)
    sprite('ph450_cutin10', 2)
    CreateObject('AstralHeatEff_DelFire', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 20)
    CommonSE('019_quake_1')
    sprite('ph450_cutin10', 2)
    CreateObject('AstralHeatEff_DelFire', 0)
    sprite('ph450_cutin10', 2)
    CreateObject('AstralHeatEff_DelFire2', 1)
    CommonSE('015_blaze_2')
    sprite('ph450_cutin10', 2)
    CreateObject('AstralHeatEff_DelFire', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    CommonSE('019_quake_1')
    sprite('ph450_cutin10', 2)

@State
def AstralHeatEff_SetugouFire():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
    label(0)
    sprite('null', 25)
    CreateObject('AstralHeatEff_DelFire', -1)
    gotoLabel(0)

@State
def AstralHeatEff_HinoAdd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(3)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        AlphaValue(0)
    sprite('vrph450_30', 10)
    ConstantAlphaModifier(26)
    sprite('vrph450_30', 10)
    ConstantAlphaModifier(0)
    sprite('vrph450_30', 20)
    ConstantAlphaModifier(-13)

@State
def AstralHeatEff_Rougoku():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('pheff450_ori00', '')
        Size(825)
        AddY(-3000)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    sprite('null', 100)

@State
def AstralHeatEff_DelFire():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        Size(1600)
        SetScaleSpeed(7)
    sprite('vr_phcmn_00', 4)
    sprite('vr_phcmn_01', 4)
    sprite('vr_phcmn_02', 4)
    sprite('vr_phcmn_03', 4)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    CreateParticle('phef450_hinoko', 0)
    CreateParticle('phef450_hinoko', 1)
    CreateParticle('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def AstralHeatEff_DelFire2():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        Size(1800)
        SetScaleSpeed(7)
        AddY(-30000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    CreateParticle('phef450_hinoko', 0)
    CreateParticle('phef450_hinoko', 1)
    CreateParticle('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def AstralHeat_Camera():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        CameraFast(1)
    sprite('null', 7)
    AddX(400000)
    AddY(-800000)
    physicsYImpulse(48000)
    sprite('null', 30)
    CameraFast(0)
    physicsYImpulse(18000)
    LinkParticle('phef_shashaend')
    sprite('null', 10)
    physicsYImpulse(3000)
    sprite('null', 5)
    physicsYImpulse(1500)
    sprite('null', 210)
    physicsYImpulse(0)
    sprite('null', 10)
    CameraFast(1)
    AddY(-1200000)
    XPositionRelativeFacing(0)
    ApplyFunctionsToObjects(22)
    Visibility(0)
    ApplyFunctionsToSelf()
    CreateObject('AstralHeatEff_Rougoku2', -1)
    sprite('null', 32767)
    CameraFast(0)
    CameraPosition(1300)

@State
def AstralHeatEff_Rougoku2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('pheff450_ori00', '')
        LinkParticle('phef450_rou_jizoku')
        Size(600)
        AddY(300000)
        Visibility(1)
    sprite('ph450_cutin06', 160)
    CreateObject('AstralHeatEff_Rougoku2Sub', -1)

@State
def AstralHeatEff_Rougoku2Sub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        Size(700)
        RemoveOnCallStateEnd(2)
        AlphaValue(0)
    label(0)
    sprite('ph450_cutin06', 2)
    CreateObject('AstralHeatEff_DelFire', 0)
    ApplyFunctionsToObjects(1)
    AddScale(-450)
    AlphaValue(180)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin06', 2)
    CreateObject('AstralHeatEff_DelFire2', 1)
    ApplyFunctionsToObjects(1)
    AddScale(-450)
    AlphaValue(180)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin06', 2)
    CreateObject('AstralHeatEff_DelFire', 2)
    ApplyFunctionsToObjects(1)
    AddScale(-450)
    AlphaValue(180)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin06', 2)
    CreateObject('AstralHeatEff_DelFire2', 3)
    ApplyFunctionsToObjects(1)
    AddScale(-450)
    AlphaValue(180)
    AddX(30000)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin06', 2)
    CreateObject('AstralHeatEff_DelFire', 4)
    ApplyFunctionsToObjects(1)
    AddScale(-450)
    AddX(-30000)
    AlphaValue(180)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin06', 2)
    CreateObject('AstralHeatEff_DelFire2', 5)
    ApplyFunctionsToObjects(1)
    AddScale(-200)
    AddY(60000)
    AlphaValue(180)
    ApplyFunctionsToSelf()
    sprite('ph450_cutin06', 13)
    gotoLabel(0)

@State
def AstralHeat_ShakeFallMeteo():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddX(-400000)
        AddY(-800000)
    label(0)
    sprite('null', 5)
    ScreenShake(5000, 5000)
    gotoLabel(0)

@State
def AstralHeatEff_MeteoLast():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('pheff450_meteo01', '')
        Rotation(-45000)
        SetScaleX(3500)
        SetScaleY(3500)
        AddX(650000)
        RenderLayer(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
    sprite('null', 7)
    physicsYImpulse(-40000)
    physicsXImpulse(28000)
    CreateObject('AstralHeat_ShakeFallMeteo', -1)
    sprite('null', 7)
    physicsYImpulse(-30000)
    physicsXImpulse(21000)
    sprite('null', 15)
    physicsYImpulse(-20000)
    physicsXImpulse(14000)
    sprite('null', 6)
    physicsYImpulse(-20000)
    physicsXImpulse(14000)

@State
def Eff_450_Lastbomb():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff450_lastbomb00', '')
        Size(1200)
        AbsoluteY(0)
        XPositionRelativeFacing(0)
        RenderLayer(1)
    sprite('null', 2)
    sprite('null', 2)
    AddScale(200)
    AddY(25000)
    sprite('null', 2)
    AddY(25000)
    sprite('null', 5)
    CreateObject('Eff_450_LastbombEnd', -1)
    AddScale(100)
    AddY(25000)
    ConstantAlphaModifier(-51)

@State
def Eff_450_LastbombEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff450_lastbomb01', '')
        IgnoreScreenfreeze(1)
        Size(500)
        AddY(-300000)
        RenderLayer(1)
    sprite('null', 4)
    sprite('null', 10)
    CreateParticle('phef_lastbomb_end', -1)
    sprite('null', 9)
    ConstantAlphaModifier(-26)

@State
def Eff_450_Burning():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff450_winbg', '')
        IgnoreScreenfreeze(1)
        AddX(600000)
        Size(800)
        LinkParticle('pheff450_winbg')
    label(0)
    sprite('null', 10)
    CommonSE('019_quake_0')
    sprite('null', 10)
    CommonSE('019_quake_1')
    loopRest()
    gotoLabel(0)

@State
def AstralHeatEff_Meteo():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('pheff450_meteo00', '')
        physicsYImpulse(-48000)
        physicsXImpulse(48000)
        Rotation(-45000)
        sendToLabelUpon(2, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    CreateParticle('phef_bgr_atk_end', -1)
    AlphaValue(0)
    physicsYImpulse(0)
    physicsXImpulse(0)
    CreateObject('AstralHeatEff_MeteoMag', -1)
    ScreenShake(0, 10000)

@State
def AstralHeatEff_MeteoMag():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1000)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        RandAddScaleX(-300, 0)
    sprite('null', 10)
    CreateObject('Eff_450_bomb', -1)
    AlphaValue(0)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    AlphaValue(255)
    SetScaleSpeedY(75)
    label(0)
    sprite('null', 2)
    SetScaleSpeedY(0)
    AddScaleX(-300)
    AddX(10000)
    sprite('null', 2)
    AddScaleX(300)
    AddX(-10000)
    gotoLabel(0)

@State
def Eff_450_bomb():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('pheff431_bomb00', '')
        LinkParticle('phef431_blm')
        AddY(200000)
        AddX(100000)
        Size(600)
    sprite('null', 2)
    sprite('null', 2)
    AddScale(200)
    AddY(25000)
    sprite('null', 2)
    AddY(25000)
    sprite('null', 5)
    CreateObject('Eff_450_bombEnd', -1)
    AddScale(100)
    AddY(25000)
    ConstantAlphaModifier(-51)
    CreateParticle('phef_400_bom', -1)
    CreateParticle('phef_400_blm', -1)

@State
def Eff_450_bombEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff431_bomb01', '')
        IgnoreScreenfreeze(1)
        Size(250)
        AddY(-250000)
    sprite('null', 14)
    CreateParticle('phef_402_end_g', -1)
    sprite('null', 9)
    CreateParticle('pheff431_gsmoke_pos', -1)
    ConstantAlphaModifier(-26)

@State
def AstralHeatEff_MeteoMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        XPositionRelativeFacing(-800000)
        AbsoluteY(0)
        AddY(500000)
        sendToLabelUpon(2, 0)
    sprite('null', 8)
    CreateObject('AstralHeatEff_Meteo', -1)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 8)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(1000000)
    AddScale(400)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('213_bound_1')
    sprite('null', 8)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(500000)
    AddScale(500)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 8)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(-1000000)
    AddScale(600)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('213_bound_1')
    sprite('null', 6)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(-500000)
    AddScale(700)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 6)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(750000)
    AddScale(800)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('213_bound_0')
    sprite('null', 4)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(250000)
    AddScale(900)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 15)
    CreateObject('AstralHeatEff_Meteo', -1)
    ApplyFunctionsToObjects(1)
    AddX(-250000)
    AddScale(1000)
    ApplyFunctionsToSelf()
    CommonSE('016_explode_2')
    CommonSE('213_bound_0')
    sprite('null', 15)
    CreateObject('AstralHeatEff_MeteoLast', -1)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 15)
    sprite('null', 10)
    CreateObject('Eff_450_Lastbomb', -1)
    DespawnEAEffect('AstralHeatEff_Meteo')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    CommonSE('213_bound_1')
    sprite('null', 4)
    CreateObject('Eff_450_Burning', -1)

@State
def phAst_ShaSha00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('pheff450_shasha00', '')
        E0EAEffectPosition(2)
        RenderLayer(1)
        AddY(-400000)
    sprite('null', 39)

@State
def Entry_Hinokagutsuchi():

    def upon_IMMEDIATE():
        pass
    sprite('ph601cutin_ex01', 5)

@State
def Entry_HinoEff():

    def upon_IMMEDIATE():
        LinkParticle('phef601_root')
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 1)
        SetActionMark(0)

        def upon_33():
            clearUponHandler(33)
            SLOT_51 = 1
            SetActionMark(1)
    label(0)
    sprite('null', 16)
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddX(-350000)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddX(300000)
    AddY(100000)
    AddScale(500)
    RenderLayer(2)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddX(-300000)
    AddY(100000)
    AddScale(800)
    RenderLayer(2)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddX(180000)
    AddY(25000)
    AddScale(600)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddX(-200000)
    AddScale(600)
    ApplyFunctionsToSelf()
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddScaleX(300)
    ApplyFunctionsToSelf()
    if SLOT_2:
        CommonSE('019_quake_1')
    gotoLabel(0)
    label(1)
    sprite('null', 15)
    CreateObject('Entry_FireEnd', -1)
    ConstantAlphaModifier(25)

@State
def Entry_Fire():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        Size(1000)
        SetScaleSpeedY(15)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        DeviationX(-25000, 25000)
        AddY(-50000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    ConstantAlphaModifier(-26)
    CreateParticle('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def Entry_FireEnd():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        Eff3DEffect('pheff601_fire00', '')
        Size(800)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    CreateParticle('phef601_endray', -1)
    CreateObject('Entry_FireEndsub_b', -1)
    ApplyFunctionsToObjects(1)
    AddY(100000)
    AddScale(1000)
    ApplyFunctionsToSelf()
    sprite('null', 2)
    CreateObject('Entry_FireEndsub_a', -1)
    ApplyFunctionsToObjects(1)
    AddY(100000)
    AddScale(-2000)
    ApplyFunctionsToSelf()
    sprite('null', 2)
    CreateObject('Entry_FireEndsub_a', -1)
    ApplyFunctionsToObjects(1)
    AddY(200000)
    ApplyFunctionsToSelf()
    sprite('null', 2)
    CreateObject('Entry_FireEndsub_a', -1)
    ApplyFunctionsToObjects(1)
    AddY(300000)
    AddScale(-2000)
    ApplyFunctionsToSelf()
    sprite('null', 2)
    CreateObject('Entry_FireEndsub_a', -1)
    ApplyFunctionsToObjects(1)
    AddY(400000)
    AddScale(-1500)
    ApplyFunctionsToSelf()
    sprite('null', 2)
    CreateObject('Entry_FireEndsub_a', -1)
    ApplyFunctionsToObjects(1)
    AddY(550000)
    AddScale(-1200)
    ApplyFunctionsToSelf()
    sprite('null', 3)
    CreateObject('Entry_FireEndsub2', -1)

@State
def Entry_FireEndsub_a():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari01', '')
        IgnoreScreenfreeze(1)
        Size(3800)
        AddY(10000)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(240)
    CreateObject('Entry_FireEndsub_b2', -1)

@State
def Entry_FireEndsub_b():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff432_yari01', '')
        IgnoreScreenfreeze(1)
        Size(3800)
        AddY(10000)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(120)

@State
def Entry_FireEndsub_b2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('pheff_rrr00', '')
        Size(2500)
        AlphaValue(255)
        RotationAngle(20000)
    sprite('null', 5)
    sprite('null', 10)
    SetScaleSpeed(120)
    ConstantAlphaModifier(-26)

@State
def Entry_FireEndsub2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('pheff432_yari03', '')
        IgnoreScreenfreeze(1)
        SetScaleX(1500)
        SetScaleY(1700)
    sprite('null', 10)
    sprite('null', 4)
    CreateObject('Entry_Fire', -1)
    ApplyFunctionsToObjects(1)
    AddY(100000)
    AddScale(1200)
    RenderLayer(2)
    ApplyFunctionsToSelf()

@State
def BurstDDEff():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(5)
        LinkParticle('phef402_mc3')
        TeleportToObject(22)
        RotationAngle(90000)
    sprite('ph402_cutin_a', 2)
    CommonSE('005_swing_grap_2_2')
    sprite('ph402_cutin_b', 1)
    CommonSE('016_explode_2')
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    CreateObject('Eff_402Fire', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(90000)
    AddX(28000)
    ApplyFunctionsToSelf()
    sprite('ph402_cutin', 15)
    RemoveOnCallStateEnd(0)
    IgnorePauses(0)
    sprite('ph402_cutin', 2)
    ConstantAlphaModifier(-26)
    CreateParticle('phef402_end_sita', -1)
    CreateParticle('phef402_end', 0)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 1)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 2)
    sprite('ph402_cutin', 2)
    CreateParticle('phef402_end', 3)

@State
def BurstDDRevEff():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(2400)
        AttackP2(100)
        AttackType(4)
        AirPushbackX(-1000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        AirHitstunAnimation(18)
        Hitstop(0)
        EnemyHitstopAddition(15, 15, 18)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        DamageFromStateOnly('BurstDDBomb')
        CHStateIfCHStart(3)
        OnlyHitPlayer(1)
        PassByArmor(1)

        def upon_OPPONENT_HIT():
            ScreenShake(50000, 10000)
            CommonSE('025_cleanhit_grap')
            if SLOT_2:
                CreateObject('BurstDDBomb', -1)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(5)
        BlendMode_Normal()
        LinkParticle('phef402_mc2')
        TeleportToObject(22)
        RotationAngle(-90000)

        def upon_32():
            DefeatOpponentBehavior(1)
            SetActionMark(1)
    sprite('ph402_cutin_aRev', 2)
    sprite('ph402_cutin_bRev', 1)
    sprite('ph402_cutin_cRev', 1)
    sprite('ph402_cutinRev', 3)
    CreateObject('Eff_402Fire', -1)
    ApplyFunctionsToObjects(1)
    RotationAngle(-90000)
    AddY(-45000)
    AddX(-28000)
    ApplyFunctionsToSelf()
    sprite('ph402_cutinRev', 15)
    RemoveOnCallStateEnd(0)
    IgnorePauses(0)
    sprite('ph402_cutinRev', 2)
    ConstantAlphaModifier(-26)
    CreateParticle('phef402_end_sita', -1)
    CreateParticle('phef402_end', 0)
    sprite('ph402_cutinRev', 2)
    CreateParticle('phef402_end', 1)
    sprite('ph402_cutinRev', 2)
    CreateParticle('phef402_end', 2)
    sprite('ph402_cutinRev', 2)
    CreateParticle('phef402_end', 3)
    if (not SLOT_2):
        ObjectUpon(3, 32)

@State
def BurstDDBomb():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        AttackDefaults_SuperProjectile()
        AttackType(4)
        Size(20000)
        AttackLevel_(5)
        Damage(2800)
        AttackP2(100)
        UseFireHitspark(1)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(25000)
        AirUntechableTime(120)
        HitAnywhere(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        DamageFromStateOnly('BurstDDBomb')
        CHStateIfCHStart(3)
        OnlyHitPlayer(1)
        PassByArmor(1)
        Visibility(1)
    sprite('null', 20)
    sprite('null', 5)
    CreateObject('BurstDDBomb2', -1)
    ApplyFunctionsToObjects(1)
    AddScale(400)
    AddY(-175000)
    ApplyFunctionsToSelf()
    sprite('vr_ph_magictest', 3)
    ScreenShake(25000, 100000)
    sprite('null', 5)
    ObjectUpon(3, 32)

@State
def BurstDDBomb2():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        CancelIfPlayerHit(3)
        Size(800)
    sprite('vr_ph400_04', 2)
    IgnoreFinishStop(1)
    sprite('vr_ph400_05', 3)
    AddY(200000)
    ScreenShake(10000, 10000)
    SetScaleSpeed(15)
    CreateObject('pheff_400sub2', 1)
    ApplyFunctionsToObjects(1)
    RandAddRotation(-40000, 40000)
    IgnoreFinishStop(1)
    ApplyFunctionsToSelf()
    CreateParticle('phef_400_bom', 1)
    CreateParticle('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    CreateParticle('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    CreateObject('ph320BombEff_Circle', -1)
    ApplyFunctionsToObjects(1)
    IgnoreFinishStop(1)
    RandAddRotation(20000, 30000)
    AddScale(-600)
    ApplyFunctionsToSelf()
    CreateObject('phEff400_corebom', 0)
    ConstantAlphaModifier(-51)

@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)

        def upon_FRAME_STEP():
            TeleportToObject(3)
            SLOT_51 = SLOT_19
            SLOT_51 = (SLOT_51 / 4)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 22)
            CopyFromRightToLeft(23, 2, 53, 22, 2, 22)
            if (SLOT_52 < SLOT_53):
                SLOT_22 = (SLOT_22 + SLOT_51)
            elif (SLOT_52 > SLOT_53):
                SLOT_22 = (SLOT_22 - SLOT_51)
            else:
                pass
            SLOT_22 = (SLOT_22 + 200000)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 120)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    label(1)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)

@State
def ph900Eff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        RemoveOnCallStateEnd(2)
        Size(260)
        Eff3DEffect('pheff001_fire00', '')
        LinkParticle('phef001_hinoko')
    sprite('null', 15)
    AlphaValue(0)
    sprite('null', 50)
    ConstantAlphaModifier(4)
    label(0)
    sprite('null', 25)
    physicsYImpulse(150)
    ConstantAlphaModifier(0)
    SetScaleSpeed(-2)
    sprite('null', 5)
    SetScaleSpeed(-1)
    physicsYImpulse(75)
    sprite('null', 25)
    physicsYImpulse(-150)
    SetScaleSpeed(2)
    sprite('null', 5)
    SetScaleSpeed(1)
    physicsYImpulse(-75)
    gotoLabel(0)

@State
def ph900Eff2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        RemoveOnCallStateEnd(2)
        LinkParticle('phef432_yuge')
        AddY(-22500)
    sprite('null', 15)
    AlphaValue(0)
    sprite('null', 50)
    ConstantAlphaModifier(5)
    sprite('null', 32767)

@State
def ph900Eff3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
        RemoveOnCallStateEnd(2)
    sprite('null', 20)
    label(0)
    sprite('null', 22)
    ParticleSize(300)
    CallCustomizableParticle('phef900_fire00', -1)
    gotoLabel(0)

@State
def EventBGBlack():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        PaletteIndex(3)
        BlendMode_Normal()
        SetScaleX(20000)
        SetScaleY(20000)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        RenderLayer(15)
        SetZVal(10000)
    sprite('vr_screen_black', 30)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    label(0)
    sprite('vr_screen_black', 32767)
    AlphaValue(90)
    ConstantAlphaModifier(0)
    gotoLabel(0)
    label(1)
    sprite('vr_screen_black', 30)
    ConstantAlphaModifier(-3)

@State
def Event_ph032FireEff2():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vr_ph32_00', 3)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    ConstantAlphaModifier(-12)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def Event_MidAssault_Atk():

    def upon_IMMEDIATE():
        SetScaleX(6000)
        SetScaleY(15000)
        AddY(80000)
        WallCollisionDetection(1)
        TeleportToObject(22)
        AddY(80000)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Visibility(1)
        NoAttackDuringAction(1)
    sprite('null', 10)
    sprite('null', 4)
    CreateObject('Eff_402', -1)
    CommonSE('016_explode_1')
    sprite('vr_ph_magictest', 5)
    KnockdownEffects(104, 1, 1)
    ExitState()

@State
def Event_DriveAtk_RRR():

    def upon_IMMEDIATE():
        SetScaleX(6000)
        SetScaleY(15000)
        AddX(360000)
        AddY(75000)
        Visibility(1)
    sprite('vr_ph_magictest', 3)
    CreateObject('Eff_RRR', -1)

@State
def Event_phef_600_bg():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(3)
        BlendMode_Normal()
        SetScaleX(20000)
        SetScaleY(20000)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        RenderLayer(15)
        SetZVal(10000)
    sprite('vr_screen_black', 30)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('vr_screen_black', 60)
    AlphaValue(95)
    ConstantAlphaModifier(0)
    sprite('vr_screen_black', 30)
    ConstantAlphaModifier(-3)

@State
def Event_phef_600_Fire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    CreateParticle('phef_600bigen', 100)

@State
def Event_phef_600_Fire2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def Event_phef_600_FireWall():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('pheff600_firewall', '')
        FaceSpawnLocation()
        BlendMode_Add()
        LinkParticle('phef_600ground')
    sprite('null', 6)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_1')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_1')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    CommonSE('019_quake_0')
    sprite('null', 6)
    CreateParticle('phef_600fireblow', -1)
    sprite('null', 16)
    ConstantAlphaModifier(-16)
    CreateObject('Event_phef_600_Fire_End', -1)

@State
def Event_phef_600_Fire_End():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 1)
    CreateParticle('phef_600fire_end', -1)

@State
def Act3Event_phEff_RRB():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 11)
        EndMomentum(1)
    sprite('vr_phrrb_01', 2)
    CreateObject('Act3Event_phEff_RRBSub', -1)
    PrivateSE('phse_04')
    CommonSE('019_quake_1')
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    sprite('vr_phrrb_02', 2)
    sprite('vr_phrrb_03', 2)
    sprite('vr_phrrb_04', 2)
    LinkParticle('phef_rrb_jizoku')
    sprite('vr_phrrb_05', 2)
    sprite('vr_phrrb_00', 4)
    label(0)
    sprite('vr_phrrb_00', 6)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageSize_1(1200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_phrrb_00', 6)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageSize_1(1200)
    CommonSE('019_quake_1')
    ScreenShake(4000, 4000)
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('vr_phrrb_00', 10)
    physicsXImpulse(80000)
    physicsYImpulse(-80000)
    label(11)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()

@State
def Act3Event_phEff_RRBSub():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        RotationAngle(-45000)
        EndMomentum(1)
    sprite('null', 30)
    LinkParticle('phef_rrb_start')
    loopRest()