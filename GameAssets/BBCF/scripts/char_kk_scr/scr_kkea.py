@State
def EMB_KK():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_KK.DIG', '')
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
    sprite('null', 30)
    sprite('null', 50)
    AlphaValue(0)


@State
def EMB_KK_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_KK.DIG', '')
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
def EMB_KK_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(256000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_KK.DIG', '')
        Size(1400)
        AddY(16000)
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
def __3Dtest():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef_gate.DIG', '')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        RenderLayer(2)
        SetZVal(100)
        FaceSpawnLocation()
        ForceBloomMaskOn(1)
        AddY(192000)
        AddX(-64000)
    CreateObject('3Dtest_b', -1)
    sprite('null', 8)
    Size(100)
    SetScaleSpeed(100)
    sprite('null', 10)
    SetScaleSpeed(0)
    sprite('null', 20)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('null', 9)
    SetScaleSpeed(-100)
    sprite('null', 0)


@State
def __3Dtest_b():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef_gate_b.DIG', '')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        SetZVal(100)
        FaceSpawnLocation()
        ForceBloomMaskOn(1)
    sprite('null', 8)
    Size(100)
    SetScaleSpeed(100)
    sprite('null', 10)
    SetScaleSpeed(0)
    sprite('null', 20)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('null', 9)
    SetScaleSpeed(-100)
    sprite('null', 0)


@State
def test_gate():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Normal()
        AlphaValue(255)
        SetZVal(100)
        ForceBloomMaskOn(1)
    sprite('vrkkef_hole_a00', 8)
    Size(100)
    SetScaleSpeed(50)
    sprite('vrkkef_hole_a00', 10)
    SetScaleY(550)
    SetScaleX(700)
    SetScaleSpeed(0)
    sprite('vrkkef_hole_a00', 11)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 3)
    sprite('vrkkef_hole_a03', 9)
    SetScaleSpeed(-100)


@State
def efkk_210():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('null', 32767)
    LinkParticle('kkef_210')


@State
def efkk_202_smoke():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('null', 32767)
    CreateParticle('kkef_202_fire', -1)
    CreateParticle('kkef_202', -1)


@State
def efkk_202_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-80000)
        AddY(176000)
        Size(800)
    sprite('vrkkef_hole_a10', 2)
    sprite('vrkkef_hole_a11', 4)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_a00', 12)
    CreateObject('efkk_202_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_202_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_202_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_202_weapon():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(0)
        BlendMode_Normal()
        AddX(-176000)
        AddY(128000)
    sprite('vrkkef202weapon', 5)
    physicsXImpulse(-3000)
    physicsYImpulse(3000)
    setGravity(2500)

    def upon_LANDING():
        physicsYImpulse(22000)
        CreateParticle('kkef235_bound', -1)
    sprite('vrkkef202weapon', 10)
    CreateObject('efkk_202_hole_out', -1)
    sprite('vrkkef202weapon', 9)
    sprite('vrkkef202weapon_out', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)


@State
def efkk_202_hole_out():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        SetZVal(500)
        PaletteIndex(3)
        AddX(-64000)
        AddY(64000)
        Size(950)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 16)
    CreateObject('efkk_202_out_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_202_out_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_202_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_212_burner():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrkkef212_00', 4)
    SetZVal(100)
    sprite('vrkkef212_01', 4)
    sprite('vrkkef212_02', 3)
    SetZVal(-100)
    CreateParticle('kkef_fire_kira', 0)
    CreateParticle('kkef_fire_kira', 1)
    CreateParticle('kkef_fire_kira', 2)
    CreateParticle('kkef_fire_kira', 3)
    sprite('vrkkef212_03', 3)
    SetZVal(100)
    CreateParticle('kkef_fire_kira', 0)
    CreateParticle('kkef_fire_kira', 1)
    sprite('vrkkef212_04', 3)
    CreateParticle('kkef_fire_kira', 0)


@State
def efkk_212_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-160000)
        AddY(192000)
        Size(950)
    sprite('vrkkef_hole_a10', 3)
    sprite('vrkkef_hole_a11', 3)
    sprite('vrkkef_hole_a00', 9)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    CreateObject('efkk_212_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_212_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_212_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_212_hole_out():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        Flip()
        AddX(128000)
        AddY(112000)
        RotationAngle(-80000)
        Size(850)
    sprite('vrkkef_hole_a00', 3)
    CreateObject('efkk_202_out_electric', -1)
    sprite('vrkkef_hole_a01', 1)
    sprite('vrkkef_hole_a01', 2)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 3)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_202_out_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_202_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_232_burner():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrkkef232_00', 3)
    SetZVal(100)
    CreateParticle('kkef_fire_kira', 0)
    sprite('vrkkef232_01', 3)
    SetZVal(-100)
    CreateParticle('kkef_fire_kira', 0)
    CreateParticle('kkef_fire_kira', 1)
    sprite('vrkkef232_02', 3)


@State
def efkk_232_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-192000)
        AddY(164000)
        Size(800)
    sprite('vrkkef_hole_a10', 2)
    sprite('vrkkef_hole_a11', 3)
    sprite('vrkkef_hole_a00', 2)
    CreateObject('efkk_232_electric', -1)
    sprite('vrkkef_hole_a00', 5)
    E0EAEffectPosition(0)
    sprite('vrkkef_hole_a01', 2)
    DespawnEAEffect('efkk_232_electric')
    IgnorePauses(0)
    sprite('vrkkef_hole_a21', 2)


@State
def efkk_232_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_232_hole_out():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-112000)
        AddY(256000)
        Size(750)
        Flip()
    sprite('vrkkef_hole_a10', 3)
    sprite('vrkkef_hole_a11', 3)
    sprite('vrkkef_hole_a00', 3)
    CreateObject('efkk_232_out_electric', -1)
    sprite('vrkkef_hole_a00', 1)
    E0EAEffectPosition(0)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 3)
    DespawnEAEffect('efkk_232_out_electric')
    sprite('vrkkef_hole_a21', 3)


@State
def efkk_232_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_235_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-192000)
        AddY(160000)
        Size(750)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 2)
    sprite('vrkkef_hole_a11', 2)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_a00', 3)
    CreateObject('efkk_235_electric', -1)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_235_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_235_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_235_weapon():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(0)
        BlendMode_Normal()
        AddX(-224000)
        AddY(96000)
    sprite('vrkkef235weapon', 11)
    physicsXImpulse(-8000)
    setGravity(2500)

    def upon_LANDING():
        physicsYImpulse(30000)
        CreateParticle('kkef235_bound', -1)
    sprite('vrkkef235weapon', 9)
    CreateObject('efkk_235_hole_out', -1)
    sprite('vrkkef235weapon_out', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)


@State
def efkk_235_hole_out():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-88000)
        AddY(192000)
        Size(800)
    sprite('vrkkef_hole_a10', 4)
    CreateObject('efkk_235_out_electric', -1)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 6)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    E0EAEffectPosition(0)
    DespawnEAEffect('efkk_235_out_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_235_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_252_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-128000)
        AddY(192000)
        RotationAngle(40000)
        Size(850)
    sprite('vrkkef_hole_a11', 10)
    sprite('vrkkef_hole_a00', 8)
    CreateObject('efkk_252_electric', -1)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 3)
    DespawnEAEffect('efkk_252_electric')
    sprite('vrkkef_hole_a21', 3)


@State
def efkk_252_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_252_weapon():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(0)
        BlendMode_Normal()
    sprite('vrkkef252weapon', 2)
    sprite('vrkkef252weapon', 8)
    physicsXImpulse(-20000)
    physicsYImpulse(4000)
    setGravity(2000)
    CreateObject('efkk_252_hole_out', -1)
    sprite('vrkkef252weapon_out', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)


@State
def efkk_252_hole_out():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-320000)
        AddY(320000)
        RotationAngle(-15000)
        Size(850)
    sprite('vrkkef_hole_a10', 4)
    E0EAEffectPosition(0)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 9)
    CreateObject('efkk_252_out_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 11)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_252_out_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_252_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_253_burner():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrkkef253_00', 6)
    CreateParticle('kkef_fire_kira', 0)
    sprite('vrkkef253_01', 3)
    CreateParticle('kkef_fire_kira', 0)
    CreateParticle('kkef_fire_kira', 1)
    sprite('vrkkef253_02', 3)
    CreateParticle('kkef_fire_kira', 0)
    sprite('vrkkef253_03', 3)
    CreateParticle('kkef_fire_kira', 0)
    E0EAEffectPosition(0)


@State
def efkk_253_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        Flip()
        AddX(110000)
        AddY(133000)
        RotationAngle(-60000)
        Size(1000)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 4)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_a00', 3)
    CreateObject('efkk_253_electric', -1)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 3)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_253_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_253_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_253_weapon():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(0)
        BlendMode_Normal()
    sprite('vrkkef253_weapon2', 4)
    CreateObject('efkk_253_hole_out', -1)


@State
def efkk_253_hole_out():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Unknown4024(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-192000)
        AddY(96000)
        RotationAngle(30000)
        Size(950)
    sprite('vrkkef_hole_a00', 4)
    CreateObject('efkk_253_out_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 3)
    DespawnEAEffect('efkk_253_out_electric')
    sprite('vrkkef_hole_a21', 3)


@State
def efkk_253_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_340():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
        AlphaValue(255)
    sprite('vrkkef340_00', 3)
    sprite('vrkkef340_01', 3)
    SetZVal(100)
    CreateParticle('kkef_fire_kira', 0)
    sprite('vrkkef340_02', 2)
    SetZVal(-100)
    CreateParticle('kkef_fire_kira', 0)
    sprite('vrkkef340_03', 3)
    CreateParticle('kkef_fire_kira', 0)
    sprite('vrkkef340_04', 4)
    CreateParticle('kkef_fire_kira', 0)


@State
def efkk_340_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(96000)
        AddY(360000)
    sprite('vrkkef_hole_b', 3)
    Size(600)
    SetScaleSpeed(100)
    sprite('vrkkef_hole_b', 3)
    Size(1000)
    SetScaleSpeed(0)
    sprite('vrkkef_hole_b', 15)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_b', 6)
    SetScaleSpeed(-100)


@State
def efkk_340_hole_out():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-189000)
        AddY(120000)
        RotationAngle(-40000)
    sprite('vrkkef_hole_b2', 6)
    Size(0)
    SetScaleSpeed(100)
    sprite('vrkkef_hole_b2', 5)
    Size(600)
    SetScaleSpeed(0)
    sprite('vrkkef_hole_b2', 11)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef_hole_b2', 6)
    SetScaleSpeed(-100)


@State
def efkk_340_out_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_throw():

    def upon_IMMEDIATE():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 0)
    CreateParticle('kkef311_linework_b', -1)


@State
def efkk_airdash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 32767)
    LinkParticle('kkef_airdash')


@State
def efkk_airdash_back():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 32767)
    LinkParticle('kkef_airdash_back')


@State
def efkk_airbackdash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 32767)
    LinkParticle('kkef_airbackdash')


@State
def efkk_airbackdash_back():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 32767)
    LinkParticle('kkef_airbackdash_back')


@State
def kkef_601():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        AddX(-40000)
        AddY(110000)
    sprite('null', 32767)
    LinkParticle('kkef_601')


@State
def efkk_611():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        AddX(10000)
        AddY(30000)
    sprite('null', 19)
    LinkParticle('kkef_611')


@State
def efkk_611b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        AddX(10000)
        AddY(30000)
    sprite('null', 32767)
    LinkParticle('kkef_611b')


@State
def efkk_denpa():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        Flip()
        BlendMode_Add()
    sprite('vrkkef_denpa_00', 2)
    sprite('vrkkef_denpa_01', 2)
    sprite('vrkkef_denpa_02', 2)
    sprite('vrkkef_denpa_03', 2)


@State
def efkk_denpa2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrkkef_denpa_00', 2)
    sprite('vrkkef_denpa_01', 2)
    sprite('vrkkef_denpa_02', 2)
    sprite('vrkkef_denpa_03', 2)


@Subroutine
def Drive_SetPosition():
    WallCollisionDetection(1)
    TurnAround()
    NoAttackDuringAction(1)
    NoDamageAction(1)
    PaletteIndex(0)
    SetZVal(500)
    AddX(260000)
    AddY(200000)

    def upon_33():
        SetPosXByScreenPer(10)
        SetPosYByScreenPer(90)
        if SLOT_YDistanceFromFloor <= 100000:
            AddY(100000)

    def upon_34():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(90)
        if SLOT_YDistanceFromFloor <= 100000:
            AddY(100000)

    def upon_35():
        SetPosXByScreenPer(90)
        SetPosYByScreenPer(90)
        if SLOT_YDistanceFromFloor <= 100000:
            AddY(100000)

    def upon_36():
        SetPosXByScreenPer(10)
        SetPosYByScreenPer(50)

    def upon_38():
        SetPosXByScreenPer(90)
        SetPosYByScreenPer(50)

    def upon_39():
        SetPosXByScreenPer(10)
        SetPosYByScreenPer(10)

    def upon_40():
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(10)

    def upon_41():
        SetPosXByScreenPer(90)
        SetPosYByScreenPer(10)


