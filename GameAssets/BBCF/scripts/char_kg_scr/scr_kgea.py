@State
def EMB_KG():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_KG.DIG', '')
        RenderLayer(5)
        Size(1400)
        AddY(16000)
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
def EMB_KG_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_KG.DIG', '')
        RenderLayer(5)
        Size(1400)
        AddY(16000)
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
def EMB_KG_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_KG.DIG', '')
        RenderLayer(5)
        Size(1400)
        AddY(16000)
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
def EntrySword():

    def upon_IMMEDIATE():
        SetZVal(500)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)

        def upon_41():
            Visibility(1)
    label(0)
    sprite('kg600_08s', 2)
    gotoLabel(0)
    label(1)
    sprite('kg600_09s', 3)
    Visibility(0)
    physicsYImpulse(40000)
    EndYPhysicsImpulse()
    label(2)
    sprite('kg600_10s', 3)
    sprite('kg600_11s', 3)
    sprite('kg600_12s', 3)
    sprite('kg600_13s', 3)
    loopRest()
    gotoLabel(2)


@State
def EntryKaguraGirl():

    def upon_IMMEDIATE():
        AddX(65000)
        AddY(100000)
        physicsYImpulse(70000)
        EndYPhysicsImpulse()
        uponSendToLabel(32, 110)
        uponSendToLabel(33, 120)
        uponSendToLabel(34, 130)
        uponSendToLabel(35, 140)
    sprite('null', 1)
    label(110)
    sprite('kg601girl_a05', 30)
    ExitState()
    label(120)
    sprite('kg601girl_b05', 30)
    ExitState()
    label(130)
    sprite('kg601girl_c05', 30)
    ExitState()
    label(140)
    sprite('kg601girl_d05', 30)
    ExitState()


@State
def MatchWinKaguraGirl():

    def upon_IMMEDIATE():
        AddY(650000)
        physicsYImpulse(-10000)
        EndYPhysicsImpulse()
        uponSendToLabel(32, 110)
        uponSendToLabel(33, 120)
        uponSendToLabel(34, 130)
        uponSendToLabel(35, 140)
        uponSendToLabel(41, 150)
    sprite('null', 1)
    label(110)
    sprite('kg611girl_a00', 3)
    sprite('kg611girl_a01', 3)
    gotoLabel(110)
    label(120)
    sprite('kg611girl_b00', 3)
    sprite('kg611girl_b01', 3)
    gotoLabel(120)
    label(130)
    sprite('kg611girl_c00', 3)
    sprite('kg611girl_c01', 3)
    gotoLabel(130)
    label(140)
    sprite('kg611girl_d00', 3)
    sprite('kg611girl_d01', 3)
    gotoLabel(140)
    label(150)
    sprite('null', 1)
    ExitState()


@State
def LoseKaguraGirl():

    def upon_IMMEDIATE():
        Unknown4022(3)
        PaletteIndex(4)
        AddY(650000)
        physicsYImpulse(-30000)
        Flip()
        AddX(30000)
        uponSendToLabel(32, 110)
        uponSendToLabel(33, 120)
        uponSendToLabel(34, 130)
        uponSendToLabel(35, 140)
        uponSendToLabel(41, 150)
    sprite('null', 1)
    label(110)
    uponSendToLabel(LANDING, 115)
    label(111)
    sprite('kg611girl_a00', 3)
    sprite('kg611girl_a01', 3)
    gotoLabel(111)
    label(120)
    uponSendToLabel(LANDING, 125)
    label(121)
    sprite('kg611girl_b00', 3)
    sprite('kg611girl_b01', 3)
    gotoLabel(121)
    label(130)
    uponSendToLabel(LANDING, 135)
    label(131)
    sprite('kg611girl_c00', 3)
    sprite('kg611girl_c01', 3)
    gotoLabel(131)
    label(140)
    uponSendToLabel(LANDING, 145)
    label(141)
    sprite('kg611girl_d00', 3)
    sprite('kg611girl_d01', 3)
    gotoLabel(141)
    label(115)
    sprite('kg611girl_a00', 3)
    ObjectUpon(EVERY_FRAME, 32)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    EndMomentum(1)
    physicsYImpulse(25000)
    EndYPhysicsImpulse()
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 118)
    sprite('kg611girl_a01', 3)
    gotoLabel(111)
    label(125)
    sprite('kg611girl_b00', 3)
    ObjectUpon(EVERY_FRAME, 32)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    EndMomentum(1)
    physicsYImpulse(25000)
    EndYPhysicsImpulse()
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 128)
    sprite('kg611girl_b01', 3)
    gotoLabel(121)
    label(135)
    sprite('kg611girl_c00', 3)
    ObjectUpon(EVERY_FRAME, 32)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    EndMomentum(1)
    physicsYImpulse(25000)
    EndYPhysicsImpulse()
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 138)
    sprite('kg611girl_c01', 3)
    gotoLabel(131)
    label(145)
    sprite('kg611girl_d00', 3)
    ObjectUpon(EVERY_FRAME, 32)
    ParticleSize(1200)
    CallCustomizableParticle('ef_hitmd', 108)
    CommonSE('100_hit_grap_0')
    EndMomentum(1)
    physicsYImpulse(25000)
    EndYPhysicsImpulse()
    clearUponHandler(LANDING)
    uponSendToLabel(LANDING, 148)
    sprite('kg611girl_d01', 3)
    gotoLabel(141)
    label(118)
    sprite('kg611girl_a09', 6)
    EndMomentum(1)
    sprite('kg611girl_a10', 32767)
    CreateParticle('kgef_lose', 0)
    label(128)
    sprite('kg611girl_b09', 6)
    EndMomentum(1)
    sprite('kg611girl_b10', 32767)
    CreateParticle('kgef_lose', 0)
    label(138)
    sprite('kg611girl_c09', 6)
    EndMomentum(1)
    sprite('kg611girl_c10', 32767)
    CreateParticle('kgef_lose', 0)
    label(148)
    sprite('kg611girl_d09', 6)
    EndMomentum(1)
    sprite('kg611girl_d10', 32767)
    CreateParticle('kgef_lose', 0)


@State
def TimeUpSword():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    sprite('kg620_05s', 10)
    ScreenShake(0, 15000)
    AltKnockdownEffects(100, 1, 1)
    sprite('kg620_05s', 32767)


@State
def efkg_203():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        AddY(300000)
        AddX(-50000)
    sprite('null', 5)
    Eff3DEffect('kgef203_kira', '')
    FaceSpawnLocation()
    sprite('null', 2)
    PrivateSE('kgse_02')
    sprite('null', 7)
    ParticleSize(400)
    CallCustomizableParticle('kgef_kamaekira_pos01', -1)


@State
def efkg_213():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        AddY(300000)
        AddX(-50000)
    sprite('null', 5)
    Eff3DEffect('kgef213_kira', '')
    FaceSpawnLocation()
    sprite('null', 3)
    PrivateSE('kgse_02')
    sprite('null', 4)
    ParticleSize(500)
    CallCustomizableParticle('kgef_kamaekira_pos00', -1)


@State
def efkg_233():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        AddY(320000)
        AddX(-48000)
    sprite('null', 5)
    Eff3DEffect('kgef233_kira', '')
    FaceSpawnLocation()
    sprite('null', 7)
    PrivateSE('kgse_02')


@State
def efkg_253():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        AddY(330000)
        AddX(-30000)
    sprite('null', 5)
    Eff3DEffect('kgef253_kira', '')
    FaceSpawnLocation()
    sprite('null', 2)
    PrivateSE('kgse_02')
    sprite('null', 7)
    ParticleSize(400)
    CallCustomizableParticle('kgef_kamaekira_pos02', -1)


@State
def efkg_254():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        AddY(350000)
        AddX(-90000)
    sprite('null', 5)
    Eff3DEffect('kgef254_kira', '')
    FaceSpawnLocation()
    sprite('null', 2)
    PrivateSE('kgse_02')
    sprite('null', 7)
    ParticleSize(400)
    CallCustomizableParticle('kgef_kamaekira_pos02', -1)


@State
def efkg_255():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        AddY(330000)
        AddX(-40000)
    sprite('null', 5)
    Eff3DEffect('kgef255_kira', '')
    FaceSpawnLocation()
    sprite('null', 3)
    PrivateSE('kgse_02')
    sprite('null', 4)
    ParticleSize(500)
    CallCustomizableParticle('kgef_kamaekira_pos00', -1)


