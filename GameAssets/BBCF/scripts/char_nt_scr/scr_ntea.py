@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emblem_NT.DIG', '')
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
def EMB_NT_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emblem_NT', '')
        RenderLayer(5)
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
def EMB_NT_AH():

    def upon_IMMEDIATE():
        Size(1400)
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emblem_NT', '')
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
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        FaceSpawnLocation()
        ColorFromPaletteIndex(224)
        IgnoreScreenfreeze(1)
    sprite('null', 74)


@State
def BackThrow_DashStop():

    def upon_IMMEDIATE():
        ForceFaceSprite()
    sprite('null', 20)
    SkidEffects(100, 1, 1)


@State
def ntef_340():

    def upon_IMMEDIATE():
        Eff3DEffect('ntef340_wind.DIG', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        AddX(150000)
        AddY(-42500)
        physicsXImpulse(-3000)
        AddScaleX(350)
        AlphaValue(130)
    sprite('vr_nt340_00', 4)
    CreateParticle('ntef_340_gsmoke', 0)
    CreateParticle('ntef_340_gsmoke', 1)
    CreateParticle('ntef_340_add', 2)
    sprite('vr_nt340_01', 8)
    sprite('vr_nt340_02', 4)
    CreateParticle('ntef_340_gsmoke', 0)
    CreateParticle('ntef_340_gsmoke', 1)
    sprite('vr_nt340_03', 4)
    ConstantAlphaModifier(-7)
    sprite('vr_nt340_04', 4)
    sprite('vr_nt340_05', 4)


@State
def ntef_340_pt():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)


@State
def ntef_400_aura():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddScale(200)
        CancelIfPlayerHit(3)
    sprite('vr_nt400_00', 3)
    sprite('vr_nt400_01', 3)
    sprite('vr_nt400_02', 3)
    sprite('vr_nt400_03', 3)
    ConstantAlphaModifier(-20)
    sprite('vr_nt400_04', 2)
    sprite('vr_nt400_05', 2)


@State
def ntef_401_aura1():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('vr_nt401_00', 32767)


@State
def ntef_401_aura2():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        AddScale(350)
        AddX(-75000)
        CancelIfPlayerHit(3)
    sprite('vr_nt401_01', 4)
    sprite('vr_nt401_02', 4)
    sprite('vr_nt401_03', 2)
    CreateParticle('ntef_402_aura2_pos', 0)
    CreateParticle('ntef_402_aura3_pos', 1)
    sprite('vr_nt401_04', 2)


@State
def ntef_402():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreFinishStop(1)
    sprite('vr_nt402_00', 3)
    sprite('vr_nt402_01', 3)
    AddScale(500)
    AddY(-150000)
    AddX(-150000)
    sprite('vr_nt402_02', 2)
    CreateParticle('ntef_402_aura', 2)
    CreateParticle('ntef_402_aura', 3)
    CreateParticle('ntef_402_aura', 4)
    sprite('vr_nt402_03', 2)
    IgnoreFinishStop(0)
    sprite('vr_nt402_04', 2)
    CreateParticle('ntef_402_aura2_pos', 0)
    CreateParticle('ntef_402_aura3_pos', 1)
    CreateParticle('ntef_402_aura4', 2)
    sprite('vr_nt402_05', 2)


@State
def ntef_403():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddScale(500)
        AddY(-75000)
    sprite('vr_nt403_00', 3)
    sprite('vr_nt403_01', 3)
    sprite('vr_nt403_02', 3)
    sprite('vr_nt403_03', 2)
    sprite('vr_nt403_04', 2)
    CreateParticle('ntef_403_aura', 0)
    CreateParticle('ntef_403_aura', 1)
    CreateParticle('ntef_403_aura', 2)
    CreateParticle('ntef_403_aura3', 3)
    CreateParticle('ntef_403_aura2', 4)
    sprite('vr_nt403_05', 2)


@State
def ntef_405Weak():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(300000)
        AddX(100000)
        RotationAngle(15000)
        AlphaValue(210)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 2)
    sprite('vr_nt405_20', 32767)
    CreateObject('ntef_405WeakSub', -1)
    CreateObject('ntef_405WeakSmoke', -1)
    Size(750)
    label(0)
    sprite('vr_nt405_20', 2)
    TriggerUponForState('ntef_405WeakSub', 32)
    AddY(100000)
    AddX(50000)
    Size(1200)
    label(1)
    sprite('vr_nt405_21', 2)
    sprite('vr_nt405_22', 2)
    sprite('vr_nt405_20', 2)
    gotoLabel(1)
    label(2)
    sprite('null', 14)
    CreateObject('ntef_405WeakEnd', -1)
    DespawnEAEffect('ntef_405WeakSub')


@State
def ntef_405WeakSub():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        RenderLayer(11)
        uponSendToLabel(32, 1)
        AlphaValue(210)
    sprite('vr_nt405_30', 32767)
    label(1)
    sprite('vr_nt405_31', 2)
    sprite('vr_nt405_32', 2)
    sprite('vr_nt405_30', 2)
    gotoLabel(1)


@State
def ntef_405WeakEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        Eff3DEffect('ntef405_syoryu01', '')
    sprite('null', 13)
    Size(600)
    SetScaleSpeed(-15)
    ConstantAlphaModifier(-15)
    AddX(-160000)


@State
def ntef_405WeakAir():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(300000)
        AddX(100000)
        Size(650)
        AlphaValue(210)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 2)
    sprite('vr_nt405_20', 32767)
    CreateObject('ntef_405WeakSub', -1)
    label(0)
    sprite('vr_nt405_20', 2)
    TriggerUponForState('ntef_405WeakSub', 32)
    AddY(100000)
    AddX(50000)
    Size(800)
    label(1)
    sprite('vr_nt405_21', 2)
    Size(1200)
    sprite('vr_nt405_22', 2)
    sprite('vr_nt405_20', 2)
    gotoLabel(1)
    label(2)
    sprite('null', 14)
    DespawnEAEffect('ntef_405WeakSub')
    CreateObject('ntef_405WeakEnd', -1)


@State
def ntef_405WeakSmoke():

    def upon_IMMEDIATE():
        LinkParticle('ntef_405_smoke')
        IgnorePauses(3)
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
        Size(1100)
    sprite('null', 30)


