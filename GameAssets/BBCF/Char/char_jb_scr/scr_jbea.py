@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        Size(1100)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_JB.DIG', '')
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
def EMB_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        Size(1250)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_JB.DIG', '')
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
def EMB_JB_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        Size(1250)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_JB.DIG', '')
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
def jb611_Tail():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
    sprite('jb611_00s', 8)
    sprite('jb611_01s', 8)
    sprite('jb611_02s', 8)
    label(0)
    sprite('jb611_03s', 10)
    sprite('jb611_04s', 10)
    sprite('jb611_05s', 10)
    sprite('jb611_06s', 10)
    loopRest()
    gotoLabel(0)


@Subroutine
def zanzou():
    TurnParticleColorable1(1)
    PaletteEffType(2)
    PaletteColor2(240)
    PaletteColor3(241)
    PaletteColor1(242)
    PaletteColor4(0)


@Subroutine
def zanzou2():
    TurnParticleColorable1(1)
    PaletteEffType(2)
    PaletteColor2(240)
    PaletteColor3(241)
    PaletteColor1(242)
    PaletteColor4(1)


@State
def jbef202_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
        AddX(-88000)
    sprite('vrefjb202_00', 3)
    sprite('vrefjb202_01', 4)


@State
def jbef202_zanzou_2nd():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(-88000)
        callSubroutine('zanzou')
    sprite('vrefjb202_10', 3)
    sprite('vrefjb202_11', 4)


@State
def jbef232_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb232_00', 6)
    sprite('vrefjb232_01', 4)


@State
def jbef212_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb212_00', 10)
    AddX(64000)


@State
def jbef235_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(-38000)
        callSubroutine('zanzou')
    sprite('vrefjb235_00', 3)
    sprite('vrefjb235_01', 3)
    E0EAEffectPosition(0)


@State
def jbef235_zanzou_2nd():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(-199000)
        TurnParticleColorable1(1)
        callSubroutine('zanzou')
    sprite('vrefjb235_10', 2)
    AddX(192000)
    sprite('vrefjb235_10', 8)
    E0EAEffectPosition(0)


@State
def jbef252_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb252_00', 2)
    sprite('vrefjb252_01', 4)
    sprite('vrefjb252_01', 4)
    E0EAEffectPosition(0)


@State
def jbef252_zanzou_2nd():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb252_10', 2)
    sprite('vrefjb252_10', 4)
    sprite('vrefjb252_10', 4)
    E0EAEffectPosition(0)


@State
def jbef255_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb255_00', 2)
    sprite('vrefjb255_01', 3)
    sprite('vrefjb255_01', 4)
    E0EAEffectPosition(0)


@State
def jbef340_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb340_00', 3)
    AddX(128000)
    sprite('vrefjb340_01', 7)


@State
def jbef210_atemi():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(100)
    sprite('vrefjb210_00', 3)
    CreateObject('jbef_210_bloom', 0)
    RedColorValue(0)
    AlphaValue(0)
    ConstantAlphaModifier(85)
    sprite('keep', 1)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('keep', 15)
    ConstantAlphaModifier(-16)


@State
def jbef211_atemi():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(100)
    sprite('vrefjb211_00', 3)
    CreateObject('jbef_210_bloom', 0)
    RedColorValue(0)
    AlphaValue(0)
    ConstantAlphaModifier(85)
    sprite('keep', 1)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    sprite('keep', 15)
    ConstantAlphaModifier(-16)


@State
def jbef_210_bloom():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        LinkParticle('jbef_210bloom')
    sprite('null', 30)


@State
def jbef311_claw():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(90000)
        SetZVal(100)
    sprite('vrefjb311_00', 10)
    sprite('vrefjb311_01', 10)
    ConstantAlphaModifier(-25)


@State
def jbef_DashSmoke():

    def upon_IMMEDIATE():
        pass
    sprite('null', 15)
    CreateParticle('jbef_403smoke', 100)


@State
def jbef_claw_pt():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        LinkParticle('jbef_claw')
    sprite('null', 3)
    sprite('null', 60)
    E0EAEffectPosition(0)


@State
def jbef400_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(-40000)
    sprite('vrefjb400_00', 2)
    CreateObject('jbef_claw_pt', 0)
    sprite('vrefjb400_00', 4)
    E0EAEffectPosition(0)
    sprite('vrefjb400_01', 12)
    ConstantAlphaModifier(-21)


@State
def jbef400_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        Rotation(3000)
    sprite('vrefjb400_10', 2)
    CreateParticle('jbef_claw_pt', 0)
    sprite('vrefjb400_10', 4)
    E0EAEffectPosition(0)
    sprite('vrefjb400_11', 12)
    ConstantAlphaModifier(-21)


@State
def jbef401_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddY(96000)
        AddX(-32000)
        SetScaleY(1050)
        SetScaleX(1200)
    sprite('vrefjb401_00', 2)
    sprite('vrefjb401_00', 4)
    E0EAEffectPosition(0)
    sprite('vrefjb401_01', 12)
    ConstantAlphaModifier(-21)


@State
def jbef402_slash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(100000)
        AddY(-10000)
        CreateObject('jbef402_slash2', 100)
    sprite('vrefjb402_00', 2)
    sprite('vrefjb402_00', 4)
    E0EAEffectPosition(0)
    sprite('vrefjb402_01', 12)
    ConstantAlphaModifier(-21)


@State
def jbef402_slash2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrefjb402_10', 2)
    sprite('vrefjb402_10', 4)
    E0EAEffectPosition(0)
    sprite('vrefjb402_11', 12)
    ConstantAlphaModifier(-21)


@State
def jbef403_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou2')
    sprite('vrefjb403_00', 3)
    sprite('vrefjb403_01', 10)


@State
def jbef403_zanzou2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou2')
    sprite('vrefjb403_10', 3)
    sprite('vrefjb403_11', 10)


@State
def jbef404_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb404_00', 4)
    sprite('vrefjb404_01', 10)
    E0EAEffectPosition(0)


@State
def jbef404_zanzou_air():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb404_00ex', 3)
    sprite('vrefjb404_01ex', 10)
    E0EAEffectPosition(0)


@State
def jbef405_loop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 32767)
    CreateObject('jbef405_loop_swords', 100)
    CreateObject('jbef405_loop_claws', 100)


@State
def jbef405_loop_swords():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    label(0)
    sprite('null', 3)
    CreateObject('jbef405_loop_sword', 100)
    CommonSE('010_swing_sword_0')
    sprite('null', 3)
    CreateObject('jbef405_loop_sword2', 100)
    CommonSE('010_swing_sword_0')
    sprite('null', 3)
    CreateObject('jbef405_loop_sword3', 100)
    CommonSE('010_swing_sword_0')
    sprite('null', 3)
    CreateObject('jbef405_loop_sword4', 100)
    CommonSE('010_swing_sword_0')
    gotoLabel(0)