@State
def efkk_Drive():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(600)
        Hitstop(0)
        EnemyHitstopAddition(10, 10, 15)
        AirHitstunAnimation(18)
        AirUntechableTime(60)
        PushbackX(8000)
        AirPushbackX(1000)
        YImpulseBeforeWallbounce(1600)
        AttackDirection(1)
        OnlyHitIfHitstun(1)
        OnlyHitPlayer(1)
        OppMovementUnlock(1)
        PreventBlocking(1)
        Unknown12052(2)
        callSubroutine('Drive_SetPosition')
        SLOT_5 = 1
        PhysicsPull(999, 5000, 3000)

        def upon_EVERY_FRAME():
            if not SLOT_21:
                sendToLabel(0)
            if SLOT_5 == 2:
                EndSE()
                PhysicsPull(0, 0, 0)
                DespawnEAEffect('efkk_203')
                DespawnEAEffect('efkk_203_yugami_loop')
                sendToLabel(10)
                if SLOT_2:
                    TriggerUponForState('SpinAssault', 33)
            if SLOT_5 == 3:
                EndSE()
                PhysicsPull(0, 0, 0)
                DespawnEAEffect('efkk_203')
                DespawnEAEffect('efkk_203_yugami_loop')
                sendToLabel(13)
                if SLOT_2:
                    TriggerUponForState('SpinAssault', 33)
                clearUponHandler(EVERY_FRAME)
                clearUponHandler(17)
                uponSendToLabel(PLAYER_BLOCKS, 0)

        def upon_37():
            sendToLabel(0)

        def upon_PLAYER_DAMAGED():
            sendToLabel(0)
        RunLoopUpon(17, 240)
        uponSendToLabel(17, 0)

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrkkef203weapon00', 1)
    AlphaValue(0)
    PaletteIndex(0)
    sprite('vrkkef203weapon00', 1)
    AlphaValue(255)
    CreateObject('efkk_203', 0)
    CreateParticle('kkef_203appear', 0)
    CreateObject('efkk_203_yugami_loop', 0)
    sprite('vrkkef203weapon01', 3)
    sprite('vrkkef203weapon02', 3)
    sprite('vrkkef203weapon03', 3)
    sprite('vrkkef203weapon04', 3)
    PrivateSE('kkse_08')
    sprite('vrkkef203weapon05', 3)
    SpecialSE('kkse_09')
    label(100)
    sprite('vrkkef203weapon00', 3)
    sprite('vrkkef203weapon01', 3)
    sprite('vrkkef203weapon02', 3)
    sprite('vrkkef203weapon03', 3)
    sprite('vrkkef203weapon04', 3)
    sprite('vrkkef203weapon05', 3)
    loopRest()
    gotoLabel(100)
    label(10)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(17)
    uponSendToLabel(PLAYER_BLOCKS, 0)
    sprite('keep', 30)
    uponSendToLabel(32, 11)
    label(11)
    sprite('vrkkef203weapon05', 111)
    uponSendToLabel(RELEASE_D, 12)
    label(13)
    sprite('vrkkef203weapon05', 10)
    label(12)
    sprite('vrkkef203weapon06', 2)
    clearUponHandler(RELEASE_D)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    CreateObject('efkk_203_repuls', -1)
    CreateObject('efkk_203_yugami_group', -1)
    TriggerUponForState('efkk_fireball_Hontai', 32)
    TriggerUponForState('efkk_UltraSokidan_Hontai', 32)
    TriggerUponForState('efkk_UltraSokidan_Hontai_OD', 32)
    PrivateSE('kkse_10')
    NoAttackDuringAction(0)
    PhysicsPull(6, -50000, -30000)
    SLOT_31 = SLOT_31 + -1
    SetActionMark(1)
    sprite('vrkkef203weapon07', 4)
    sprite('vrkkef203weapon08', 20)
    NoAttackDuringAction(1)
    SetActionMark(0)
    sprite('vrkkef203weapon06', 8)
    DespawnEAEffect('efkk_203_repuls')
    sprite('vrkkef203weapon03', 30)
    PhysicsPull(0, 0, 0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(17)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    clearUponHandler(RELEASE_D)
    clearUponHandler(37)
    EndSE()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    DespawnEAEffect('efkk_203')
    DespawnEAEffect('efkk_203_yugami_loop')
    DespawnEAEffect('efkk_203_repuls')
    ConstantAlphaModifier(-4)
    ExitState()
    label(0)
    sprite('vrkkef203weapon00', 10)
    PhysicsPull(0, 0, 0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(17)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    clearUponHandler(RELEASE_D)
    clearUponHandler(37)
    EndSE()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    DespawnEAEffect('efkk_203')
    DespawnEAEffect('efkk_203_yugami_loop')
    DespawnEAEffect('efkk_203_repuls')
    sprite('vrkkef203weapon01', 10)
    sprite('vrkkef203weapon02', 10)
    sprite('vrkkef203weapon03', 30)
    ConstantAlphaModifier(-4)


@State
def efkk_Drive_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(900)
        Hitstop(0)
        EnemyHitstopAddition(10, 15, 20)
        AirHitstunAnimation(18)
        AirUntechableTime(60)
        PushbackX(8000)
        AirPushbackX(1000)
        YImpulseBeforeWallbounce(1600)
        AttackDirection(1)
        OnlyHitIfHitstun(1)
        OnlyHitPlayer(1)
        OppMovementUnlock(1)
        PreventBlocking(1)
        Unknown12052(2)
        callSubroutine('Drive_SetPosition')
        SLOT_5 = 1
        PhysicsPull(999, 10000, 6000)

        def upon_EVERY_FRAME():
            TriggerUponForState('SpinAssault', 32)
            if not SLOT_21:
                sendToLabel(0)
            if SLOT_5 == 2:
                EndSE()
                PhysicsPull(0, 0, 0)
                DespawnEAEffect('efkk_203')
                DespawnEAEffect('efkk_203_yugami_loop')
                sendToLabel(10)
                if SLOT_2:
                    TriggerUponForState('SpinAssault', 33)
            if SLOT_5 == 3:
                EndSE()
                PhysicsPull(0, 0, 0)
                DespawnEAEffect('efkk_203')
                DespawnEAEffect('efkk_203_yugami_loop')
                sendToLabel(13)
                if SLOT_2:
                    TriggerUponForState('SpinAssault', 33)
                clearUponHandler(EVERY_FRAME)
                clearUponHandler(17)
                uponSendToLabel(PLAYER_BLOCKS, 0)

        def upon_37():
            sendToLabel(0)

        def upon_PLAYER_DAMAGED():
            sendToLabel(0)
        RunLoopUpon(17, 360)
        uponSendToLabel(17, 0)

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrkkef203weapon00', 1)
    AlphaValue(0)
    PaletteIndex(0)
    sprite('vrkkef203weapon00', 1)
    AlphaValue(255)
    CreateObject('efkk_203', 0)
    CreateParticle('kkef_203appear', 0)
    CreateObject('efkk_203_yugami_loop', 0)
    sprite('vrkkef203weapon01', 2)
    sprite('vrkkef203weapon02', 2)
    sprite('vrkkef203weapon03', 2)
    sprite('vrkkef203weapon04', 2)
    PrivateSE('kkse_08')
    sprite('vrkkef203weapon05', 2)
    DespawnEAEffect('efkk_203b')
    CreateObject('efkk_203', -1)
    SpecialSE('kkse_09')
    label(100)
    sprite('vrkkef203weapon00', 2)
    sprite('vrkkef203weapon01', 2)
    sprite('vrkkef203weapon02', 2)
    sprite('vrkkef203weapon03', 2)
    sprite('vrkkef203weapon04', 2)
    sprite('vrkkef203weapon05', 2)
    loopRest()
    gotoLabel(100)
    label(10)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(17)
    uponSendToLabel(PLAYER_BLOCKS, 0)
    sprite('keep', 30)
    uponSendToLabel(32, 11)
    label(11)
    sprite('vrkkef203weapon05', 111)
    uponSendToLabel(RELEASE_D, 12)
    label(13)
    sprite('vrkkef203weapon05', 10)
    label(12)
    sprite('vrkkef203weapon06', 2)
    clearUponHandler(RELEASE_D)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    CreateObject('efkk_203_repuls', -1)
    CreateObject('efkk_203_yugami_group', -1)
    TriggerUponForState('efkk_fireball_Hontai', 32)
    TriggerUponForState('efkk_UltraSokidan_Hontai', 32)
    TriggerUponForState('efkk_UltraSokidan_Hontai_OD', 32)
    PrivateSE('kkse_10')
    NoAttackDuringAction(0)
    PhysicsPull(6, -50000, -30000)
    SLOT_31 = SLOT_31 + -1
    SetActionMark(1)
    sprite('vrkkef203weapon07', 4)
    sprite('vrkkef203weapon08', 20)
    NoAttackDuringAction(1)
    SetActionMark(0)
    sprite('vrkkef203weapon06', 8)
    DespawnEAEffect('efkk_203_repuls')
    sprite('vrkkef203weapon03', 30)
    PhysicsPull(0, 0, 0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(17)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    clearUponHandler(RELEASE_D)
    clearUponHandler(37)
    EndSE()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    DespawnEAEffect('efkk_203')
    DespawnEAEffect('efkk_203_yugami_loop')
    DespawnEAEffect('efkk_203_repuls')
    ConstantAlphaModifier(-4)
    ExitState()
    label(0)
    sprite('vrkkef203weapon00', 10)
    PhysicsPull(0, 0, 0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(17)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    clearUponHandler(RELEASE_D)
    clearUponHandler(37)
    EndSE()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    DespawnEAEffect('efkk_203')
    DespawnEAEffect('efkk_203_yugami_loop')
    DespawnEAEffect('efkk_203_repuls')
    sprite('vrkkef203weapon01', 10)
    sprite('vrkkef203weapon02', 10)
    sprite('vrkkef203weapon03', 30)
    AlphaValue(128)
    ConstantAlphaModifier(-4)


@State
def efkk_203():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
    label(0)
    sprite('null', 6)
    CreateParticle('kkef_203gravi', -1)
    gotoLabel(0)


@State
def efkk_203_repuls():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
    CreateObject('efkk_203_repuls_yugami', -1)
    CreateParticle('kkef_203repuls_b', -1)
    label(0)
    sprite('null', 5)
    CreateParticle('kkef_203repuls', -1)
    gotoLabel(0)


@State
def efkk_203_yugami_loop():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
    label(0)
    sprite('null', 15)
    CreateObject('efkk_203_yugami', -1)
    CreateParticle('kkef_203gravi_b', -1)
    sprite('null', 15)
    CreateObject('efkk_203_yugami', -1)
    gotoLabel(0)


@State
def efkk_203_yugami():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        ParticleTransparency(1)
        PlayerTransparency(50000)
        Size(1000)
        AlphaValue(0)
    sprite('vrdist10', 32)
    ConstantAlphaModifier(8)
    SetScaleSpeed(-10)
    RotationSomething(3000)
    RandAddRotation(-90000, 90000)
    sprite('vrdist10', 32)
    ConstantAlphaModifier(-8)


@State
def efkk_203_yugami_group():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    sprite('null', 1)
    CreateObject('efkk_203_repuls_yugami', -1)
    sprite('null', 1)
    CreateObject('efkk_203_repuls_yugami', -1)


@State
def efkk_203_repuls_yugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        ParticleTransparency(1)
        PlayerTransparency(75000)
        Size(500)
        AlphaValue(255)
    sprite('vrdist10', 10)
    SetScaleSpeed(250)


@State
def efkk_403_TrapA():

    def upon_IMMEDIATE():
        TurnAround()
        WallCollisionDetection(1)
        AddX(110000)
        NoDamageAction(1)
        PaletteIndex(0)
        SLOT_33 = 0

        def upon_STATE_END():
            SLOT_33 = 1
        uponSendToLabel(PLAYER_DAMAGED, 0)
        uponSendToLabel(41, 0)
    sprite('kk403_h00', 1)
    physicsYImpulse(-10000)
    sprite('kk403_h00', 1)
    EndMomentum(1)
    CreateParticle('kkef403_smoke01', 0)
    PrivateSE('kkse_02')
    sprite('kk403_h01', 1)
    sprite('kk403_h02', 1)
    sprite('kk403_h03', 1)
    sprite('kk403_h04', 1)
    sprite('kk403_h05', 1)
    sprite('kk403_h06', 1)
    sprite('kk403_h07', 1)
    sprite('kk403_h08', 1)
    PrivateSE('kkse_03')
    sprite('kk403_h09', 1)
    sprite('kk403_h10', 1)
    sprite('kk403_h11', 1)
    sprite('kk403_h12', 1)
    sprite('kk403_h13', 1)
    CreateObject('efkk_403_beam', -1)
    sprite('kk403_h13', 6)
    CreateObject('efkk_403A_Atk', -1)
    sprite('kk403_h13', 30)
    TriggerUponForState('efkk_403_beam', 32)
    sprite('kk403_h12', 3)
    sprite('kk403_h11', 3)
    sprite('kk403_h10', 3)
    sprite('kk403_h09', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('kk403_h04', 30)
    sprite('kk403_h04', 36)
    ConstantAlphaModifier(-6)
    loopRest()
    ExitState()
    label(0)
    EndMomentum(1)
    AbsoluteY(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    clearUponHandler(41)
    NoAttackDuringAction(1)
    sprite('keep', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('null', 45)
    TriggerUponForState('efkk_403_beam', 32)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk_403_TrapB():

    def upon_IMMEDIATE():
        TurnAround()
        WallCollisionDetection(1)
        AddX(110000)
        NoAttackDuringAction(1)
        NoDamageAction(1)
        PaletteIndex(0)
        SLOT_33 = 0

        def upon_STATE_END():
            SLOT_33 = 1
        uponSendToLabel(PLAYER_DAMAGED, 0)
        uponSendToLabel(41, 0)
    sprite('kk403_h00', 10)
    physicsYImpulse(-1000)
    sprite('kk403_h00', 2)
    EndMomentum(1)
    CreateParticle('kkef403_smoke01', 0)
    PrivateSE('kkse_02')
    sprite('kk403_h01', 2)
    sprite('kk403_h02', 2)
    sprite('kk403_h03', 2)
    sprite('kk403_h04', 2)
    sprite('kk403_h05', 2)
    sprite('kk403_h06', 2)
    sprite('kk403_h07', 2)
    sprite('kk403_h08', 2)
    PrivateSE('kkse_03')
    sprite('kk403_h09', 2)
    sprite('kk403_h10', 2)
    sprite('kk403_h11', 2)
    sprite('kk403_h12', 2)
    sprite('kk403_h13', 90)

    def upon_EVERY_FRAME():
        if SLOT_19 < 250000:
            sendToLabel(1)
        if not SLOT_21:
            sendToLabel(0)
    label(1)
    sprite('kk403_h13', 20)
    CharacterFlash(16777215, 5, 20)
    clearUponHandler(EVERY_FRAME)
    sprite('kk403_h13', 1)
    CreateObject('efkk_403_beam', -1)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    sprite('kk403_h13', 16)
    CharacterFlash(0, 0, 0)
    CreateObject('efkk_403B_Atk', -1)
    sprite('kk403_h13', 10)
    TriggerUponForState('efkk_403_beam', 32)
    sprite('kk403_h13', 20)
    sprite('kk403_h12', 3)
    sprite('kk403_h11', 3)
    sprite('kk403_h10', 3)
    sprite('kk403_h09', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('kk403_h04', 30)
    sprite('kk403_h04', 36)
    ConstantAlphaModifier(-6)
    loopRest()
    ExitState()
    label(0)
    EndMomentum(1)
    AbsoluteY(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(PLAYER_BLOCKS)
    clearUponHandler(41)
    NoAttackDuringAction(1)
    sprite('keep', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('null', 45)
    TriggerUponForState('efkk_403_beam', 32)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk_403A_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(860)
        Hitstop(0)
        EnemyHitstopAddition(7, 7, 27)
        AirPushbackX(0)
        AttackP1(80)
        AirUntechableTime(40)
        GroundedHitstunAnimation(14)
        AirHitstunAnimation(14)
        StarterRating(2)
        Unknown12052(1)
        SetScaleY(5000)
        CancelIfPlayerHit(3)
    sprite('kk403_Atkcol', 6)


@State
def efkk_403B_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(450)
        Hitstop(0)
        EnemyHitstopAddition(7, 7, 27)
        PushbackX(8000)
        AirPushbackX(0)
        AttackP1(80)
        AirUntechableTime(40)
        SingleProration(1)
        GroundedHitstunAnimation(14)
        AirHitstunAnimation(14)
        StarterRating(2)
        Unknown12052(1)
        SetScaleY(5000)
        CancelIfPlayerHit(3)
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()


@State
def efkk_403_beam():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('kkef403_beam00', '')
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    CreateParticle('kkef403jizoku_00', -1)
    ScreenShake(5000, 5000)
    CreateObject('efkk_ThunderTakusan', -1)
    label(0)
    sprite('null', 5)
    AlphaValue(0)
    CreateParticle('kkef403end_00', -1)


@State
def efkk_ThunderTakusan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
    label(0)
    sprite('null', 3)
    CreateObject('efkk_403_beamThunder00', -1)
    CommonSE('013_thunder_0')
    CreateObject('efkk_403_beamThunder01', -1)
    CreateObject('efkk_403_beamThunder02', -1)
    sprite('null', 3)
    CreateObject('efkk_403_beamThunder00', -1)

    def RunOnObject_1():
        Flip()
    CreateObject('efkk_403_beamThunder01', -1)

    def RunOnObject_1():
        Flip()
    CreateObject('efkk_403_beamThunder02', -1)

    def RunOnObject_1():
        Flip()
    gotoLabel(0)


@State
def efkk_403_beamThunder00():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef403_beam01', '')
        FaceSpawnLocation()
        BlendMode_Normal()
    sprite('null', 8)
    SetScaleXPerFrame(-30)
    DeviationY(0, 650000)
    RandAddScaleX(-500, 100)


@State
def efkk_403_beamThunder01():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef403_beam01', '')
        FaceSpawnLocation()
        BlendMode_Normal()
    sprite('null', 8)
    SetScaleXPerFrame(-30)
    DeviationY(650000, 1300000)
    RandAddScaleX(-500, 100)


@State
def efkk_403_beamThunder02():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef403_beam01', '')
        FaceSpawnLocation()
        BlendMode_Normal()
    sprite('null', 8)
    SetScaleXPerFrame(-30)
    DeviationY(1300000, 1950000)
    RandAddScaleX(-500, 100)


@Subroutine
def Fireball_Hontai():

    def upon_EVERY_FRAME():
        if SLOT_2:
            if SLOT_5 == 1:
                ExternalForcesRate(300, 300)
            if SLOT_5 >= 2:

                def upon_32():
                    ExternalForcesRate(200, 40)
                    clearUponHandler(EVERY_FRAME)
                    clearUponHandler(32)
                    sendToLabel(1)
        if not SLOT_21:
            clearUponHandler(EVERY_FRAME)
            sendToLabel(99)
    SLOT_32 = 0

    def upon_STATE_END():
        SLOT_32 = 1

    def upon_33():
        sendToLabel(10)

    def upon_34():
        sendToLabel(20)

    def upon_35():
        sendToLabel(30)

    def upon_5():
        if SLOT_5:
            YAccel(-50)
        else:
            clearUponHandler(5)
            sendToLabel(99)
    if SLOT_52 == 1:
        HitsPerCall(4, 1, 1, 1, 4, 0, 4, 4)
        RunLoopUpon(17, 240)
    if SLOT_53 == 1:
        HitsPerCall(12, 1, 1, 1, 1, 0, 0, 0)
        RunLoopUpon(17, 360)
    if SLOT_54 == 1:
        HitsPerCall(18, 1, 1, 1, 1, 0, 0, 0)
        RunLoopUpon(17, 360)

    def upon_54():
        sendToLabel(99)

    def upon_17():
        sendToLabel(99)

    def upon_41():
        sendToLabel(99)


@State
def efkk_fireball_Hontai():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        SLOT_52 = 1
        callSubroutine('Fireball_Hontai')
        AttackLevel_(2)
        Damage(360)
        AttackP1(80)
        AttackP2(75)
        SingleProration(1)
        AirUntechableTime(24)
        Hitstop(4)
        UseFireHitspark(1)
        AttackDirection(0)
        StarterRating(2)
        Unknown12052(1)
        UseFireHitspark(1)
        CreateObject('efkk_fireballStart', -1)
        if SLOT_137:
            DamageMultiplier(80)
    label(10)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    AddY(150000)
    physicsYImpulse(12000)
    physicsXImpulse(2000)
    setGravity(200)
    CreateObject('efkk_FireBallroop', -1)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(20)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    AddY(150000)
    physicsYImpulse(12000)
    physicsXImpulse(4000)
    setGravity(200)
    CreateObject('efkk_FireBallroop', -1)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(30)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    AddY(150000)
    physicsYImpulse(12000)
    physicsXImpulse(8000)
    setGravity(200)
    CreateObject('efkk_FireBallroop', -1)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(5)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CreateParticle('kkef402jizoku_2p', -1)
    else:
        CreateParticle('kkef402jizoku', -1)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    CreateObject('efkk_fireDust01', -1)
    loopRest()
    gotoLabel(5)
    label(1)
    sprite('vrkkef402Atk', 2)
    SLOT_55 = 14
    RefreshMultihit()
    AttackLevel_(4)
    Damage(750)
    ResetAttackP2()
    SingleProration(0)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(60)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    Hitstop(5)
    EnemyHitstopAddition(10, 10, 10)
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CreateParticle('kkef402jizoku_2p', -1)
    else:
        CreateParticle('kkef402jizoku', -1)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust01', -1)
    label(2)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CreateParticle('kkef402jizoku_2p', -1)
    else:
        CreateParticle('kkef402jizoku', -1)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust01', -1)
    SLOT_55 = SLOT_55 + -1
    if not SLOT_55:
        notConditionalSendToLabel(99)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 3)
    SetActionMark(0)
    EndMomentum(1)
    TriggerUponForState('efkk_FireBallroop', 32)
    Eff3DEffect('kkef402_fire04', '')
    FaceSpawnLocation()
    RandAddRotation(0, 360000)
    sprite('null', 3)
    if SLOT_95:
        CreateParticle('kkef402hit_03_2p', -1)
    else:
        CreateParticle('kkef402hit_03', -1)
    CreateObject('efkk_fireDust01', -1)
    CreateObject('efkk_fireDust02', -1)


@State
def efkk_FireBallroop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        RenderLayer(1)
        Size(700)
        if SLOT_95:
            PaletteIndex(4)
        else:
            PaletteIndex(2)
        uponSendToLabel(32, 1)
    sprite('vrkkef402_00', 1)
    label(0)
    sprite('vrkkef402_00', 3)
    PrivateSE('kkse_13')
    sprite('vrkkef402_01', 3)
    sprite('vrkkef402_02', 3)
    sprite('vrkkef402_03', 3)
    gotoLabel(0)
    label(1)
    sprite('vrkkef402_03', 2)


@State
def efkk_fireDust00():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        Size(850)
        AlphaValue(150)
        if SLOT_95:
            Eff3DEffect('kkef402_fire03_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire03', '')
            FaceSpawnLocation()
    sprite('null', 10)
    SetScaleSpeed(-30)
    AddRotationPerFrame(-5000)
    RandAddRotation(0, 360000)


@State
def efkk_fireDust01():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AlphaValue(150)
        Size(1000)
        if SLOT_95:
            Eff3DEffect('kkef402_fire03_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire03', '')
            FaceSpawnLocation()
    sprite('null', 10)
    SetScaleSpeed(-30)
    AddRotationPerFrame(5000)
    RandAddRotation(0, 360000)


@State
def efkk_fireDust02():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AlphaValue(150)
        Size(1000)
        if SLOT_95:
            Eff3DEffect('kkef402_fire03_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire03', '')
            FaceSpawnLocation()
    sprite('null', 10)
    SetScaleSpeed(30)
    RandAddRotation(0, 360000)
    CommonSE('015_blaze_0')


@State
def efkk_fireballStart():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        Size(1200)
        if SLOT_95:
            Eff3DEffect('kkef402_fire00_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire00', '')
            FaceSpawnLocation()
    sprite('null', 10)
    if SLOT_95:
        CreateParticle('kkef402star_fire_2p', -1)
    else:
        CreateParticle('kkef402star_fire', -1)
    sprite('null', 10)
    AlphaValue(0)
    CreateObject('efkk_fireballStart01', -1)
    loopRest()
    DeleteObject(23)


@State
def efkk_fireballStart01():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        Size(1200)
        if SLOT_95:
            Eff3DEffect('kkef402_fire01_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire01', '')
            FaceSpawnLocation()
    sprite('null', 10)


@State
def efkk_freezwind00():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('kkef401_freezewind00', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        AlphaValue(0)
        SetScaleX(1300)
        RotationAngle(15000)
        uponSendToLabel(32, 1)
    sprite('null', 5)
    CreateParticle('kkef401icewind_start', -1)
    ConstantAlphaModifier(26)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    label(0)
    sprite('null', 20)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-51)


@State
def efkk_401weapon():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        PaletteIndex(0)
        BlendMode_Normal()
        AddX(-192000)
        AddY(148000)
    sprite('vrkkef401wpn00', 3)
    sprite('vrkkef401wpn01', 3)
    sprite('vrkkef401wpn02', 3)


@State
def efkk_401weapon2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        PaletteIndex(0)
        BlendMode_Normal()
        SetZVal(100)
        AddX(-192000)
        AddY(148000)
    sprite('vrkkef401wpn00b', 3)
    sprite('vrkkef401wpn01b', 3)
    sprite('vrkkef401wpn02b', 3)


@State
def efkk_401_hole():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(3)
        SetZVal(500)
        AddX(-192000)
        AddY(148000)
        Size(975)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 24)
    CreateObject('efkk_401_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 4)
    sprite('vrkkef_hole_a20', 4)
    DespawnEAEffect('efkk_401_electric')
    sprite('vrkkef_hole_a21', 4)


@State
def efkk_401_electric():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Unknown4024(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        ForceBloomMaskOn(1)
        PaletteIndex(3)
        BlendMode_Add()
        SetZVal(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)


@State
def efkk_401tama():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Damage(80)
        AttackP2(98)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirUntechableTime(50)
        WallbounceReboundTime(10)
        Floorslide(20)
        PushbackX(24800)
        Hitstop(0)
        HitsparkSize(400)
        IgnoreComboTime(1)
        CHStateIfCHStart(3)
        AirPushbackX(30000)
        AirPushbackY(2000)

        def upon_OPPONENT_HIT_OR_BLOCK():
            NoAttackDuringAction(1)
            sendToLabel(1)
            TriggerUponForState('Freeze_Shot', 32)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(800)
        LinkParticle('kkef401tama_mato')
        uponSendToLabel(32, 1)
        uponSendToLabel(CORNERED, 1)

        def upon_33():
            CommonSE('016_explode_0')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vr_blt', 120)
    CreateParticle('kkef401tamacircle00', -1)
    Visibility(1)
    RefreshMultihit()
    RandSpeedX(85000, 100000)
    DeviationY(-80000, 80000)
    label(1)
    sprite('null', 5)
    physicsXImpulse(0)
    ConstantAlphaModifier(-51)


@State
def efkk_Mazleflash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('kkef401mazle_mato')
        BlendMode_Normal()
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 2)
    CreateObject('efkk_401tama', -1)
    ObjectUpon(STATE_END, 33)
    CopyFromRightToLeft(23, 2, 52, 3, 2, 57)
    if not SLOT_52:
        DeleteObject(23)
    sprite('null', 2)
    CreateObject('efkk_401tama', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def efkk_BLTtakusan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    label(0)
    sprite('null', 2)
    CreateObject('efkk_BLT', -1)
    CopyFromRightToLeft(23, 2, 52, 3, 2, 57)
    if not SLOT_52:
        DeleteObject(23)
    sprite('null', 2)
    CreateObject('efkk_BLT', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 8)


@State
def efkk_BLT():

    def upon_IMMEDIATE():
        PaletteIndex(2)

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            PrivateSE('nose_02')
    sprite('vr_blt', 40)
    AddRotationPerFrame(10000)
    RandAddRotation(0, 360000)
    PrivateSE('nose_02')
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    RandSpeedX(-1000, 1000)
    RandSpeedY(-1000, 5000)


@State
def efkk401_micile():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(500)
        SingleProration(1)
        MinimumDamage(100)
        Hitstop(1)
        AirUntechableTime(45)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(1800)
        OppMovementUnlock(1)
        IgnoreComboTime(1)
        TeleportToObject(22)
        BlendMode_Normal()
        RunLoopUpon(17, 60)
        uponSendToLabel(17, 1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrkkef401_micile00', 15)
    RefreshMultihit()
    CreateParticle('kkef401micileroot_02', -1)
    CreateObject('efkk401_micilefire', -1)
    physicsYImpulse(10000)
    setGravity(-500)
    PrivateSE('kkse_24')
    sprite('vrkkef401_micile00', 3)
    Damage(100)
    RefreshMultihit()
    OppMovementUnlock(0)
    PerGravity(500)
    AirPushbackY(30000)
    label(0)
    sprite('vrkkef401_micile00', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrkkef401_micile00', 1)


@State
def efkk401_micile_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(500)
        SingleProration(1)
        MinimumDamage(100)
        Hitstop(1)
        AirUntechableTime(45)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpulseBeforeWallbounce(1800)
        OppMovementUnlock(1)
        IgnoreComboTime(1)
        AttackType(4)
        TeleportToObject(22)
        BlendMode_Normal()
        RunLoopUpon(17, 60)
        uponSendToLabel(17, 1)

        def upon_OPPONENT_HIT():
            AddActionMark(1)

        def upon_EVERY_FRAME():
            if SLOT_2 >= 5:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrkkef401_micile00', 15)
    RefreshMultihit()
    CreateParticle('kkef401micileroot_02', -1)
    CreateObject('efkk401_micilefire', -1)
    physicsYImpulse(10000)
    setGravity(-500)
    PrivateSE('kkse_24')
    sprite('vrkkef401_micile00', 3)
    Damage(100)
    RefreshMultihit()
    OppMovementUnlock(0)
    PerGravity(500)
    AirPushbackY(33000)
    label(0)
    sprite('vrkkef401_micile00', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrkkef401_micile00', 2)
    AttackOff()
    sprite('vrkkef401_micile00', 1)
    CreateObject('efkk401_LastBomb', -1)


@State
def efkk401_micilefire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('kkef401micilefire_mato')
        AddY(-390000)
        Size(1500)
        AlphaValue(0)
    sprite('null', 15)
    ConstantAlphaModifier(51)
    label(0)
    sprite('null', 2)
    CreateParticle('kkef401micilesmoke_01', -1)
    gotoLabel(0)


@State
def efkk401_LastBomb():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(500)
        MinimumDamage(100)
        AttackP2(100)
        Hitstop(1)
        AirUntechableTime(50)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(45000)
        YImpulseBeforeWallbounce(1800)
        AttackType(4)
        UseFireHitspark(1)
        Eff3DEffect('kkef401_bomb', '')
        BlendMode_Normal()
        Size(1000)
        Rotation(20000)
        IgnoreScreenfreeze(1)
        RenderLayer(1)
        Visibility(1)
    sprite('vrkkef401_micile00', 3)
    CommonSE('015_blaze_2')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    CommonSE('025_cleanhit_grap')
    sprite('vrkkef401_micile00', 3)
    AddScale(250)
    sprite('vrkkef401_micile00', 3)
    AddScale(150)
    CallCustomizableParticle('kkef_401_bloom', -1)
    ScreenShake(15000, 15000)
    sprite('vrkkef401_micile00', 9)
    AddScale(100)


@State
def efkk401_minigunbrake():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    sprite('vrkkef401_brake', 20)
    setGravity(1000)
    physicsYImpulse(5000)
    physicsXImpulse(-8000)
    sprite('vrkkef401_brake', 1)
    setGravity(0)
    CreateParticle('kkef403koware_03', 0)
    CreateParticle('kkef403koware_03', 1)


@State
def efkk401_reitouhou():

    def upon_IMMEDIATE():

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
        uponSendToLabel(LANDING, 0)
    sprite('kk401_11z', 40)
    AddRotationPerFrame(5000)
    RandAddRotation(0, 360000)
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    RandSpeedX(-1000, 1000)
    RandSpeedY(-1000, 5000)
    label(0)
    sprite('null', 10)
    ParticleSize(800)
    CallCustomizableParticle('kkef403koware_05', -1)


@State
def efkk401_MisileAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        AirUntechableTime(60)
        Hitstop(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        HardKnockdown(1)
        OnlyHitPlayer(1)
        CounterHitSetting(1)
        PassByArmor(1)
        DamageEffect(9, '')
        NoAttackOffset(1)
        DefeatOpponentBehavior(1)
        ShutUp(1)
        IgnoreComboTime(1)

        def upon_OPPONENT_HIT():
            TriggerUponForState('Freeze_Shot', 35)
    sprite('vrkkef401_MisileAtk', 1)


@State
def efkk400A_fire00():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        uponSendToLabel(34, 3)
    sprite('null', 7)
    label(0)
    sprite('vrkkef400_00', 2)
    sprite('vrkkef400_01', 2)
    EnableAfterimage(1)
    gotoLabel(0)
    label(1)
    sprite('vrkkef400_02', 2)
    EnableAfterimage(0)
    sprite('vrkkef400_03', 2)
    sprite('vrkkef400_04', 3)
    sprite('vrkkef400_05', 3)
    sprite('vrkkef400_06', 3)
    sprite('vrkkef400_07', 2)
    sprite('null', 32767)
    label(2)
    sprite('vrkkef400_08', 2)
    sprite('vrkkef400_09', 2)
    sprite('vrkkef400_10', 6)
    sprite('vrkkef400_11', 2)
    sprite('vrkkef400_12', 2)
    sprite('vrkkef400_13', 2)
    sprite('null', 32767)
    label(3)
    sprite('vrkkef400_14', 2)
    AddX(50000)
    sprite('vrkkef400_15', 2)
    sprite('vrkkef400_16', 2)


@State
def efkk400_Hand00():

    def upon_IMMEDIATE():
        AddY(185000)
        AddX(95000)
        uponSendToLabel(32, 1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(22)
    sprite('kk400_13\x82\x9a', 1)
    label(0)
    sprite('kk400_13\x82\x9a', 2)
    CreateParticle('kkef400miniboost_00', 0)
    AddScale(3)
    AddY(-2500)
    AddX(-500)
    Rotation(4000)
    sprite('kk400_13\x82\x9a', 2)
    CreateParticle('kkef400miniboost_00', 1)
    AddY(-2500)
    sprite('kk400_13\x82\x9a', 2)
    CreateParticle('kkef400miniboost_00', 2)
    AddY(5000)
    AddX(500)
    Rotation(-4000)
    gotoLabel(0)
    label(1)
    sprite('null', 1)


@State
def efkk400_Hand002nd():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        Unknown4024(3)
        AttackLevel_(4)
        Damage(600)
        AttackP2(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(12000)
        PushbackX(12000)
        AirUntechableTime(35)
        StarterRating(2)
        Unknown12052(1)
        E0EAEffectDirection(3)
        UseFireHitspark(1)
        uponSendToLabel(34, 2)

        def upon_45():
            PrivateFunction3(22, 0, -50000, 100, 1)
    sprite('null', 1)
    CreateObject('efkk400_Handarame', -1)
    sprite('null', 166)
    label(2)
    sprite('null', 25)
    label(8)
    sprite('vrdmy_kk400', 1)
    clearUponHandler(EVERY_FRAME)
    SetScaleX(4000)
    SetScaleY(2000)
    ScreenShake(20000, 20000)
    CreateParticle('kkef400addatk_02', -1)
    CommonSE('016_explode_1')
    PrivateSE('kkse_16')


@State
def efkk400_Handarame():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(45000)
        Size(700)
        LinkParticle('kkef400arame_04')
    sprite('null', 30)
    PrivateSE('kkse_21')
    sprite('null', 30)
    PrivateSE('kkse_21')
    sprite('null', 30)
    PrivateSE('kkse_21')
    sprite('null', 30)
    PrivateSE('kkse_21')
    label(0)
    sprite('null', 15)
    PrivateSE('kkse_21')
    loopRest()
    gotoLabel(0)


@State
def efkk400_Hand01():

    def upon_IMMEDIATE():
        AddY(185000)
        AddX(95000)
    sprite('kk400_25z', 7)
    CreateObject('efkk400_Handjet', -1)
    CreateParticle('kkef400rokepanimp_01', -1)
    physicsXImpulse(1500)
    sprite('kk400_25z', 7)
    CreateObject('efkk401_hand01smoke', -1)
    physicsXImpulse(3000)
    sprite('kk400_25z', 15)
    physicsXImpulse(75000)


@State
def efkk401_hand01smoke():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 2)
    label(0)
    sprite('null', 2)
    CreateParticle('kkef400rokepankidou_02', -1)
    gotoLabel(0)


@State
def efkk400_Handjet():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(26500)
        AddX(-80000)
        Size(1200)
        RotationAngle(90000)
        LinkParticle('kkef401micilefire_mato')
    label(0)
    sprite('null', 32767)


@State
def efkk400_CircleRenzok():

    def upon_IMMEDIATE():
        pass
    sprite('null', 10)
    CreateParticle('kkef400asimotofire_01', -1)
    CreateObject('efkk400_CircleFire01', -1)
    sprite('null', 6)
    CreateObject('efkk400_CircleFire00', -1)


@State
def efkk400_CircleFire00():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        AlphaValue(200)
        AddX(100000)
        AddY(-7000)
        Size(1200)
    sprite('vrkkef400_30', 3)
    sprite('vrkkef400_31', 3)
    sprite('vrkkef400_32', 3)
    sprite('vrkkef400_33', 3)
    sprite('vrkkef400_34', 3)
    sprite('vrkkef400_35', 3)
    sprite('vrkkef400_36', 3)


@State
def efkk400_CircleFire01():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        AddX(250000)
        AddY(-7000)
        AlphaValue(200)
        Size(1000)
    sprite('vrkkef400_30', 3)
    sprite('vrkkef400_31', 3)
    sprite('vrkkef400_32', 3)
    sprite('vrkkef400_33', 3)
    sprite('vrkkef400_34', 3)
    sprite('vrkkef400_35', 3)
    sprite('vrkkef400_36', 3)


@State
def Warp01():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        RemoveOnCallStateEnd(3)
    sprite('kk404_00', 2)
    sprite('kk404_01', 3)
    sprite('kk404_02', 3)
    CreateParticle('kkef_404', 0)
    sprite('kk404_03', 3)
    CreateParticle('kkef_404', 0)
    sprite('kk404_04', 3)
    CreateParticle('kkef_404', 0)
    sprite('kk404_05', 3)
    CreateParticle('kkef_404', 0)
    sprite('kk404_06', 3)
    CreateParticle('kkef_404', 0)
    CreateParticle('kkef_404_3', 1)
    sprite('kk404_07', 3)
    sprite('kk404_08', 3)
    sprite('kk404_09', 3)


@State
def efkk_UltraSokidan_Hontai():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        SLOT_53 = 1
        callSubroutine('Fireball_Hontai')
        AttackLevel_(3)
        Damage(360)
        AttackP1(80)
        AttackP2(60)
        SingleProration(1)
        Hitstop(3)
        AirPushbackY(18000)
        AirPushbackX(3000)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        UseFireHitspark(1)
        AttackDirection(0)
        StarterRating(2)
        MinimumDamage(15)
        Size(5000)
        CreateObject('efkk_430Start', -1)
        if SLOT_137:
            DamageMultiplier(80)
    label(10)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    AddY(150000)
    physicsYImpulse(40000)
    physicsXImpulse(2000)
    setGravity(1000)
    CreateObject('efkk_UltrafireRotate', -1)
    CreateObject('efkk_UltraFireBallroop', -1)
    Size(1600)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(20)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    AddY(150000)
    physicsYImpulse(60000)
    physicsXImpulse(4000)
    setGravity(1000)
    CreateObject('efkk_UltrafireRotate', -1)
    CreateObject('efkk_UltraFireBallroop', -1)
    Size(1600)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(30)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    AddY(150000)
    physicsYImpulse(80000)
    physicsXImpulse(8000)
    setGravity(1000)
    CreateObject('efkk_UltrafireRotate', -1)
    CreateObject('efkk_UltraFireBallroop', -1)
    Size(1600)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(5)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    CreateObject('efkk_UltrafireDust00', -1)
    if SLOT_95:
        CallCustomizableParticle('kkef402jizoku_00_2p', -1)
    else:
        CallCustomizableParticle('kkef402jizoku_00', -1)
    ParticleSize(1500)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    CreateObject('efkk_fireDust01', -1)
    gotoLabel(5)
    label(1)
    sprite('vrkkef402Atk', 2)
    SLOT_55 = 14
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1500)
    ResetAttackP2()
    SingleProration(0)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(90)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    Hitstop(5)
    EnemyHitstopAddition(10, 10, 10)
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CallCustomizableParticle('kkef402jizoku_00_2p', -1)
    else:
        CallCustomizableParticle('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust01', -1)
    label(2)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CallCustomizableParticle('kkef402jizoku_00_2p', -1)
    else:
        CallCustomizableParticle('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust01', -1)
    SLOT_55 = SLOT_55 + -1
    if not SLOT_55:
        notConditionalSendToLabel(99)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 3)
    SetActionMark(0)
    EndMomentum(1)
    TriggerUponForState('efkk_UltrafireRotate', 32)
    TriggerUponForState('efkk_UltraFireBallroop', 32)
    CreateObject('efkk_UltraFireBallBrake', -1)
    RandAddRotation(0, 360000)
    AddScale(200)
    sprite('null', 3)
    if SLOT_95:
        CreateParticle('kkef402hit_03_2p', -1)
    else:
        CreateParticle('kkef402hit_03', -1)
    CreateObject('efkk_fireDust01', -1)
    CreateObject('efkk_fireDust02', -1)


@State
def efkk_UltraSokidan_Hontai_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        SLOT_54 = 1
        callSubroutine('Fireball_Hontai')
        AttackLevel_(3)
        Damage(360)
        AttackP1(80)
        AttackP2(60)
        SingleProration(1)
        Hitstop(3)
        AirPushbackY(18000)
        AirPushbackX(3000)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        UseFireHitspark(1)
        AttackDirection(0)
        AttackType(4)
        StarterRating(2)
        MinimumDamage(15)
        Size(5000)
        CreateObject('efkk_430Start', -1)
        if SLOT_137:
            DamageMultiplier(80)
    label(10)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    AddY(150000)
    physicsYImpulse(40000)
    physicsXImpulse(2000)
    setGravity(1000)
    CreateObject('efkk_UltrafireRotate', -1)
    CreateObject('efkk_UltraFireBallroop', -1)
    Size(1600)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(20)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    AddY(150000)
    physicsYImpulse(60000)
    physicsXImpulse(4000)
    setGravity(1000)
    CreateObject('efkk_UltrafireRotate', -1)
    CreateObject('efkk_UltraFireBallroop', -1)
    Size(1600)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(30)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    AddY(150000)
    physicsYImpulse(80000)
    physicsXImpulse(8000)
    setGravity(1000)
    CreateObject('efkk_UltrafireRotate', -1)
    CreateObject('efkk_UltraFireBallroop', -1)
    Size(1600)
    SetActionMark(1)
    loopRest()
    gotoLabel(5)
    label(5)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    CreateObject('efkk_UltrafireDust00', -1)
    if SLOT_95:
        CallCustomizableParticle('kkef402jizoku_00_2p', -1)
    else:
        CallCustomizableParticle('kkef402jizoku_00', -1)
    ParticleSize(1500)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    CreateObject('efkk_fireDust01', -1)
    gotoLabel(5)
    label(1)
    sprite('vrkkef402Atk', 2)
    SLOT_55 = 14
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2000)
    ResetAttackP2()
    SingleProration(0)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(90)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    Hitstop(5)
    EnemyHitstopAddition(10, 10, 10)
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CallCustomizableParticle('kkef402jizoku_00_2p', -1)
    else:
        CallCustomizableParticle('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust01', -1)
    label(2)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust00', -1)
    if SLOT_95:
        CallCustomizableParticle('kkef402jizoku_00_2p', -1)
    else:
        CallCustomizableParticle('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    CreateObject('efkk_fireDust01', -1)
    SLOT_55 = SLOT_55 + -1
    if not SLOT_55:
        notConditionalSendToLabel(99)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 3)
    SetActionMark(0)
    EndMomentum(1)
    RandAddRotation(0, 360000)
    AddScale(200)
    TriggerUponForState('efkk_UltrafireRotate', 32)
    TriggerUponForState('efkk_UltraFireBallroop', 32)
    CreateObject('efkk_UltraFireBallBrake', -1)
    sprite('null', 3)
    if SLOT_95:
        CreateParticle('kkef402hit_03_2p', -1)
    else:
        CreateParticle('kkef402hit_03', -1)
    CreateObject('efkk_fireDust01', -1)
    CreateObject('efkk_fireDust02', -1)


@State
def efkk_UltrafireDust00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1600)
        AlphaValue(150)
        if SLOT_95:
            Eff3DEffect('kkef402_fire03_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire03', '')
            FaceSpawnLocation()
    sprite('null', 10)
    SetScaleSpeed(-30)
    AddRotationPerFrame(-5000)
    RandAddRotation(0, 360000)


@State
def efkk_430Start():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(2000)
        if SLOT_95:
            Eff3DEffect('kkef402_fire00_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire00', '')
            FaceSpawnLocation()
    sprite('null', 5)
    ParticleSize(1500)
    if SLOT_95:
        CreateParticle('kkef402star_fire_2p', -1)
    else:
        CreateParticle('kkef402star_fire', -1)
    sprite('null', 5)
    CreateObject('efkk_430Start02', -1)
    sprite('null', 10)
    AlphaValue(0)
    CreateObject('efkk_430Start01', -1)


@State
def efkk_430Start01():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(2000)
        if SLOT_95:
            Eff3DEffect('kkef402_fire01_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire01', '')
            FaceSpawnLocation()
    sprite('null', 10)


@State
def efkk_430Start02():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(500)
        if SLOT_95:
            Eff3DEffect('kkef430_fireballstart00_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef430_fireballstart00', '')
            FaceSpawnLocation()
    sprite('null', 5)
    SetScaleSpeed(200)
    sprite('null', 5)
    SetScaleSpeed(0)


@State
def efkk_UltraFireBallroop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        RenderLayer(3)
        Size(1300)
        if SLOT_95:
            PaletteIndex(4)
        else:
            PaletteIndex(2)
        uponSendToLabel(32, 1)
    sprite('vrkkef402_00', 1)
    label(0)
    sprite('vrkkef402_00', 3)
    PrivateSE('kkse_13')
    sprite('vrkkef402_01', 3)
    sprite('vrkkef402_02', 3)
    sprite('vrkkef402_03', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    AlphaValue(0)


@State
def efkk_UltrafireRotate():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(1300)
        if SLOT_95:
            Eff3DEffect('kkef430_fireball00_2p', '')
        else:
            Eff3DEffect('kkef430_fireball00', '')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    AddRotationPerFrame(1000)
    label(0)
    sprite('null', 5)
    SetScaleSpeed(40)
    ConstantAlphaModifier(-26)


@State
def efkk_UltraFireBallBrake():

    def upon_IMMEDIATE():
        if SLOT_95:
            Eff3DEffect('kkef402_fire04_2p', '')
            FaceSpawnLocation()
        else:
            Eff3DEffect('kkef402_fire04', '')
            FaceSpawnLocation()
    sprite('null', 7)


@State
def efkk401_Kakyufire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('kkef401micilefire_mato')
        Size(1000)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 15)
    ConstantAlphaModifier(51)
    label(0)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(-50)


@State
def efkk_AtkGravityBall():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('efkk_AtkGravityBallexe', 3, 0, 0)
        PreventBlocking(1)
        OnlyHitPlayer(1)
        PassByArmor(1)
        PreventAirborneHit(0)
        ThrowTechWindow(-1)
        RangeCheck(80000)
        DistanceCheck(80000, -80000, -1, -1)
        AttackP2(60)
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
        PaletteIndex(2)
        RenderLayer(1)
        AddY(200000)
        AddX(700000)
        PhysicsPull(999, 8000, 8000)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(3)
            NoAttackDuringAction(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            NoAttackDuringAction(1)
            ObjectUpon(EVERY_FRAME, 41)
    sprite('null', 4)
    sprite('vrkkef431_00', 3)
    PrivateSE('kkse_26')
    sprite('vrkkef431_01', 3)
    sprite('vrkkef431_02', 3)
    sprite('vrkkef431_03', 3)
    sprite('vrkkef431_04', 3)
    sprite('vrkkef431_05', 3)
    CreateObject('efkk_GravityAura01', -1)
    CreateObject('efkk_HandMato', -1)
    label(1)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    PrivateSE('kkse_27')
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    loopRest()
    gotoLabel(1)
    label(3)
    sprite('vrkkef431_09', 3)
    TriggerUponForState('efkk_HandMato', 33)
    TriggerUponForState('efkk_GravityAura01', 32)
    PhysicsPull(0, 0, 0)
    sprite('vrkkef431_10', 3)
    sprite('vrkkef431_11', 3)
    sprite('vrkkef431_12', 3)
    label(4)
    sprite('null', 3)


@State
def efkk_AtkGravityBallexe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        RenderLayer(3)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        YImpulseBeforeWallbounce(1400)
        AirPushbackX(0)
        Hitstop(0)
        AirHitstunAnimation(11)
        AirUntechableTime(100)
        HardKnockdown(1)
        DamageEffect(9, '')
        CameraControlEnable(1)
        CameraPosition(800)
        HeatCooldown(240)
        WallCollisionDetection(1)
    sprite('keep', 9)
    AttackOff()
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    TriggerUponForState('efkk_GravityAura01', 32)
    TriggerUponForState('efkk_HandMato', 32)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    PrivateSE('kkse_15')

    def RunOnObject_22():
        SetScaleSpeed(-9)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)

    def RunOnObject_22():
        CharacterFlash(16777215, 6, 6)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_09', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    TriggerUponForState('efkk_HandMato', 34)
    DisableOppSprite(0)
    CameraPosition(1250)
    TriggerUponForState('UltimateBlackhole', 35)
    sprite('vrkkef431_10', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('vrkkef431_11', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 24)
    AlphaValue(0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)

    def RunOnObject_22():
        AddY(1000000)
    if random_(2, 0, 50):
        conditionalSendToLabel(9)
    sprite('vrkkef431_12', 1)
    if random_(2, 0, 50):
        conditionalSendToLabel(9)
    sprite('vrkkef431_12', 1)
    if random_(2, 0, 50):
        conditionalSendToLabel(9)
    label(9)
    sprite('vrkkef431_08', 3)
    DisableOppSprite(1)
    RefreshMultihit()
    HitAnywhere(1)
    CreateObject('efkk_AtkGravityBallexe2nd', -1)
    sprite('vrkkef431_08', 5)
    StartMultihit()
    CameraControlEnable(0)


@State
def efkk_AtkGravityBallexe2nd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(0)
        Damage(1200)
        MinimumDamage(100)
        AttackP2(100)
        AirHitstunAnimation(11)
        AirPushbackY(-200000)
        Hitstop(0)
        DamageEffect(9, '')
        DefeatOpponentBehavior(1)
        NoAttackDuringAction(1)
        IgnorePauses(22)
        IgnoreScreenfreeze(1)
        ExternalForcesRate(0, 0)
        AbsoluteY(50000)

        def upon_OPPONENT_HIT():
            AltKnockdownEffects(104, 1, 1)
            ScreenShake(0, 10000)

        def upon_EVERY_FRAME():
            if random_(2, 0, 50):
                NoAttackDuringAction(0)
                RefreshMultihit()
    sprite('vrkkef431Atk', 33)
    sprite('vrkkef431Atk', 33)
    CancelIfPlayerHit(22)


@State
def efkk_HandMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        RenderLayer(1)
        Flip()
        AddX(60000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        Visibility(1)
    sprite('null', 4)
    sprite('vrkkef431_40', 32767)
    CreateObject('efkk_HandRing', -1)
    label(0)
    sprite('vrkkef431_40', 32767)
    TriggerUponForState('efkk_HandRing', 32)
    gotoLabel(2)
    label(1)
    sprite('vrkkef431_40', 5)
    TriggerUponForState('efkk_HandRing', 33)
    label(2)
    sprite('null', 1)


@State
def efkk_HandRing():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        BlendMode_Normal()
        RenderLayer(4)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        Visibility(1)
    sprite('vrkkef431_41', 7)
    sprite('vrkkef431_41', 7)
    CharacterFlash(16777215, 15, 1)
    label(0)
    sprite('vrkkef431_41', 2)
    AddY(2000)
    sprite('vrkkef431_41', 2)
    AddY(-2000)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    LinkParticle('kkef_gravityring_02')
    Eff3DEffect('kkef431_rotatering00', '')
    AddX(-55000)
    CharacterFlash(0, 10, 1)
    Size(200)
    SetScaleSpeed(25)
    sprite('null', 10)
    ScreenShake(40000, 4000)
    SetScaleSpeed(75)
    sprite('null', 20)
    SetScaleSpeed(0)
    sprite('null', 25)
    SetScaleSpeed(-25)
    sprite('null', 25)
    sprite('null', 5)
    CharacterFlash(16777215, 5, 1)
    gotoLabel(3)
    label(2)
    sprite('vrkkef431_41', 5)
    CharacterFlash(0, 5, 1)
    label(3)
    sprite('null', 1)


@State
def efkk_GravityAura01():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef431_backaura00', '')
        FaceSpawnLocation()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        uponSendToLabel(32, 1)
        Size(400)
    label(0)
    sprite('null', 9)
    CreateParticle('kkef431aura_minisubpos', -1)
    CreateObject('efkk_GravityYugami', -1)
    AddRotationPerFrame(600)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    CreateObject('efkk_GravityYugami', -1)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def efkk_GravityYugami():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ParticleTransparency(1)
        PlayerTransparency(60000)
        Size(2400)
    sprite('vrdist00', 20)
    SetScaleSpeed(-65)
    RotationSomething(3000)
    RandAddRotation(-90000, 90000)


@State
def efkk_GravityBall():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 3)
        AddY(167000)
        AddX(100000)
        RenderLayer(3)
    sprite('null', 10)
    sprite('vrkkef431_00', 4)
    PrivateSE('kkse_26')
    sprite('vrkkef431_01', 4)
    sprite('vrkkef431_02', 4)
    sprite('vrkkef431_03', 4)
    sprite('vrkkef431_04', 4)
    sprite('vrkkef431_05', 32767)
    SetScaleSpeed(-1)
    label(1)
    sprite('vrkkef431_06', 3)
    Size(1000)
    physicsXImpulse(-6000)
    PrivateSE('kkse_27')
    sprite('vrkkef431_07', 3)
    physicsXImpulse(0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_GravityAura00', -1)
    label(2)
    sprite('vrkkef431_06', 3)
    CreateParticle('kkef431aura_00', -1)
    CreateObject('efkk_Gravitythunder00', -1)
    PrivateSE('kkse_27')
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    gotoLabel(2)
    label(3)
    sprite('vrkkef431_09', 3)
    TriggerUponForState('efkk_GravityAura00', 32)
    sprite('vrkkef431_10', 3)
    sprite('vrkkef431_11', 3)
    sprite('vrkkef431_12', 3)


@State
def efkk_Gravitythunder00():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef431_randthunder00', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(191)
    sprite('null', 2)
    AlphaValue(255)
    RandAddScale(-600, 300)
    RandAddRotation(0, 360000)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(255)
    sprite('null', 2)
    AlphaValue(0)


@State
def efkk_Gravitythunder01():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef431_randthunder00', '')
        FaceSpawnLocation()
        PaletteIndex(2)
        ColorFromPaletteIndex(191)
        BlendMode_Normal()
    sprite('null', 4)
    AlphaValue(0)
    RandAddRotation(0, 360000)
    sprite('null', 1)
    AlphaValue(255)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 1)
    AlphaValue(255)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 1)
    AlphaValue(255)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 1)
    AlphaValue(255)


@State
def efkk_Gravitythunder02():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef431_randthunder00', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(191)
    sprite('null', 8)
    RandAddScale(-600, 300)
    RandAddRotation(0, 360000)


@State
def efkk_GravityAura00():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef431_backaura00', '')
        FaceSpawnLocation()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
        Size(800)
        RenderLayer(2)
    sprite('null', 32767)
    AddRotationPerFrame(600)
    label(0)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def efkk_AtkGravityBall_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('efkk_AtkGravityBallexe_OD', 3, 0, 0)
        PreventBlocking(1)
        OnlyHitPlayer(1)
        PassByArmor(1)
        PreventAirborneHit(0)
        ThrowTechWindow(-1)
        RangeCheck(80000)
        DistanceCheck(80000, -80000, -1, -1)
        AttackP2(60)
        IgnoreScreenfreeze(1)
        CancelIfPlayerHit(3)
        PaletteIndex(2)
        RenderLayer(1)
        AddY(200000)
        AddX(700000)
        WallCollisionDetection(1)
        PhysicsPull(999, 12000, 12000)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(3)
            NoAttackDuringAction(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            NoAttackDuringAction(1)
            ObjectUpon(EVERY_FRAME, 41)
    sprite('null', 4)
    sprite('vrkkef431_00', 3)
    PrivateSE('kkse_26')
    sprite('vrkkef431_01', 3)
    sprite('vrkkef431_02', 3)
    sprite('vrkkef431_03', 3)
    sprite('vrkkef431_04', 3)
    sprite('vrkkef431_05', 3)
    CreateObject('efkk_GravityAura01', -1)
    CreateObject('efkk_HandMato', -1)
    label(1)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    PrivateSE('kkse_27')
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    loopRest()
    gotoLabel(1)
    label(3)
    sprite('vrkkef431_09', 3)
    TriggerUponForState('efkk_HandMato', 33)
    TriggerUponForState('efkk_GravityAura01', 32)
    PhysicsPull(0, 0, 0)
    sprite('vrkkef431_10', 3)
    sprite('vrkkef431_11', 3)
    sprite('vrkkef431_12', 3)
    label(4)
    sprite('null', 3)


@State
def efkk_AtkGravityBallexe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(3, 0, 0)
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        RenderLayer(3)
        WallCollisionDetection(1)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        YImpulseBeforeWallbounce(1400)
        AirPushbackX(0)
        Hitstop(0)
        AirHitstunAnimation(11)
        AirUntechableTime(100)
        HardKnockdown(1)
        DamageEffect(9, '')
        CameraControlEnable(1)
        CameraPosition(800)
        HeatCooldown(240)
    sprite('keep', 9)
    AttackOff()
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    TriggerUponForState('efkk_GravityAura01', 32)
    TriggerUponForState('efkk_HandMato', 32)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    PrivateSE('kkse_15')

    def RunOnObject_22():
        SetScaleSpeed(-9)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    CreateObject('efkk_Gravitythunder02', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    CreateObject('efkk_Gravitythunder00', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)

    def RunOnObject_22():
        CharacterFlash(16777215, 6, 6)
    sprite('vrkkef431_08', 3)
    CreateObject('efkk_Gravitythunder01', -1)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    sprite('vrkkef431_09', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(1, 1, 1, 0, 0)
    TriggerUponForState('efkk_HandMato', 34)
    DisableOppSprite(0)
    CameraPosition(1250)
    TriggerUponForState('UltimateBlackhole_OD', 35)
    sprite('vrkkef431_10', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('vrkkef431_11', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 3)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 24)
    AlphaValue(0)
    OppThrowAnimation(0, 0)
    OppThrowPosition(0, 4, 4, 0, 0)

    def RunOnObject_22():
        AddY(1000000)
    if random_(2, 0, 50):
        conditionalSendToLabel(9)
    sprite('vrkkef431_12', 1)
    if random_(2, 0, 50):
        conditionalSendToLabel(9)
    sprite('vrkkef431_12', 1)
    if random_(2, 0, 50):
        conditionalSendToLabel(9)
    label(9)
    sprite('vrkkef431_08', 3)
    DisableOppSprite(1)
    RefreshMultihit()
    HitAnywhere(1)
    CreateObject('efkk_AtkGravityBallexe2nd_OD', -1)
    sprite('vrkkef431_08', 5)
    StartMultihit()
    CameraControlEnable(0)


@State
def efkk_AtkGravityBallexe2nd_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(0)
        Damage(1800)
        MinimumDamage(100)
        AirHitstunAnimation(11)
        AirPushbackY(-200000)
        AttackP2(100)
        Hitstop(0)
        DamageEffect(9, '')
        DefeatOpponentBehavior(1)
        AttackType(4)
        NoAttackDuringAction(1)
        WallCollisionDetection(1)
        IgnorePauses(22)
        IgnoreScreenfreeze(1)
        ExternalForcesRate(0, 0)
        AbsoluteY(50000)

        def upon_OPPONENT_HIT():
            KnockdownEffects(104, 1, 1)
            AltKnockdownEffects(104, 1, 1)
            ScreenShake(0, 10000)

        def upon_EVERY_FRAME():
            if random_(2, 0, 50):
                NoAttackDuringAction(0)
                RefreshMultihit()
    sprite('vrkkef431Atk', 33)
    sprite('vrkkef431Atk', 33)
    CancelIfPlayerHit(22)


@State
def vrkkef432_Land():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        SetZVal(100)
        AddX(110000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(PLAYER_DAMAGED, 1)
    sprite('null', 10)
    sprite('vrkkef432_Land00', 3)
    sprite('vrkkef432_Land01', 3)
    sprite('vrkkef432_Land02', 3)
    sprite('vrkkef432_Land03', 3)
    sprite('vrkkef432_Land04', 3)
    sprite('vrkkef432_Land05', 32767)
    label(0)
    sprite('vrkkef432_Land06', 32767)
    label(1)
    sprite('vrkkef432_Land06', 3)
    E0EAEffectPosition(0)
    clearUponHandler(PLAYER_DAMAGED)
    sprite('vrkkef432_Land07', 3)
    sprite('vrkkef432_Land08', 3)
    sprite('vrkkef432_Land09', 3)
    sprite('vrkkef432_Land10', 3)
    sprite('vrkkef432_Land00', 30)


@State
def vrkkef432_Air():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        SetZVal(100)
        AddX(110000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(PLAYER_DAMAGED, 1)
        RunLoopUpon(17, 550)
        uponSendToLabel(17, 1)
    sprite('vrkkef432_Air00', 15)
    Unknown23123(16777215, 12)
    AddY(-90000)
    physicsYImpulse(6000)
    CreateObject('efkk432_burner1', 0)
    CreateObject('efkk432_burner2', 1)
    CreateObject('efkk432_burner3', 2)
    sprite('vrkkef432_Air00a', 10)
    physicsYImpulse(0)
    sprite('vrkkef432_Air01', 3)
    sprite('vrkkef432_Air02', 3)
    sprite('vrkkef432_Air03', 3)
    sprite('vrkkef432_Air04', 3)
    sprite('vrkkef432_Air05', 32767)
    label(0)
    sprite('vrkkef432_Air06', 32767)
    label(1)
    sprite('vrkkef432_Air06', 3)
    E0EAEffectPosition(0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(17)
    sprite('vrkkef432_Air07', 3)
    sprite('vrkkef432_Air08', 3)
    sprite('vrkkef432_Air09', 3)
    sprite('vrkkef432_Air10', 3)
    sprite('vrkkef432_Air00', 10)
    sprite('vrkkef432_Air00', 20)
    TriggerUponForState('efkk432_burner1', 32)
    TriggerUponForState('efkk432_burner2', 32)
    TriggerUponForState('efkk432_burner3', 32)
    ConstantAlphaModifier(-10)


@State
def efkk432_burner1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('kkef432micilefire_mato')
        Size(700)
        RotationAngle(0)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 16)
    ConstantAlphaModifier(16)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-25)
    SetScaleSpeed(-21)


@State
def efkk432_burner2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('kkef432micilefire_mato')
        Size(625)
        RotationAngle(-11250)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 16)
    ConstantAlphaModifier(16)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-25)
    SetScaleSpeed(-20)


@State
def efkk432_burner3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        LinkParticle('kkef432micilefire_mato')
        Size(625)
        RotationAngle(11250)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 16)
    ConstantAlphaModifier(16)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-25)
    SetScaleSpeed(-20)


@State
def efkk_BigTager():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        PaletteIndex(6)
        SetZVal(500)
        AddX(0)
        AddY(25000)
        Size(1000)

        def upon_41():
            EnableCollision(1)
            SetYCollisionFromOrigin(400)
            SetXCollisionFromOrigin(200)
            PreventSelfPush(1)

        def upon_STATE_END():
            EnableCollision(0)
            SetYCollisionFromOrigin(-1)
            SetXCollisionFromOrigin(-1)
            PreventSelfPush(0)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        uponSendToLabel(PLAYER_DAMAGED, 2)
        RunLoopUpon(17, 550)
        uponSendToLabel(17, 2)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    CommonSE('019_quake_1')
    CreateObject('efkk_TagerHole', -1)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    sprite('kk432tgcutin_20', 4)
    ScreenShake(1000, 4000)
    CommonSE('019_quake_1')
    PrivateSE('kkse_16')
    PrivateSE('kkse_16')
    sprite('kk432tgcutin_21', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_23', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_24', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_25', 4)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_26', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_00', 12)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_01', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_02', 4)
    label(0)
    sprite('kk432tgcutin_03', 32767)
    CreateObject('efkk_BeamCharge', -1)
    label(1)
    sprite('kk432tgcutin_03', 1)
    TriggerUponForState('efkk_BeamCharge', 32)
    sprite('kk432tgcutin_03', 32767)
    CreateObject('efkk_Beam00', -1)
    label(99)
    sprite('null', 4)
    sprite('kk432tgcutin_20', 4)
    ScreenShake(1000, 4000)
    CommonSE('019_quake_1')
    PrivateSE('kkse_16')
    PrivateSE('kkse_16')
    sprite('kk432tgcutin_21', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_23', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_24', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_25', 4)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_26', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_00', 10)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_01', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_02', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('kk432tgcutin_02', 4)
    E0EAEffectPosition(0)
    EnableCollision(0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(17)
    sprite('kk432tgcutin_01', 4)
    sprite('kk432tgcutin_00', 4)
    sprite('kk432tgcutin_26', 4)
    TriggerUponForState('efkk_TagerHole', 32)
    ScreenShake(5500, 5500)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_25', 4)
    sprite('kk432tgcutin_24', 4)
    ScreenShake(5500, 5500)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_23', 4)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(5500, 5500)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_21', 4)
    sprite('kk432tgcutin_20', 4)
    ScreenShake(5500, 5500)
    sprite('null', 15)


@State
def efkk_TagerHole():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        BlendMode_Sub()
        SetZVal(500)
        LinkParticle('kkef430_02')
        Size(1300)
        AddX(-300000)
        uponSendToLabel(32, 0)
    sprite('vrkkef432_bloom', 40)
    sprite('vrkkef432_bloom', 10)
    SetScaleXPerFrame(-60)
    physicsXImpulse(24000)
    sprite('vrkkef432_bloom', 32767)
    SetScaleXPerFrame(0)
    physicsXImpulse(0)
    label(0)
    sprite('vrkkef432_bloom', 3)
    SetScaleXPerFrame(60)
    physicsXImpulse(-40000)
    sprite('vrkkef432_bloom', 5)
    SetScaleXPerFrame(0)
    sprite('vrkkef432_bloom', 15)
    physicsXImpulse(0)
    sprite('vrkkef432_bloom', 4)
    CreateParticle('kkef430_end', -1)
    ConstantAlphaModifier(-32)
    SetScaleSpeed(-50)


@State
def efkk_Beam00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        Eff3DEffect('kkef432_beam00', '')
        FaceSpawnLocation()
        Size(2000)
        AddY(300000)
        AddX(150000)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    ScreenShake(150000, 150000)
    label(0)
    sprite('null', 1)
    CreateParticle('kkef432_beamcircle01', -1)
    SetScaleY(2000)
    CreateObject('efkk_Beamthunder00', -1)
    PrivateSE('kkse_18')
    sprite('null', 1)
    SetScaleY(1900)
    CreateObject('efkk_Beamthunder01', -1)
    sprite('null', 1)
    SetScaleY(1950)
    CreateObject('efkk_Beamthunder02', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    CreateParticle('kkef432_beamend_flash', -1)
    AlphaValue(230)


@State
def efkk_Beamthunder00():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 2)
    AlphaValue(255)
    RandAddScale(0, 600)
    RandAddRotation(0, 360000)


@State
def efkk_Beamthunder01():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        Flip()
        BlendMode_Normal()
    sprite('null', 4)
    AlphaValue(255)
    RandAddScale(0, 600)
    RandAddRotation(0, 360000)


@State
def efkk_Beamthunder02():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 2)
    RandAddScale(0, 600)
    RandAddRotation(0, 360000)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(255)


@State
def efkk_Beamthunder03():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef431_randthunder00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 2)
    AlphaValue(255)
    RandAddScale(-600, 300)
    RandAddRotation(0, 360000)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(255)
    sprite('null', 2)
    AlphaValue(0)


@State
def efkk_BeamCharge():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddY(300000)
        AddX(150000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 3)
    CreateObject('efkk_Beamthunder02', -1)
    PrivateSE('kkse_17')

    def RunOnObject_1():
        AlphaValue(150)
    CreateObject('efkk_BeamCharge00', -1)
    CreateParticle('kkef432charge_sub', -1)
    sprite('null', 3)
    CreateObject('efkk_Beamthunder03', -1)

    def RunOnObject_1():
        AlphaValue(150)
    sprite('null', 4)
    CreateObject('efkk_Beamthunder03', -1)

    def RunOnObject_1():
        AlphaValue(150)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def efkk_BeamCharge00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('kkef432_charge00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Size(800)
        AlphaValue(0)
    sprite('null', 10)
    SetScaleSpeed(-40)
    ConstantAlphaModifier(26)
    AddRotationPerFrame(6000)
    RandAddRotation(0, 360000)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def efkk_BigTagerAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(5)
        Damage(300)
        MinimumDamage(5)
        AttackP2(97)
        ChipPercentage(10)
        AirUntechableTime(100)
        HardKnockdown(1)
        Hitstop(0)
        AirPushbackX(100000)
        AirPushbackY(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickDuration(50)
        OppPositionOnHit(1, 1000000, 120000)
        HitsparkSize(300)
        PassByArmor(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SetActionMark(1)
            ObjectUpon(EVERY_FRAME, 32)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1

        def upon_EVERY_FRAME():
            if SLOT_51 <= 20:
                Damage(300)
            else:
                if SLOT_51 > 20:
                    Damage(260)
                if SLOT_51 > 40:
                    Damage(220)
                if SLOT_51 > 60:
                    Damage(180)
                    MinimumDamage(20)
                if SLOT_51 > 80:
                    Damage(140)
                    MinimumDamage(20)
                if SLOT_51 > 100:
                    Damage(100)
                    MinimumDamage(20)
            if SLOT_2:
                OppPositionOnHit(3, 5000, 0)

        def upon_33():
            pass
        uponSendToLabel(32, 0)
    label(1)
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    DamageEffect(0, 'ef_exhit_sub')
    GuardEffect(0, 'ef_girds')
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    DamageEffect(0, 'ef_exhit_sub')
    GuardEffect(0, 'ef_girds')
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()


@State
def efkk_ODBigTager():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        PaletteIndex(6)
        SetZVal(500)
        AddX(0)
        AddY(25000)
        Size(1000)

        def upon_41():
            EnableCollision(1)
            SetYCollisionFromOrigin(400)
            SetXCollisionFromOrigin(200)
            PreventSelfPush(1)

        def upon_STATE_END():
            EnableCollision(0)
            SetYCollisionFromOrigin(-1)
            SetXCollisionFromOrigin(-1)
            PreventSelfPush(0)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        uponSendToLabel(PLAYER_DAMAGED, 2)
        RunLoopUpon(17, 550)
        uponSendToLabel(17, 2)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    CommonSE('019_quake_1')
    CreateObject('efkk_TagerHole', -1)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    sprite('kk432tgcutin_30', 4)
    ScreenShake(1000, 4000)
    CommonSE('019_quake_1')
    PrivateSE('kkse_16')
    PrivateSE('kkse_16')
    sprite('kk432tgcutin_31', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_32', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_33', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_34', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_35', 4)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_36', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_04', 12)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_05', 4)
    ScreenShake(2000, 8000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_06', 4)
    label(0)
    sprite('kk432tgcutin_07', 32767)
    CreateObject('efkk_ODBeamCharge', -1)
    label(1)
    sprite('kk432tgcutin_07', 1)
    TriggerUponForState('efkk_ODBeamCharge', 32)
    sprite('kk432tgcutin_07', 32767)
    CreateObject('efkk_ODBeam00', -1)
    label(99)
    sprite('null', 4)
    sprite('kk432tgcutin_30', 4)
    ScreenShake(1000, 4000)
    CommonSE('019_quake_1')
    PrivateSE('kkse_16')
    PrivateSE('kkse_16')
    sprite('kk432tgcutin_31', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_33', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_34', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_35', 4)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_36', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_04', 10)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_05', 4)
    ScreenShake(2000, 6000)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_06', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('kk432tgcutin_06', 4)
    E0EAEffectPosition(0)
    EnableCollision(0)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(17)
    sprite('kk432tgcutin_05', 4)
    sprite('kk432tgcutin_04', 4)
    sprite('kk432tgcutin_36', 4)
    TriggerUponForState('efkk_TagerHole', 32)
    ScreenShake(5500, 5500)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_35', 4)
    sprite('kk432tgcutin_34', 4)
    ScreenShake(5500, 5500)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_33', 4)
    sprite('kk432tgcutin_32', 4)
    ScreenShake(5500, 5500)
    CommonSE('019_quake_1')
    sprite('kk432tgcutin_31', 4)
    sprite('kk432tgcutin_30', 4)
    ScreenShake(5500, 5500)


@State
def efkk_ODBeam00():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Normal()
        Eff3DEffect('kkef432_beam01', '')
        FaceSpawnLocation()
        Size(2000)
        AddY(300000)
        AddX(150000)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    ScreenShake(150000, 150000)
    label(0)
    sprite('null', 1)
    CreateParticle('kkef432_beamcircle01', -1)
    SetScaleY(2000)
    CreateObject('efkk_ODBeamthunder00', -1)
    PrivateSE('kkse_18')
    sprite('null', 1)
    SetScaleY(1900)
    CreateObject('efkk_ODBeamthunder01', -1)
    sprite('null', 1)
    SetScaleY(1950)
    CreateObject('efkk_ODBeamthunder02', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    CreateParticle('kkef432_odbeamend_flash', -1)
    AlphaValue(230)


@State
def efkk_ODBeamthunder00():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder01', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 2)
    AlphaValue(255)
    RandAddScale(0, 600)
    RandAddRotation(0, 360000)


@State
def efkk_ODBeamthunder01():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder01', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        Flip()
        BlendMode_Normal()
    sprite('null', 4)
    AlphaValue(255)
    RandAddScale(0, 600)
    RandAddRotation(0, 360000)


@State
def efkk_ODBeamthunder02():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder01', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 2)
    RandAddScale(0, 600)
    RandAddRotation(0, 360000)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(255)


@State
def efkk_ODBeamthunder03():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder01', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
    sprite('null', 2)
    AlphaValue(255)
    RandAddScale(-600, 300)
    RandAddRotation(0, 360000)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(255)
    sprite('null', 2)
    AlphaValue(0)


@State
def efkk_ODBeamCharge():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddY(300000)
        AddX(150000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 3)
    CreateObject('efkk_ODBeamthunder02', -1)
    PrivateSE('kkse_17')

    def RunOnObject_1():
        AlphaValue(150)
    CreateObject('efkk_ODBeamCharge00', -1)
    CreateParticle('kkef432odcharge_sub', -1)
    sprite('null', 3)
    CreateObject('efkk_ODBeamthunder03', -1)

    def RunOnObject_1():
        AlphaValue(150)
    sprite('null', 4)
    CreateObject('efkk_ODBeamthunder03', -1)

    def RunOnObject_1():
        AlphaValue(150)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def efkk_ODBeamCharge00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('kkef432_charge01', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Size(800)
        AlphaValue(0)
    sprite('null', 10)
    SetScaleSpeed(-40)
    ConstantAlphaModifier(26)
    AddRotationPerFrame(6000)
    RandAddRotation(0, 360000)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def efkk_BigTagerAtk_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(5)
        Damage(200)
        MinimumDamage(5)
        AttackP2(97)
        ChipPercentage(10)
        AirUntechableTime(100)
        HardKnockdown(1)
        Hitstop(0)
        AirPushbackX(100000)
        AirPushbackY(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickDuration(50)
        OppPositionOnHit(1, 1000000, 120000)
        AttackType(4)
        HitsparkSize(300)
        PassByArmor(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(OPPONENT_HIT)
            SetActionMark(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            SLOT_51 = SLOT_51 + 1

        def upon_EVERY_FRAME():
            if SLOT_51 <= 20:
                Damage(300)
            else:
                if SLOT_51 > 20:
                    Damage(260)
                if SLOT_51 > 40:
                    Damage(220)
                if SLOT_51 > 60:
                    Damage(180)
                    MinimumDamage(20)
            if SLOT_2:
                OppPositionOnHit(3, 10000, 0)

        def upon_33():
            pass
        uponSendToLabel(32, 0)
    label(1)
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    DamageEffect(0, '')
    GuardEffect(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    gotoLabel(1)
    label(0)
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    DamageEffect(0, '')
    GuardEffect(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    DamageEffect(0, '')
    GuardEffect(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    GuardEffect(8, '')
    DamageEffect(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    DamageEffect(0, '')
    GuardEffect(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()


@State
def __450Cam():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        BlendMode_Normal()
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 0)
        CameraNoScreenCollision(1)
        CameraControlEnable(1)
        CameraNoCeiling(1)
    sprite('null', 32767)
    TeleportToObject(22)
    CameraPosition(1300)
    label(0)
    sprite('null', 60)
    CameraFast(1)
    TeleportToObject(3)
    AddX(200000)
    CameraPosition(1000)
    CreateObject('450Shake', -1)
    sprite('null', 10)
    CameraFast(0)
    CameraPosition(950)
    CommonSE('019_quake_1')
    CommonSE('019_quake_1')
    CommonSE('019_quake_0')
    sprite('null', 10)
    CameraPosition(925)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(900)
    sprite('null', 10)
    CameraPosition(875)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(850)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(825)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(800)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(775)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(750)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(725)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(700)
    sprite('null', 10)
    CameraPosition(675)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(650)
    sprite('null', 10)
    CameraPosition(625)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(600)
    sprite('null', 10)
    CameraPosition(575)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(550)
    sprite('null', 10)
    CameraPosition(525)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(500)
    sprite('null', 10)
    CameraPosition(475)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(450)
    sprite('null', 10)
    CameraPosition(425)
    CommonSE('019_quake_1')
    sprite('null', 10)
    CameraPosition(400)
    sprite('null', 15)
    CameraPosition(375)
    CommonSE('019_quake_1')
    sprite('null', 15)
    CameraPosition(350)
    sprite('null', 15)
    CameraPosition(325)
    CommonSE('019_quake_1')
    sprite('null', 15)
    CameraPosition(300)
    sprite('null', 15)
    CameraPosition(275)
    CommonSE('019_quake_1')
    sprite('null', 15)
    CameraPosition(250)
    sprite('null', 15)
    CameraPosition(225)
    CommonSE('019_quake_1')
    sprite('null', 15)
    CameraPosition(200)
    sprite('null', 15)
    CameraPosition(175)
    CommonSE('019_quake_1')
    sprite('null', 15)
    CameraPosition(150)
    sprite('null', 15)
    CameraPosition(125)
    CommonSE('019_quake_1')
    sprite('null', 32767)
    label(1)
    sprite('null', 3)
    CameraPosition(150)
    PrivateSE('kkse_29')
    PrivateSE('kkse_29')
    sprite('null', 3)
    CameraPosition(175)
    sprite('null', 3)
    CameraPosition(200)
    sprite('null', 3)
    CameraPosition(225)
    sprite('null', 3)
    CameraPosition(250)
    sprite('null', 3)
    CameraPosition(275)
    sprite('null', 3)
    CameraPosition(300)
    sprite('null', 3)
    CameraPosition(325)
    sprite('null', 3)
    CameraPosition(350)
    sprite('null', 3)
    CameraPosition(375)
    sprite('null', 3)
    CameraPosition(400)
    sprite('null', 3)
    CameraPosition(425)
    sprite('null', 3)
    CameraPosition(450)
    sprite('null', 3)
    CameraPosition(475)
    sprite('null', 3)
    CameraPosition(500)
    sprite('null', 3)
    CameraPosition(525)
    sprite('null', 3)
    CameraPosition(550)
    sprite('null', 3)
    CameraPosition(575)
    sprite('null', 3)
    CameraPosition(600)
    sprite('null', 3)
    CameraPosition(625)
    sprite('null', 3)
    CameraPosition(650)
    sprite('null', 3)
    CameraPosition(675)
    sprite('null', 3)
    CameraPosition(700)
    sprite('null', 3)
    CameraPosition(725)
    sprite('null', 3)
    CameraPosition(750)
    sprite('null', 3)
    CameraPosition(775)
    sprite('null', 3)
    CameraPosition(1000)
    sprite('null', 3)
    CameraPosition(1025)
    sprite('null', 3)
    CameraPosition(1050)
    sprite('null', 3)
    CameraPosition(1075)
    sprite('null', 32767)
    CameraPosition(1100)


@State
def __450Shake():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 10)
    ScreenShake(4000, 4000)
    sprite('null', 5)
    gotoLabel(0)
    label(1)
    sprite('null', 5)


@State
def __450Shake2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 10)
    ScreenShake(20000, 20000)
    sprite('null', 5)
    gotoLabel(0)
    label(1)
    sprite('null', 5)


@State
def efkk_WinBG():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        LinkParticle('kkef450winbg_01')
        Size(900)
        AddY(30000)
    sprite('null', 32767)
    CreateObject('efkk_WinBG2', -1)


@State
def efkk_WinBG2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(3)
        RenderLayer(2)
        Eff3DEffect('kkef450_finishbg', '')
    sprite('null', 32767)


@State
def efkk_Whiteout():

    def upon_IMMEDIATE():
        LinkParticle('kkef450scenechange_03')
    sprite('null', 110)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def efkk_AHJishaku00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('kkef450_jishaku00', '')
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Flip()
        Size(1000)
        TeleportToObject(22)
        AbsoluteY(0)
        LinkParticle('kkef450ray2_00')
    sprite('null', 120)


@State
def efkk_InsekiEff():

    def upon_IMMEDIATE():
        AddY(380000)
        AddX(200000)
    sprite('null', 60)
    ScreenShake(20000, 20000)
    ParticleRotationAngle(500)
    CallCustomizableParticle('kkef450insekimagi_00', -1)


@State
def efkk202_BLT():

    def upon_IMMEDIATE():
        PaletteIndex(2)

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            PrivateSE('kkse_31')
        RenderLayer(1)
    sprite('vr_blt202', 40)
    AddRotationPerFrame(10000)
    RandAddRotation(0, 360000)
    PrivateSE('nose_02')
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    RandSpeedX(-1000, 1000)
    RandSpeedY(-1000, 5000)


@State
def efkk402_BLT():

    def upon_IMMEDIATE():

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            PrivateSE('kkse_31')
        RenderLayer(1)
    sprite('vr_blt402', 40)
    AddRotationPerFrame(10000)
    RandAddRotation(0, 360000)
    PrivateSE('nose_02')
    setGravity(1600)
    physicsYImpulse(8000)
    physicsXImpulse(-10000)
    RandSpeedX(-1000, 1000)
    RandSpeedY(-1000, 5000)


@State
def efkk_610_hole_out():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        Unknown4024(3)
        IgnorePauses(3)
        PaletteIndex(3)
        AddX(-115000)
        AddY(-14000)
        RotationAngle(-90000)
    sprite('vrkkef601_hole', 10)
    Size(0)
    SetScaleXPerFrame(50)
    SetScaleSpeedY(80)
    sprite('vrkkef601_hole', 23)
    SetScaleX(500)
    SetScaleY(800)
    SetScaleSpeed(0)
    sprite('vrkkef601_hole', 11)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    sprite('vrkkef601_hole', 6)
    SetScaleSpeed(-100)


@State
def efkk_TagerHole_event():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(2)
        SetZVal(500)
        LinkParticle('kkef430_02')
        Size(700)
    sprite('vrkkef432_bloom', 40)
    sprite('vrkkef432_bloom', 10)
    SetScaleXPerFrame(-80)
    sprite('vrkkef432_bloom', 32767)
    SetScaleXPerFrame(0)
    Size(0)
    Visibility(1)


@State
def BurstDD_AtkMatome():

    def upon_IMMEDIATE():
        pass
    sprite('null', 10)
    label(0)
    sprite('null', 10)
    CreateObject('BurstDD_Atk', -1)
    loopRest()
    gotoLabel(0)


@State
def BurstDD_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(200)
        AttackP2(100)
        SameMoveProration(-1)
        AirUntechableTime(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(12000)
        WallbounceReboundTime(50)
        Hitstop(4)
        HardKnockdown(1)
        UseFireHitspark(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        Visibility(1)
        EffectPosition(22, 105)
    sprite('vr_blt', 6)
    RefreshMultihit()


@State
def BurstDD_missile():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(60)
        AttackP2(100)
        SameMoveProration(-1)
        AirUntechableTime(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(40000)
        AirPushbackY(3000)
        WallbounceReboundTime(50)
        Hitstop(1)
        HardKnockdown(1)
        UseFireHitspark(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        BounceOffWall(1)
        Unknown9219(1)
        DamageEffect(4, '')
        DamageFromStateOnly('BurstDD_missile')
        OppMovementUnlock(1)

        def upon_32():
            DamageFromStateOnly('BurstDD_missile2')
        CollideWithWall(1)

        def upon_EVERY_FRAME():
            ObjectUpon26(22, 0, 50000, 30000, 1)
        Size(700)
        uponSendToLabel(OPPONENT_CHAR_HIT_OR_BLOCK, 1)
        EnableAfterimage(1)
        RenderLayer(1)
    sprite('vrkkef_missile', 2)
    LinkParticle('kkef440_jet')
    physicsXImpulse(15000)
    physicsYImpulse(7500)
    CreateParticle('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    CreateParticle('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    physicsXImpulse(30000)
    physicsYImpulse(3750)
    AddRotationPerFrame(2250)
    CreateParticle('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    CreateParticle('kkef440_jetkidou', 0)
    label(0)
    sprite('vrkkef_missile', 1)
    physicsXImpulse(45000)
    physicsYImpulse(-7500)
    AddRotationPerFrame(0)
    CreateParticle('kkef440_jetkidou', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('BurstDD_Bomb', -1)


@State
def BurstDD_missile2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(60)
        AttackP2(100)
        AirUntechableTime(200)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(-15000)
        AirPushbackY(40000)
        Hitstop(1)
        GroundBounce(2)
        BouncePercentage(60)
        HardKnockdown(1)
        UseFireHitspark(1)
        DefeatOpponentBehavior(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        DamageEffect(4, '')
        DamageFromStateOnly('BurstDDAdd')
        OppMovementUnlock(1)
        CollideWithWall(1)

        def upon_EVERY_FRAME():
            ObjectUpon26(22, 0, 50000, 30000, 1)
        Size(1000)
        RenderLayer(1)
        uponSendToLabel(OPPONENT_CHAR_HIT_OR_BLOCK, 1)
    sprite('vrkkef_missile', 2)
    LinkParticle('kkef440_jet')
    physicsXImpulse(15000)
    physicsYImpulse(3750)
    CreateParticle('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    CreateParticle('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    physicsXImpulse(30000)
    physicsYImpulse(1875)
    AddRotationPerFrame(1125)
    CreateParticle('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    CreateParticle('kkef440_jetkidou', 0)
    label(0)
    sprite('vrkkef_missile', 2)
    physicsXImpulse(45000)
    physicsYImpulse(-3750)
    AddRotationPerFrame(0)
    CreateParticle('kkef440_jetkidou', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('BurstDD_Bomb', -1)


@State
def BurstDD_Bomb():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        DeviationX(0, 300000)
    sprite('vrkkef440_00', 2)
    CommonSE('016_explode_1')
    sprite('vrkkef440_01', 2)
    sprite('vrkkef440_02', 2)
    sprite('vrkkef440_03', 2)
    AddScale(-300)
    RandAddRotation(0, 360000)
    EnableAfterimage(1)
    AfterimageCount(3)
    sprite('vrkkef440_03', 2)
    AddScale(100)
    sprite('vrkkef440_03', 2)
    AddScale(100)
    sprite('vrkkef440_03', 2)
    AddScale(100)
    sprite('vrkkef440_04', 4)
    SetScaleSpeed(75)
    sprite('vrkkef440_05', 2)
    ConstantAlphaModifier(-51)
    sprite('vrkkef440_06', 2)


@State
def BurstDD_thunderball():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        AddX(250000)
        AlphaValue(255)
        Eff3DEffect('kkef440_thunderball00', '')
        LinkParticle('kkef440_thunderLoop')
        uponSendToLabel(32, 1)
        CreateObject('BurstDD_Camera', -1)
    label(0)
    sprite('null', 2)
    AddScale(80)
    CreateObject('efkk440_thunder00', -1)
    ScreenShake(2500, 2500)
    CommonSE('014_electric_sl')
    sprite('null', 2)
    AddScale(-80)
    CreateObject('efkk440_thunder01', -1)
    ScreenShake(2500, 2500)
    CommonSE('014_electric_m')
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(100)
    CreateObject('BurstDD_thunderballSub', -1)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    CreateObject('efkk440_thunderEnd', -1)


@State
def efkk440_thunder00():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        Flip()
        BlendMode_Normal()
        AddY(170000)
        Size(800)
        IgnoreFinishStop(1)
    sprite('null', 2)
    AlphaValue(255)
    RandAddRotation(0, 360000)


@State
def efkk440_thunder01():

    def upon_IMMEDIATE():
        Eff3DEffect('kkef432_thunder00', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        AddY(170000)
        Size(800)
        IgnoreFinishStop(1)
    sprite('null', 2)
    RandAddRotation(0, 360000)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 2)
    AlphaValue(255)


@State
def efkk440_thunderEnd():

    def upon_IMMEDIATE():
        AddY(170000)
    sprite('null', 30)
    ParticleSize(1700)
    LinkParticle('kkef440_thunderEnde')
    SetScaleSpeed(50)
    sprite('null', 10)
    SetScaleSpeed(12)
    sprite('null', 10)
    SetScaleSpeed(6)
    sprite('null', 10)
    SetScaleSpeed(3)


@State
def BurstDD_thunderballSub():

    def upon_IMMEDIATE():
        AddY(170000)
        Size(400)
        BlendMode_Normal()
        Eff3DEffect('kkef440_thunderball01', '')
    sprite('null', 6)
    SetScaleSpeed(30)
    sprite('null', 5)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(60)


@State
def BurstDDEx_SmokeHead():

    def upon_IMMEDIATE():
        LinkParticle('kkef440_bombhead_00')
        E0EAEffectScale(2)
        SetScaleY(979)
        SetScaleX(1050)
        AddY(450000)
        IgnoreFinishStop(1)
    sprite('null', 10)
    physicsYImpulse(40000)
    SetScaleSpeed(3)
    sprite('null', 5)
    physicsYImpulse(8750)
    sprite('null', 20)
    physicsYImpulse(0)
    sprite('null', 40)
    IgnoreFinishStop(0)


@State
def BurstDDEx_SmokeBody():

    def upon_IMMEDIATE():
        Size(1500)
        AddX(200000)
        IgnoreFinishStop(1)
    sprite('null', 5)
    CreateParticle('kkef440_flash', -1)
    sprite('null', 30)
    LinkParticle('kkef440_bombbody_00')
    CreateObject('BurstDDEx_SmokeHead', -1)
    sprite('null', 40)
    IgnoreFinishStop(0)


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        uponSendToLabel(32, 0)
        IgnoreFinishStop(1)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    AbsoluteY(0)
    CameraPosition(1300)
    physicsYImpulse(45000)
    sprite('null', 35)
    physicsYImpulse(0)
    IgnoreFinishStop(0)
    sprite('null', 15)
    physicsYImpulse(-64000)
    CameraPosition(1000)
    sprite('null', 60)
    physicsYImpulse(0)


@State
def efkk440_PartsA():

    def upon_IMMEDIATE():
        setGravity(3000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk440_16_w1', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk440_PartsB():

    def upon_IMMEDIATE():
        setGravity(3000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk440_16_w2', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk440_PartsC():

    def upon_IMMEDIATE():
        setGravity(3000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk440_16_w3', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    ParticleLayer(12)
    CallCustomizableParticle('kkef403koware_05', -1)


@State
def efkk440_PartsD():

    def upon_IMMEDIATE():
        setGravity(3000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk440_16_w4', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    ParticleLayer(12)
    CallCustomizableParticle('kkef403koware_05', -1)


@State
def efkk440_MissileFire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('kkef_440_missileEnter')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def efkk440_Koge():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(2)
        AlphaValue(180)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('vrkkef440_koge', 30)
    sprite('vrkkef440_koge', 15)
    CreateParticle('kkef_440_kogesmoke', 0)
    CreateParticle('kkef_440_kogesmoke', 1)
    CreateParticle('kkef_440_kogesmoke', 2)
    CreateParticle('kkef_440_kogesmoke', 3)
    CreateParticle('kkef_440_kogesmoke', 4)
    sprite('vrkkef440_koge', 5)
    ConstantAlphaModifier(-36)


@State
def efkk440_Parts2A():

    def upon_IMMEDIATE():
        setGravity(1000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk440_23w1', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)
    CommonSE('016_explode_0')


@State
def efkk440_Parts2B():

    def upon_IMMEDIATE():
        setGravity(1000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk440_23w2', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk440_Parts2C():

    def upon_IMMEDIATE():
        setGravity(1000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
        AddRotationPerFrame(-2500)
    sprite('kk440_23w3', 4)
    physicsXImpulse(-12000)
    physicsYImpulse(12000)
    label(0)
    sprite('kk440_23w3', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(-15000)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)
    CommonSE('016_explode_0')


@State
def efkk440_Parts2D():

    def upon_IMMEDIATE():
        setGravity(1000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
        AddRotationPerFrame(-1000)
    label(0)
    sprite('kk440_23w4', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk440_ThunderTame():

    def upon_IMMEDIATE():
        Size(750)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('kkef_440_thunder_tame')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 2)
    AddX(2500)
    AddY(-2500)
    sprite('null', 2)
    AddX(-2500)
    AddY(2500)
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    AddY(65000)


@State
def efkk405_Fire00():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        uponSendToLabel(32, 0)
        Eff3DEffect('kkef405_fire00', '')
    sprite('vrkkef405_00', 3)
    CreateParticle('kkef405_fire', 0)
    CreateParticle('kkef405_fire', 1)
    sprite('vrkkef405_01', 3)
    CreateParticle('kkef405_fire', 0)
    CreateParticle('kkef405_fire', 1)
    sprite('vrkkef405_02', 3)
    CreateParticle('kkef405_fire', 0)
    CreateParticle('kkef405_fire', 1)
    sprite('vrkkef405_03', 3)
    CreateParticle('kkef405_fire', 0)
    CreateParticle('kkef405_fire', 1)
    sprite('vrkkef405_04', 3)
    CreateParticle('kkef405_fire', 0)
    CreateParticle('kkef405_fire', 1)
    label(0)
    sprite('null', 10)
    IgnorePauses(0)
    ConstantAlphaModifier(-30)
    SetScaleSpeed(20)
    physicsYImpulse(-10000)


@State
def efkk405_PartsA():

    def upon_IMMEDIATE():
        setGravity(1000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk405_11a', 4)
    CreateParticle('kkef405_smoke', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)


@State
def efkk405_PartsB():

    def upon_IMMEDIATE():
        setGravity(1000)
        uponSendToLabel(LANDING, 1)
        NoDamageAction(1)
    label(0)
    sprite('kk405_11b', 4)
    CreateParticle('kkef405_smoke', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateParticle('kkef403koware_05', -1)
    CommonSE('016_explode_0')


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act3Event_kkvsph_no():

    def upon_IMMEDIATE():
        LoadSpritePalette(0)
        uponSendToLabel(32, 0)
        AddX(-160000)
        SetZVal(500)
    sprite('no064_04', 3)
    sprite('no064_04', 32767)
    loopRest()
    label(0)
    sprite('no064_05', 4)
    sprite('no064_06', 4)
    sprite('no064_07', 4)
    sprite('no064_08', 4)
    sprite('no032_00', 1)
    Flip()
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(18000)
    sprite('no032_01', 2)
    sprite('no032_02', 4)
    sprite('no032_03', 4)
    sprite('no032_04', 4)
    DashEffects(100, 1, 1)
    sprite('no032_05', 4)
    sprite('no032_06', 4)
    sprite('no032_07', 4)
    sprite('no032_08', 4)
    DashEffects(100, 1, 1)
    sprite('no032_09', 4)
    loopRest()


@State
def Act3Event_kgvskk_mu():

    def upon_IMMEDIATE():
        LoadSpritePalette(1)
        uponSendToLabel(32, 1)
        TeleportToObject(22)
        Flip()
        AddX(-100000)
        SetZVal(500)
    label(0)
    sprite('mu000_00', 6)
    sprite('mu000_01', 6)
    sprite('mu000_02', 6)
    sprite('mu000_03', 6)
    sprite('mu000_04', 6)
    sprite('mu000_05', 6)
    sprite('mu000_06', 6)
    sprite('mu000_07', 6)
    sprite('mu000_08', 6)
    sprite('mu000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mu003_00', 3)
    Flip()
    sprite('mu003_01', 3)
    sprite('mu003_02', 3)
    sprite('mu032_00', 2)
    ScreenCollision(0)
    EnableCollision(0)
    physicsXImpulse(24000)
    CommonSE('000_airdash_0')
    CreateParticle('muef_ny030', -1)
    sprite('mu032_01', 4)
    sprite('mu032_02', 4)
    sprite('mu032_03', 4)
    CreateParticle('muef_ny032', 106)
    sprite('mu032_04', 4)
    CreateParticle('muef_ny032', 106)
    sprite('mu032_01', 4)
    sprite('mu032_02', 4)
    sprite('mu032_03', 4)
    CreateParticle('muef_ny032', 106)
    sprite('mu032_04', 4)
    PrivateSE('muse_10')
    CreateParticle('muef_ny032', 106)


@State
def Noise():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_eventnoise.DIG', '')
        FaceSpawnLocation()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 30)
    CommonSE('014_electric_ml')
    loopRest()


@State
def Eventoffset_Sosai_arvskk():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(150000)
        DeviationX(-20000, 20000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)