@State
def ntef_405Test():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('ntef405_Bloodsyoryu00', '')
        Rotation(10000)
        AddX(50000)
        Size(1300)
        uponSendToLabel(32, 1)
    sprite('null', 3)
    CreateObject('ntef_405Sub', -1)
    CreateParticle('ntef_405_nokosi', -1)
    sprite('null', 1)
    Size(1300)
    AddY(80000)
    AddX(60000)
    CreateParticle('ntef_405_nokosi', -1)
    IgnorePauses(0)
    label(0)
    sprite('null', 3)
    CreateParticle('ntef_405_nokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 4)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    CreateParticle('ntef_405_nokosi', -1)
    AddX(-60000)
    AddY(-140000)
    Rotation(-10000)
    Eff3DEffect('ntef405_Bloodsyoryu01', '')
    sprite('null', 4)
    CreateParticle('ntef_405_nokosi', -1)
    sprite('null', 4)
    CreateParticle('ntef_405_nokosi', -1)
    sprite('null', 5)
    CreateParticle('ntef_405_nokosi', -1)


@State
def ntef_405():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        uponSendToLabel(32, 1)
        ParticleLayer(12)
        CallPrivateEffect('tef_405_back')
    sprite('vr_nt405_00', 1)
    CreateObject('ntef_405Sub', -1)
    Size(950)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_00', 2)
    AddY(80000)
    AddX(40000)
    IgnorePauses(0)
    sprite('vr_nt405_01', 2)
    label(0)
    sprite('vr_nt405_00', 2)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_00', 2)
    sprite('vr_nt405_01', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('ntef_405end', -1)


@State
def ntef_405end():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1100)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_02', 4)
    sprite('vr_nt405_03', 4)
    sprite('vr_nt405_04', 4)
    sprite('vr_nt405_05', 4)


@State
def ntef_405Sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        AbsoluteY(0)
        AddY(-15000)
        AddX(40000)
        Size(1000)
        RenderLayer(6)
    sprite('vr_nt405_10', 6)
    IgnorePauses(2)
    sprite('vr_nt405_11', 6)
    sprite('vr_nt405_12', 4)
    IgnorePauses(0)
    sprite('vr_nt405_13', 4)
    sprite('vr_nt405_14', 4)
    sprite('vr_nt405_15', 4)
    sprite('vr_nt405_16', 4)


@State
def ntef_405AirTest():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('ntef405_Bloodsyoryu00', '')
        Rotation(10000)
        AddX(50000)
        Size(1300)
        uponSendToLabel(32, 1)
    sprite('null', 3)
    CreateParticle('ntef_405_nokosi', -1)
    sprite('null', 1)
    Size(1300)
    AddY(80000)
    AddX(60000)
    CreateParticle('ntef_405_nokosi', -1)
    IgnorePauses(0)
    label(0)
    sprite('null', 3)
    CreateParticle('ntef_405_nokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 4)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    CreateParticle('ntef_405_nokosi', -1)
    AddX(-60000)
    AddY(-140000)
    Rotation(-10000)
    Eff3DEffect('ntef405_Bloodsyoryu01', '')
    sprite('null', 4)
    CreateParticle('ntef_405_nokosi', -1)
    sprite('null', 4)
    CreateParticle('ntef_405_nokosi', -1)
    sprite('null', 5)
    CreateParticle('ntef_405_nokosi', -1)


@State
def ntef_405Air():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        ParticleLayer(12)
        CallPrivateEffect('tef_405_back')
        uponSendToLabel(32, 1)
    sprite('vr_nt405_00', 1)
    sprite('vr_nt405_01', 2)
    sprite('vr_nt405_00', 2)
    AddY(80000)
    AddX(40000)
    IgnorePauses(0)
    EnableAfterimage(1)
    sprite('vr_nt405_01', 2)
    label(0)
    sprite('vr_nt405_00', 2)
    Size(800)
    CreateParticle('ntef_D_aura', 0)
    CreateParticle('ntef_D_aura', 1)
    CreateParticle('ntef_D_aura', 2)
    CreateParticle('ntef_D_aura', 3)
    CreateParticle('ntef_D_aura', 4)
    sprite('vr_nt405_01', 2)
    Size(1000)
    sprite('vr_nt405_00', 2)
    Size(800)
    sprite('vr_nt405_01', 2)
    Size(1000)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    CreateObject('ntef_405end', -1)


@State
def ntef_409():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef409_strike00', '')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddY(400000)
        Size(1700)
    sprite('null', 14)


@State
def ntef_410():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef409_strike01', '')
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddY(300000)
        AddX(50000)
        Size(1500)
        uponSendToLabel(32, 0)
    sprite('null', 10)
    sprite('null', 9)
    Eff3DEffect('ntef409_strike02', '')
    physicsYImpulse(-15000)


@State
def ntef_430_bloodMatome():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddY(180000)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
    sprite('null', 6)
    CreateObject('ntef_430_blood2', -1)
    CreateObject('ntef_430_blood', -1)

    def RunOnObject_1():
        Rotation(35000)
    CreateObject('ntef_430_aura00', -1)
    sprite('null', 6)
    CreateObject('ntef_430_blood', -1)

    def RunOnObject_1():
        Rotation(-35000)
    sprite('null', 6)
    CreateObject('ntef_430_blood2', -1)


@State
def ntef_430_blood():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef430_aura00', '')
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
    sprite('null', 24)
    SetScaleSpeed(-5)


@State
def ntef_430_blood2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef430_aura01', '')
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        AddY(-200000)
    sprite('null', 7)
    SetScaleXPerFrame(37)
    SetScaleSpeedY(37)
    sprite('null', 7)
    SetScaleXPerFrame(75)
    SetScaleSpeedY(75)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ntef_430_aura00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        AddY(-130000)
        Visibility(1)
        ContinueState(20)
    sprite('vr_nt430aurapos', 6)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 0)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 1)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 4)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 5)
    CallCustomizableParticle('tef_430_auranml', 0)
    CallCustomizableParticle('tef_430_auranml', 1)
    CallCustomizableParticle('tef_430_auranml', 4)
    CallCustomizableParticle('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 0)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 1)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 4)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 5)
    CallCustomizableParticle('tef_430_auranml', 0)
    CallCustomizableParticle('tef_430_auranml', 1)
    CallCustomizableParticle('tef_430_auranml', 4)
    CallCustomizableParticle('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 0)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 1)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 4)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 5)
    CallCustomizableParticle('tef_430_auranml', 0)
    CallCustomizableParticle('tef_430_auranml', 1)
    CallCustomizableParticle('tef_430_auranml', 4)
    CallCustomizableParticle('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 0)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 1)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 4)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 5)
    CallCustomizableParticle('tef_430_auranml', 0)
    CallCustomizableParticle('tef_430_auranml', 1)
    CallCustomizableParticle('tef_430_auranml', 4)
    CallCustomizableParticle('tef_430_auranml', 5)
    sprite('vr_nt430aurapos', 6)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 0)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 1)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 4)
    ParticleLayer(11)
    CallCustomizableParticle('tef_430_aura', 5)
    CallCustomizableParticle('tef_430_auranml', 0)
    CallCustomizableParticle('tef_430_auranml', 1)
    CallCustomizableParticle('tef_430_auranml', 4)
    CallCustomizableParticle('tef_430_auranml', 5)