@State
def efkg_202():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef202_00', 3)
    sprite('vrkgef202_01', 120)


@State
def efkg_212():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef212_00', 3)
    sprite('vrkgef212_01', 120)


@State
def efkg_232():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef232_00', 2)
    sprite('vrkgef232_01', 2)
    sprite('vrkgef232_02', 120)


@State
def efkg_232_test():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        TurnParticleColorable1(1)
        BlendMode_Normal()
        PaletteIndex(0)
        PaletteEffType(1)
        PaletteColor1(16)
        PaletteColor2(50)
        PaletteColor3(50)
        PaletteColor4(2147483898)
    sprite('vrkgef232_00', 4)
    sprite('vrkgef232_01', 120)


@State
def efkg_232_test_2():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        BlendMode_Add()
        GreenColorValue(0)
        BlueColorValue(0)
        SetZVal(-500)
    sprite('vrkgef232_00b', 16)
    ConstantAlphaModifier(-16)


@State
def efkg_235():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef235_00', 3)
    sprite('vrkgef235_01', 120)
    E0EAEffectPosition(0)


@State
def efkg_252():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef252_00', 3)
    sprite('vrkgef252_01', 3)


@State
def efkg_311():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef311_00', 3)
    sprite('vrkgef311_01', 3)
    sprite('vrkgef311_02', 120)


@State
def efkg_340():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(0)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(36)
        PaletteColor1(36)
        PaletteColor3(255)
        PaletteColor4(1)
        AlphaValue(127)
    sprite('vrkgef340_01', 2)
    sprite('vrkgef340_02', 2)
    sprite('vrkgef340_03', 120)


@State
def efkg_411():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Normal()
        AlphaValue(200)
        PaletteIndex(1)
        Eff3DEffect('kgef411_grd', '')
        FaceSpawnLocation()
    sprite('vrkgef411_01', 3)
    CreateParticle('kgef411_smoke', 0)
    CreateParticle('kgef411_smoke', 1)
    sprite('vrkgef411_02', 4)
    CreateParticle('kgef411_smoke', 1)
    CreateParticle('kgef411_smoke', 3)
    CreateParticle('kgef411_smoke', 4)
    sprite('vrkgef411_03', 4)
    E0EAEffectPosition(0)
    CreateParticle('kgef411_smoke', 1)
    sprite('vrkgef411_04', 4)
    CreateParticle('kgef411_smoke', 0)


@State
def efkg_411_splash():

    def upon_IMMEDIATE():
        Flip()
        Eff3DEffect('kgef411_splash', '')
        FaceSpawnLocation()
        BlendMode_Add()
    sprite('null', 13)


@State
def efkg_411Sub00():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Normal()
        AlphaValue(255)
        Size(600)
        AddY(500000)
        AddX(100000)
        Eff3DEffect('kgef411_special00', '')
        FaceSpawnLocation()
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def efkg_411Sub01():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        BlendMode_Normal()
        LinkParticle('kgef411grsp_00')
    sprite('null', 10)
    CreateParticle('kgef411grsp_hit', -1)
    sprite('null', 20)
    CreateParticle('kgef411grsp_fly', -1)


@State
def efkg_slash():

    def upon_IMMEDIATE():
        pass
    sprite('null', -1)
    CallCustomizableParticle('ef_hitlz', 0)
    CommonSE('101_hit_slash_0')


@State
def __401slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
        Size(800)
        AddY(360000)
        AddX(130000)
    sprite('null', 7)
    Eff3DEffect('kgef401_slash00', '')
    FaceSpawnLocation()
    sprite('null', 7)


@State
def __401slash01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Visibility(1)
    sprite('vrkgef401papos_00', 4)
    sprite('vrkgef401papos_00', 4)
    CallCustomizableParticle('kgefcmnkira_00', 1)
    sprite('vrkgef401papos_00', 4)
    CallCustomizableParticle('kgefcmnkira_00', 2)


@State
def __402slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
    sprite('null', 14)
    CreateObject('402slash02', -1)
    Eff3DEffect('kgef402_slash00', '')
    FaceSpawnLocation()
    sprite('null', 3)
    AlphaValue(0)


@State
def __402slash01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
        PaletteIndex(2)
        AddY(-30000)
        AddX(-75000)
    sprite('vrkgef402_00', 3)
    sprite('vrkgef402_01', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(2)
    AfterimageInterval(1)
    CallCustomizableParticle('kgefcmnkira_00', 1)
    CallCustomizableParticle('kgefcmnkira_00', 3)
    sprite('vrkgef402_02', 3)
    AddX(75000)
    sprite('vrkgef402_03', 3)
    sprite('vrkgef402_04', 3)


@State
def __402slash02():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Visibility(1)
    sprite('vrkgef402papos_00', 3)
    CallCustomizableParticle('kgefcmnkira_00', 0)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)
    CallCustomizableParticle('kgefcmnkira_00', 2)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)
    CallCustomizableParticle('kgefcmnkira_00', 4)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)
    CallCustomizableParticle('kgefcmnkira_00', 6)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)
    CallCustomizableParticle('kgefcmnkira_00', 8)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)
    CallCustomizableParticle('kgefcmnkira_00', 10)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)
    sprite('vrkgef402papos_00', 3)


@State
def __403slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
        AddY(-50000)
    sprite('null', 10)
    CreateObject('403slash01', -1)
    Eff3DEffect('kgef403_slash00', '')
    FaceSpawnLocation()
    sprite('null', 10)
    AlphaValue(0)