@State
def jbef405_loop_claws():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddY(9000)
    label(0)
    sprite('null', 4)
    CreateObject('jbef405_loop_claw', 100)
    PrivateSE('jbse_02')
    sprite('null', 4)
    CreateObject('jbef405_loop_claw2', 100)
    sprite('null', 4)
    CreateObject('jbef405_loop_claw3', 100)
    PrivateSE('jbse_02')
    sprite('null', 4)
    CreateObject('jbef405_loop_claw4', 100)
    gotoLabel(0)


@State
def jbef405_loop_sword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
        AddX(40000)
    sprite('vrefjb405_00', 3)
    sprite('vrefjb405_01', 3)


@State
def jbef405_loop_sword2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb405_10', 3)
    sprite('vrefjb405_11', 3)


@State
def jbef405_loop_sword3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb405_20', 3)
    sprite('vrefjb405_21', 3)


@State
def jbef405_loop_sword4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb405_30', 3)
    sprite('vrefjb405_31', 3)


@State
def jbef405_loop_claw():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        RotationAngle(-15000)
        SetScaleX(1050)
        SetScaleY(1250)
        AddX(-80000)
        AddY(200000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)


@State
def jbef405_loop_claw2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(100)
        RotationAngle(45000)
        SetScaleX(800)
        SetScaleY(1200)
        AddX(48000)
        AddY(224000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)


@State
def jbef405_loop_claw3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        RotationAngle(120000)
        SetScaleX(800)
        SetScaleY(1200)
        AddX(-48000)
        AddY(80000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)


@State
def jbef405_loop_claw4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        RotationAngle(65000)
        SetScaleX(700)
        SetScaleY(1050)
        AddX(192000)
        AddY(64000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)


@State
def jbef405_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb405_80', 3)
    sprite('vrefjb405_81', 10)


@State
def jbef406_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb406_00', 6)


@State
def jbef406_zanzou2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou')
    sprite('vrefjb406_10', 6)


@State
def jbef600_manto():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(0)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        SetZVal(100)
    sprite('efjb600_00', 3)
    AddX(80000)
    AddY(-128000)
    physicsXImpulse(-30000)
    physicsYImpulse(8000)
    sprite('efjb600_00', 60)