@State
def ntef_430atk():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        BlendMode_Normal()
        AlphaValue(230)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 3)
    label(0)
    sprite('vr_nt430_00', 2)
    sprite('vr_nt430_01', 2)
    gotoLabel(0)
    label(1)
    sprite('vr_nt430_02', 4)
    IgnoreFinishStop(1)
    sprite('vr_nt430_03', 4)
    sprite('vr_nt430_04', 4)
    sprite('vr_nt430_05', 4)
    sprite('vr_nt430_06', 4)
    sprite('vr_nt430_07', 6)
    sprite('vr_nt430_08', 3)
    sprite('vr_nt430_09', 3)
    sprite('vr_nt430_10', 2)
    sprite('vr_nt430_20', 2)
    CreateObject('ntef_430blood_3d', -1)
    Size(1150)
    AlphaValue(200)
    AddY(220000)
    AddX(290000)
    RenderLayer(11)
    IgnorePauses(2)
    IgnoreFinishStop(0)
    CreateObject('ntef_atksub', -1)
    label(2)
    sprite('vr_nt430_21', 3)
    sprite('vr_nt430_20', 3)
    gotoLabel(2)
    label(3)
    sprite('vr_nt430_21', 2)
    RemoveOnCallStateEnd(0)
    TriggerUponForState('ntef_atksub', 32)
    sprite('vr_nt430_22', 4)
    RenderLayer(0)
    E0EAEffectPosition(0)
    TriggerUponForState('ntef_430blood_3d', 32)
    sprite('vr_nt430_23', 2)
    sprite('vr_nt430_23', 2)
    CreateParticle('ntef_430_sibuki', 1)
    CreateParticle('ntef_430_sibuki', 3)
    CreateParticle('ntef_430_sibuki', 5)
    CreateParticle('ntef_430_sibuki', 0)
    CreateParticle('ntef_430_sibuki', 2)
    CreateParticle('ntef_430_sibuki', 4)
    sprite('vr_nt430_24', 4)
    sprite('vr_nt430_25', 3)
    CreateParticle('tef_430_last', 0)
    CreateParticle('tef_430_last', 1)
    CreateParticle('tef_430_last', 2)
    CreateParticle('tef_430_last', 3)


@State
def ntef_atksub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('tef_430_core')
        Visibility(1)
        uponSendToLabel(32, 1)
        E0EAEffectRotation(2)
    label(0)
    sprite('vr_nt430_22', 7)
    CreateParticle('tef_430_tossin_00', 0)
    CreateParticle('tef_430_tossin_00', 1)
    CreateParticle('tef_430_tossin_00', 2)
    CreateParticle('tef_430_tossin_00', 3)
    CreateParticle('tef_430_tossin_00', 4)
    gotoLabel(0)
    label(1)
    sprite('vr_nt430_22', 7)
    ConstantAlphaModifier(-51)
    CreateParticle('tef_430_tossin_00', 0)
    CreateParticle('tef_430_tossin_00', 1)
    CreateParticle('tef_430_tossin_00', 2)
    CreateParticle('tef_430_tossin_00', 3)
    CreateParticle('tef_430_tossin_00', 4)


@State
def ntef_430blood_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        E0EAEffectRotation(2)
        Eff3DEffect('ntef430_blood.DIG', '')
        BlendMode_Normal()
        RemoveOnContact(2)
        RenderLayer(11)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 15)
    RenderLayer(0)
    Eff3DEffect('ntef430_blood2.DIG', '')


@State
def ntef_Air430atk():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        BlendMode_Normal()
        PaletteIndex(1)
        AlphaValue(230)
        AddY(80000)
        AddX(20000)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 3)
    label(0)
    sprite('vr_nt430_00', 2)
    sprite('vr_nt430_01', 2)
    gotoLabel(0)
    label(1)
    sprite('vr_nt430_30', 6)
    IgnoreFinishStop(1)
    AddY(-80000)
    AddX(-20000)
    sprite('vr_nt430_31', 8)
    sprite('vr_nt430_32', 6)
    sprite('vr_nt430_33', 6)
    sprite('vr_nt430_34', 4)
    RenderLayer(11)
    sprite('vr_nt430_20', 2)
    CreateObject('ntef_430blood_3d', -1)
    Size(1150)
    AddY(-50000)
    AddX(290000)
    AlphaValue(250)
    IgnorePauses(2)
    IgnoreFinishStop(0)
    CreateObject('ntef_atksub', -1)
    RotationAngle(45000)
    label(2)
    sprite('vr_nt430_21', 3)
    sprite('vr_nt430_20', 3)
    gotoLabel(2)
    label(3)
    sprite('vr_nt430_21', 2)
    RemoveOnCallStateEnd(0)
    TriggerUponForState('ntef_atksub', 32)
    XPositionRelativeFacing(290000)
    AbsoluteY(-50000)
    RotationAngle(45000)
    sprite('vr_nt430_22', 3)
    TriggerUponForState('ntef_430blood_3d', 32)
    RenderLayer(0)
    E0EAEffectPosition(0)
    sprite('vr_nt430_23', 3)
    sprite('vr_nt430_24', 3)
    sprite('vr_nt430_25', 3)
    CreateParticle('tef_430_last', 0)
    CreateParticle('tef_430_last', 1)
    CreateParticle('tef_430_last', 2)
    CreateParticle('tef_430_last', 3)


@State
def ntef_430_AirbloodMatome():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddY(180000)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
    sprite('null', 6)
    CreateObject('ntef_430_blood', -1)

    def RunOnObject_1():
        Rotation(35000)
        SetScaleSpeed(-30)
        AddScale(300)
    CreateObject('ntef_430_aura00', -1)
    sprite('null', 6)
    CreateObject('ntef_430_blood', -1)

    def RunOnObject_1():
        Rotation(-35000)
        SetScaleSpeed(-15)
        AddScale(100)
    sprite('null', 6)


@State
def ntef_430atkOD():

    def upon_IMMEDIATE():
        Flip()
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        PaletteIndex(1)
        AbsoluteY(0)
        AddY(-30000)
        AddX(-55000)
        RedColorValue(255)
        BlueColorValue(223)
        GreenColorValue(223)
    sprite('vr_nt430_40', 6)
    CreateObject('ntef_430atkODsub', -1)
    CreateParticle('tef_430a_tossin_00', 0)
    CreateParticle('tef_430a_tossin_00', 1)
    CreateParticle('tef_430a_tossin_00', 2)
    CreateParticle('tef_430a_tossin_00', 3)
    CreateParticle('tef_430a_tossin_00', 4)
    sprite('vr_nt430_41', 6)
    IgnorePauses(2)
    CreateObject('ntef_430atkODsub', -1)
    CreateParticle('tef_430a_tossin_00', 0)
    CreateParticle('tef_430a_tossin_00', 1)
    CreateParticle('tef_430a_tossin_00', 2)
    CreateParticle('tef_430a_tossin_00', 3)
    CreateParticle('tef_430a_tossin_00', 4)
    sprite('vr_nt430_42', 5)
    sprite('vr_nt430_43', 4)
    sprite('vr_nt430_44', 4)


@State
def ntef_430atkODsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1500)
        AlphaValue(200)
        Eff3DEffect('ntef430a_moya2', '')
        RemoveOnCallStateEnd(2)
        Flip()
    sprite('null', 17)
    SetScaleSpeed(75)


@State
def ntef_430_moya():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1500)
        AddX(300000)
        AddY(75000)
        LinkParticle('tef_430a_yotyou')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        uponSendToLabel(32, 0)
    sprite('null', 15)
    sprite('null', 32767)
    CreateObject('ntef_430_moyaa', -1)
    E0EAEffectPosition(0)
    label(0)
    sprite('null', 1)