@State
def __403Zanzo():

    def upon_IMMEDIATE():
        BlendMode_HalfAdd()
        PaletteIndex(2)
        AddX(-259000)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
    sprite('vrkg403_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 0)
    CallCustomizableParticle('kgefcmnkira_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 7)
    CallCustomizableParticle('kgefcmnkira_00', 9)
    CallCustomizableParticle('kgef403eye_00', 10)
    AlphaValue(100)
    sprite('vrkg403_00', 2)
    CreateObject('Yugami', 0)
    CreateObject('Yugami', 1)
    CreateObject('Yugami', 2)
    CreateObject('Yugami', 3)
    CreateObject('Yugami', 4)
    CreateObject('Yugami', 5)
    CreateObject('Yugami', 6)
    CreateObject('Yugami', 7)
    CreateObject('Yugami', 8)
    CreateObject('Yugami', 9)
    AlphaValue(200)
    sprite('vrkg403_01', 3)
    sprite('vrkg403_02', 3)
    sprite('vrkg403_03', 3)
    sprite('vrkg403_04', 3)
    sprite('vrkg403_05', 3)


@State
def __404slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
        Flip()
        AddY(-100000)
        AddX(200000)
    sprite('null', 10)
    CreateObject('403slash01', -1)
    Eff3DEffect('kgef403_slash00', '')
    FaceSpawnLocation()
    sprite('null', 10)
    AlphaValue(0)


@State
def Yugami():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        ParticleTransparency(1)
        PlayerTransparency(8000)
        SetScaleX(4000)
        SetScaleY(4000)
    sprite('vrdist00', 10)
    RandAddRotation(-90000, 90000)
    sprite('vrdist00', 10)


@State
def __403slash01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        Visibility(1)
    sprite('vrkgef403papos_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 0)
    sprite('vrkgef403papos_00', 2)
    sprite('vrkgef403papos_00', 2)
    sprite('vrkgef403papos_00', 2)
    sprite('vrkgef403papos_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 4)
    sprite('vrkgef403papos_00', 2)


@State
def __405Slash():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(2)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        SetZVal(-100)
        uponSendToLabel(32, 0)
    sprite('null', 4)
    CreateObject('405noko2', -1)
    sprite('vrkgef405_00', 3)
    AlphaValue(150)
    CallCustomizableParticle('kgefcmnkira_01', 0)
    sprite('vrkgef405_01', 3)
    AlphaValue(200)
    label(1)
    sprite('vrkgef405_02', 3)
    CreateObject('405noko', -1)
    IgnorePauses(3)
    sprite('vrkgef405_02', 3)
    CreateObject('405noko', -1)
    CallCustomizableParticle('kgefcmnkira_01', 0)
    sprite('vrkgef405_02', 3)
    CreateObject('405noko', -1)
    gotoLabel(1)
    label(0)
    sprite('vrkgef405_03', 3)
    AddX(80000)
    CreateObject('405noko', -1)
    CallCustomizableParticle('kgefcmnkira_01', 0)
    sprite('vrkgef405_04', 3)
    CreateObject('405noko', -1)
    sprite('vrkgef405_05', 2)


@State
def __405noko():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddY(250000)
        AddX(150000)
        AlphaValue(200)
    sprite('null', 15)
    RandAddScale(0, 1000)
    Eff3DEffect('kgef405_nokori', '')
    FaceSpawnLocation()
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def __405noko2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AddY(250000)
        AddX(150000)
        AlphaValue(200)
    sprite('null', 60)
    Eff3DEffect('kgef405_nokori2', '')
    FaceSpawnLocation()


@State
def __406slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
        Flip()
        IgnoreFinishStop(1)
    sprite('null', 13)
    CreateObject('406slash01', -1)
    CreateObject('406Rock', -1)
    CreateObject('406Rock', -1)

    def RunOnObject_1():
        Flip()
        AddX(-150000)
        Size(700)
    CreateObject('403slash01', -1)
    Eff3DEffect('kgef406_slash00', '')
    FaceSpawnLocation()


@State
def __406Rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddX(-100000)
        AddY(-50000)
        Size(1200)
    sprite('null', 5)
    physicsYImpulse(10000)
    sprite('null', 13)
    EndMomentum(1)
    Eff3DEffect('kgef406_rock00', '')
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    physicsYImpulse(-1500)


@State
def __406slash01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        RemoveOnCallStateEnd(2)
        Flip()
        Visibility(1)
        AddX(-150000)
    sprite('vrkgef406papos_00', 2)
    sprite('vrkgef406papos_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 1)
    sprite('vrkgef406papos_00', 2)
    sprite('vrkgef406papos_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 3)
    sprite('vrkgef406papos_00', 2)
    sprite('vrkgef406papos_00', 2)
    CallCustomizableParticle('kgefcmnkira_00', 5)


@State
def __408slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
    sprite('null', 9)
    CreateObject('408slashparticle00', -1)
    Eff3DEffect('kgef407_slash00', '')
    FaceSpawnLocation()


@State
def __408slashparticle00():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('vrkgef408papos_00', 1)
    CallCustomizableParticle('kgefcmnkira_00', 0)
    sprite('vrkgef408papos_00', 1)
    sprite('vrkgef408papos_00', 1)
    CallCustomizableParticle('kgefcmnkira_00', 2)
    sprite('vrkgef408papos_00', 1)
    sprite('vrkgef408papos_00', 1)
    CallCustomizableParticle('kgefcmnkira_00', 4)
    sprite('vrkgef408papos_00', 1)
    sprite('vrkgef408papos_00', 1)
    CallCustomizableParticle('kgefcmnkira_00', 6)
    sprite('vrkgef408papos_00', 1)


@State
def __408slash01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(200)
        IgnoreFinishStop(1)
    sprite('null', 10)
    CreateObject('408slashparticle01', -1)
    Eff3DEffect('kgef407_slash01', '')
    FaceSpawnLocation()
    CreateObject('406Rock', -1)

    def RunOnObject_1():
        AddX(150000)
        Size(700)
    CreateObject('406Rock', -1)

    def RunOnObject_1():
        Flip()
        AddX(-325000)


@State
def __408slashparticle01():

    def upon_IMMEDIATE():
        Visibility(1)
    sprite('vrkgef408papos_01', 1)
    CallCustomizableParticle('kgefcmnkira_00', 0)
    sprite('vrkgef408papos_01', 1)
    sprite('vrkgef408papos_01', 1)
    CallCustomizableParticle('kgefcmnkira_00', 2)
    sprite('vrkgef408papos_01', 1)
    sprite('vrkgef408papos_01', 1)
    CallCustomizableParticle('kgefcmnkira_00', 4)


@State
def efkg_407():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
    sprite('null', 1)
    CreateParticle('kgef407', -1)


@State
def ShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(700)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(94)
        GroundedHitstunAnimation(9)
        SameMoveProration(10)
        AttackDirection(2)
        Size(800)
        AddX(200000)
        AddY(200000)
        Hitstop(2)
        PushbackX(-7000)
        AirPushbackX(-4000)
        AirPushbackY(15000)
        AirUntechableTime(25)
        UseSlashHitspark(1)
        StarterRating(2)
        PaletteIndex(3)
        LinkParticle('kgef_410core_00')
        CollideWithWall(1)
        uponSendToLabel(PLAYER_DAMAGED, 2)
        RunLoopUpon(17, 70)
        uponSendToLabel(17, 2)
        SetActionMark(4)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)
            XImpulseAcceleration(50)
            if SLOT_2 >= 5:
                sendToLabel(2)
                NoAttackDuringAction(1)
                AttackOff()
                EndAttack()
    sprite('vrkg410_11', 2)
    physicsXImpulse(10000)
    sprite('vrkg410_12', 2)
    PrivateSE('kgse_05')
    sprite('vrkg410_13', 3)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    XImpulseAcceleration(125)
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    XImpulseAcceleration(125)
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    CreateObject('ShotNokosi', -1)
    PrivateSE('kgse_05')
    XImpulseAcceleration(110)
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    XImpulseAcceleration(110)
    sprite('vrkg410_14', 3)
    AddActionMark(-1)
    RefreshMultihit()
    Damage(600)
    XImpulseAcceleration(120)
    AirPushbackX(-3500)
    AirPushbackY(12500)
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    XImpulseAcceleration(120)
    PrivateSE('kgse_05')
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    XImpulseAcceleration(120)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    XImpulseAcceleration(120)
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    sprite('vrkg410_14', 3)
    AddActionMark(-1)
    RefreshMultihit()
    AirPushbackX(-3000)
    AirPushbackY(10000)
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    label(0)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    gotoLabel(0)
    label(2)
    sprite('vrkg410_15', 2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(17)
    XImpulseAcceleration(50)
    sprite('vrkg410_16', 2)
    sprite('vrkg410_17', 2)
    CreateParticle('kgef_410shotend_03', -1)
    DespawnEAEffect('ShotNokosi')
    EndMomentum(1)
    sprite('vrkg410_18', 2)
    sprite('vrkg410_19', 2)
    sprite('vrkg410_20', 2)
    ExitState()
    label(1)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    sprite('vrkg410_14', 3)
    physicsXImpulse(10000)
    sprite('vrkg410_15', 3)
    PrivateSE('kgse_05')
    RefreshMultihit()
    sprite('vrkg410_16', 3)
    gotoLabel(2)


@State
def ChargeShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(650)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(94)
        SameMoveProration(10)
        AttackDirection(4)
        Size(850)
        AirPushbackX(1000)
        AirPushbackY(12000)
        AddX(200000)
        AddY(180000)
        AirUntechableTime(19)
        Hitstop(2)
        PushbackX(-5000)
        UseSlashHitspark(1)
        StarterRating(2)
        PaletteIndex(3)
        LinkParticle('kgef_410core_00')
        CollideWithWall(1)
        uponSendToLabel(PLAYER_DAMAGED, 2)
        RunLoopUpon(17, 130)
        uponSendToLabel(17, 2)
        SetActionMark(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)
            XImpulseAcceleration(50)
            if SLOT_2 >= 5:
                sendToLabel(2)
                NoAttackDuringAction(1)
                AttackOff()
                EndAttack()
            SLOT_51 = 1
    sprite('vrkg410_11', 2)
    SLOT_5 = 0
    physicsXImpulse(4000)
    PrivateSE('kgse_05')
    sprite('vrkg410_12', 2)
    sprite('vrkg410_13', 4)
    sprite('vrkg410_14', 4)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 4)
    RefreshMultihit()
    sprite('vrkg410_16', 4)
    XImpulseAcceleration(125)
    RefreshMultihit()
    sprite('vrkg410_14', 4)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 4)
    RefreshMultihit()
    sprite('vrkg410_16', 4)
    XImpulseAcceleration(160)
    RefreshMultihit()
    sprite('vrkg410_14', 4)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 4)
    RefreshMultihit()
    sprite('vrkg410_16', 4)
    RefreshMultihit()
    XImpulseAcceleration(180)
    Size(850)
    SetScaleSpeed(20)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    sprite('vrkg410_16', 4)
    if not SLOT_51:
        AddActionMark(-2)
        Damage(500)
        if SLOT_137:
            DamageMultiplier(80)
        Size(1050)
        SetScaleSpeed(0)
    SLOT_5 = SLOT_5 + 2
    RefreshMultihit()
    CreateObject('ShotNokosi', -1)
    XImpulseAcceleration(180)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    sprite('vrkg410_16', 4)
    RefreshMultihit()
    XImpulseAcceleration(120)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    sprite('vrkg410_16', 4)
    RefreshMultihit()
    XImpulseAcceleration(120)
    Size(1050)
    SetScaleSpeed(20)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    XImpulseAcceleration(120)
    Size(1450)
    SetScaleSpeed(0)
    AddActionMark(-2)
    Damage(350)
    SLOT_5 = SLOT_5 + 2
    label(0)
    sprite('vrkg410_14', 3)
    RefreshMultihit()
    PrivateSE('kgse_05')
    sprite('vrkg410_15', 3)
    RefreshMultihit()
    sprite('vrkg410_16', 3)
    RefreshMultihit()
    XImpulseAcceleration(80)
    gotoLabel(0)
    label(2)
    sprite('vrkg410_14', 2)
    BlendMode_Add()
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(17)
    DespawnEAEffect('ShotNokosi')
    EndAttack()
    sprite('vrkg410_14', 2)
    sprite('vrkg410_15', 2)
    sprite('vrkg410_16', 2)
    sprite('vrkg410_14', 2)
    sprite('vrkg410_15', 2)
    EndMomentum(1)
    sprite('vrkg410_17', 2)
    CreateParticle('kgef_410shotend_03', -1)
    sprite('vrkg410_18', 2)
    sprite('vrkg410_19', 2)
    sprite('vrkg410_20', 2)


@State
def ShotNokosi():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 5)
    CreateParticle('kgef_410nokosi_01', -1)
    gotoLabel(0)


@State
def ChargeTameFinFast():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(3)
        BlendMode_Normal()
        AlphaValue(255)
        AddY(280000)
        AddX(130000)
    sprite('vrkg410_07', 2)
    CreateParticle('kgef_410tameend_ray', 0)
    sprite('vrkg410_08', 3)
    sprite('vrkg410_09', 3)
    sprite('vrkg410_10', 2)


@State
def ChargeTameFin():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(3)
        BlendMode_Normal()
        AlphaValue(255)
        AddY(280000)
        AddX(130000)
    sprite('vrkg410_04', 1)
    sprite('vrkg410_05', 1)
    sprite('vrkg410_06', 4)
    sprite('vrkg410_07', 4)
    CreateParticle('kgef_410tameend_ray', 0)
    sprite('vrkg410_08', 3)
    sprite('vrkg410_09', 3)
    sprite('vrkg410_10', 2)


@State
def ChargeTameJizoku():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(3)
        BlendMode_Normal()
        AlphaValue(255)
        AddY(280000)
        AddX(130000)
    sprite('vrkg410_00', 3)
    sprite('vrkg410_01', 3)
    ConstantAlphaModifier(-17)
    sprite('vrkg410_02', 3)
    sprite('vrkg410_03', 3)


@State
def ChargeTameAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PrivateSE('kgse_04')
        LinkParticle('kgef_410tame_05')
        AddY(460000)
        AddX(50000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def UltimateShotMaster():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
        if SLOT_19 < 300000:
            CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
        else:
            AddX(300000)
    sprite('null', 13)
    CreateObject('UltimateShotObj', -1)

    def RunOnObject_1():
        Size(700)
    sprite('null', 13)
    CreateObject('UltimateShotObj', -1)

    def RunOnObject_1():
        Size(1000)
        AddX(200000)
    sprite('null', 30)
    CreateObject('UltimateShotObj', -1)

    def RunOnObject_1():
        Size(1200)
        AddX(400000)


@State
def UltimateShotObj():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(2)
        AttackLevel_(4)
        Damage(1100)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        VoodooDamageMultiplier(3)
        MinimumDamage(15)
        StarterRating(2)
        AttackDirection(2)
        Hitstop(3)
        UseFireHitspark(1)
        AirUntechableTime(30)
        AirPushbackX(20000)
        AirPushbackY(15000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        PushbackX(15000)
        CHStateIfCHStart(2)
        BlendMode_Normal()
        PaletteIndex(2)
        SetZVal(-500)
        WallCollisionDetection(1)
        IgnoreScreenfreeze(1)
        AttackOff()

        def upon_EVERY_FRAME():
            if SLOT_19 < 300000:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(EVERY_FRAME, 41)
                ObjectUpon(LANDING, 41)
    sprite('vrkgef430_00', 3)
    CreateObject('ShotAdd', 100)
    sprite('vrkgef430_01', 3)
    PrivateSE('kgse_06')
    CreateObject('UltimateShotUnderRay', -1)
    CreateObject('UltimateShotrock', -1)
    CreateObject('UltimateShotAura', 100)
    sprite('vrkgef430_02', 3)
    RefreshMultihit()
    sprite('vrkgef430_03', 3)
    CreateObject('NokoribiRenzok', -1)
    sprite('vrkgef430_04', 3)
    EndAttack()
    CreateObject('UltimateShotNokoribi', -1)

    def RunOnObject_1():
        AddX(280000)
        AddScale(300)
    sprite('vrkgef430_05', 3)
    sprite('vrkgef430_06', 3)
    sprite('vrkgef430_07', 3)
    sprite('vrkgef430_08', 2)


@State
def UltimateShotMasterOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(2)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
        if SLOT_19 < 300000:
            CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
        else:
            AddX(300000)
    sprite('null', 13)
    CreateObject('UltimateShotObjOD', -1)

    def RunOnObject_1():
        Size(700)
    sprite('null', 13)
    CreateObject('UltimateShotObjOD', -1)

    def RunOnObject_1():
        Size(1000)
        AddX(200000)
    sprite('null', 30)
    CreateObject('UltimateLastShotObjOD', -1)

    def RunOnObject_1():
        Size(1200)
        AddX(400000)


@State
def UltimateShotObjOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(2)
        AttackLevel_(4)
        Damage(1100)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        VoodooDamageMultiplier(3)
        MinimumDamage(15)
        StarterRating(2)
        AttackDirection(2)
        AttackType(4)
        Hitstop(3)
        UseFireHitspark(1)
        DefeatOpponentBehavior(1)
        AirUntechableTime(40)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        PushbackX(15000)
        CHStateIfCHStart(2)
        BlendMode_Normal()
        PaletteIndex(2)
        SetZVal(-500)
        WallCollisionDetection(1)
        IgnoreScreenfreeze(1)
        AttackOff()

        def upon_EVERY_FRAME():
            if SLOT_19 < 300000:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(EVERY_FRAME, 41)
                ObjectUpon(LANDING, 41)
    sprite('vrkgef430_00', 3)
    CreateObject('ShotAdd', 100)
    sprite('vrkgef430_01', 3)
    PrivateSE('kgse_06')
    CreateObject('UltimateShotUnderRay', -1)
    CreateObject('UltimateShotrock', -1)
    CreateObject('UltimateShotAura', 100)
    sprite('vrkgef430_02', 3)
    RefreshMultihit()
    sprite('vrkgef430_03', 3)
    CreateObject('NokoribiRenzok', -1)
    sprite('vrkgef430_04', 3)
    EndAttack()
    CreateObject('UltimateShotNokoribi', -1)

    def RunOnObject_1():
        AddX(280000)
        AddScale(300)
    sprite('vrkgef430_05', 3)
    sprite('vrkgef430_06', 3)
    sprite('vrkgef430_07', 3)
    sprite('vrkgef430_08', 2)


@State
def UltimateLastShotObjOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(2)
        AttackLevel_(4)
        Damage(1100)
        if SLOT_137:
            DamageMultiplier(80)
        VoodooDamageMultiplier(3)
        MinimumDamage(15)
        AttackDirection(2)
        DefeatOpponentBehavior(1)
        Hitstop(3)
        UseFireHitspark(1)
        AirUntechableTime(40)
        HardKnockdown(10)
        AirPushbackX(2500)
        AirPushbackY(15000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        PushbackX(15000)
        CHStateIfCHStart(2)
        OppPositionOnHit(1, 100000, 300000)
        BlendMode_Normal()
        PaletteIndex(2)
        SetZVal(-500)
        WallCollisionDetection(1)
        IgnoreScreenfreeze(1)
        AttackOff()

        def upon_OPPONENT_HIT():
            ObjectUpon(EVERY_FRAME, 32)
    sprite('vrkgef430_00', 3)
    CreateObject('ShotAdd', 100)
    sprite('vrkgef430_01', 3)
    PrivateSE('kgse_06')
    CreateObject('UltimateShotrock', -1)
    CreateObject('UltimateShotAura', 100)
    sprite('vrkgef430_02', 3)
    RefreshMultihit()
    sprite('vrkgef430_03', 3)
    CreateObject('NokoribiRenzok', -1)
    sprite('vrkgef430_04', 3)
    EndAttack()
    CreateObject('UltimateShotNokoribi', -1)

    def RunOnObject_1():
        AddX(280000)
        AddScale(300)
    sprite('vrkgef430_05', 3)
    sprite('vrkgef430_06', 3)
    sprite('vrkgef430_07', 3)
    sprite('vrkgef430_08', 2)


@State
def UltimateShotObjODAdd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(2)
        AttackLevel_(4)
        Damage(380)
        if SLOT_137:
            DamageMultiplier(80)
        VoodooDamageMultiplier(3)
        AttackDirection(2)
        Hitstop(3)
        UseSlashHitspark(1)
        AttackType(4)
        AirUntechableTime(40)
        AirPushbackX(25000)
        AirPushbackY(-5000)
        YImpulseBeforeWallbounce(1000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        PushbackX(15000)
        Wallbounce(1)
        WallbounceReboundTime(10)
        AirHitstunAfterWallbounce(50)
        CHStateIfCHStart(3)
        PaletteIndex(3)
        IgnoreScreenfreeze(1)
        CollideWithWall(1)
        AddY(200000)
        Size(3000)
        physicsXImpulse(90000)
        Visibility(1)
        CreateObject('UltimateShotModel', -1)
        SetActionMark(0)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            AddActionMark(1)
            if SLOT_2 >= 3:
                AirPushbackY(10000)
                EndAttack()
    label(0)
    sprite('vrkg410_14', 2)
    RefreshMultihit()
    sprite('vrkg410_15', 2)
    RefreshMultihit()
    sprite('vrkg410_16', 2)
    RefreshMultihit()
    gotoLabel(0)


@State
def UltimateShotModel():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('kgef_410core_00')
        Eff3DEffect('kgef430_spiar00', '')
        FaceSpawnLocation()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        IgnoreScreenfreeze(1)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    CreateParticle('kgef_450addshot_00', -1)
    label(0)
    sprite('null', 3)
    CreateParticle('kgef_450groundwind', -1)
    CreateObject('UltimateShotYugami', -1)
    SetScaleSpeed(0)
    gotoLabel(0)


@State
def UltimateShotYugami():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        ParticleTransparency(1)
        PlayerTransparency(50000)
        Size(1300)
        AddY(40000)
        AddX(20000)
    sprite('vrdist01', 10)
    SetScaleSpeed(100)


@State
def UltimateShotUnderRay():

    def upon_IMMEDIATE():
        AddY(30000)
    sprite('null', 30)
    PaletteIndex(2)
    ParticleColorFromPalette(96, 96, 96)
    CallCustomizableParticle('kgef_430ray_02', -1)


@State
def UltimateShotAura():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        IgnorePauses(2)
        CancelIfPlayerHit(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 30)
    PaletteIndex(2)
    ParticleColorFromPalette(96, 96, 96)
    CallPrivateEffect('kgef_430endaura_01')


@State
def ShotAdd():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(100)
    sprite('vrkgef430_10', 3)
    sprite('vrkgef430_11', 3)
    sprite('vrkgef430_12', 3)
    sprite('vrkgef430_13', 3)
    sprite('vrkgef430_14', 3)
    sprite('vrkgef430_15', 3)
    sprite('vrkgef430_16', 3)
    sprite('vrkgef430_17', 6)


@State
def UltimateShotAura():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        IgnorePauses(2)
    sprite('null', 30)
    PaletteIndex(2)
    ParticleColorFromPalette(96, 96, 96)
    CallPrivateEffect('kgef_430endaura_01')


@State
def UltimateShotImpact():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AddX(180000)
        PaletteIndex(2)
        ColorFromPaletteIndex(97)
        Size(600)
    sprite('null', 17)
    Eff3DEffect('kgef430_impact00', '')
    FaceSpawnLocation()


@State
def UltimateShotrock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddY(0)
        RandAddScaleY(-300, 0)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 35)
    Eff3DEffect('kgef430_rock', '')
    FaceSpawnLocation()
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def NokoribiRenzok():

    def upon_IMMEDIATE():
        BlendMode_Normal()
    sprite('null', 6)
    CreateObject('UltimateShotNokoribi', -1)
    sprite('null', 6)
    CreateObject('UltimateShotNokoribi', -1)

    def RunOnObject_1():
        AddX(-30000)
        AddScaleY(-300)


@State
def UltimateShotNokoribi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(97)
        RenderLayer(2)
        IgnoreScreenfreeze(1)
    sprite('null', 21)
    Eff3DEffect('kgef430_nokoribi00', '')
    FaceSpawnLocation()


@State
def ImpactAuraMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        BlendMode_Add()
        uponSendToLabel(32, 1)
        AddY(260000)
        AddX(-130000)
    sprite('null', 1)
    label(0)
    sprite('null', 28)
    CreateObject('ImpactAura', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 15)
    DespawnEAEffect('ImpactAura')


@State
def ImpactAuraMatoAir():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Add()
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        AddY(450000)
        RotationAngle(100000)
    sprite('null', 1)
    label(0)
    sprite('null', 28)
    ParticleRotationAngle(-50000)
    CallCustomizableParticle('kgef_431sordaura', -1)
    CreateObject('ImpactAuraAir', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Rotation(-65000)
    AddY(-30000)
    label(2)
    sprite('null', 30)
    Rotation(-55000)
    DespawnEAEffect('ImpactAura')


@State
def ImpactAura():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AlphaValue(0)
        BlendMode_Normal()
    sprite('null', 18)
    SetScaleSpeed(-5)
    ConstantAlphaModifier(51)
    Eff3DEffect('kgef431_sordaura00', '')
    FaceSpawnLocation()
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ImpactAuraAir():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        AlphaValue(150)
        BlendMode_Add()
    sprite('null', 28)
    Eff3DEffect('kgef431_sordaura00', '')
    FaceSpawnLocation()


@State
def ImpactFirstShock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
    sprite('null', 3)
    CreateObject('ImpactShock00', -1)

    def RunOnObject_1():
        AddX(250000)
    sprite('null', 10)
    CreateObject('ImpactShock01', -1)


@State
def ImpactShock00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        SetScaleX(300)
        SetScaleY(700)
        PaletteIndex(2)
        ColorFromPaletteIndex(97)
    sprite('null', 7)
    Eff3DEffect('kgef430_impact00', '')
    FaceSpawnLocation()
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ImpactShock01():

    def upon_IMMEDIATE():
        AddX(250000)
    sprite('null', 70)
    LinkParticle('kgef_431_bomstart_smoke')


@State
def UltimateImpactHibasira():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
        RenderLayer(2)
        AddX(240000)
        SetScaleX(1400)
    sprite('null', 7)
    CreateObject('UltimateImpactBom', -1)
    CreateObject('UltimateImpactCamera', -1)
    sprite('null', 7)
    CreateObject('UltimateImpactGround', -1)
    sprite('null', 60)
    LinkParticle('kgef_431_jizokuray')
    Eff3DEffect('kgef431_hibasira00', '')
    CreateObject('UltimateImpactRock', -1)
    label(0)
    sprite('null', 20)
    sprite('null', 7)
    TriggerUponForState('UltimateImpactCamera', 32)
    TriggerUponForState('UltimateImpactGround', 32)
    CreateParticle('kgef_431jizokurayend_00', -1)
    ConstantAlphaModifier(-26)
    sprite('null', 8)


@State
def UltimateImpactCamera():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 0)
    sprite('null', 1)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    sprite('null', 32767)
    label(0)
    sprite('null', 40)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)


@State
def UltimateImpactBom():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Size(2000)
        AddY(15000)
    sprite('null', 7)
    Eff3DEffect('kgef431_hibasira01', '')
    sprite('null', 3)
    CreateParticle('kgef_431_bomray_pos', -1)
    sprite('null', 4)
    ScreenShake(75000, 75000)


@State
def UltimateImpactRock():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AddY(-20000)
        SetScaleX(1500)
        SetScaleY(2000)
        SetZVal(-1000)
    sprite('null', 120)
    Eff3DEffect('kgef430_rock', '')
    FaceSpawnLocation()
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def UltimateImpactGround():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AlphaValue(0)
        AddY(-20000)
        SetScaleY(1300)
        RenderLayer(1)
        uponSendToLabel(32, 0)
    sprite('null', 5)
    ConstantAlphaModifier(26)
    sprite('null', 32767)
    Eff3DEffect('kgef430_ground', '')
    FaceSpawnLocation()
    label(0)
    sprite('null', 10)
    sprite('null', 15)
    ConstantAlphaModifier(-13)


@State
def efkg_431_splash():

    def upon_IMMEDIATE():
        Flip()
        Eff3DEffect('kgef431_slash', '')
        FaceSpawnLocation()
        SetScaleY(850)
        SetScaleX(1100)
        AddX(-273000)
    sprite('null', 10)


@State
def efkg_440Slash():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Flip()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        AddScaleY(100)
        AddScaleX(300)
        EnableAfterimage(1)
        uponSendToLabel(32, 1)
    label(0)
    sprite('vrkgef440_00', 2)
    sprite('vrkgef440_01', 2)
    sprite('vrkgef440_02', 2)
    AddScaleY(300)
    sprite('vrkgef440_03', 2)
    AddScaleY(-300)
    gotoLabel(0)
    label(1)
    sprite('keep', 5)
    ConstantAlphaModifier(-51)


@State
def efkg_440AIMG():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        AlphaValue(160)
    sprite('null', 5)
    Eff3DEffect('kgef440_slash00', '')
    ConstantAlphaModifier(-51)


@State
def efkg_440AIMG2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        AlphaValue(160)
    sprite('null', 5)
    Eff3DEffect('kgef440_slash01', '')
    ConstantAlphaModifier(-51)


@State
def efkg_440AIMG3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        AlphaValue(160)
    sprite('null', 5)
    Eff3DEffect('kgef440_slash03', '')
    ConstantAlphaModifier(-51)


@State
def efkg_440AIMG4():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        AlphaValue(255)
    sprite('null', 10)
    Eff3DEffect('kgef440_slash04', '')
    ConstantAlphaModifier(-26)


@State
def efkg_440BlackFire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('kgef440_blackfire00', '')
        AbsoluteY(0)
        Size(2000)
        AddX(240000)
    sprite('null', 10)
    IgnoreFinishStop(1)
    CreateObject('efkg_440BlackFireSub', -1)
    ScreenShake(20000, 20000)
    sprite('null', 15)
    IgnoreFinishStop(0)
    sprite('null', 5)


@State
def efkg_440BlackFireSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('kgef440_core')
        Size(1000)
    sprite('null', 10)
    IgnoreFinishStop(1)
    sprite('null', 58)
    IgnoreFinishStop(0)
    SetScaleSpeed(10)
    physicsXImpulse(3000)


@State
def efkg_440BlackFireEx():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('kgef440_blackfire01', '')
        AbsoluteY(0)
        Size(2000)
        AddX(300000)
        uponSendToLabel(32, 1)
    sprite('null', 10)
    IgnoreFinishStop(1)
    ScreenShake(20000, 20000)
    CreateObject('efkg_440ExBlackFireSub', -1)
    label(0)
    sprite('null', 2)
    IgnoreFinishStop(0)
    AddScale(-400)
    ScreenShake(1000, 1000)
    sprite('null', 2)
    AddScale(400)
    gotoLabel(0)
    label(1)
    sprite('null', 15)
    SetScaleSpeed(-30)
    ConstantAlphaModifier(-26)
    TriggerUponForState('efkg_440ExBlackFireSub', 32)


@State
def efkg_440ExBlackFireSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('kgef440ex_fire')
        Size(1000)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 15)
    ConstantAlphaModifier(-18)


@State
def efkg_412SlashEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(250000)
        AddY(-15000)
        AlphaValue(220)
    sprite('vrkgef412_00', 4)
    ParticleSize(900)
    CallCustomizableParticle('kgefcmnkira_01', 0)
    ParticleSize(900)
    CallCustomizableParticle('kgefcmnkira_01', 1)
    ParticleSize(800)
    CallCustomizableParticle('kgefcmnkira_01', 2)
    ParticleSize(700)
    CallCustomizableParticle('kgefcmnkira_01', 3)
    sprite('vrkgef412_01', 3)
    ParticleSize(600)
    CallCustomizableParticle('kgefcmnkira_01', 0)
    ParticleSize(600)
    CallCustomizableParticle('kgefcmnkira_01', 1)
    ParticleSize(600)
    CallCustomizableParticle('kgefcmnkira_01', 2)
    sprite('vrkgef412_02', 3)
    ParticleSize(600)
    CallCustomizableParticle('kgefcmnkira_01', 0)
    ParticleSize(600)
    CallCustomizableParticle('kgefcmnkira_01', 1)
    sprite('vrkgef412_03', 3)


@State
def __450slash00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('null', 10)
    Eff3DEffect('kgef450_slash00', '')
    FaceSpawnLocation()


@State
def __450slash01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(255)
    sprite('null', 10)
    Eff3DEffect('kgef450_slash01', '')
    FaceSpawnLocation()


@State
def AstKousokuEff():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        Flip()
        AddX(-500000)
        SetScaleX(1100)
        IgnoreFinishStop(1)
        ScreenCollision(1)
    sprite('vrkgef450_00', 3)
    CreateObject('AstKousokuEffParticle', -1)
    sprite('vrkgef450_01', 3)
    label(0)
    sprite('vrkgef450_02', 3)
    sprite('vrkgef450_03', 3)
    sprite('vrkgef450_04', 3)
    sprite('vrkgef450_05', 3)
    CreateObject('UltimateShotNokoribi', 106)

    def RunOnObject_1():
        RenderLayer(1)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    DespawnEAEffect('UltimateShotNokoribi')


@State
def AstKousokuEffParticle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        ScreenCollision(1)
    sprite('null', 200)
    LinkParticle('kgef_450start_00')


@State
def AstKousokuEff2():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        AddX(230000)
        SetScaleY(600)
        SetScaleX(1100)
        RenderLayer(2)
        IgnoreFinishStop(1)
        ScreenCollision(1)
    sprite('vrkgef450_00', 3)
    sprite('vrkgef450_01', 3)
    label(0)
    sprite('vrkgef450_02', 3)
    sprite('vrkgef450_03', 3)
    sprite('vrkgef450_04', 3)
    sprite('vrkgef450_05', 3)
    CreateObject('UltimateShotNokoribi', 106)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    DespawnEAEffect('UltimateShotNokoribi')


@State
def AstBG00():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        BlendMode_Normal()
        AddX(600000)
        AddY(-100000)
        Size(1500)
        AlphaValue(255)
        RenderLayer(2)
    sprite('null', 20)
    CreateObject('AstAura', -1)
    CreateObject('AstOpenSky', -1)
    Eff3DEffect('kgef450_sordaura00', '')
    sprite('null', 100)
    ScreenShake(10000, 10000)


@State
def AstBG01():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        BlendMode_Normal()
        AddY(-40000)
        Size(1200)
        AlphaValue(0)
        RenderLayer(2)
    sprite('null', 8)
    CreateObject('AstBGRay', -1)
    ConstantAlphaModifier(26)
    SetScaleSpeed(-50)
    Eff3DEffect('kgef450_sordaura02', '')
    sprite('null', 150)
    SetScaleSpeed(0)


@State
def AstBGRay():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        BlendMode_Normal()
        AddY(850000)
        RenderLayer(2)
    sprite('null', 150)
    LinkParticle('kgef_450sky_ray2')


@State
def AstAura():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('kgef450_sordaura01', '')
        Size(1500)
        RenderLayer(1)
        AlphaValue(0)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 100)


@State
def AstAura2():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('kgef450_sordaura03', '')
        RenderLayer(1)
        AlphaValue(215)
        SetScaleY(600)
        SetScaleX(300)
        AddY(150000)
    sprite('null', 40)
    CreateObject('AstNemoto2', -1)
    SetScaleXPerFrame(5)
    PrivateSE('kgse_09')
    sprite('null', 33)
    SetScaleXPerFrame(0)
    physicsYImpulse(-5000)
    sprite('null', 33)
    physicsYImpulse(0)
    DespawnEAEffect('AstNemoto2')
    sprite('null', 120)
    AlphaValue(0)
    CreateObject('AstAura3', -1)


@State
def AstAura3():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('kgef450_sordaura04', '')
        RenderLayer(1)
        AddY(0)
        Size(100)
    sprite('null', 10)
    physicsYImpulse(-60000)
    sprite('null', 120)
    physicsYImpulse(-50)


@State
def AstOpenSky():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        ScreenCollision(1)
        BlendMode_Normal()
        AddY(650000)
        AddX(-900000)
        Size(600)
    sprite('null', 120)
    CreateObject('AstShake', 0)
    CallPrivateEffect('kgef_450opensky_02')


@State
def AstNemoto():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AlphaValue(0)
        ParticleLayer(4)
        CallPrivateEffect('kgef_450nemoto_00')
    sprite('null', 10)
    ConstantAlphaModifier(51)
    sprite('null', 120)


@State
def AstNemoto2():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        ParticleLayer(1)
        CallPrivateEffect('kgef_450nemoto_01')
        Size(700)
    sprite('null', 32767)


@State
def AstCutin00():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RenderLayer(1)
        AddX(700000)
        AddY(-80000)
        Size(800)
        RotationAngle(-7500)
    sprite('kg450cutin_06', 10)
    sprite('kg450cutin_06', 120)
    CreateObject('AstNemoto', 0)


@State
def AstCutin01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(0)
        ScreenCollision(1)
    sprite('null', 10)
    ConstantAlphaModifier(10)
    CreateObject('AstCamera01', -1)
    sprite('kg450cutin_00', 4)
    sprite('kg450cutin_01', 4)
    sprite('kg450cutin_02', 4)
    sprite('kg450cutin_00', 4)
    sprite('kg450cutin_01', 4)
    sprite('kg450cutin_02', 4)
    sprite('kg450cutin_00', 4)
    sprite('kg450cutin_01', 4)
    sprite('kg450cutin_02', 4)
    sprite('kg450cutin_00', 4)
    sprite('kg450cutin_01', 4)
    sprite('kg450cutin_02', 4)
    sprite('kg450cutin_03', 3)
    sprite('kg450cutin_04', 3)
    sprite('kg450cutin_05', 3)
    sprite('kg450_20', 3)
    SetScaleSpeed(-100)
    CreateObject('AstBG01', -1)
    CreateObject('AstAura2', -1)
    sprite('kg450_20', 3)
    Size(800)
    sprite('kg450_20ex', 2)
    SetScaleSpeed(0)
    sprite('kg450_20ex', 3)
    sprite('kg450_21ex', 2)
    sprite('kg450_22ex', 2)
    sprite('kg450_20ex', 2)
    sprite('kg450_21ex', 2)
    sprite('kg450_22ex', 2)
    sprite('kg450_20ex', 2)
    sprite('kg450_21ex', 2)
    sprite('kg450_22ex', 2)
    sprite('kg450_20ex', 2)
    sprite('kg450_21ex', 2)
    sprite('kg450_22ex', 2)
    TriggerUponForState('AstCamera01', 32)
    SetScaleSpeed(0)
    sprite('kg450_21ex', 2)
    sprite('kg450_22ex', 2)
    sprite('kg450_20ex', 2)
    sprite('kg450_21ex', 40)
    sprite('kg450_22ex', 2)
    TriggerUponForState('AstCamera01', 33)
    sprite('kg450_23', 4)
    CreateObject('AstRockMato', -1)
    sprite('kg450_24', 4)
    sprite('kg450_25', 4)
    SetScaleSpeed(-1)
    PrivateSE('kgse_11')
    PrivateSE('kgse_11')
    sprite('kg450_26', 4)
    PrivateSE('kgse_08')
    PrivateSE('kgse_03')
    sprite('kg450_27', 4)
    sprite('kg450_25', 4)
    sprite('kg450_26', 4)
    sprite('kg450_27', 4)
    sprite('null', 32767)
    DespawnEAEffect('AstBG01')


@State
def AstCamera00():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RemoveOnCallStateEnd(2)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        PaletteIndex(2)
        RenderLayer(1)
        AddX(0)
        Visibility(1)
    sprite('vrkgef410dmy_00', 15)
    sprite('vrkgef410dmy_00', 10)
    physicsYImpulse(45000)
    physicsXImpulse(-25000)
    sprite('vrkgef410dmy_00', 20)
    EndMomentum(1)
    CameraPosition(800)
    sprite('vrkgef410dmy_00', 70)
    ParticleLayer(4)
    CallPrivateEffect('kgef_450kirikae_01')


@State
def AstCamera01():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RemoveOnCallStateEnd(2)
        CameraControlEnable(1)
        CameraFast(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        PaletteIndex(2)
        RenderLayer(1)
        AddY(300000)
        Visibility(1)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
    label(0)
    sprite('vrkgef410dmy_00', 32767)
    CreateObject('AstShake', 0)
    label(0)
    label(1)
    sprite('vrkgef410dmy_00', 2)
    AddY(400000)
    CameraPosition(950)
    CameraFast(0)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(925)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(900)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(875)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(850)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(825)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(800)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(775)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(750)
    sprite('vrkgef410dmy_00', 2)
    CameraPosition(725)
    sprite('vrkgef410dmy_00', 32767)
    TriggerUponForState('AstShake', 32)
    CameraPosition(700)
    gotoLabel(1)
    label(2)
    sprite('vrkgef410dmy_00', 32767)
    TriggerUponForState('AstShake', 33)
    AddY(-300000)
    CameraPosition(1000)
    physicsYImpulse(0)


@State
def AstShake():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        ScreenCollision(1)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        CommonSE('019_quake_1')
    label(0)
    sprite('null', 10)
    ScreenShake(25, 25)
    label(0)
    label(1)
    sprite('null', 10)
    ScreenShake(5000, 5000)
    CommonSE('019_quake_1')
    sprite('null', 10)
    ScreenShake(5000, 5000)
    gotoLabel(1)
    label(2)
    sprite('null', 7)
    ScreenShake(20000, 20000)
    gotoLabel(2)


@State
def AstRockMato():

    def upon_IMMEDIATE():
        ScreenCollision(1)
        RenderLayer(1)
    sprite('null', 2)
    CreateObject('AstRock', -1)

    def RunOnObject_1():
        AddScale(-500)
    sprite('null', 2)
    CreateObject('AstRock', -1)
    sprite('null', 2)
    CreateObject('AstRock', -1)

    def RunOnObject_1():
        AddScale(300)
    sprite('null', 2)
    CreateObject('AstRock2', -1)

    def RunOnObject_1():
        AddScale(1600)


@State
def AstRock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ScreenCollision(1)
        ParticleLayer(4)
        CallPrivateEffect('kgef_450hahen_mato')
        E0EAEffectPosition(2)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def AstRock2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ScreenCollision(1)
        ParticleLayer(4)
        CallPrivateEffect('kgef_450hahen_sub')
        E0EAEffectPosition(2)
    sprite('null', 145)


@State
def EntryMasterForKG():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)

    def RunOnObject_22():
        enterState('CmnActStand')
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(0)
        AddY(300000)
        Size(250)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(150000)
        AddY(60000)
    label(0)
    sprite('null', 32767)

    def RunOnObject_22():
        EndSprite(1)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-50000)
        AddY(200000)
        Size(150)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
        Size(200)
    gotoLabel(0)
    label(3)
    sprite('null', 1)

    def RunOnObject_22():
        enterState('CmnActEntry')
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)