@State
def __5DStartEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        FloorCollision(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_markerMove', '')
        AddX(100000)
        AddY(150000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    SetScaleXPerFrame(40)
    CreateObject('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    CancelIfPlayerHit(0)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-42)


@State
def AIR5DStartEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        FloorCollision(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_markerMove', '')
        AddX(100000)
        RotationAngle(60000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    SetScaleXPerFrame(40)
    CreateObject('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    CancelIfPlayerHit(0)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-42)


@State
def AIR6DStartEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        FloorCollision(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_markerMove', '')
        AddX(100000)
        AddY(100000)
        RotationAngle(30000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    SetScaleXPerFrame(40)
    CreateObject('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    CancelIfPlayerHit(0)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-42)


@State
def Drive_AddAtk():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(880)
        AirPushbackX(30000)
        AirPushbackY(-60000)
        PushbackX(19800)
        Floorslide(20)
        AttackDirection(0)
        StarterRating(2)
        UseSlashHitspark(1)
        HitsparkSize(700)
        DamageEffect(4, 'jbef_driveslash_sumi')

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_32 = 300
            TriggerUponForState('NmlAtk5D', 32)
            TriggerUponForState('NmlAtkAIR5D', 32)
            TriggerUponForState('AN_NmlAtkAIR6D', 32)
    sprite('null', 25)
    sprite('Drive_Atk', 3)
    EffectPosition(22, 103)
    RefreshMultihit()


@State
def jbef_DriveHit():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_DriveSlash00.DIG', '')
        LinkParticle('jbef_driveslash_speed')
        RotationAngle(10000)
        TeleportToObject(22)
        AddY(180000)
        AddScaleY(200)
        RenderLayer(11)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    CreateParticle('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    SetScaleSpeed(10)
    Eff3DEffect('jbef_DriveSlashEnd', '')


@State
def jbef_Air5DHit():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_DriveSlash00.DIG', '')
        LinkParticle('jbef_driveslash_speed')
        RenderLayer(11)
        RotationAngle(60000)
        TeleportToObject(22)
        AddX(-50000)
        AddY(120000)
        AddScaleY(200)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    ParticleRotationAngle(80000)
    CallCustomizableParticle('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    SetScaleSpeed(10)
    Eff3DEffect('jbef_DriveSlashEnd', '')


@State
def jbef_Air6DHit():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_DriveSlash00.DIG', '')
        LinkParticle('jbef_driveslash_speed')
        RenderLayer(11)
        RotationAngle(30000)
        TeleportToObject(22)
        AddX(-50000)
        AddY(170000)
        AddScaleY(200)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    ParticleRotationAngle(80000)
    CallCustomizableParticle('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    SetScaleSpeed(10)
    Eff3DEffect('jbef_DriveSlashEnd', '')


@Subroutine
def DriveAtk_AtkVector():
    if SLOT_XVelocity >= 90000:
        AirPushbackX(60000)
    elif SLOT_XVelocity > 0:
        AirPushbackX(30000)
    elif SLOT_XVelocity == 0:
        AirPushbackX(0)
    elif SLOT_XVelocity < 0:
        AirPushbackX(-30000)
    elif SLOT_XVelocity <= -90000:
        AirPushbackX(-60000)
    if SLOT_YVelocity >= 90000:
        AirPushbackY(60000)
    elif SLOT_YVelocity > 0:
        AirPushbackY(30000)
    elif SLOT_YVelocity == 0:
        AirPushbackY(0)
    elif SLOT_YVelocity < 0:
        AirPushbackY(-30000)
    elif SLOT_YVelocity <= -90000:
        AirPushbackY(-60000)


@Subroutine
def DriveAtk():
    AttackLevel_(4)
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    MoveAttributes(1, 0, 0, 0, 0)
    Damage(550)
    AttackP1(80)
    GroundedHitstunAnimation(9)
    PushbackX(80000)
    AirUntechableTime(40)
    Floorslide(10)
    Hitstop(0)
    EnemyHitstopAddition(0, 2, 2)
    AttackDirection(0)
    UseSlashHitspark(1)
    OppPositionOnHit(1, 0, -110000)
    DistanceCheck(200000, -200000, 400000, -400000)
    StarterRating(2)
    callSubroutine('DriveAtk_AtkVector')

    def upon_OPPONENT_HIT():
        SLOT_32 = 300


@Subroutine
def DriveAtkFinish():
    AttackLevel_(4)
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    MoveAttributes(1, 0, 0, 0, 0)
    Damage(550)
    AttackP1(80)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(60)
    AirPushbackY(30000)
    AirPushbackX(30000)
    ResetPushbackX()
    FloorslideReset()
    Hitstop(0)
    EnemyHitstopAddition(0, 0, 5)
    DistanceCheck(200000, -200000, 400000, -400000)
    AttackDirection(0)
    UseSlashHitspark(1)
    StarterRating(2)


@Subroutine
def LeverInput():
    if CheckInput(0x45):
        SLOT_57 = 2
    if CheckInput(0x93):
        SLOT_57 = 8
    SLOT_55 = 1


@Subroutine
def CheckPosY():
    if SLOT_57 == 2:
        AddY(-200000)
    elif SLOT_57 == 8:
        AddY(200000)
    if SLOT_YDistanceFromFloor <= 150000:
        AbsoluteY(150000)
    elif SLOT_YDistanceFromFloor >= 3000000:
        AbsoluteY(3000000)


@Subroutine
def CourseSetting():
    WallCollisionDetection(1)
    CopyFromRightToLeft(23, 2, 58, 3, 2, 58)
    if SLOT_51:
        clearUponHandler(32)
        if SLOT_58:
            SLOT_55 == 1
        else:
            SLOT_55 == 3
        if SLOT_0:
            AddX(200000)
            AddY(400000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(5, 1)
        if SLOT_58:
            SLOT_55 == 2
        else:
            SLOT_55 == 6
        if SLOT_0:
            AddX(400000)
            AddY(-400000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(6, 1)
        if SLOT_58:
            SLOT_55 == 3
        else:
            SLOT_55 == 9
        if SLOT_0:
            AddX(400000)
            AddY(400000)
            if SLOT_57 == 2:
                AddY(200000)
            elif SLOT_57 == 8:
                AddY(-200000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(7, 1)
        if SLOT_58:
            SLOT_55 == 4
        else:
            SLOT_55 == 12
        if SLOT_0:
            AddX(400000)
            AddY(-400000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(8, 1)
    if SLOT_52:
        clearUponHandler(32)
        if SLOT_58:
            SLOT_55 == 1
        else:
            SLOT_55 == 3
        if SLOT_0:
            AddX(200000)
            AddY(400000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(5, 1)
        if SLOT_58:
            SLOT_55 == 2
        else:
            SLOT_55 == 6
        if SLOT_0:
            AddX(800000)
            AddY(0)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(6, 1)
        if SLOT_58:
            SLOT_55 == 3
        else:
            SLOT_55 == 9
        if SLOT_0:
            AddX(-400000)
            AddY(-400000)
            if SLOT_57 == 2:
                AddY(200000)
            elif SLOT_57 == 8:
                AddY(-200000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(7, 1)
        if SLOT_58:
            SLOT_55 == 4
        else:
            SLOT_55 == 12
        if SLOT_0:
            AddX(800000)
            AddY(0)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(8, 1)
    if SLOT_53:
        clearUponHandler(32)
        if SLOT_58:
            SLOT_55 == 1
        else:
            SLOT_55 == 3
        if SLOT_0:
            AddX(200000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(5, 1)
        if SLOT_58:
            SLOT_55 == 2
        else:
            SLOT_55 == 6
        if SLOT_0:
            AddX(400000)
            AddY(400000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(6, 1)
        if SLOT_58:
            SLOT_55 == 3
        else:
            SLOT_55 == 9
        if SLOT_0:
            AddX(400000)
            AddY(-400000)
            if SLOT_57 == 2:
                AddY(200000)
            elif SLOT_57 == 8:
                AddY(-200000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(7, 1)
        if SLOT_58:
            SLOT_55 == 4
        else:
            SLOT_55 == 12
        if SLOT_0:
            AddX(400000)
            AddY(400000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(8, 1)
    if SLOT_54:
        clearUponHandler(32)
        if SLOT_58:
            SLOT_55 == 1
        else:
            SLOT_55 == 3
        if SLOT_0:
            AddX(200000)
            AddY(0)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(5, 1)
        if SLOT_58:
            SLOT_55 == 2
        else:
            SLOT_55 == 6
        if SLOT_0:
            AddX(400000)
            AddY(0)
            if SLOT_57 == 2:
                AddX(-100000)
                AddY(-100000)
            elif SLOT_57 == 8:
                AddX(-100000)
                AddY(100000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(6, 1)
        if SLOT_58:
            SLOT_55 == 3
        else:
            SLOT_55 == 9
        if SLOT_0:
            AddX(400000)
            AddY(0)
            if SLOT_57 == 2:
                AddX(-100000)
                AddY(-100000)
            elif SLOT_57 == 8:
                AddX(-100000)
                AddY(100000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(7, 1)
        if SLOT_58:
            SLOT_55 == 4
        else:
            SLOT_55 == 12
        if SLOT_0:
            AddX(400000)
            AddY(0)
            if SLOT_57 == 2:
                AddX(-100000)
                AddY(-100000)
            elif SLOT_57 == 8:
                AddX(-100000)
                AddY(100000)
            callSubroutine('CheckPosY')
            CreateObject('Mark', 100)
            RegisterObject(8, 1)
    if SLOT_58:
        SLOT_55 == 5
    else:
        SLOT_55 == 13
    if SLOT_0:
        clearUponHandler(EVERY_FRAME)
        sendToLabel(0)
    SLOT_55 = SLOT_55 + 1


@Subroutine
def DriveSpeed():
    XImpulseAcceleration(20)
    YAccel(20)
    RotationSomething(0)
    if SLOT_XVelocity:
        if SLOT_YVelocity:
            CreateObject('MAKERMoveEff', -1)
    CopyFromRightToLeft(3, 2, 12, 23, 2, 12)
    CopyFromRightToLeft(3, 2, 13, 23, 2, 13)


@State
def __5D_SPMark():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        if SLOT_113:
            SLOT_55 = 1
            if random_(2, 0, 25):
                SLOT_51 = 1
            elif random_(2, 0, 33):
                SLOT_52 = 1
            elif random_(2, 0, 50):
                SLOT_53 = 1
            else:
                SLOT_54 = 1
            if random_(2, 0, 50):
                SLOT_57 = 0
            elif random_(2, 0, 50):
                SLOT_57 = 2
            else:
                SLOT_57 = 8

        def upon_EVERY_FRAME():
            if not SLOT_55:
                if CheckInput(INPUT_HOLD_A):
                    callSubroutine('LeverInput')
                    SLOT_51 = 1
                    SLOT_52 = 0
                    SLOT_53 = 0
                    SLOT_54 = 0
                elif CheckInput(INPUT_HOLD_B):
                    callSubroutine('LeverInput')
                    SLOT_51 = 0
                    SLOT_52 = 1
                    SLOT_53 = 0
                    SLOT_54 = 0
                elif CheckInput(INPUT_HOLD_C):
                    callSubroutine('LeverInput')
                    SLOT_51 = 0
                    SLOT_52 = 0
                    SLOT_53 = 1
                    SLOT_54 = 0
                elif SLOT_11:
                    if CheckInput(INPUT_HOLD_D):
                        callSubroutine('LeverInput')
                        SLOT_51 = 0
                        SLOT_52 = 0
                        SLOT_53 = 0
                        SLOT_54 = 1
            else:
                clearUponHandler(32)
                callSubroutine('CourseSetting')

        def upon_32():
            SLOT_51 = 0
            SLOT_52 = 0
            SLOT_53 = 0
            SLOT_54 = 1
            SLOT_55 = 1
            SLOT_11 = 1
    sprite('null', 300)
    AddY(150000)
    label(0)
    sprite('null', 5)
    ObjectUpon(EVERY_FRAME, 32)
    TeleportToObject(3)
    AddY(150000)
    CommonSE('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    CopyFromRightToLeft(23, 2, 56, 5, 2, 22)
    if SLOT_IsFacingRight:
        PrivateFunction(1, 2, 22, 2, 56, 2, 12)
    else:
        PrivateFunction(1, 2, 56, 2, 22, 2, 12)
    CopyFromRightToLeft(23, 2, 56, 5, 2, 23)
    PrivateFunction(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    PrivateSE('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    ObjectUpon(5, 32)
    EndMomentum(1)
    CopyFromRightToLeft(3, 2, 12, 23, 2, 12)
    CopyFromRightToLeft(3, 2, 13, 23, 2, 13)
    TeleportToObject(5)
    CommonSE('002_highjump_0')
    CreateObject('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    CopyFromRightToLeft(23, 2, 56, 6, 2, 22)
    if SLOT_IsFacingRight:
        PrivateFunction(1, 2, 22, 2, 56, 2, 12)
    else:
        PrivateFunction(1, 2, 56, 2, 22, 2, 12)
    CopyFromRightToLeft(23, 2, 56, 6, 2, 23)
    PrivateFunction(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    PrivateSE('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    ObjectUpon(6, 32)
    EndMomentum(1)
    CopyFromRightToLeft(3, 2, 12, 23, 2, 12)
    CopyFromRightToLeft(3, 2, 13, 23, 2, 13)
    TeleportToObject(6)
    CommonSE('001_airbackdash_0')
    CreateObject('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    CopyFromRightToLeft(23, 2, 56, 7, 2, 22)
    if SLOT_IsFacingRight:
        PrivateFunction(1, 2, 22, 2, 56, 2, 12)
    else:
        PrivateFunction(1, 2, 56, 2, 22, 2, 12)
    CopyFromRightToLeft(23, 2, 56, 7, 2, 23)
    PrivateFunction(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    PrivateSE('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    ObjectUpon(CORNERED, 32)
    EndMomentum(1)
    CopyFromRightToLeft(3, 2, 12, 23, 2, 12)
    CopyFromRightToLeft(3, 2, 13, 23, 2, 13)
    TeleportToObject(7)
    CommonSE('000_airdash_0')
    CreateObject('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    CopyFromRightToLeft(23, 2, 56, 8, 2, 22)
    if SLOT_IsFacingRight:
        PrivateFunction(1, 2, 22, 2, 56, 2, 12)
    else:
        PrivateFunction(1, 2, 56, 2, 22, 2, 12)
    CopyFromRightToLeft(23, 2, 56, 8, 2, 23)
    PrivateFunction(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    PrivateSE('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    ObjectUpon(8, 32)
    ObjectUpon(EVERY_FRAME, 33)
    EndMomentum(1)
    TeleportToObject(8)


@State
def Mark():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_marker.DIG', '')
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('jbef_drive_add')
        PrivateSE('jbse_06')

        def upon_32():
            CreateParticle('jbef_drive_move', -1)
            sendToLabel(0)
        uponSendToLabel(PLAYER_DAMAGED, 0)
    sprite('null', 120)
    label(0)
    sprite('null', 6)
    clearUponHandler(32)
    clearUponHandler(PLAYER_DAMAGED)
    sprite('null', 6)
    SetScaleSpeed(120)
    ConstantAlphaModifier(-42)


@State
def MAKERMoveEff():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RotationSomething(0)
        FloorCollision(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_markerMove', '')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    label(1)
    sprite('null', 6)
    SetScaleXPerFrame(-100)
    CreateObject('MAKERMoveEffSumi', 100)
    ExitState()
    label(0)
    sprite('null', 6)
    ConstantAlphaModifier(-42)


@State
def MAKERMoveEffSumi():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Visibility(1)
    sprite('vrefjb_markerMoveEXpoints', 1)
    PaletteIndex(2)
    CallCustomizableParticle('jbef_drive_sumi', 0)
    CallCustomizableParticle('jbef_drive_sumi', 1)
    CallCustomizableParticle('jbef_drive_sumi', 2)


@State
def jbef203_zanzou():

    def upon_IMMEDIATE():
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou2')
    sprite('vrefjb203_00', 10)


@State
def test1():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AddY(-200000)
        Size(950)
        ColorForTransition(4280295424)
        NoDamageAction(1)
        NoAttackDuringAction(1)
    sprite('jb252_08', 15)
    ConstantAlphaModifier(30)
    sprite('jb252_08', 10)
    ConstantAlphaModifier(-20)


@State
def test2():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AddY(-100000)
        Size(950)
        ColorForTransition(4280295424)
        NoDamageAction(1)
        NoAttackDuringAction(1)
    sprite('jb431_09', 15)
    ConstantAlphaModifier(30)
    sprite('jb431_09', 10)
    ConstantAlphaModifier(-20)


@State
def test3():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        AddY(-200000)
        Size(950)
        ColorForTransition(4280295424)
        NoDamageAction(1)
        NoAttackDuringAction(1)
    sprite('jb404_05', 15)
    ConstantAlphaModifier(30)
    sprite('jb404_05', 10)
    ConstantAlphaModifier(-20)


@State
def MarkingPoint():

    def upon_IMMEDIATE():
        RemoveOnContact(22)
        BlendMode_Normal()
        Size(700)

        def upon_16():
            PrivateFunction3(22, 0, 0, 100, 1)

        def upon_32():
            sendToLabel(0)
    sprite('null', 32767)
    AlphaValue(170)
    LinkParticle('jbef_marking_hatudo')
    Eff3DEffect('jbef_marker2.DIG', '')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def jbeff_warp():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_shunsin', '')
        IgnoreScreenfreeze(1)
        Size(1000)
        AddY(150000)
        AlphaValue(150)
    sprite('null', 7)
    CreateParticle('jbef_shunsin', -1)
    SetScaleSpeed(350)
    sprite('null', 14)
    SetScaleSpeed(30)


@State
def Shot_Eff():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(800)
        AttackP1(80)
        SameMoveProration(80)
        AirPushbackY(15000)
        UseFireHitspark(1)
        StarterRating(2)
        if SLOT_137:
            DamageMultiplier(80)
        physicsXImpulse(10000)
        physicsYImpulse(26000)
        setGravity(1600)
        Size(2000)

        def upon_32():
            physicsXImpulse(5000)
        WallCollisionDetection(1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            sendToLabel(580)

        def upon_EVERY_FRAME():
            if SLOT_2 >= 3:
                sendToLabel(0)
        LandingHeight(100000)

        def upon_5():
            AddActionMark(1)
            YAccel(-90)
            if SLOT_YVelocity <= 26000:
                physicsYImpulse(26000)
            LandingEffects(104, 1, 0)
            CommonSE('015_blaze_1')
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('Shot_Atk', 300)
    Visibility(1)
    CreateObject('jbef407_Nekodama', -1)
    label(0)
    sprite('Shot_Atk', 1)
    clearUponHandler(EVERY_FRAME)
    label(580)
    sprite('null', 20)
    AttackOff()
    EndMomentum(1)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(54)
    TriggerUponForState('jbef407_Nekodama', 32)


@State
def jbef407_NekodamaRady():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(2)
        if SLOT_95:
            PaletteIndex(3)
        AlphaValue(170)
        AddY(-50000)
    sprite('vrefjb407_00', 5)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 0)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 1)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 2)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 3)
    sprite('vrefjb407_01', 5)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 0)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 1)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 2)
    sprite('vrefjb407_02', 5)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 0)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 1)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 2)
    sprite('vrefjb407_03', 5)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 0)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 1)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 2)
    sprite('vrefjb407_04', 10)
    ParticleColorFromPalette(2, 2, 2)
    CallCustomizableParticle('jbef_407_nokosi', 0)


@State
def jbef407_Nekodama():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        PaletteIndex(2)
        if SLOT_95:
            PaletteIndex(3)
        AlphaValue(170)
        EnableAfterimage(1)
        AfterimageCount(3)
        AfterimageInterval(2)
        uponSendToLabel(32, 1)
    sprite('vrefjb407_10', 1)
    ParticleSize(800)
    ParticleRotationAngle(-30000)
    CallCustomizableParticle('jbef_407_shock', -1)
    CommonSE('015_blaze_0')
    label(0)
    sprite('vrefjb407_10', 3)
    Rotation(45000)
    ParticleColorFromPalette(2, 2, 2)
    ParticleSize(1500)
    CallCustomizableParticle('jbef_407_nokosi', -1)
    sprite('vrefjb407_10', 3)
    Rotation(45000)
    gotoLabel(0)
    label(1)
    sprite('vrefjb407_20', 2)
    EnableAfterimage(0)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    ParticleColorFromPalette(2, 2, 2)
    ParticleSize(2000)
    CallCustomizableParticle('jbef_407_nokosi', -1)
    CreateObject('jbef407_NekodamaAura', -1)
    sprite('vrefjb407_21', 2)
    sprite('vrefjb407_22', 2)
    sprite('vrefjb407_23', 2)
    sprite('vrefjb407_24', 2)
    loopRest()


@State
def jbef407_NekodamaAura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        Size(1500)
        AddRotationPerFrame(1500)
        PaletteIndex(2)
        if SLOT_95:
            PaletteIndex(3)
        ColorFromPaletteIndex(2)
        Eff3DEffect('jbef_407Aura00', '')
    sprite('null', 30)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    ConstantAlphaModifier(-8)
    SetScaleSpeed(15)
    loopRest()


@State
def jbef408_DashEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('jbef_408_dash')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 8)
    ConstantAlphaModifier(-31)
    loopRest()


@State
def jb430_slashMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
        BlendMode_Normal()
    sprite('null', 3)
    CreateObject('jb430_slash1', 100)
    CommonSE('012_stab_deep')
    sprite('null', 3)
    CreateObject('jb430_slash2', 100)
    CommonSE('012_stab_deep')
    sprite('null', 3)
    CreateObject('jb430_slash3', 100)
    CommonSE('012_stab_deep')
    sprite('null', 3)
    CreateObject('jb430_slashAdd', 100)
    CreateObject('jb430_slash4', 100)
    CreateParticle('jbef_430_suminokosi', 100)
    CommonSE('012_stab_deep')
    sprite('null', 15)
    sprite('null', 58)
    RemoveOnCallStateEnd(0)
    TriggerUponForState('jb430_slashAdd', 32)
    CreateObject('jb430_slashEnd', 100)
    DespawnEAEffect('jb430_slash1')
    DespawnEAEffect('jb430_slash2')
    DespawnEAEffect('jb430_slash3')
    DespawnEAEffect('jb430_slash4')


@State
def jb430_slashEnd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        AbsoluteY(0)
        IgnoreScreenfreeze(1)
    sprite('null', 58)
    Eff3DEffect('jbef_430fallslashEnd', '')
    DespawnEAEffect('jb430_slash1')
    DespawnEAEffect('jb430_slash2')
    DespawnEAEffect('jb430_slash3')
    DespawnEAEffect('jb430_slash4')
    SetScaleSpeedY(7)


@State
def jb430_slashAdd():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        AbsoluteY(0)
        AddY(-20000)
        AddScaleX(400)
        uponSendToLabel(32, 0)
        RenderLayer(12)
    sprite('null', 32767)
    Eff3DEffect('jbef_430baclkaura00', '')
    label(0)
    sprite('null', 10)
    IgnoreScreenfreeze(1)
    SetScaleXPerFrame(20)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def jb430_slash1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_430fallslash00', '')
        AbsoluteY(0)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 32767)


@State
def jb430_slash2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_430fallslash01', '')
        AbsoluteY(0)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 32767)


@State
def jb430_slash3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_430fallslash02', '')
        AbsoluteY(0)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 32767)


@State
def jb430_slash4():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_430fallslash03', '')
        AbsoluteY(0)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 32767)


@State
def jb430_ODSlash00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AbsoluteY(0)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Size(800)
    sprite('null', 4)
    Eff3DEffect('jbef_430OD_slash00', '')
    CreateObject('jb430_ODSlash00BG', 100)
    sprite('null', 4)
    Eff3DEffect('jbef_430OD_slash01', '')
    sprite('null', 10)
    Eff3DEffect('jbef_430OD_slash02', '')
    ScreenShake(10000, 10000)
    SetScaleSpeed(5)
    physicsYImpulse(-1250)
    sprite('null', 58)
    Eff3DEffect('jbef_430OD_slash02End', '')
    RemoveOnCallStateEnd(0)


@State
def jb430_ODSlash00BG():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AbsoluteY(0)
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('jbef_431od_slashadd')
    sprite('null', 18)
    sprite('null', 58)
    ConstantAlphaModifier(-4)
    RemoveOnCallStateEnd(0)


@State
def jb431_SlashEndEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        AddY(200000)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
    sprite('null', 6)
    LinkParticle('jbef_431crossAdd')
    Eff3DEffect('jbef_430cross00.DIG', '')
    Size(2)
    AddScaleX(100)
    SetScaleSpeed(100)
    PrivateSE('jbse_09')
    sprite('null', 20)
    SetScaleSpeed(1)
    sprite('null', 27)
    ScreenShake(10000, 10000)
    CreateParticle('jbef_431slashEnd', -1)
    Eff3DEffect('jbef_430slash00.DIG', '')
    SetScaleSpeed(0)
    AddScale(400)
    CommonSE('025_cleanhit_slash')
    sprite('null', 15)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def jb431_SlashEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        AbsoluteY(0)
        AddY(200000)
        CallPrivateEffect('jbef_431slash')
    sprite('null', 15)
    CreateObject('jb431_SlashBloomEff', 100)


@State
def jb431_SlashBloomEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(2)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('jbef_431slashBloom')
    sprite('null', 15)


@State
def jb431_CircleShockEff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Size(2000)
    sprite('null', 15)
    Eff3DEffect('jbef_430circle00.DIG', '')
    SetScaleSpeed(40)


@State
def jb431OD_SlashEffMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 4)
    CreateObject('jb431OD_SlashEff00', -1)
    sprite('null', 4)
    CreateObject('jb431OD_SlashEff01', -1)
    sprite('null', 32767)
    CreateObject('jb431OD_SlashEff02', -1)
    label(0)
    sprite('null', 4)
    TriggerUponForState('jb431OD_SlashEff00', 32)
    sprite('null', 4)
    TriggerUponForState('jb431OD_SlashEff01', 32)
    sprite('null', 1)
    TriggerUponForState('jb431OD_SlashEff02', 32)


@State
def jb431OD_SlashEff00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AddY(200000)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        AddX(-1000000)
        Size(1000)
        Eff3DEffect('jbef_430ODslash00.DIG', '')
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('jbef_431od_slashadd')
        uponSendToLabel(32, 1)
    sprite('null', 5)
    AlphaValue(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    CreateObject('jb431OD_jubei00', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    RemoveOnCallStateEnd(0)
    Eff3DEffect('jbef_430ODslash00End.DIG', '')
    SetScaleSpeed(5)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def jb431OD_SlashEff01():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AddY(200000)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        AddX(-700000)
        Size(800)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('jbef_431od_slashadd')
        Eff3DEffect('jbef_430ODslash01.DIG', '')
        uponSendToLabel(32, 1)
    sprite('null', 5)
    AlphaValue(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    CreateObject('jb431OD_jubei01', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    RemoveOnCallStateEnd(0)
    Eff3DEffect('jbef_430ODslash01End.DIG', '')
    SetScaleSpeed(5)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def jb431OD_SlashEff02():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        AddY(200000)
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        AddX(-300000)
        Size(800)
        ParticleColorFromPalette(1, 1, 1)
        CallPrivateEffect('jbef_431od_slashadd')
        Eff3DEffect('jbef_430ODslash02.DIG', '')
        uponSendToLabel(32, 1)
    sprite('null', 5)
    AlphaValue(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    CreateObject('jb431OD_jubei02', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    RemoveOnCallStateEnd(0)
    Eff3DEffect('jbef_430ODslash02End.DIG', '')
    SetScaleSpeed(5)
    sprite('null', 30)
    ConstantAlphaModifier(-8)


@State
def jb431OD_jubei00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        AddY(-100000)
        RenderLayer(1)
    sprite('jb201_03', 10)
    PrivateSE('jbse_09')
    CommonSE('000_airdash_0')
    sprite('jb201_03', 10)
    ConstantAlphaModifier(-26)
    physicsXImpulse(3000)


@State
def jb431OD_jubei01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        AddY(-100000)
        RenderLayer(1)
    sprite('jb211_06', 10)
    PrivateSE('jbse_02')
    sprite('jb211_06', 10)
    ConstantAlphaModifier(-26)
    physicsXImpulse(3000)


@State
def jb431OD_jubei02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        AddY(-100000)
        RenderLayer(1)
    sprite('jb400_03', 10)
    physicsXImpulse(3000)
    CommonSE('000_airdash_0')
    sprite('jb400_03', 10)
    ConstantAlphaModifier(-26)
    physicsXImpulse(3000)


@State
def jb432_eyerayEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(2)
        IgnoreScreenfreeze(2)
    sprite('vrefjb432_00', 6)
    sprite('vrefjb432_01', 6)
    sprite('vrefjb432_02', 6)
    sprite('vrefjb432_03', 6)
    CallCustomizableParticle('jbef_432buff_hatudo', 100)


@State
def jb432_BodyAuraEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('jbef_432Aura00.DIG', '')
        AddY(250000)
        Size(900)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    CreateParticle('jbef_432_shock', 100)
    CreateObject('jb432_BodyAuraEffCore', 100)
    sprite('null', 10)
    sprite('null', 20)
    ConstantAlphaModifier(-12)
    sprite('null', 20)
    sprite('null', 20)
    ConstantAlphaModifier(-12)


@State
def jb432_BodyAuraEffCore():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreScreenfreeze(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('jbef_432AuraCore.DIG', '')
        Size(400)
        AddY(-50000)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    sprite('null', 10)
    sprite('null', 20)
    ConstantAlphaModifier(-12)


@State
def jb440_startAtk00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Eff3DEffect('jbef_440startAtk00', '')
        Size(400)
        AddY(300000)
        AddX(150000)
    sprite('null', 3)
    AddScaleX(150)
    AddScaleY(45)
    sprite('null', 3)
    AddScaleX(300)
    AddScaleY(75)
    sprite('null', 3)
    AddScaleX(300)
    AddScaleY(75)
    sprite('null', 3)
    AddScaleX(150)
    AddScaleY(37)
    sprite('null', 3)
    Eff3DEffect('jbef_440startAtk01', '')
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    IgnorePauses(0)
    SetScaleSpeed(5)
    sprite('null', 56)
    AddScaleY(75)
    Eff3DEffect('jbef_440startAtk01end', '')
    ConstantAlphaModifier(-4)


@State
def jb440_slash00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Eff3DEffect('jbef_440slash00.DIG', '')
        Size(400)
        AddY(300000)
        AddX(200000)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    IgnoreFinishStop(1)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('jbef_440suminokosi', 100)
    sprite('null', 5)
    IgnoreFinishStop(0)
    sprite('null', 57)
    Eff3DEffect('jbef_440slash00End.DIG', '')
    SetScaleSpeed(2)


@State
def jb440_AddAtk():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(500)
        AddX(50000)
    sprite('null', 4)
    CreateObject('jb440_AddAtk00', 100)
    IgnoreFinishStop(1)
    sprite('null', 4)
    CreateObject('jb440_AddAtk01', 100)
    sprite('null', 10)
    SetScaleSpeed(3)
    physicsYImpulse(-2500)
    physicsXImpulse(-1500)
    PaletteIndex(2)
    ParticleColorFromPalette(1, 1, 1)
    CallCustomizableParticle('jbef_440suminokosi2', 100)
    ColorFromPaletteIndex(1)
    Eff3DEffect('jbef_440AddAtk02.DIG', '')
    IgnoreFinishStop(0)
    sprite('null', 57)
    Eff3DEffect('jbef_440AddAtk02End.DIG', '')
    RemoveOnCallStateEnd(0)


@State
def jb440_AddAtk00():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Eff3DEffect('jbef_440AddAtk00.DIG', '')
        Size(500)
    sprite('null', 4)
    sprite('null', 5)
    AlphaValue(128)
    ConstantAlphaModifier(-25)


@State
def jb440_AddAtk01():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(1)
        Eff3DEffect('jbef_440AddAtk01.DIG', '')
        Size(500)
    sprite('null', 4)
    sprite('null', 5)
    AlphaValue(128)
    ConstantAlphaModifier(-25)


@State
def jb430_Eff():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        SetScaleX(600)
        SetScaleY(6000)
    sprite('null', 30)


@State
def jb430_EffOD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        SetScaleX(1000)
        SetScaleY(10000)
    sprite('null', 30)


@State
def jb430_BunshinA():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        NoDamageAction(1)
    sprite('jb430_04', 12)
    physicsXImpulse(25000)
    ConstantAlphaModifier(-21)


@State
def jb430_BunshinB():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        NoDamageAction(1)
    sprite('jb430_04', 12)
    physicsXImpulse(-25000)
    ConstantAlphaModifier(-21)


@State
def jb431_Eff():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        SetScaleX(6000)
        SetScaleY(600)
    sprite('null', 30)
    LinkParticle('ef_ukemi')


@State
def jb431_EffOD():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        SetScaleY(600)
        RandAddScaleX(1000, 5000)
        RandAddRotation(10000, 60000)
    sprite('null', 3)
    LinkParticle('ef_ukemi')


@State
def jb431_BunshinA():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        NoDamageAction(1)
    sprite('jb431_01', 12)
    physicsXImpulse(25000)
    ConstantAlphaModifier(-21)


@State
def jb431_BunshinB():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        NoDamageAction(1)
    sprite('jb431_01', 12)
    physicsXImpulse(-25000)
    ConstantAlphaModifier(-21)


@State
def UltimateChage_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(1500)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(18)
        AirPushbackX(-1000)
        AirPushbackY(35000)
        YImpulseBeforeWallbounce(1800)
        Stagger(51)
        Crumple(41)
        PushbackX(8000)
        AirUntechableTime(60)
        StarterRating(2)
        Size(1200)
    sprite('Chage_Atk', 3)


@State
def UltimateChageEX_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(1500)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(30000)
        PushbackX(8000)
        AirUntechableTime(60)
        StarterRating(2)
        Size(1200)
    sprite('Chage_Atk', 3)


@State
def jb432_Eff():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        Size(1500)
        EffectPosition(3, 103)
    sprite('null', 30)
    LinkParticle('ef_ukemi')


@State
def ChageAuraGenerator():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            SLOT_51 = SLOT_51 + 1
            if not SLOT_51 % 30:
                SLOT_52 = 0
                CopyFromRightToLeft(23, 2, 52, 2, 2, 30)
                if not SLOT_52:

                    def RunOnObject_3():
                        CreateObject('ChageAura', 103)
    sprite('null', 32767)


@State
def ChageAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnContact(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1000)
    sprite('null', 30)
    LinkParticle('jbef_432_buffNml')


@State
def ChageAura2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnContact(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1000)
    sprite('null', 30)
    LinkParticle('jbef_432_buff2')


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(580)
        AddX(350000)
    sprite('null', 3000)
    CameraControlEnable(1)
    CameraFollowTarget(23, 23)
    label(580)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraFollowTarget(0, 0)


@State
def Astral_Camera():

    def upon_IMMEDIATE():
        Unknown4022(3)
        AddX(300000)

        def upon_32():
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)

        def upon_35():
            sendToLabel(3)

        def upon_36():
            sendToLabel(4)

        def upon_37():
            sendToLabel(5)

        def upon_38():
            sendToLabel(6)
    sprite('null', 32767)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    CameraWinnerControlStop(1)
    label(0)
    sprite('null', 32767)
    CameraPosition(600)
    AddX(300000)
    label(1)
    sprite('null', 32767)
    CameraPosition(1000)
    AddX(-300000)
    label(2)
    sprite('null', 32767)
    Unknown4022(0)
    physicsXImpulse(50000)
    label(3)
    sprite('null', 32767)
    physicsXImpulse(0)
    AddX(-300000)
    label(4)
    sprite('null', 32767)
    E0EAEffectPosition(22)
    label(5)
    sprite('null', 32767)
    E0EAEffectPosition(0)
    label(6)
    sprite('null', 110)
    XPositionRelativeFacing(700000)
    AbsoluteY(1000000)
    sprite('null', 20)
    physicsXImpulse(-34000)
    physicsYImpulse(-36000)
    sprite('null', 32767)
    EndMomentum(1)


@State
def jb450_ZanEff():

    def upon_IMMEDIATE():
        E0EAEffectRotation(2)
    sprite('null', 6)
    CommonSE('006_swing_blade_1')
    CommonSE('010_swing_sword_2')


@State
def jb450_AtkAura():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_450atkaura00', '')
        LinkParticle('jbef_450_underlight')
        uponSendToLabel(32, 0)
    sprite('null', 10)
    AlphaValue(0)
    CreateObject('jb450_AtkAura2', -1)
    CommonSE('016_explode_0')
    sprite('null', 10)
    ConstantAlphaModifier(13)
    CommonSE('016_explode_0')
    sprite('null', 32767)
    CreateObject('jb450_AtkAura2', -1)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(15)
    ConstantAlphaModifier(-12)


@State
def jb450_AtkAura2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('jbef_450atkaura01', '')
        Size(500)
    sprite('null', 39)


@State
def jb450_kaihouAura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Eff3DEffect('jbef_450kaihoaura00', '')
        Size(1200)
        AddScaleY(300)
    sprite('null', 8)
    ScreenShake(10000, 10000)
    CreateObject('jb450_kaihouShock', -1)
    sprite('null', 1)
    sprite('null', 230)
    sprite('null', 15)
    ConstantAlphaModifier(-17)
    E0EAEffectPosition(0)


@State
def jb450_kaihouShock():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_450kaihoshock', '')
        Size(1300)
        AddScaleZ(300)
    sprite('null', 10)
    CreateParticle('jbef_450shockbrust', -1)
    SetScaleXPerFrame(30)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleXPerFrame(10)


@State
def jb450_kidou():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou2')
        EnableAfterimage(1)
        AlphaValue(180)
    sprite('vrefjb450_00kidou', 8)
    sprite('vrefjb450_01kidou', 16)


@State
def jb450_kidou2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        PaletteIndex(1)
        BlendMode_Add()
        callSubroutine('zanzou2')
        EnableAfterimage(1)
        AlphaValue(180)
    sprite('vrefjb450_02kidou', 8)
    sprite('vrefjb450_03kidou', 24)


@State
def jbef_450flash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        BlendMode_Normal()
        LinkParticle('jbef_450flash')
    sprite('null', 30)


@State
def jbef_450weakpointBG():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_430weakpointBG', '')
        Size(1200)
        AddScaleX(-100)
        TeleportToObject(22)
        AddY(180000)
        AddX(-10000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    SetScaleSpeed(120)
    ConstantAlphaModifier(-12)
    loopRest()


@State
def jbef_450weakpoint():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        BlendMode_Normal()
        LinkParticle('jbef_450weakpoint')
        uponSendToLabel(32, 0)
        EffectPosition(22, 109)
        E0EAEffectPosition(22)
    sprite('null', 20)
    AlphaValue(0)
    Size(10)
    sprite('null', 10)
    AlphaValue(255)
    SetScaleSpeed(100)
    sprite('null', 32767)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    SetScaleSpeed(-80)
    loopRest()


@State
def jbef_450weakpoint_Terumi():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        BlendMode_Normal()
        Flip()
        PaletteIndex(4)
        uponSendToLabel(32, 0)
        TeleportToObject(22)
        E0EAEffectPosition(22)
        uponSendToLabel(32, 0)
        Eff3DEffect('jbef_450terumi', '')
        AddY(25000)
    sprite('null', 30)
    AlphaValue(0)
    sprite('null', 40)
    ConstantAlphaModifier(8)
    physicsXImpulse(-100)
    physicsYImpulse(100)
    sprite('null', 32767)
    physicsXImpulse(-50)
    physicsYImpulse(25)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def jbef_450weakpoint_Hazama():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        BlendMode_Normal()
        Flip()
        PaletteIndex(4)
        uponSendToLabel(32, 0)
        TeleportToObject(22)
        E0EAEffectPosition(22)
        uponSendToLabel(32, 0)
        Eff3DEffect('jbef_450terumi', '')
        AddY(25000)
    sprite('null', 30)
    AlphaValue(0)
    sprite('null', 40)
    ConstantAlphaModifier(2)
    physicsXImpulse(-100)
    physicsYImpulse(100)
    sprite('null', 32767)
    physicsXImpulse(-50)
    physicsYImpulse(25)
    ConstantAlphaModifier(-6)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def jb450_BG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_450wasibg', '')
        RenderLayer(2)
        SetScaleY(800)
        SetScaleZ(1000)
        SetScaleX(1000)
        AddY(80000)
        AlphaValue(240)
    sprite('null', 150)
    CreateObject('jb450_BGsub', -1)
    sprite('null', 9)
    ConstantAlphaModifier(-26)


@State
def jb450_BGsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_450filmgate', '')
        RenderLayer(1)
        SetScaleY(800)
        SetScaleZ(1000)
        SetScaleX(1000)
    sprite('null', 150)
    sprite('null', 9)
    ConstantAlphaModifier(-26)


@State
def jbef_450ZanzoNokosiMato():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        E0EAEffectPosition(2)
        AbsoluteY(0)
    sprite('null', 3)
    CreateObject('jbef_450ZanzoNokosi', -1)

    def RunOnObject_1():
        AddX(-400000)
    sprite('null', 3)
    CreateObject('jbef_450ZanzoNokosi', -1)

    def RunOnObject_1():
        AddX(-300000)
    sprite('null', 3)
    CreateObject('jbef_450ZanzoNokosi', -1)

    def RunOnObject_1():
        AddX(-200000)
    sprite('null', 60)
    CreateObject('jbef_450ZanzoNokosi', -1)

    def RunOnObject_1():
        AddX(-100000)


@State
def jbef_450ZanzoNokosi():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        E0EAEffectPosition(2)
        RenderLayer(11)
        AbsoluteY(0)
    sprite('jb450_26', 50)
    ConstantAlphaModifier(-5)


@State
def jb450_RedBG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        Eff3DEffect('jbef_450redbg', '')
        RenderLayer(2)
    sprite('null', 30)
    AlphaValue(0)
    sprite('null', 55)
    AlphaValue(255)


@State
def jb450_BG2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_450_wasibg2', '')
        RenderLayer(2)
        Size(400)
        AddX(-325000)
        AlphaValue(225)
        IgnoreScreenfreeze(1)
    sprite('null', 40)
    sprite('null', 50)
    ConstantAlphaModifier(-12)
    sprite('null', 1)
    CreateObject('jb450_BGEnd', -1)


@State
def jb450_BGEnd():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        Eff3DEffect('jbef_450bgend', '')
        RotationAngle(-25000)
        Size(1200)
        RenderLayer(4)
        AddX(-1300000)
    sprite('null', 115)


@State
def jb450_Slash():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_450slash00', '')
        AddX(-50000)
    sprite('null', 5)
    ScreenShake(50000, 50000)
    SetScaleSpeed(5)
    Size(800)
    sprite('null', 5)
    ScreenShake(40000, 40000)
    sprite('null', 4)
    Size(850)
    sprite('null', 4)
    Size(900)
    sprite('null', 6)
    Eff3DEffect('jbef_450slash01', '')
    Size(1100)
    sprite('null', 6)
    Eff3DEffect('jbef_450slash02', '')
    sprite('null', 40)
    CreateObject('jb450_SlashSub', -1)
    AlphaValue(0)


@State
def jb450_SlashSub():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('jbef_450slashRotate', '')
        Size(700)
        AddY(1000000)
        AddX(-1250000)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 4)
    Rotation(600000)
    PrivateSE('jbse_08')
    sprite('null', 4)
    Rotation(600000)
    sprite('null', 4)
    Rotation(600000)
    sprite('null', 4)
    Rotation(600000)
    AddScale(100)
    sprite('null', 4)
    Rotation(600000)
    AddScale(100)
    sprite('null', 4)
    Rotation(600000)
    AddScale(100)
    sprite('null', 4)
    Rotation(600000)
    AddScale(100)
    sprite('null', 4)
    Rotation(600000)
    AddScale(100)
    sprite('null', 4)
    Rotation(600000)
    AddScale(100)
    sprite('null', 4)
    Rotation(600000)
    ConstantAlphaModifier(-31)
    sprite('null', 4)
    Rotation(600000)


@State
def jb610_Slash():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('jbef_610slash00', '')
        AddX(100000)
        AddY(75000)
        Size(1500)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 20)
    sprite('null', 57)
    ConstantAlphaModifier(-4)
    Eff3DEffect('jbef_610slash01', '')


@State
def jb900_Ase():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('jbef_900ase')
    sprite('null', 20)
    AlphaValue(0)
    ConstantAlphaModifier(12)
    sprite('null', 32767)


@State
def jb611_Tail_Event():

    def upon_IMMEDIATE():
        SetZVal(500)
    sprite('jb611_00s', 8)
    sprite('jb611_01s', 8)
    sprite('jb611_02s', 8)
    label(0)
    sprite('jb611_03s', 10)
    sprite('jb611_04s', 10)
    sprite('jb611_05s', 10)
    sprite('jb611_06s', 10)
    loopRest()
    gotoLabel(0)


@State
def NOISE():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ef_eventnoise.DIG', '')
        FaceSpawnLocation()
        RenderLayer(4)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 120)
    loopRest()