@State
def ntef_430_moyaa():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('ntef430a_moya', '')
        RemoveOnCallStateEnd(2)
        AddScale(500)
        AlphaValue(200)
        AddY(-100000)
    sprite('null', 20)
    AlphaValue(0)
    ConstantAlphaModifier(15)
    sprite('null', 21)
    ConstantAlphaModifier(0)


@State
def ntef_431():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(693)
        AttackP2(94)
        Hitstop(3)
        EnemyHitstopAddition(1, 1, 1)
        Blockstun(13)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(36000)
        AirUntechableTime(60)
        StarterRating(2)
        IgnorePauses(2)
        E0EAEffectPosition(3)

        def upon_33():
            clearUponHandler(56)
            NoAttackDuringAction(1)
            E0EAEffectPosition(0)

        def upon_56():
            E0EAEffectPosition(0)
        BlendMode_Normal()
        AddScale(50)
        AddX(100000)
        AddY(-30000)
    sprite('vr_nt431_00', 3)
    CreateObject('ntef_431_3d', -1)
    physicsXImpulse(24000)
    ScreenShake(10000, 10000)
    CreateObject('ntef_431Sub', 2)
    sprite('vr_nt431_00', 3)
    AddScale(300)
    physicsXImpulse(6000)
    sprite('vr_nt431_01', 3)
    IgnorePauses(0)
    physicsXImpulse(4000)
    sprite('vr_nt431_01', 3)
    RefreshMultihit()
    AddScale(300)
    physicsXImpulse(3000)
    CreateObject('ntef_431OdLastSub', -1)

    def RunOnObject_1():
        SetScaleX(1500)
        SetScaleY(1000)
        AddY(30000)
        AddX(-250000)
    sprite('vr_nt431_02', 6)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('vr_nt431_03', 4)
    sprite('vr_nt431_04', 4)
    TriggerUponForState('ntef_431_3d', 32)
    TriggerUponForState('ntef_431Sub', 32)
    sprite('vr_nt431_05', 4)
    CreateParticle('tef_430a_tossin_00', 0)
    CreateParticle('tef_430a_tossin_00', 1)
    CreateParticle('tef_430a_tossin_00', 2)
    CreateParticle('tef_430a_tossin_00', 3)
    CreateParticle('tef_430a_tossin_00', 4)
    CreateParticle('tef_430a_tossin_00', 5)


@State
def ntef_431_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Eff3DEffect('ntef431_upper.DIG', '')
        BlendMode_Normal()
        RemoveOnContact(2)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
        Size(1200)
        AddY(-16000)
        AddX(32000)
    sprite('null', 3)
    sprite('null', 3)
    AddScale(120)
    sprite('null', 3)
    sprite('null', 3)
    AddScale(180)
    sprite('null', 2)
    sprite('null', 4)
    AlphaValue(225)
    sprite('null', 4)
    AlphaValue(200)
    label(0)
    sprite('null', 4)
    Eff3DEffect('ntef431_upper2.DIG', '')
    AlphaValue(175)
    sprite('null', 4)


@State
def ntef_431_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(803)
        AttackP2(94)
        Hitstop(3)
        EnemyHitstopAddition(1, 1, 1)
        Blockstun(13)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(36000)
        AirUntechableTime(60)
        AttackType(4)
        StarterRating(2)
        IgnorePauses(2)
        E0EAEffectPosition(3)

        def upon_33():
            clearUponHandler(56)
            NoAttackDuringAction(1)
            E0EAEffectPosition(0)

        def upon_56():
            E0EAEffectPosition(0)
        BlendMode_Normal()
        Size(1050)
        AddX(100000)
        AddY(-30000)
    sprite('vr_nt431_00', 3)
    CreateObject('ntef_431_3d', -1)
    physicsXImpulse(24000)
    ScreenShake(10000, 10000)
    CreateObject('ntef_431Sub', 2)
    sprite('vr_nt431_00', 3)
    AddScale(300)
    physicsXImpulse(6000)
    sprite('vr_nt431_01', 3)
    IgnorePauses(0)
    physicsXImpulse(4000)
    sprite('vr_nt431_01', 3)
    RefreshMultihit()
    AddScale(300)
    physicsXImpulse(3000)
    CreateObject('ntef_431OdLastSub', -1)

    def RunOnObject_1():
        SetScaleX(1500)
        SetScaleY(1000)
        AddY(30000)
        AddX(-250000)
    sprite('vr_nt431_02', 6)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('vr_nt431_03', 4)
    sprite('vr_nt431_04', 4)
    TriggerUponForState('ntef_431_3d', 32)
    TriggerUponForState('ntef_431Sub', 32)
    sprite('vr_nt431_05', 4)
    CreateParticle('tef_430a_tossin_00', 0)
    CreateParticle('tef_430a_tossin_00', 1)
    CreateParticle('tef_430a_tossin_00', 2)
    CreateParticle('tef_430a_tossin_00', 3)
    CreateParticle('tef_430a_tossin_00', 4)
    CreateParticle('tef_430a_tossin_00', 5)


@State
def ntef_431AddAtk():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef431_addslash00', '')
        RemoveOnCallStateEnd(2)
        AddY(185000)
        Size(2000)
    sprite('null', 2)
    CreateParticle('ntef_431_speed', -1)
    CreateObject('ntef_431shockwave', -1)
    sprite('null', 2)
    AddScaleY(1600)
    sprite('null', 2)
    AddScaleY(-1600)
    sprite('null', 2)
    AddScaleY(1600)
    sprite('null', 2)
    AddScaleY(-1600)
    sprite('null', 5)
    sprite('null', 10)
    SetScaleSpeedY(-200)


@State
def ntef_431shockwave():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef431_saddslash01', '')
        RemoveOnCallStateEnd(2)
        Size(150)
    sprite('null', 8)
    sprite('null', 5)
    physicsXImpulse(10000)
    SetScaleSpeed(50)
    sprite('null', 5)
    SetScaleSpeed(100)


@State
def ntef_431Sub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('tef_431_ground')
        RemoveOnCallStateEnd(2)
        Size(850)
        AddX(75000)
        Flip()
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    loopRest()


@State
def ntef_431OD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
    sprite('vr_nt431_10', 4)
    AddX(-20000)
    sprite('vr_nt431_11', 4)
    sprite('vr_nt431_12', 4)
    AddX(-30100)
    sprite('vr_nt431_13', 4)
    AddX(50100)
    sprite('vr_nt431_14', 4)
    sprite('vr_nt431_15', 2)
    sprite('vr_nt431_16', 2)
    sprite('vr_nt431_17', 2)
    AddX(-50100)
    CreateObject('ntef_431OdSub', 0)
    sprite('vr_nt431_18', 5)
    CreateObject('ntef_431OdLastAtk', -1)
    sprite('vr_nt431_19', 4)
    sprite('vr_nt431_20', 6)
    sprite('vr_nt431_21', 6)
    sprite('vr_nt431_22', 6)