@State
def EntryMasterForNO():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-22000)
        AddY(270000)
        Size(230)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(28000)
        AddY(216000)
        Size(150)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-24000)
        AddY(168000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(7500)
        AddY(360000)


@State
def EntryMasterForRC():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-10000)
        AddY(245000)
        Size(160)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(15000)
        AddY(200000)
        Size(180)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(24000)
        AddY(175000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(7500)
        AddY(360000)


@State
def EntryMasterForTK():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(15000)
        AddY(225000)
        Size(160)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-35000)
        AddY(180000)
        Size(180)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-5000)
        AddY(140000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(85000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(7500)
        AddY(360000)


@State
def EntryMasterForLC():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(15000)
        AddY(275000)
        Size(200)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(30000)
        AddY(220000)
        Size(150)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-15000)
        AddY(165000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30500)
        AddY(360000)


@State
def EntryMasterForNU():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-3000)
        AddY(290000)
        Size(170)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(7500)
        AddY(250000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(15000)
        AddY(220000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30500)
        AddY(360000)


@State
def EntryMasterForTB():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(15000)
        AddY(275000)
        Size(200)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(30500)
        AddY(240000)
        Size(160)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30500)
        AddY(200000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(40500)
        AddY(360000)


@State
def EntryMasterForMU():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(3000)
        AddY(290000)
        Size(170)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(3000)
        AddY(252000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(14500)
        AddY(220000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30500)
        AddY(360000)


@State
def EntryMasterForMK():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-25000)
        AddY(290000)
        Size(170)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(17500)
        AddY(240000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(15500)
        AddY(185000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)


@State
def EntryMasterForCE():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-2000)
        AddY(255000)
        Size(170)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(5000)
        AddY(205000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(10000)
        AddY(155000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 60)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(500)
        AddY(360000)


@State
def EntryMasterForRM():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(12000)
        AddY(275000)
        Size(170)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-20000)
        AddY(235000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(50000)
        AddY(210000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 60)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)


@State
def EntryMasterForPT():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(10000)
        AddY(225000)
        Size(160)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-12500)
        AddY(175000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-4000)
        AddY(140000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(90000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(7500)
        AddY(300000)


@State
def EntryMasterForIZ():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-20000)
        AddY(285000)
        Size(180)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(20000)
        AddY(245000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(9000)
        AddY(185000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(55000)
        AddY(120000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(7500)
        AddY(380000)


@State
def EntryMasterForBL():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-28000)
        AddY(230000)
        Size(200)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-4000)
        AddY(200000)
        Size(130)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(45000)
        AddY(175000)
        Size(180)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(55000)
        AddY(120000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30000)
        AddY(320000)


@State
def EntryMasterForKK():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(10000)
        AddY(255000)
        Size(150)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-3000)
        AddY(215000)
        Size(100)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(35000)
        AddY(185000)
        Size(145)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(55000)
        AddY(120000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30000)
        AddY(320000)


@State
def EntryMasterForAM():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(5000)
        AddY(305000)
        Size(150)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-3000)
        AddY(265000)
        Size(100)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(25000)
        AddY(185000)
        Size(145)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(55000)
        AddY(120000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(30000)
        AddY(390000)


@State
def EntryMasterForCA():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(160000)
        AddY(285000)
        Size(150)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(-183000)
        AddY(265000)
        Size(100)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(235000)
        AddY(245000)
        Size(145)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-95000)
        AddY(180000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-120000)
        AddY(360000)