@State
def ntef_431OdSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef431_slash00', '')
        IgnorePauses(2)
        SetScaleX(1600)
        SetScaleY(1000)
        AddY(-20000)
        CameraNoScreenCollision(1)
        EnableCollision(0)
        WallCollisionDetection(0)
        ScreenCollision(0)
    sprite('null', 12)
    CreateObject('ntef_431OdShake', -1)
    CameraControlEnable(2)
    CameraPosition(900)


@State
def ntef_431OdShake():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        LinkParticle('tef_431od_tame')
    label(0)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    gotoLabel(0)


@State
def ntef_431OdLastAtk():

    def upon_IMMEDIATE():
        LinkParticle('tef_431_ground_00')
        AddX(600000)
        Flip()
        Size(1200)
    sprite('null', 120)
    ScreenShake(20000, 20000)


@State
def ntef_431OdLastSubMato():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(2200)
        MinimumDamage(25)
        AttackP2(75)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(45000)
        AirPushbackY(20000)
        AirUntechableTime(100)
        Floorslide(25)
        AttackType(4)
        HitAnywhere(1)
        UseSlashHitspark(1)
        CHStateIfCHStart(3)
        RemoveOnCallStateEnd(2)
        Visibility(1)

        def upon_OPPONENT_HIT():
            TriggerUponForState('UltimateEdgeAssault_Exe_OD', 32)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 0)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 2)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 3)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 1)
    sprite('null', 6)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 0)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 2)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 3)
    sprite('vr_nt431_atk', 4)
    CreateObject('ntef_431OdLastSub', 1)


@State
def ntef_431OdLastSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef_cmnblood00', '')
        Size(2500)
        RandAddScale(-300, 300)
    sprite('null', 23)


@State
def ntef_440Axe():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
    sprite('vr_nt440_06', 3)
    CreateObject('ntef_440Last', -1)

    def RunOnObject_1():
        AddX(200000)
        AddScaleY(1000)
        AddScaleX(600)
    sprite('vr_nt440_06', 3)
    Visibility(1)
    CreateObject('ntef_440Last', -1)

    def RunOnObject_1():
        AddX(400000)
        AddScale(400)
    sprite('vr_nt440_06', 3)
    Visibility(1)
    CreateObject('ntef_440Last', -1)

    def RunOnObject_1():
        AddX(600000)
        AddScaleX(1200)
        AddScaleY(0)
    CreateParticle('ntef_611_end', 0)
    CreateParticle('ntef_611_end', 1)
    CreateParticle('ntef_611_end', 2)
    CreateParticle('ntef_611_end', 3)
    CreateParticle('ntef_611_end', 4)


@State
def ntef_440Last():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef_cmnblood00', '')
        Size(1000)
    sprite('null', 23)


@State
def ntef_440LastEx():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Flip()
        LinkParticle('tef_431_ground_00')
        Size(1200)
        AddX(-400000)
        AddY(100000)
    sprite('null', 40)
    ScreenShake(40000, 40000)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        AddX(200000)
    sprite('null', 32767)


@State
def ntef_451aura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef451_aura00', '')
        IgnoreScreenfreeze(1)
        Size(300)
    sprite('null', 24)
    SetScaleSpeed(65)


@State
def ntef_451():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('vr_nt451_02', 5)
    sprite('vr_nt451_02', 5)
    ConstantAlphaModifier(-51)
    CreateParticle('tef_451_tame00', 0)
    CreateParticle('tef_451_tame00', 1)
    CreateParticle('tef_451_tame00', 2)
    CreateParticle('tef_451_tame00', 3)
    CreateParticle('tef_451_tame00', 4)
    CreateParticle('tef_451_tame00', 5)
    CreateParticle('tef_451_tame00', 6)
    ExitState()


@State
def ntef_451_hit():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('vr_nt451_02', 15)
    sprite('vr_nt451_02', 10)
    ConstantAlphaModifier(-25)
    CreateParticle('tef_451_tame00', 0)
    CreateParticle('tef_451_tame00', 1)
    CreateParticle('tef_451_tame00', 2)
    CreateParticle('tef_451_tame00', 3)
    CreateParticle('tef_451_tame00', 4)
    CreateParticle('tef_451_tame00', 5)
    CreateParticle('tef_451_tame00', 6)


@State
def ntef_451_2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 3)
        uponSendToLabel(34, 10)
    sprite('vr_nt451_04', 2)
    label(0)
    sprite('vr_nt451_05', 2)
    CreateParticle('tef_451_tame00', 0)
    CreateParticle('tef_451_tame00', 1)
    CreateParticle('tef_451_tame00', 2)
    CreateParticle('tef_451_tame00', 3)
    CreateParticle('tef_451_tame00', 4)
    CreateParticle('tef_451_tame00', 5)
    CreateParticle('tef_451_tame00', 6)
    ScreenShake(2000, 2000)
    sprite('vr_nt451_05a', 2)
    sprite('vr_nt451_05b', 2)
    sprite('vr_nt451_05c', 2)
    sprite('vr_nt451_05d', 2)
    sprite('vr_nt451_05e', 2)
    gotoLabel(0)
    label(10)
    sprite('null', 32767)
    label(1)
    sprite('vr_nt451_28', 3)
    CreateObject('ntef_451slash_kyushu', 0)
    RenderLayer(11)
    label(2)
    sprite('vr_nt451_29', 3)
    sprite('vr_nt451_28', 3)
    gotoLabel(2)
    label(3)
    sprite('vr_nt451_31', 15)
    RenderLayer(0)
    CreateObject('ntef_451slash3', 0)
    sprite('vr_nt451_32', 3)
    sprite('vr_nt451_33', 3)
    sprite('vr_nt451_34', 3)


@State
def ntef_451slash():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        Eff3DEffect('ntef451_slash00', '')
        Size(1400)
    sprite('null', 21)


@State
def ntef_451slash2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        Eff3DEffect('ntef451_slash01', '')
        Size(1400)
    sprite('null', 21)


@State
def ntef_451slash3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        Eff3DEffect('ntef451_slash02', '')
        Size(1300)
        AddX(-150000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    ScreenShake(15000, 20000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    ScreenShake(20000, 20000)
    sprite('null', 2)


@State
def ntef_451SubMato():

    def upon_IMMEDIATE():
        Visibility(1)
        Flip()
        AddX(-600000)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 0)

    def RunOnObject_1():
        AddScale(600)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 2)

    def RunOnObject_1():
        AddScale(600)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 3)

    def RunOnObject_1():
        AddScale(600)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddScale(600)
    sprite('null', 6)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 0)

    def RunOnObject_1():
        AddScale(600)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 2)

    def RunOnObject_1():
        AddScale(600)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 3)

    def RunOnObject_1():
        AddScale(600)
    sprite('nt431_23', 4)
    CreateObject('ntef_431OdLastSub', 1)

    def RunOnObject_1():
        AddScale(600)


@State
def ntef_451slash_kyushu():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1000)
        PerAngleSpeed(20)
        LinkParticle('tef_451_core')
        uponSendToLabel(32, 1)
    sprite('null', 1)
    CreateObject('ntef_451slash_kyushuSub', -1)
    TriggerUponForState('ntef_451_BG', 32)
    label(0)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    PrivateSE('ntse_09')
    sprite('null', 4)
    AddScale(50)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def ntef_451slash_kyushuSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef451_kyushu', '')
        Size(1200)
        PerAngleSpeed(20)
    sprite('null', 19)


@State
def ntef_451_BG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('tef_451_bg')
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ntef_611():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AddX(150000)
        AddY(300000)
    sprite('vr_nt611_00', 4)
    SetScaleSpeed(5)
    physicsXImpulse(1400)
    physicsYImpulse(1000)
    sprite('vr_nt611_01', 3)
    sprite('vr_nt611_02', 3)
    sprite('vr_nt611_03', 4)
    sprite('vr_nt611_04', 4)
    sprite('vr_nt611_05', 4)
    CreateParticle('ntef_611_end', 0)
    CreateParticle('ntef_611_end', 1)
    CreateParticle('ntef_611_end', 2)
    CreateParticle('ntef_611_end', 3)
    CreateParticle('ntef_611_end', 4)
    CreateParticle('ntef_611_end', 5)
    CreateParticle('ntef_611_end', 6)
    CreateParticle('ntef_611_end', 7)
    CreateParticle('ntef_611_end', 8)
    CreateParticle('ntef_611_end', 9)
    CreateParticle('ntef_611_end', 10)
    CreateParticle('ntef_611_end', 11)
    sprite('vr_nt611_06', 3)
    sprite('vr_nt611_07', 3)
    ConstantAlphaModifier(-26)
    sprite('vr_nt611_08', 3)


@State
def ntef_OverDrive():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ntef333_syuyaku00', '')
        RandAddRotation(-100000, 100000)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
    sprite('null', 10)
    SetScaleSpeed(75)
    ConstantAlphaModifier(-13)
    sprite('null', 10)


@State
def ntef_D_bodyaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        LinkParticle('ntef_D_bodyaura')
        uponSendToLabel(32, 0)
    sprite('null', 8)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    sprite('null', 32767)
    label(0)
    sprite('null', 25)
    ConstantAlphaModifier(-10)


@State
def ntef_D_handaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
    label(1)
    sprite('null', 9)
    CreateObject('ntef_D_handaura_1', -1)
    PrivateSE('ntse_01')
    gotoLabel(1)
    label(0)
    sprite('null', 0)
    DeleteObject(23)


@State
def ntef_D_handaura_1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        RemoveOnContact(2)
        LinkParticle('ntef_D_handaura')
    sprite('null', 30)


@State
def ntef_D_handaura_3D():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
    label(1)
    sprite('null', 6)
    CreateObject('ntef_D_handaura_3D_1', -1)
    gotoLabel(1)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-25)
    IgnorePauses(0)


@State
def ntef_D_handaura_3D_1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Eff3DEffect('ntef_D_charge.DIG', '')
        IgnorePauses(3)
        RemoveOnContact(2)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        RandRotationAngle()
        RenderLayer(11)
        Size(1250)
    sprite('null', 15)


@Subroutine
def BloodEdge():
    AlphaIsColorOnPalette(208, 255)
    AlphaIsColorOnPalette(209, 15)
    AlphaIsColorOnPalette(210, 23)
    AlphaIsColorOnPalette(211, 31)
    AlphaIsColorOnPalette(212, 39)
    AlphaIsColorOnPalette(213, 47)
    AlphaIsColorOnPalette(214, 55)
    AlphaIsColorOnPalette(215, 63)
    AlphaIsColorOnPalette(216, 71)
    AlphaIsColorOnPalette(217, 79)
    AlphaIsColorOnPalette(218, 87)
    AlphaIsColorOnPalette(219, 95)
    AlphaIsColorOnPalette(220, 103)
    AlphaIsColorOnPalette(221, 111)
    AlphaIsColorOnPalette(222, 119)
    AlphaIsColorOnPalette(223, 127)
    AlphaIsColorOnPalette(224, 135)
    AlphaIsColorOnPalette(225, 143)
    AlphaIsColorOnPalette(226, 151)
    AlphaIsColorOnPalette(227, 159)
    AlphaIsColorOnPalette(228, 167)
    AlphaIsColorOnPalette(229, 175)
    AlphaIsColorOnPalette(230, 183)
    AlphaIsColorOnPalette(231, 191)
    AlphaIsColorOnPalette(232, 199)
    AlphaIsColorOnPalette(233, 207)
    AlphaIsColorOnPalette(234, 215)
    AlphaIsColorOnPalette(235, 223)
    AlphaIsColorOnPalette(236, 231)
    AlphaIsColorOnPalette(237, 239)
    AlphaIsColorOnPalette(238, 247)
    AlphaIsColorOnPalette(239, 255)
    AlphaIsColorOnPalette(240, 255)
    AlphaIsColorOnPalette(241, 255)
    AlphaIsColorOnPalette(242, 255)
    AlphaIsColorOnPalette(243, 255)
    AlphaIsColorOnPalette(244, 255)
    AlphaIsColorOnPalette(254, 127)


@State
def MaskTexture():

    def upon_IMMEDIATE():
        ArakuneSpriteOverlay('vrntef000_00', 16, 0, 128000, 0, 2000, 
            2147483647, 1000, 500)
        PaletteIndex(1)
        BlendMode_Add()
        AddY(192000)
    sprite('vr_nt203_20', 300)


@Subroutine
def BloodEdge_Particle():
    CreateParticle('ntef_test', 0)
    CreateParticle('ntef_test', 1)
    CreateParticle('ntef_test', 2)
    CreateParticle('ntef_test', 3)
    CreateParticle('ntef_test', 4)
    CreateParticle('ntef_test', 5)


@State
def ntef_looptest():

    def upon_IMMEDIATE():
        FaceSpawnLocation()
        BlendMode_Normal()
        AddY(256000)
        AddX(256000)
    sprite('null', 1)
    FaceLeft()
    Eff3DEffect('ntef_looptest.DIG', '')
    sprite('null', 31)
    Eff3DEffect('ntef_looptest.DIG', '')
    sprite('null', 1)
    Eff3DEffect('ntef_looptest.DIG', '')
    sprite('null', 32)
    Eff3DEffect('ntef_looptest.DIG', '')


@State
def ntef_253_a():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
    sprite('vr_nt253_20', 3)
    sprite('vr_nt253_21', 3)


@State
def ntef_253_b():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
    sprite('vr_nt253_40', 3)
    sprite('vr_nt253_41', 3)