@State
def EntryMasterForPH():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(20000)
        AddY(290000)
        Size(200)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(10000)
        AddY(245000)
        Size(150)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(50000)
        AddY(220000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-20000)
        AddY(400000)
    loopRest()


@State
def EntryMasterForES():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-22000)
        AddY(240000)
        Size(230)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(35000)
        AddY(255000)
        Size(150)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-5000)
        AddY(235000)
        Size(150)
    sprite('null', 5)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(7500)
        AddY(360000)


@State
def EntryMasterForMA():

    def upon_IMMEDIATE():
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-22000)
        AddY(270000)
        Size(230)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        Flip()
        AddX(35000)
        AddY(230000)
        Size(150)
    gotoLabel(0)
    label(2)
    sprite('null', 1)
    CreateObject('KaguraMeter00', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-85000)
        AddY(205000)
        Size(150)
    sprite('null', 5)
    CreateObject('KaguraMeter01', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(75000)
        AddY(100000)
    gotoLabel(0)
    label(3)
    sprite('null', 30)
    TriggerUponForState('KaguraMeter00', 32)
    TriggerUponForState('KaguraMeter01', 32)
    sprite('null', 60)
    CreateObject('KaguraQuestion', -1)

    def RunOnObject_1():
        TeleportToObject(22)
        AddX(-50000)
        AddY(360000)


@State
def KaguraMeter00():

    def upon_IMMEDIATE():
        Eff3DEffect('KaguraMeter00', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        Size(200)
        uponSendToLabel(32, 0)
    sprite('null', 189)
    label(0)
    sprite('null', 10)
    SetScaleSpeed(-30)
    ConstantAlphaModifier(-26)


@State
def KaguraMeter01():

    def upon_IMMEDIATE():
        Eff3DEffect('KaguraMeter01', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        Size(400)
        FaceLeft()
        uponSendToLabel(32, 0)
        RenderLayer(1)
    sprite('null', 189)
    label(0)
    sprite('null', 10)
    sprite('null', 5)
    SetScaleSpeedY(60)
    SetScaleXPerFrame(-100)
    ConstantAlphaModifier(-51)


@State
def KaguraQuestion():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('KaguraMeter02', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        Size(500)
        uponSendToLabel(32, 0)
        FaceLeft()
    sprite('null', 49)
    sprite('null', 10)
    SetScaleSpeed(-30)
    ConstantAlphaModifier(-26)


@State
def kgef_enter():

    def upon_IMMEDIATE():
        PaletteIndex(5)
        AddY(32000)
        AddX(-8000)
        FaceLeft()
        SetZVal(-500)
    sprite('vrkgef601_00', 3)
    Size(500)
    SetScaleSpeed(100)
    sprite('vrkgef601_00', 13)
    SetScaleSpeed(0)


@State
def kgef_enter2():

    def upon_IMMEDIATE():
        PaletteIndex(5)
        FaceLeft()
        SetZVal(-500)
        AlphaValue(0)
    sprite('null', 4)
    sprite('vrkgef601_10', 3)
    physicsYImpulse(3000)
    Size(500)
    SetScaleSpeed(100)
    sprite('vrkgef601_10', 9)
    physicsYImpulse(0)
    SetScaleSpeed(0)


@State
def EntryBike():
    sprite('kg603_05b', 3)
    physicsXImpulse(-27500)
    PreDashEffects(-1, 1, 0)
    sprite('kg603_05b', 3)
    PreDashEffects(-1, 1, 0)
    sprite('kg603_05b', 3)
    PreDashEffects(-1, 1, 0)
    sprite('kg603_05b', 3)
    PreDashEffects(-1, 1, 0)
    sprite('kg603_05b', 3)
    PreDashEffects(-1, 1, 0)
    sprite('kg603_05b', 3)
    PreDashEffects(-1, 1, 0)
    sprite('kg603_05b', 3)
    PreDashEffects(-1, 1, 0)


@State
def MatchWinSword():
    label(0)
    sprite('kg611_02s', 1)
    loopRest()
    gotoLabel(0)


@State
def EventHB():

    def upon_IMMEDIATE():
        SetZVal(500)
        AlphaValue(0)
        ConstantAlphaModifier(2)
        LoadSpritePalette(7)
        XPositionRelativeFacing(-260000)
        AbsoluteY(0)
        RunLoopUpon(17, 80)

        def upon_17():
            clearUponHandler(17)
            AlphaValue(255)
            sendToLabel(1)
    sprite('hb031_00', 7)
    physicsXImpulse(-1200)
    label(0)
    sprite('hb031_01', 7)
    sprite('hb031_02', 7)
    sprite('hb031_03', 7)
    sprite('hb031_04', 7)
    sprite('hb031_05', 7)
    XImpulseAcceleration(80)
    sprite('hb031_06', 7)
    sprite('hb031_07', 7)
    sprite('hb031_08', 7)
    sprite('hb031_09', 7)
    XImpulseAcceleration(80)
    loopRest()
    gotoLabel(0)
    label(1)
    EndMomentum(1)
    AddX(-8000)
    label(2)
    sprite('hb000_00', 7)
    sprite('hb000_01', 7)
    sprite('hb000_02', 7)
    sprite('hb000_03', 7)
    sprite('hb000_04', 7)
    sprite('hb000_05', 7)
    sprite('hb000_06', 7)
    sprite('hb000_07', 7)
    sprite('hb000_08', 7)
    sprite('hb000_09', 7)
    loopRest()
    gotoLabel(2)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Eventoffset_Sosai_kgvsrg():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(200000)
        DeviationX(-20000, 20000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)


@State
def Eventoffset_Sosai_kgvsmu():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(150000)
        DeviationX(-20000, 20000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)