@State
def ntef_610():

    def upon_IMMEDIATE():
        FaceLeft()
        TeleportToObject(22)
        AbsoluteY(150000)
    sprite('null', 1)
    if CharacterIDCheck('rg'):
        pass
    if CharacterIDCheck('jn'):
        pass
    if CharacterIDCheck('no'):
        pass
    if CharacterIDCheck('rc'):
        pass
    if CharacterIDCheck('tk'):
        pass
    if CharacterIDCheck('tg'):
        AddY(50000)
    if CharacterIDCheck('lc'):
        pass
    if CharacterIDCheck('ar'):
        pass
    if CharacterIDCheck('bn'):
        pass
    if CharacterIDCheck('ca'):
        pass
    if CharacterIDCheck('ha'):
        pass
    if CharacterIDCheck('ny'):
        pass
    if CharacterIDCheck('tb'):
        pass
    if CharacterIDCheck('hz'):
        pass
    if CharacterIDCheck('mu'):
        pass
    if CharacterIDCheck('mk'):
        pass
    if CharacterIDCheck('vh'):
        pass
    if CharacterIDCheck('pt'):
        pass
    if CharacterIDCheck('rl'):
        pass
    if CharacterIDCheck('iz'):
        pass
    if CharacterIDCheck('am'):
        pass
    if CharacterIDCheck('bl'):
        pass
    if CharacterIDCheck('az'):
        pass
    if CharacterIDCheck('kg'):
        pass
    if CharacterIDCheck('kk'):
        pass
    if CharacterIDCheck('tm'):
        pass
    if CharacterIDCheck('ce'):
        pass
    if CharacterIDCheck('rm'):
        pass
    if CharacterIDCheck('hb'):
        pass
    if CharacterIDCheck('ph'):
        pass
    if CharacterIDCheck('nt'):
        pass
    if CharacterIDCheck('mi'):
        pass
    if random_(2, 0, 50):
        conditionalSendToLabel(1)
    sprite('null', 1)
    CreateObject('ntef_610_a', -1)
    loopRest()
    label(1)
    sprite('null', 32767)
    CreateObject('ntef_610_b', -1)
    loopRest()


@State
def ntef_610_a():
    sprite('null', 1)
    CreateParticle('ntef_610_smoke', -1)
    AddX(40000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 35)


@State
def ntef_610_b():
    sprite('null', 1)
    CreateParticle('ntef_610_smoke', -1)
    AddX(40000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 36)


@State
def ntef_601():

    def upon_IMMEDIATE():
        FaceLeft()
        TeleportToObject(22)
        AbsoluteY(475000)
    sprite('null', 1)
    CreateObject('ntef_601_bg', -1)
    if CharacterIDCheck('rg'):
        CreateObject('ntef_601_rg', -1)
    if CharacterIDCheck('jn'):
        CreateObject('ntef_601_jn', -1)
    if CharacterIDCheck('no'):
        CreateObject('ntef_601_no', -1)
    if CharacterIDCheck('rc'):
        CreateObject('ntef_601_rc', -1)
    if CharacterIDCheck('tk'):
        CreateObject('ntef_601_tk', -1)
    if CharacterIDCheck('tg'):
        AddY(60000)
        CreateObject('ntef_601_tg', -1)
    if CharacterIDCheck('lc'):
        CreateObject('ntef_601_lc', -1)
    if CharacterIDCheck('ar'):
        CreateObject('ntef_601_ar', -1)
    if CharacterIDCheck('bn'):
        CreateObject('ntef_601_bn', -1)
    if CharacterIDCheck('ca'):
        CreateObject('ntef_601_ca', -1)
    if CharacterIDCheck('ha'):
        CreateObject('ntef_601_ha', -1)
    if CharacterIDCheck('ny'):
        CreateObject('ntef_601_ny', -1)
    if CharacterIDCheck('tb'):
        CreateObject('ntef_601_tb', -1)
    if CharacterIDCheck('hz'):
        CreateObject('ntef_601_hz', -1)
    if CharacterIDCheck('mu'):
        CreateObject('ntef_601_mu', -1)
    if CharacterIDCheck('mk'):
        CreateObject('ntef_601_mk', -1)
    if CharacterIDCheck('vh'):
        CreateObject('ntef_601_vh', -1)
    if CharacterIDCheck('pt'):
        CreateObject('ntef_601_pt', -1)
    if CharacterIDCheck('rl'):
        CreateObject('ntef_601_rl', -1)
    if CharacterIDCheck('iz'):
        CreateObject('ntef_601_iz', -1)
    if CharacterIDCheck('am'):
        CreateObject('ntef_601_am', -1)
    if CharacterIDCheck('bl'):
        CreateObject('ntef_601_bl', -1)
    if CharacterIDCheck('az'):
        CreateObject('ntef_601_az', -1)
    if CharacterIDCheck('kg'):
        CreateObject('ntef_601_kg', -1)
    if CharacterIDCheck('kk'):
        CreateObject('ntef_601_kk', -1)
    if CharacterIDCheck('tm'):
        CreateObject('ntef_601_tm', -1)
    if CharacterIDCheck('ce'):
        CreateObject('ntef_601_ce', -1)
    if CharacterIDCheck('rm'):
        CreateObject('ntef_601_rm', -1)
    if CharacterIDCheck('hb'):
        CreateObject('ntef_601_hb', -1)
    if CharacterIDCheck('ph'):
        CreateObject('ntef_601_ph', -1)
    if CharacterIDCheck('nt'):
        CreateObject('ntef_601_nt', -1)
    if CharacterIDCheck('mi'):
        CreateObject('ntef_601_mi', -1)
    if CharacterIDCheck('su'):
        AddY(30000)
        CreateObject('ntef_601_su', -1)
    if CharacterIDCheck('es'):
        AddY(-70000)
        CreateObject('ntef_601_es', -1)
    if CharacterIDCheck('ma'):
        AddY(-10000)
        CreateObject('ntef_601_ma', -1)
    if CharacterIDCheck('jb'):
        AddY(-75000)
        CreateObject('ntef_601_jb', -1)
    label(99)


@State
def ntef_601_bg():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        CallPrivateEffect('ntef_601_black')
    sprite('null', 40)
    AlphaValue(0)
    ConstantAlphaModifier(3)

    def RunOnObject_22():
        ColorTransition(4294934399, 30)
    sprite('null', 5)
    ConstantAlphaModifier(0)
    sprite('null', 25)

    def RunOnObject_22():
        ColorTransition(4294967295, 30)
    sprite('null', 30)
    sprite('null', 40)
    ConstantAlphaModifier(-3)


@State
def ntef_601dist():

    def upon_EVERY_FRAME():
        RenderLayer(9)
        E0EAEffectPosition(2)
        ParticleTransparency(1)
        PlayerTransparency(10000)
        Unknown3059(-1000)
    sprite('vr_nt601_dist', 64)
    RandRotationAngle()
    SetScaleY(500)
    SetScaleX(500)
    SetScaleSpeedY(5)
    SetScaleXPerFrame(5)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('vr_nt601_dist', 64)
    ConstantAlphaModifier(-4)


@State
def ntef_Number_bloom():
    sprite('null', 32)
    CallPrivateEffect('ntef_601_bloom')
    Size(500)
    SetScaleSpeed(5)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('null', 64)
    ConstantAlphaModifier(-2)


@State
def ntef_Number():

    def upon_IMMEDIATE():
        FaceLeft()
        PaletteIndex(3)
        BlendMode_Add()
        RenderLayer(10)
        AlphaValue(0)
        AddScaleX(-100)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
        uponSendToLabel(37, 5)
        uponSendToLabel(38, 6)
        uponSendToLabel(39, 7)
        uponSendToLabel(40, 8)
        uponSendToLabel(41, 9)
    label(0)
    sprite('vr_nt601_number0', 0)
    gotoLabel(100)
    label(1)
    sprite('vr_nt601_number1', 0)
    gotoLabel(100)
    label(2)
    sprite('vr_nt601_number2', 0)
    gotoLabel(100)
    label(3)
    sprite('vr_nt601_number3', 0)
    gotoLabel(100)
    label(4)
    sprite('vr_nt601_number4', 0)
    gotoLabel(100)
    label(5)
    sprite('vr_nt601_number5', 0)
    gotoLabel(100)
    label(6)
    sprite('vr_nt601_number6', 0)
    gotoLabel(100)
    label(7)
    sprite('vr_nt601_number7', 0)
    gotoLabel(100)
    label(8)
    sprite('vr_nt601_number8', 0)
    gotoLabel(100)
    label(9)
    sprite('vr_nt601_number9', 0)
    gotoLabel(100)
    label(100)
    sprite('keep', 32)
    ConstantAlphaModifier(8)
    RandAddScale(-500, -400)
    SetScaleSpeed(5)
    RandAddRotation(-6000, 6000)
    ParticleSize(800)
    CallCustomizableParticle('ntef_number_smoke01', -1)
    sprite('keep', 30)
    SetScaleSpeed(2)
    CreateObject('ntef_601dist', -1)

    def RunOnObject_1():
        RandRotationAngle()
    sprite('keep', 64)
    ConstantBlueModifier(-8)
    ConstantGreenModifier(-8)
    ConstantAlphaModifier(-4)


@State
def ntef_601_rg():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-120000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-160000)
    ObjectUpon(STATE_END, 35)


@State
def ntef_601_jn():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-120000)
    ObjectUpon(STATE_END, 39)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-160000)
    ObjectUpon(STATE_END, 41)


@State
def ntef_601_no():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-120000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-160000)
    ObjectUpon(STATE_END, 37)


@State
def ntef_601_rc():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-120000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-160000)
    ObjectUpon(STATE_END, 38)


@State
def ntef_601_tk():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-120000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_tg():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-40000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-80000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-120000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(-160000)
    ObjectUpon(STATE_END, 32)


@State
def ntef_601_lc():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 40)


@State
def ntef_601_ar():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 39)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 32)


@State
def ntef_601_bn():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_ca():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 41)


@State
def ntef_601_ha():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 38)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 35)


@State
def ntef_601_ny():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 32)


@State
def ntef_601_tb():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_hz():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 36)


@State
def ntef_601_mu():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 39)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 37)


@State
def ntef_601_mk():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 38)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 34)


@State
def ntef_601_vh():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 41)


@State
def ntef_601_pt():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 41)


@State
def ntef_601_rl():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 33)


@State
def ntef_601_iz():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_am():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 40)


@State
def ntef_601_bl():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 40)


@State
def ntef_601_az():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 38)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 35)


@State
def ntef_601_kg():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 32)


@State
def ntef_601_kk():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 39)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_tm():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 39)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 36)


@State
def ntef_601_ce():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 33)


@State
def ntef_601_rm():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 32)


@State
def ntef_601_hb():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 41)


@State
def ntef_601_nt():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 37)


@State
def ntef_601_ph():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 36)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_mi():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 32)


@State
def ntef_601_su():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 41)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 36)


@State
def ntef_601_es():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 34)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 35)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 39)


@State
def ntef_601_ma():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 38)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 37)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 35)


@State
def ntef_601_jb():
    sprite('null', 1)
    CreateObject('ntef_Number_bloom', -1)
    AddX(-80000)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(0)
    ObjectUpon(STATE_END, 40)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(40000)
    ObjectUpon(STATE_END, 39)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(80000)
    ObjectUpon(STATE_END, 32)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(120000)
    ObjectUpon(STATE_END, 33)
    CreateObject('ntef_Number', -1)

    def RunOnObject_1():
        AddX(160000)
    ObjectUpon(STATE_END, 33)


@State
def Fade1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(0)
        AlphaValue(160)
        AbsoluteY(3000)
        SetZVal(-500)
        BlendMode_Normal()
    sprite('nt000_00', 15)
    ConstantAlphaModifier(-9)
    SetScaleSpeed(50)
    physicsYImpulse(-12000)
    ScreenShake(5000, 1000)
    PrivateSE('ntse_13')
    PrivateSE('ntse_13')
    PrivateSE('ntse_13')
    CreateObject('LifeLinkEff', 0)
    sprite('nt000_00', 20)
    SetScaleSpeed(-130)
    physicsYImpulse(12000)
    sprite('nt000_00', 2)
    Size(0)
    physicsYImpulse(0)


@State
def Fade2():

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
def LifeLinkEff():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 1)
    CallCustomizableParticle('ntef_story_lifelinkeff', -1)


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
        uponSendToLabel(32, 0)
    sprite('vr_white', 20)
    ConstantAlphaModifier(12)
    sprite('vr_white', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    CreateObject('Act3Event_mivsnt_eff_sl', -1)
    label(0)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-8)
    sprite('vr_white', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)


@State
def Act3Event_mivsnt_eff_sl():

    def upon_IMMEDIATE():
        AbsoluteY(185000)
    sprite('null', 1)
    ParticleRandomRotation()
    ParticleLayer(1)
    ParticleSize(1500)
    CallCustomizableParticle('ef_hitlz', 103)
    CommonSE('101_hit_slash_3')


@State
def Act3Event_mivsnt_01():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-260000)
        AddX(100000)
        LoadSpritePalette(0)
        SetZVal(-500)
    sprite('rl860_10', 32767)
    loopRest()


@State
def Act3Event_mivsnt_02_rl():

    def upon_IMMEDIATE():
        XPositionRelativeFacing(-260000)
        LoadSpritePalette(0)
        SetZVal(-501)
    sprite('rl000_00', 8)
    sprite('rl000_01', 8)
    sprite('rl000_02', 8)
    sprite('rl000_03', 8)
    sprite('rl000_04', 8)
    sprite('rl000_05', 8)
    sprite('rl000_06', 8)
    sprite('rl000_07', 8)
    label(0)
    sprite('rl000_00', 8)
    sprite('rl000_01', 8)
    sprite('rl000_02', 8)
    sprite('rl000_03', 8)
    sprite('rl000_04', 8)
    sprite('rl000_05', 8)
    sprite('rl000_06', 8)
    sprite('rl000_07', 8)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_mivsnt_02_camera():

    def upon_IMMEDIATE():
        ScreenCollision(0)
        TeleportToObject(22)
        Flip()
        AddX(-260000)
    sprite('null', 15)
    sprite('null', 32767)
    CameraControlEnable(1)
    TriggerUponForState('Act3Event_mivsnt_02_rl', 32)


@State
def Act3Event_rcef_252Wind():
    sprite('null', 100)
    Wind(80, -350, 0)
    CreateParticle('rcef_252up_mc02', -1)
