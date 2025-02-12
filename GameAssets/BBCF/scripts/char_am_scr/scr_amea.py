@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AM.DIG', '')
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
def EMB_AM_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AM.DIG', '')
        RenderLayer(5)
        Size(1400)
        AddY(16000)
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
def EMB_AM_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_AM.DIG', '')
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
def __6DTop():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(250)
        AttackP1(90)
        AttackP2(98)
        BonusProration(110)
        GroundedHitstunAnimation(1)
        Hitstop(2)
        AirPushbackY(-15000)
        HardKnockdown(1)
        AttackDirection(4)
        StarterRating(2)
        Unknown12052(1)
        HitsparkSize(500)
        ReduceHitEffects(1)
        NoDamageAction(1)
        PaletteIndex(0)
        BlendMode_Normal()
        FaceLeft()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        setGravity(3000)
        CreateParticle('amef_6D_koma', -1)
        CreateObject('6Ddrilwind', -1)
        CopyFromRightToLeft(23, 2, 56, 3, 2, 59)
        if SLOT_56 == 2:
            SLOT_57 = 1
        elif SLOT_56 == 3:
            SLOT_58 = 1

        def upon_LANDING():
            EndMomentum(1)
            setGravity(0)
            TriggerUponForState('NmlAtk6D', 32)

        def upon_32():
            clearUponHandler(32)
            ChipPercentage(10)
            PushbackX(-5000)
            AirPushbackX(-5000)
            if not SLOT_54:
                CopyFromRightToLeft(23, 2, 55, 22, 2, 22)
                if SLOT_55 >= SLOT_XDistanceFromCenterOfStage:
                    SetAcceleration(-1500)
                else:
                    SetAcceleration(1500)
            TriggerUponForState('6Ddrilwind', 33)
            sendToLabel(101)

        def upon_33():
            clearUponHandler(33)
            ChipPercentage(30)
            PushbackX(-10000)
            AirPushbackX(-10000)
            Blockstun(18)
            if not SLOT_54:
                CopyFromRightToLeft(23, 2, 55, 22, 2, 22)
                if SLOT_55 >= SLOT_XDistanceFromCenterOfStage:
                    SetAcceleration(-2000)
                else:
                    SetAcceleration(2000)
            TriggerUponForState('6Ddrilwind', 34)
            sendToLabel(201)

        def upon_34():
            clearUponHandler(34)
            MinimumDamage(5)
            ChipPercentage(50)
            PushbackX(-15000)
            AirPushbackX(-15000)
            Blockstun(20)
            CHHardKnockdown(21)
            if not SLOT_54:
                CopyFromRightToLeft(23, 2, 55, 22, 2, 22)
                if SLOT_55 >= SLOT_XDistanceFromCenterOfStage:
                    SetAcceleration(-2500)
                else:
                    SetAcceleration(2500)
            TriggerUponForState('6Ddrilwind', 35)
            sendToLabel(301)

        def upon_35():
            clearUponHandler(35)
            TriggerUponForState('6Ddrilwind', 32)
            sendToLabel(1)

        def upon_RELEASE_D():
            if SLOT_52 >= 3:
                TriggerUponForState('NmlAtk6D', 33)
        RunLoopUpon(17, 30)

        def upon_17():
            clearUponHandler(17)
            NoAttackDuringAction(1)
            SetAcceleration(0)
            TriggerUponForState('NmlAtk6D', 33)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(17)
            SLOT_54 = 1
            SetAcceleration(0)
            TriggerUponForState('NmlAtk6D', 34)
        AttackOff()
    label(100)
    sprite('vramef213_10', 3)
    SpriteIfNot0(2, 2, 57)
    SpriteIfNot0(1, 2, 58)
    PrivateSE('amse_01_loop')
    sprite('vramef213_11', 3)
    SpriteIfNot0(2, 2, 57)
    SpriteIfNot0(1, 2, 58)
    PrivateSE('amse_01_loop')
    sprite('vramef213_12', 3)
    SpriteIfNot0(2, 2, 57)
    SpriteIfNot0(1, 2, 58)
    PrivateSE('amse_01_loop')
    gotoLabel(100)
    label(101)
    sprite('vramef213_10', 3)
    RefreshMultihit()
    CallCustomizableParticle('amef_213_shock', -1)
    ParticleColorFromPalette(226, 226, 226)
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_01_loop')
    if SLOT_54:
        XImpulseAcceleration(70)
    sprite('vramef213_11', 3)
    RefreshMultihit()
    CallCustomizableParticle('amef_213_shock', -1)
    ParticleColorFromPalette(226, 226, 226)
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_01_loop')
    if SLOT_54:
        XImpulseAcceleration(70)
    sprite('vramef213_12', 3)
    RefreshMultihit()
    CallCustomizableParticle('amef_213_shock', -1)
    ParticleColorFromPalette(226, 226, 226)
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_01_loop')
    if SLOT_54:
        XImpulseAcceleration(70)
    gotoLabel(101)
    label(200)
    sprite('vramef213_10', 2)
    PrivateSE('amse_02_loop')
    sprite('vramef213_11', 2)
    PrivateSE('amse_02_loop')
    sprite('vramef213_12', 2)
    PrivateSE('amse_02_loop')
    gotoLabel(200)
    label(201)
    sprite('vramef213_10', 2)
    RefreshMultihit()
    CallCustomizableParticle('amef_213_shock', -1)
    ParticleColorFromPalette(226, 226, 226)
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_02_loop')
    if SLOT_54:
        XImpulseAcceleration(70)
    sprite('vramef213_11', 1)
    RefreshMultihit()
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_02_loop')
    if SLOT_54:
        XImpulseAcceleration(70)
    sprite('vramef213_11', 1)
    CallCustomizableParticle('amef_213_shocklv2', -1)
    ParticleColorFromPalette(226, 226, 226)
    sprite('vramef213_12', 2)
    RefreshMultihit()
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_02_loop')
    if SLOT_54:
        XImpulseAcceleration(70)
    gotoLabel(201)
    label(300)
    sprite('vramef213_10', 1)
    PrivateSE('amse_03_loop')
    sprite('vramef213_11', 1)
    PrivateSE('amse_03_loop')
    sprite('vramef213_12', 1)
    PrivateSE('amse_03_loop')
    gotoLabel(300)
    label(301)
    sprite('vramef213_10', 1)
    RefreshMultihit()
    CallCustomizableParticle('amef_213_shock', -1)
    ParticleColorFromPalette(226, 226, 226)
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_03_loop')
    if SLOT_54:
        XImpulseAcceleration(80)
    sprite('vramef213_11', 1)
    RefreshMultihit()
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_03_loop')
    if SLOT_54:
        XImpulseAcceleration(80)
    sprite('vramef213_12', 1)
    RefreshMultihit()
    SLOT_52 = SLOT_52 + 1
    PrivateSE('amse_03_loop')
    if SLOT_54:
        XImpulseAcceleration(80)
    gotoLabel(301)
    label(1)
    clearUponHandler(RELEASE_D)
    sprite('keep', 1)
    RefreshMultihit()
    CancelIfPlayerHit(0)
    RemoveOnCallStateEnd(0)
    XImpulseAcceleration(20)
    SetAcceleration(0)
    sprite('vramef213_20', 4)
    XImpulseAcceleration(20)
    sprite('vramef213_21', 4)
    XImpulseAcceleration(20)
    sprite('vramef213_22', 4)
    XImpulseAcceleration(0)
    sprite('vramef213_23', 4)
    sprite('vramef213_24', 4)
    sprite('vramef213_25', 4)
    sprite('vramef213_26', 32)
    ConstantAlphaModifier(-16)


@State
def __6Ddrilwind():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        ColorFromPaletteIndex(225)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 3)
        uponSendToLabel(33, 0)
        uponSendToLabel(34, 1)
        uponSendToLabel(35, 2)
        AlphaValue(150)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    Eff3DEffect('am_213drillwind_00.DIG', '')
    FaceSpawnLocation()
    Size(800)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('am_213drillwind_01.DIG', '')
    FaceSpawnLocation()
    Size(900)
    label(2)
    sprite('null', 32767)
    Eff3DEffect('am_213drillwind_02.DIG', '')
    FaceSpawnLocation()
    Size(950)
    label(3)
    sprite('null', 20)
    SetScaleXPerFrame(100)
    ConstantAlphaModifier(-26)


@Subroutine
def Drill_SE():
    if SLOT_51:
        PrivateSE('amse_01_loop')
    if SLOT_52:
        PrivateSE('amse_02_loop')
    if SLOT_53:
        PrivateSE('amse_03_loop')


@State
def GroundDrill():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Damage(1000)
        ChipPercentage(15)
        SameMoveProration(10)
        PushbackX(12000)
        Hitstop(2)
        UseSlashHitspark(1)
        DistanceCheck(200000, -200000, -1, -1)

        def upon_32():
            AttackLevel_(3)
            AirUntechableTime(30)
            AirPushbackX(2000)
            AirPushbackY(20000)
            AirHitstunAnimation(10)
            GroundedHitstunAnimation(10)
            TriggerUponForState('401_drill', 33)
            PrivateSE('amse_01')
            SLOT_51 = 1
            SLOT_58 = 10
            HitsPerCall(3, 0, 1, 1, 3, 0, 3, 0)

            def upon_OPPONENT_HIT():
                Hitstop(13)
                SLOT_58 = 3
                NoAttackDuringAction(1)

        def upon_33():
            AttackLevel_(4)
            AirUntechableTime(40)
            AirPushbackX(4000)
            AirPushbackY(30000)
            AirHitstunAnimation(18)
            GroundedHitstunAnimation(18)
            TriggerUponForState('401_drill', 34)
            PrivateSE('amse_02')
            SLOT_52 = 1
            SLOT_58 = 15
            HitsPerCall(5, 0, 1, 1, 5, 0, 5, 0)

            def upon_OPPONENT_HIT():
                Hitstop(14)
                SLOT_58 = 3
                NoAttackDuringAction(1)

        def upon_34():
            AttackLevel_(5)
            AirUntechableTime(50)
            AirPushbackX(6000)
            AirPushbackY(40000)
            AirHitstunAnimation(18)
            GroundedHitstunAnimation(18)
            TriggerUponForState('401_drill', 35)
            PrivateSE('amse_03')
            SLOT_53 = 1
            SLOT_58 = 20
            HitsPerCall(7, 0, 1, 1, 7, 0, 7, 0)

            def upon_OPPONENT_HIT():
                Hitstop(15)
                SLOT_58 = 3
                NoAttackDuringAction(1)
        PaletteIndex(0)
        Size(0)
        SetScaleSpeedY(80)
        SetScaleXPerFrame(160)
        WallCollisionDetection(1)
        NoDamageAction(1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0

        def upon_45():
            if not SLOT_21:
                sendToLabel(1)
        uponSendToLabel(54, 1)
        uponSendToLabel(35, 1)
        CancelIfPlayerHit(3)
    sprite('null', 1)
    IgnorePauses(3)
    sprite('null', 2)
    CallCustomizableParticle('amef_401start_skr', -1)
    ParticleColorFromPalette(226, 226, 226)
    sprite('vramef401_00', 3)
    IgnorePauses(0)
    sprite('vramef401_00', 3)
    sprite('vramef401_00', 1)
    CreateObject('401_drill', -1)
    SetScaleSpeed(0)
    label(0)
    sprite('vramef401_01', 2)
    Size(900)
    SLOT_58 = SLOT_58 + -1
    CallCustomizableParticle('amef_401dliwind_kuzu2', 0)
    ParticleColorFromPalette(226, 226, 226)
    RefreshMultihit()
    callSubroutine('Drill_SE')
    sprite('vramef401_02', 2)
    CallCustomizableParticle('amef_401dliwind_kuzu2', 0)
    ParticleColorFromPalette(226, 226, 226)
    RefreshMultihit()
    callSubroutine('Drill_SE')
    sprite('vramef401_03', 1)
    CallCustomizableParticle('amef_401dliwind_kuzu2', 0)
    ParticleColorFromPalette(226, 226, 226)
    RefreshMultihit()
    callSubroutine('Drill_SE')
    sprite('vramef401_03', 1)
    if not SLOT_58:
        sendToLabel(1)
    gotoLabel(0)
    label(1)
    sprite('vramef401_01', 4)
    clearUponHandler(45)
    SetScaleSpeed(0)
    TriggerUponForState('401_drill', 32)
    clearUponHandler(EVERY_FRAME)
    AttackOff()
    NoDamageAction(1)
    callSubroutine('Drill_SE')
    sprite('vramef401_02', 4)
    callSubroutine('Drill_SE')
    sprite('vramef401_03', 4)
    callSubroutine('Drill_SE')
    sprite('vramef401_01', 4)
    callSubroutine('Drill_SE')
    sprite('vramef401_02', 4)
    callSubroutine('Drill_SE')
    sprite('vramef401_03', 4)
    callSubroutine('Drill_SE')
    sprite('vramef401_01', 5)
    sprite('vramef401_02', 5)
    sprite('vramef401_03', 5)
    sprite('vramef401_01', 6)
    sprite('vramef401_02', 6)
    sprite('vramef401_03', 6)
    sprite('vramef401_04', 6)
    sprite('null', 10)


@State
def __202_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('null', 60)
    CreateParticle('amef_C_attack', 100)


@State
def __212_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('null', 60)
    ParticleRotationAngle(-22500)
    CallCustomizableParticle('amef_C_attack', 100)


@State
def __232_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('null', 60)
    CreateParticle('amef_C_attack', 100)


@State
def __252_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('null', 60)
    ParticleRotationAngle(20000)
    CallCustomizableParticle('amef_C_attack', 100)


@State
def __255_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('null', 60)
    CreateParticle('amef_C_attack', 100)


@State
def __256_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
    sprite('null', 60)
    ParticleRotationAngle(60000)
    CallCustomizableParticle('amef_C_attack', 100)


@State
def D_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_drillmonsholv1_kuzu', -1)
    gotoLabel(0)


@State
def D_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 3)
    CreateParticle('amef_drilv1wind00', -1)
    gotoLabel(0)


@State
def D_tornado3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 6)
    CreateParticle('amef_5D_Lv1', -1)
    gotoLabel(0)


@State
def D_lv2_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_drillmonsholv2_kuzu', -1)
    gotoLabel(0)


@State
def D_lv2_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 3)
    CreateParticle('amef_drilv2wind00', -1)
    gotoLabel(0)


@State
def D_lv2_tornado3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 6)
    CreateParticle('amef_5D_Lv2', -1)
    gotoLabel(0)


@State
def D_lv3_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_drillmonsholv3_kuzu', -1)
    gotoLabel(0)


@State
def D_lv3_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 3)
    CreateParticle('amef_shagadriwind00', -1)
    gotoLabel(0)


@State
def D_lv3_tornado3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 6)
    CreateParticle('amef_5D_Lv3', -1)
    gotoLabel(0)


@State
def __203_drill():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        ColorFromPaletteIndex(224)
        Eff3DEffect('amef_253_drillwind00.DIG', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 3)
        uponSendToLabel(33, 0)
        uponSendToLabel(34, 1)
        uponSendToLabel(35, 2)
        SetScaleY(800)
        AddX(-60000)
        AlphaValue(200)
    label(0)
    sprite('null', 32767)
    SetScaleX(1050)
    SetScaleY(600)
    AlphaValue(150)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind01.DIG', '')
    FaceSpawnLocation()
    SetScaleX(1050)
    SetScaleY(800)
    label(2)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind02.DIG', '')
    FaceSpawnLocation()
    Size(1000)
    label(3)
    sprite('null', 10)
    SetScaleSpeed(30)
    ConstantAlphaModifier(-26)


@State
def __2D_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_shagadrilv1_kuzu2', -1)
    gotoLabel(0)


@State
def __2D_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 3)
    CreateParticle('amef_shagawindlv1_01', -1)
    gotoLabel(0)


@State
def __2D_tornado3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 6)
    ParticleRotationAngle(25000)
    CallCustomizableParticle('amef_2D_Lv1', -1)
    gotoLabel(0)


@State
def __2D_lv2_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_shagadrilv2_sub', -1)
    gotoLabel(0)


@State
def __2D_lv2_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 3)
    CreateParticle('amef_shagawindlv2_01', -1)
    gotoLabel(0)


@State
def __2D_lv2_tornado3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 6)
    ParticleRotationAngle(25000)
    CreateParticle('amef_5D_Lv2', -1)


@State
def __2D_lv3_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_shagadrilv3_sub', -1)
    gotoLabel(0)


@State
def __2D_lv3_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 3)
    CreateParticle('amef_shagawindlv3_01', -1)
    gotoLabel(0)


@State
def __2D_lv3_tornado3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 6)
    ParticleRotationAngle(25000)
    CallCustomizableParticle('amef_2D_Lv3', -1)
    gotoLabel(0)


@State
def __233_drill():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('amef_253_drillwind00.DIG', '')
        FaceSpawnLocation()
        PaletteIndex(0)
        ColorFromPaletteIndex(224)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 3)
        uponSendToLabel(33, 0)
        uponSendToLabel(34, 1)
        uponSendToLabel(35, 2)
        RotationAngle(-60000)
        AddY(480000)
        AddX(140000)
        SetScaleY(800)
    label(0)
    sprite('null', 32767)
    SetScaleX(1050)
    SetScaleY(600)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind01.DIG', '')
    FaceSpawnLocation()
    SetScaleX(1050)
    SetScaleY(800)
    label(2)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind02.DIG', '')
    FaceSpawnLocation()
    Size(1000)
    label(3)
    sprite('null', 10)
    SetScaleSpeed(30)
    ConstantAlphaModifier(-26)


@State
def amef_airD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_airdrilv1_pos', -1)
    gotoLabel(0)


@State
def amef_airD2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 1)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('amef_airD', 1)
    sprite('null', 1)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('amef_airD', 1)
    sprite('null', 1)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('amef_airD', 1)
    sprite('null', 1)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('amef_airD', 1)
    sprite('null', 1)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('amef_airD', 1)
    sprite('null', 1)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('amef_airD', 1)
    gotoLabel(0)


@State
def __253_drill():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        ColorFromPaletteIndex(224)
        Eff3DEffect('amef_253_drillwind00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(44000)
        AddY(40000)
        AddX(-40000)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 3)
        uponSendToLabel(33, 0)
        uponSendToLabel(34, 1)
        uponSendToLabel(35, 2)
    label(0)
    sprite('null', 32767)
    SetScaleY(600)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind01.DIG', '')
    FaceSpawnLocation()
    SetScaleY(720)
    label(2)
    sprite('null', 32767)
    DespawnEAEffect('drilwindB')
    Eff3DEffect('amef_253_drillwind02.DIG', '')
    FaceSpawnLocation()
    SetScaleY(750)
    label(3)
    sprite('null', 1)
    AlphaValue(0)


@State
def __401_drill():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        ColorFromPaletteIndex(224)
        Eff3DEffect('am_401drillwind_00.DIG', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 3)
        uponSendToLabel(33, 0)
        uponSendToLabel(34, 1)
        uponSendToLabel(35, 2)
        Size(300)
        AlphaValue(200)
    label(0)
    sprite('null', 32767)
    AlphaValue(150)
    SetScaleX(650)
    SetScaleY(1000)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('am_401drillwind_01.DIG', '')
    FaceSpawnLocation()
    SetScaleX(750)
    SetScaleY(1100)
    label(2)
    sprite('null', 32767)
    Eff3DEffect('am_401drillwind_02.DIG', '')
    FaceSpawnLocation()
    SetScaleX(800)
    SetScaleY(1400)
    label(3)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    ConstantAlphaModifier(-26)


@State
def Air6D_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_drillmonsholv1_kuzu', -1)
    gotoLabel(0)


@State
def Air6D_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 6)
    CreateParticle('amef_air6D_Lv1', -1)
    gotoLabel(0)


@State
def Air6D_lv2_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_drillmonsholv2_kuzu', -1)
    gotoLabel(0)


@State
def Air6D_lv2_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 6)
    CreateParticle('amef_air6D_Lv2', -1)
    gotoLabel(0)


@State
def Air6D_lv3_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(0)
    label(0)
    sprite('null', 3)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('amef_drillmonsholv3_kuzu', -1)
    gotoLabel(0)


@State
def Air6D_lv3_tornado2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 6)
    CreateParticle('amef_air6D_Lv3', -1)
    gotoLabel(0)


@State
def __203_drill():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        ColorFromPaletteIndex(224)
        Eff3DEffect('amef_253_drillwind00.DIG', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        uponSendToLabel(32, 3)
        uponSendToLabel(33, 0)
        uponSendToLabel(34, 1)
        uponSendToLabel(35, 2)
        SetScaleY(800)
        AddX(-60000)
        AlphaValue(200)
    label(0)
    sprite('null', 32767)
    SetScaleX(1050)
    SetScaleY(600)
    AlphaValue(150)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind01.DIG', '')
    FaceSpawnLocation()
    SetScaleX(1050)
    SetScaleY(800)
    label(2)
    sprite('null', 32767)
    Eff3DEffect('amef_253_drillwind02.DIG', '')
    FaceSpawnLocation()
    Size(1000)
    label(3)
    sprite('null', 10)
    SetScaleSpeed(30)
    ConstantAlphaModifier(-26)


@State
def __402_punch_miss():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        AlphaValue(255)
        ForceBloomMaskOn(1)
        AddX(550000)
        AddY(-4000)
    sprite('vramef402_00', 5)
    CreateObject('402_punch_Particle', 0)
    sprite('vramef402_01', 5)
    sprite('vramef402_02', 5)
    sprite('vramef402_03', 5)
    sprite('vramef402_10', 6)
    sprite('vramef402_11', 6)
    sprite('vramef402_22', 6)


@State
def __402_punchA():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('402_punchExe', 2, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        PreventAirborneHit(0)
        PreventGroundedHit(1)
        DoNotHitKnockedDownOpp(0)
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        AlphaValue(255)
        ForceBloomMaskOn(1)
        AddX(400000)
        AddY(-4000)
        ScreenCollision(1)
        SetZVal(501)
        EnableRapidCancel(0)

        def upon_32():
            AttackOff()
    sprite('vramef402_00', 1)
    CreateObject('402_punch_Particle', 0)
    CreateObject('402_punch_Particle_b', 0)
    sprite('vramef402_00', 1)
    CommonSE('005_swing_grap_2_1')
    ScreenCollision(0)
    sprite('vramef402_01', 4)
    sprite('vramef402_02', 3)
    sprite('vramef402_03', 3)
    sprite('vramef402_03', 3)
    AttackOff()
    sprite('vramef402_10', 6)
    CommonSE('019_cloth_b')
    sprite('vramef402_11', 6)
    sprite('vramef402_22', 6)


@State
def __402_punchB():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('402_punchExe', 2, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        PreventAirborneHit(0)
        PreventGroundedHit(1)
        DoNotHitKnockedDownOpp(0)
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        AlphaValue(255)
        ForceBloomMaskOn(1)
        AddX(200000)
        AddY(-4000)
        ScreenCollision(1)
        SetZVal(501)
        EnableRapidCancel(0)

        def upon_32():
            AttackOff()
    sprite('vramef402_00', 1)
    CreateObject('402_punch_Particle', 0)
    CreateObject('402_punch_Particle_b', 0)
    sprite('vramef402_00', 1)
    CommonSE('005_swing_grap_2_1')
    ScreenCollision(0)
    sprite('vramef402_01', 4)
    sprite('vramef402_02', 3)
    sprite('vramef402_03', 3)
    sprite('vramef402_03', 3)
    AttackOff()
    sprite('vramef402_10', 6)
    CommonSE('019_cloth_b')
    sprite('vramef402_11', 6)
    sprite('vramef402_22', 6)


@State
def __402_punch():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('402_punchExe', 2, 0, 0)
        SetZLine(0, 50)
        DistanceCheck(-1, -1, -1, -1)
        RangeCheck(-1)
        ThrowTechWindow(-1)
        PreventAirborneHit(0)
        PreventGroundedHit(1)
        DoNotHitKnockedDownOpp(0)
        IgnorePauses(2)
        PaletteIndex(0)
        BlendMode_Normal()
        AlphaValue(255)
        ForceBloomMaskOn(1)
        AddX(1000000)
        AddY(-4000)
        ScreenCollision(1)
        SetZVal(501)
        EnableRapidCancel(0)

        def upon_32():
            AttackOff()
    sprite('vramef402_00', 1)
    CreateObject('402_punch_Particle', 0)
    CreateObject('402_punch_Particle_b', 0)
    sprite('vramef402_00', 1)
    CommonSE('005_swing_grap_2_1')
    ScreenCollision(0)
    sprite('vramef402_01', 4)
    sprite('vramef402_02', 3)
    sprite('vramef402_03', 3)
    sprite('vramef402_03', 3)
    AttackOff()
    sprite('vramef402_10', 6)
    CommonSE('019_cloth_b')
    sprite('vramef402_11', 6)
    sprite('vramef402_22', 6)


@State
def __402_punchExe():

    def upon_IMMEDIATE():
        AttackDefaults_SuccessThrow(2, 0, 0)
        AttackLevel_(3)
        Damage(2700)
        AttackP2(70)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(-22000)
        YImpulseBeforeWallbounce(0)
        HardKnockdown(10)
        AutoHitStopSending(1)
        MinimumDamage(0)
        Unknown12052(2)
        CHStateIfCHStart(23)
        CHAirUntechableTime(60)
        CHAirPushbackY(-45000)
        CHGroundBounce(1)
        CHHardKnockdown(0)
        SetZVal(501)
    sprite('vramef402_03', 13)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    AttackOff()
    sprite('vramef402_20', 8)
    OppThrowAnimation(28, 0)
    OppThrowPosition(0, 5, 5, 0, 0)
    RefreshMultihit()
    CommonSE('100_hit_grap_3')
    sprite('vramef402_21', 6)
    sprite('vramef402_22', 6)


@State
def __402_punch_Particle():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        E0EAEffectPosition(2)
    sprite('null', 100)
    LinkParticle('amef_402_upper')


@State
def __402_punch_Particle_b():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        E0EAEffectPosition(2)
    sprite('null', 100)
    ParticleColorFromPalette(64, 67, 67)
    CallPrivateEffect('amef_402_upper_b')


@State
def __403_tossinaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        PaletteIndex(1)
        ColorFromPaletteIndex(53)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('amef_404aura00', '')
        FaceSpawnLocation()
        AlphaValue(0)
        uponSendToLabel(32, 0)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    LinkParticle('amef_403atk_pos')
    sprite('null', 5)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    label(0)
    sprite('null', 5)
    CreateParticle('amef_403atkend_pos', -1)
    ConstantAlphaModifier(-51)


@State
def __430_tossindril():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        PaletteIndex(1)
        ColorFromPaletteIndex(63)
        RemoveOnCallStateEnd(2)
        SetScaleX(1200)
        uponSendToLabel(32, 0)
    sprite('null', 11)
    Eff3DEffect('amef_430_aura00', '')
    FaceSpawnLocation()
    LinkParticle('amef_430slash_spd2')
    sprite('null', 10)
    sprite('null', 32767)
    SetScaleXPerFrame(0)
    label(0)
    sprite('null', 10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __430_roop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        SetScaleX(1200)
        uponSendToLabel(32, 0)
    label(1)
    sprite('null', 10)
    CreateObject('430_2daura', -1)
    gotoLabel(1)
    label(0)
    sprite('null', 10)
    CreateObject('430_2daura', -1)
    ConstantAlphaModifier(-17)
    sprite('null', 5)
    sprite('null', 10)


@State
def __430_2daura():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        SetZVal(500)
        SetScaleY(1000)
        SetScaleX(1600)
        AddX(30000)
    sprite('vramef430_00', 2)
    sprite('vramef430_01', 2)
    sprite('vramef430_02', 2)
    sprite('vramef430_03', 2)
    sprite('vramef430_04', 2)
    sprite('vramef430_05', 2)
    sprite('vramef430_06', 3)
    sprite('vramef430_07', 3)
    sprite('vramef430_08', 3)
    sprite('vramef430_09', 3)
    sprite('vramef430_10', 3)


@State
def __430_slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        TeleportToObject(22)
        AddY(240000)
        uponSendToLabel(32, 0)
    label(1)
    sprite('null', 5)
    CallCustomizableParticle('amef_430slash_b', -1)
    ParticleColorFromPalette(226, 226, 226)
    gotoLabel(1)
    label(0)
    sprite('null', 20)
    CallCustomizableParticle('amef_430slash_finish', -1)
    ParticleColorFromPalette(226, 226, 226)
    CreateParticle('amef_430bomyotyou_d', -1)


@State
def __430_bomsakra():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(63)
        Eff3DEffect('amef_430_bom00.DIG', '')
        FaceSpawnLocation()
    sprite('null', 10)
    sprite('null', 15)
    CreateObject('430_bomsakrabloom', -1)
    sprite('null', 5)


@State
def __430_bomsakrabloom():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(63)
        Eff3DEffect('amef_430_bombloom.DIG', '')
        FaceSpawnLocation()
    sprite('null', 15)
    sprite('null', 10)
    SetScaleSpeed(-20)
    ConstantAlphaModifier(-26)


@State
def __430_bom():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        AddY(250000)
    sprite('null', 5)
    PaletteIndex(1)
    ParticleColorFromPalette(48, 48, 48)
    CallCustomizableParticle('amef_430bom_skr', -1)
    CreateObject('430_bomsakra', -1)
    sprite('null', 8)
    CreateObject('430_bomyugami', -1)
    sprite('null', 30)
    PaletteIndex(1)
    ColorFromPaletteIndex(63)
    Eff3DEffect('amef_430_sakura', '')
    FaceSpawnLocation()
    AddRotationPerFrame(6000)
    SetScaleSpeed(30)
    ConstantAlphaModifier(-5)


@State
def __430_bomyugami():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    sprite('vr_yugami', 20)
    ParticleTransparency(1)
    PlayerTransparency(10000)
    SetScaleSpeed(100)


@State
def __431_wind():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
        ColorFromPaletteIndex(225)
        Eff3DEffect('am_401drillwind_02.DIG', '')
        FaceSpawnLocation()
        SetScaleY(0)
        SetScaleX(800)
    sprite('null', 8)
    SetScaleSpeedY(150)
    ConstantAlphaModifier(-10)
    sprite('null', 10)
    SetScaleSpeedY(0)
    sprite('null', 10)
    SetScaleSpeedY(-150)
    ConstantAlphaModifier(-26)


@State
def amef_408():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        AttackP2(79)
        AirUntechableTime(39)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        PushbackX(50000)
        AirPushbackX(15000)
        AirPushbackY(33000)
        CHAirPushbackY(50000)
        StarterRating(2)
        Unknown12052(1)
        UseSlashHitspark(1)
        ForceBloomMaskOn(1)
        AddX(250000)
        WallCollisionDetection(1)
        PrivateSE('amse_01_loop')
        PrivateSE('amse_02_loop')
        PrivateSE('amse_02_loop')
        SLOT_58 = 2
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)

        def upon_54():
            clearUponHandler(54)
            XImpulseAcceleration(0)
            sendToLabel(9)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 3)
    CreateObject('amef_408_tornado', -1)
    sprite('vramef406ex_col', 3)
    physicsXImpulse(25000)
    WallCollisionDetection(0)
    label(0)
    sprite('vramef406_col', 3)
    SLOT_58 = SLOT_58 + -1
    XImpulseAcceleration(80)
    sprite('vramef406_col', 3)
    XImpulseAcceleration(80)
    sprite('vramef406_col', 3)
    XImpulseAcceleration(80)
    loopRest()
    if SLOT_58:
        conditionalSendToLabel(0)
    label(1)
    sprite('vramef406_col', 12)
    XImpulseAcceleration(0)
    label(9)
    sprite('null', 20)
    NoAttackDuringAction(1)
    TriggerUponForState('amef_408_tornado', 32)


@State
def amef_408_tornado():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Unknown4022(2)
        AddY(16000)
        PaletteIndex(0)
        BlendMode_Normal()
        ForceBloomMaskOn(1)
        CreateObject('amef_408_tornado_add', -1)
        uponSendToLabel(32, 0)
        Size(1000)
    sprite('vramef406_00', 3)
    label(1)
    sprite('vramef406_01', 3)
    sprite('vramef406_02', 3)
    sprite('vramef406_03', 3)
    sprite('vramef406_04', 3)
    sprite('vramef406_05', 3)
    gotoLabel(1)
    label(0)
    sprite('vramef406_10', 5)
    DespawnEAEffect('amef_408_tornado_add')
    ConstantAlphaModifier(-20)
    sprite('vramef406_11', 5)


@State
def amef_408_tornado_add():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ParticleColorFromPalette(224, 224, 224)
        CallPrivateEffect('amef_406bloom')
        AddY(-16000)
    label(1)
    sprite('null', 8)
    CreateObject('amef_408_3D', -1)
    CreateObject('amef_408_pt', -1)
    gotoLabel(1)


@State
def amef_408_3D():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('am_406wind', '')
        FaceSpawnLocation()
        PaletteIndex(0)
        ColorFromPaletteIndex(225)
        SetScaleY(750)
        DeviationX(-15000, 15000)
        RandAddRotation(-5000, 15000)
    sprite('null', 8)
    physicsYImpulse(6500)
    AlphaValue(0)
    ConstantAlphaModifier(32)
    sprite('null', 8)
    ConstantAlphaModifier(-32)


@State
def amef_408_pt():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 4)
    ParticleColorFromPalette(225, 225, 225)
    CallPrivateEffect('amef_406jimen')
    CreateParticle('amef_406sakura', -1)
    sprite('null', 16)
    CreateParticle('amef_406sakura', -1)


@State
def __430_bomsakraOD():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(63)
        Eff3DEffect('amef_430_bom00.DIG', '')
        FaceSpawnLocation()
        Size(500)
    sprite('null', 10)


@State
def __430_bomOD():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        EffectPosition(22, 105)
        DeviationX(-150000, 150000)
        Size(400)
    sprite('null', 5)
    PaletteIndex(1)
    ParticleColorFromPalette(48, 48, 48)
    CallPrivateEffect('amef_430bom_skr')
    CreateObject('430_bomsakraOD', -1)
    sprite('null', 30)
    AddRotationPerFrame(6000)
    SetScaleSpeed(30)
    ConstantAlphaModifier(-5)


@State
def amef_440finish_a():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('amef_440finish_a', -1)


@State
def amef_440finish_b():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('amef_440finish_b', -1)


@State
def __450_Hokaku():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        AddX(400000)
    sprite('null', 20)
    LinkParticle('amef_450start_moya')
    sprite('null', 20)
    CreateObject('AstralHeat_FirstAttack', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __450_HokakuCircle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        AddX(400000)
    sprite('null', 20)
    LinkParticle('amef_450start_embr')
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __450_renge():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(400000)
        RemoveOnCallStateEnd(2)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
    sprite('vramef450_00', 6)
    sprite('vramef450_01', 6)
    sprite('vramef450_01', 6)
    sprite('vramef450_02', 6)
    sprite('vramef450_03', 6)

    def RunOnObject_22():
        Visibility(1)
    sprite('vramef450_04', 6)
    sprite('vramef450_05', 6)
    sprite('vramef450_06', 6)
    sprite('null', 40)
    CreateObject('450_rengeMogomogo', -1)
    sprite('null', 76)
    TriggerUponForState('450_rengeMogomogo', 33)
    sprite('null', 20)
    TriggerUponForState('450_rengeMogomogo', 34)
    sprite('vramef450_08', 4)
    ScreenShake(0, 25000)
    TriggerUponForState('450_rengeMogomogo', 32)
    CameraControlEnable(1)
    CreateObject('450_rengeBack', -1)
    LinkParticle('amef_450rengeopen_sub')
    Eff3DEffect('amef_450kirakira_00', '')
    FaceSpawnLocation()
    sprite('vramef450_09', 4)
    CreateObject('AstralHeatAttack', -1)
    sprite('vramef450_10', 4)
    label(0)
    sprite('vramef450_09', 4)
    sprite('vramef450_10', 4)
    gotoLabel(0)


@State
def __450_bg():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
    sprite('null', 32767)
    LinkParticle('amef_ahbg_add')


@State
def __450_rengeMogomogo():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(32, 3)
    sprite('vramef450_07', 4)
    label(0)
    sprite('vramef450_07', 3)
    CreateParticle('amef_450tame_skr', 0)
    SetScaleY(900)
    SetScaleX(1100)
    sprite('vramef450_07', 3)
    SetScaleY(1000)
    SetScaleX(1000)
    sprite('vramef450_07', 3)
    SetScaleY(1100)
    SetScaleX(900)
    sprite('vramef450_07', 3)
    SetScaleY(1000)
    SetScaleX(1000)
    gotoLabel(0)
    label(1)
    sprite('vramef450_07', 2)
    CreateParticle('amef_450tame_skr', 0)
    SetScaleY(900)
    SetScaleX(1100)
    sprite('vramef450_07', 2)
    SetScaleY(1000)
    SetScaleX(1000)
    sprite('vramef450_07', 2)
    SetScaleY(1100)
    SetScaleX(900)
    sprite('vramef450_07', 2)
    SetScaleY(1000)
    SetScaleX(1000)
    gotoLabel(1)
    label(2)
    sprite('vramef450_07', 2)
    CreateParticle('amef_450tame_skr', 0)
    SetScaleY(800)
    SetScaleX(1200)
    sprite('vramef450_07', 2)
    SetScaleY(750)
    SetScaleX(1250)
    gotoLabel(2)
    label(3)
    sprite('null', 1)


@State
def __450_rengeBack():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        RemoveOnCallStateEnd(2)
    sprite('vramef450_08b', 4)
    label(0)
    sprite('vramef450_09b', 4)
    sprite('vramef450_10b', 4)
    gotoLabel(0)


@State
def __450_maku():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        Eff3DEffect('ah_am_maku', '')
        SetScaleX(1300)
    sprite('null', 10)
    sprite('null', 10)
    PrivateSE('amse_08')
    physicsXImpulse(0)
    sprite('null', 120)
    PrivateSE('amse_08')
    sprite('null', 32767)
    Eff3DEffect('amef_450maku', '')


@State
def __600_kamuro():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('vramef600_00', 32767)
    label(0)
    sprite('vramef600_01', 6)
    sprite('vramef600_02', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    sprite('vramef600_03', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    sprite('vramef600_04', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    sprite('vramef600_05', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    sprite('vramef600_06', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    sprite('vramef600_07', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    sprite('null', 6)
    CreateObject('600_kasamawaru', -1)


@State
def __600_ichiza():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('vramef600_09', 32767)
    label(0)
    sprite('vramef600_09', 30)


@State
def __600_kasamawaru():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Normal()
        AddX(-240000)
        AddY(195000)
    sprite('vramef600_08ex01', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    CreateParticle('amef_600anbleskr_skr', 6)
    CreateParticle('amef_600anbleskr_skr', 7)
    CreateParticle('amef_600anbleskr_skr', 8)
    physicsXImpulse(-15000)
    physicsYImpulse(7000)
    sprite('vramef600_08ex01', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    CreateParticle('amef_600anbleskr_skr', 6)
    CreateParticle('amef_600anbleskr_skr', 7)
    CreateParticle('amef_600anbleskr_skr', 8)
    sprite('vramef600_08ex01', 5)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    CreateParticle('amef_600anbleskr_skr', 6)
    CreateParticle('amef_600anbleskr_skr', 7)
    CreateParticle('amef_600anbleskr_skr', 8)
    physicsYImpulse(14000)
    sprite('vramef600_08ex01', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    CreateParticle('amef_600anbleskr_skr', 6)
    CreateParticle('amef_600anbleskr_skr', 7)
    CreateParticle('amef_600anbleskr_skr', 8)
    sprite('vramef600_08ex01', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    CreateParticle('amef_600anbleskr_skr', 6)
    CreateParticle('amef_600anbleskr_skr', 7)
    CreateParticle('amef_600anbleskr_skr', 8)
    sprite('vramef600_08ex01', 6)
    CreateParticle('amef_600anbleskr_skr', 0)
    CreateParticle('amef_600anbleskr_skr', 1)
    CreateParticle('amef_600anbleskr_skr', 2)
    CreateParticle('amef_600anbleskr_skr', 3)
    CreateParticle('amef_600anbleskr_skr', 4)
    CreateParticle('amef_600anbleskr_skr', 5)
    CreateParticle('amef_600anbleskr_skr', 6)
    CreateParticle('amef_600anbleskr_skr', 7)
    CreateParticle('amef_600anbleskr_skr', 8)


@State
def __610_ichiza():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Normal()
    label(0)
    sprite('vramef610_00', 6)
    sprite('vramef610_01', 6)
    gotoLabel(0)


@State
def __610_spot():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('am_610spot_00', '')
        FaceSpawnLocation()
        LinkParticle('amef_610spot_shadow')
        RemoveOnCallStateEnd(2)
        AlphaValue(0)
    sprite('null', 20)
    ConstantAlphaModifier(17)
    sprite('null', 32767)


@State
def UltimateAssaultExplosion():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Hitstop(30)
        AirUntechableTime(100)
        YImpulseBeforeWallbounce(1500)
        PushbackX(0)
        AirPushbackX(0)
        HitsparkSize(0)
        CHStateIfCHStart(3)
        PaletteIndex(0)
        CancelIfPlayerHit(3)
        TeleportToObject(22)

        def upon_32():
            AttackLevel_(3)
            Damage(3500)
            GroundedHitstunAnimation(10)
            AirHitstunAnimation(10)
            sendToLabel(100)
            if SLOT_137:
                DamageMultiplier(80)

        def upon_33():
            AttackLevel_(4)
            Damage(4000)
            GroundedHitstunAnimation(10)
            AirHitstunAnimation(10)
            AirPushbackY(42000)
            sendToLabel(200)
            if SLOT_137:
                DamageMultiplier(80)

        def upon_34():
            AttackLevel_(5)
            Damage(4500)
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            AirPushbackY(54000)
            sendToLabel(300)
            if SLOT_137:
                DamageMultiplier(80)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('UltimateAssault', 32)
    sprite('null', 3)
    label(100)
    sprite('vrdmy', 3)
    CreateObject('430_bom', -1)
    ScreenShake(40000, 40000)
    gotoLabel(1)
    label(200)
    sprite('vrdmy', 3)
    CreateObject('430_bom', -1)
    ScreenShake(60000, 60000)
    gotoLabel(1)
    label(300)
    sprite('vrdmy', 3)
    CreateObject('430_bom', -1)
    ScreenShake(80000, 80000)
    gotoLabel(1)
    label(1)
    sprite('null', 2)


@State
def UltimateAssaultExplosionOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackType(4)
        SingleProration(1)
        AirUntechableTime(100)
        AirPushbackX(0)
        PushbackX(0)
        Hitstop(1)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        HitsparkSize(0)
        AttackType(4)
        CHStateIfCHStart(3)
        PaletteIndex(0)
        CancelIfPlayerHit(3)
        TeleportToObject(22)

        def upon_32():
            AttackLevel_(3)
            Damage(400)
            SLOT_51 = 2
            SLOT_52 = 1
            if SLOT_137:
                DamageMultiplier(80)

        def upon_33():
            AttackLevel_(4)
            Damage(300)
            SLOT_51 = 3
            SLOT_53 = 1
            if SLOT_137:
                DamageMultiplier(80)

        def upon_34():
            AttackLevel_(5)
            Damage(200)
            SLOT_51 = 6
            SLOT_54 = 1
            if SLOT_137:
                DamageMultiplier(80)
    sprite('null', 3)
    label(99)
    sprite('vrdmy', 5)
    TeleportToObject(22)
    RefreshMultihit()
    CreateObject('430_bomOD', -1)
    ScreenShake(5000, 5000)
    sprite('vrdmy', 1)
    SLOT_51 = SLOT_51 + -1
    if not SLOT_51:
        AttackP2(60)
        Hitstop(30)
        YImpulseBeforeWallbounce(1500)
        if SLOT_52:
            sendToLabel(100)
        if SLOT_53:
            sendToLabel(200)
        if SLOT_54:
            sendToLabel(300)
    loopRest()
    gotoLabel(99)
    label(100)
    sprite('vrdmy', 3)
    TeleportToObject(22)
    RefreshMultihit()
    Damage(3500)
    CreateObject('430_bom', -1)
    ScreenShake(40000, 40000)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        TriggerUponForState('UltimateAssault', 32)
    if SLOT_137:
        DamageMultiplier(80)
    gotoLabel(1)
    label(200)
    sprite('vrdmy', 3)
    TeleportToObject(22)
    RefreshMultihit()
    Damage(4000)
    CreateObject('430_bom', -1)
    ScreenShake(60000, 60000)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        TriggerUponForState('UltimateAssault', 32)
    if SLOT_137:
        DamageMultiplier(80)
    gotoLabel(1)
    label(300)
    sprite('vrdmy', 3)
    TeleportToObject(22)
    RefreshMultihit()
    Damage(4500)
    CreateObject('430_bom', -1)
    ScreenShake(80000, 80000)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        TriggerUponForState('UltimateAssault', 32)
    if SLOT_137:
        DamageMultiplier(80)
    gotoLabel(1)
    label(1)
    sprite('null', 2)


@State
def ContinuationDrillCreater():

    def upon_IMMEDIATE():
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
    sprite('null', 1)
    AddX(100000)
    physicsXImpulse(26000)
    CollideWithWall(1)
    label(0)
    sprite('null', 8)
    CreateObject('ContinuationDrillMain', -1)
    loopRest()
    gotoLabel(0)


@State
def ContinuationDrillMain():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(2)
        AttackP1(100)
        AttackP2(94)
        MinimumDamage(7)
        ChipPercentage(20)
        Hitstop(0)
        AirUntechableTime(60)
        HardKnockdown(1)
        BouncePercentage(20)
        GroundedHitstunAnimation(9)
        AirPushbackX(36000)
        AirPushbackY(2000)
        PushbackX(50000)
        UseSlashHitspark(1)
        HitsparkSize(500)
        StarterRating(2)
        CHStateIfCHStart(2)
        VoodooDamageMultiplier(2)
        if SLOT_4 == 1:
            SetScaleX(780)
            SetScaleY(555)
            PrivateSE('amse_01_loop')
            PrivateSE('amse_02_loop')
            SLOT_51 = 1
            Damage(220)
        if SLOT_4 == 2:
            SetScaleX(890)
            SetScaleY(780)
            PrivateSE('amse_01_loop')
            PrivateSE('amse_02_loop')
            PrivateSE('amse_03_loop')
            SLOT_52 = 1
            Damage(260)
        if SLOT_4 == 3:
            SetScaleX(1000)
            SetScaleY(1000)
            PrivateSE('amse_01_loop')
            PrivateSE('amse_02_loop')
            PrivateSE('amse_03_loop')
            PrivateSE('amse_04_loop')
            SLOT_53 = 1
            Damage(300)
            ChipPercentage(40)

        def upon_EVERY_FRAME():
            if SLOT_4 == 3:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(LANDING, 41)
    sprite('vramef431_10', 3)
    CreateObject('431_wind', -1)
    CreateParticle('amef_431impact_crl', -1)
    RefreshMultihit()
    sprite('vramef431_11', 3)
    RefreshMultihit()
    sprite('vramef431_12', 3)
    RefreshMultihit()
    sprite('vramef431_13', 3)
    RefreshMultihit()
    sprite('vramef431_14', 3)
    RefreshMultihit()
    sprite('vramef431_15', 3)
    RefreshMultihit()
    sprite('vramef431_16', 3)
    RefreshMultihit()
    sprite('vramef431_17', 3)
    RefreshMultihit()
    sprite('vramef431_18', 3)
    RefreshMultihit()
    sprite('vramef431_19', 3)
    AttackOff()
    sprite('vramef431_20', 3)
    AttackOff()
    sprite('vramef431_21', 3)
    AttackOff()


@State
def ContinuationDrillCreaterOD():
    sprite('null', 1)
    AddX(100000)
    physicsXImpulse(26000)
    CollideWithWall(1)
    label(0)
    sprite('null', 6)
    CreateObject('ContinuationDrillMainOD', -1)
    loopRest()
    gotoLabel(0)


@State
def ContinuationDrillMainOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackType(4)
        AttackLevel_(2)
        AttackP1(100)
        AttackP2(94)
        MinimumDamage(7)
        ChipPercentage(20)
        Hitstop(0)
        AirUntechableTime(60)
        HardKnockdown(1)
        BouncePercentage(20)
        GroundedHitstunAnimation(9)
        AirPushbackX(36000)
        AirPushbackY(2000)
        PushbackX(50000)
        UseSlashHitspark(1)
        HitsparkSize(500)
        AttackType(4)
        StarterRating(2)
        CHStateIfCHStart(2)
        VoodooDamageMultiplier(2)
        if SLOT_4 == 1:
            SetScaleX(780)
            SetScaleY(555)
            PrivateSE('amse_01_loop')
            PrivateSE('amse_02_loop')
            SLOT_51 = 1
            Damage(220)
        if SLOT_4 == 2:
            SetScaleX(890)
            SetScaleY(780)
            PrivateSE('amse_01_loop')
            PrivateSE('amse_02_loop')
            PrivateSE('amse_03_loop')
            SLOT_52 = 1
            Damage(260)
        if SLOT_4 == 3:
            SetScaleX(1000)
            SetScaleY(1000)
            PrivateSE('amse_01_loop')
            PrivateSE('amse_02_loop')
            PrivateSE('amse_03_loop')
            PrivateSE('amse_04_loop')
            SLOT_53 = 1
            Damage(300)
            ChipPercentage(40)
    sprite('vramef431_10', 3)
    CreateObject('431_wind', -1)
    CreateParticle('amef_431impact_crl', -1)
    RefreshMultihit()
    sprite('vramef431_11', 3)
    RefreshMultihit()
    sprite('vramef431_12', 3)
    RefreshMultihit()
    sprite('vramef431_13', 3)
    RefreshMultihit()
    sprite('vramef431_14', 3)
    RefreshMultihit()
    sprite('vramef431_15', 3)
    RefreshMultihit()
    sprite('vramef431_16', 3)
    RefreshMultihit()
    sprite('vramef431_17', 3)
    RefreshMultihit()
    sprite('vramef431_18', 3)
    RefreshMultihit()
    sprite('vramef431_19', 3)
    AttackOff()
    sprite('vramef431_20', 3)
    AttackOff()
    sprite('vramef431_21', 3)
    AttackOff()


@State
def AstralHeat_FirstAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(4)
        Damage(0)
        MinimumDamage(100)
        PushbackX(0)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Stagger(180)
        Crumple(180)
        OppPositionOnHit(1, 0, 0)
        DamageFromStateOnly('AstralHeatAttack')
        DefeatOpponentBehavior(1)
        AbsoluteY(0)
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT():
            TriggerUponForState('AstralHeat', 32)
    sprite('vrhokakuatk', 9)


@State
def AstralHeatAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(4)
        Damage(10)
        MinimumDamage(100)
        Hitstop(0)
        AirHitstunAnimation(20)
        GroundedHitstunAnimation(20)
        OppState('AmAstralDamage')
        DamageEffect(5, '')
        DefeatOpponentBehavior(1)
        HitAnywhere(1)
        OppPositionOnHit(1, 0, 0)
        AbsoluteY(0)
        RemoveOnCallStateEnd(3)
    sprite('vrdmy', 330)
    sprite('vrdmy', 30)
    RefreshMultihit()
    Damage(20990)
    DefeatOpponentBehavior(3)
    ResetGroundedHitstunAnimation()
    AirHitstunAnimationReset()
    AirPushbackX(0)
    AirPushbackY(0)
    YImpulseBeforeWallbounce(0)


@State
def Throw_windmill():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1100)
        CancelIfPlayerHit(3)
    sprite('vramef311_00', 3)
    physicsXImpulse(5000)
    SetScaleSpeed(12)
    sprite('vramef311_01', 3)
    sprite('vramef311_02', 3)
    ConstantAlphaModifier(-12)
    sprite('vramef311_00', 3)
    sprite('vramef311_01', 3)
    sprite('vramef311_02', 3)
    sprite('vramef311_00', 3)
    sprite('vramef311_01', 3)


@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        AddX(190000)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    CameraNoScreenCollision(0)
    TeleportToObject(3)
    AddX(-150000)


@State
def Ameff_BurstDDHit():

    def upon_IMMEDIATE():
        BlendMode_Add()
        LinkParticle('amef_440hiteff_sub')
        PaletteIndex(3)
        Size(2200)
        AddY(100000)
        IgnoreFinishStop(1)
    sprite('vram440_hiteff00', 6)
    SetScaleSpeed(15)
    sprite('vram440_hiteff01', 6)
    sprite('vram440_hiteff02', 4)
    sprite('vram440_hiteff03', 4)
    CreateParticle('amef_440hiteff', -1)
    ConstantAlphaModifier(-31)
    sprite('vram440_hiteff04', 4)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act3Event_vsphCamera():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        AddX(-200000)
    sprite('null', 32767)
    CameraControlEnable(1)


@State
def Act3Event_CreateKK():

    def upon_IMMEDIATE():
        AddX(500000)
        LoadSpritePalette(0)
    sprite('kk000_00', 7)
    Flip()
    label(0)
    sprite('kk000_01', 7)
    sprite('kk000_02', 7)
    sprite('kk000_03', 7)
    sprite('kk000_04', 7)
    sprite('kk000_05', 7)
    sprite('kk000_06', 7)
    sprite('kk000_07', 7)
    sprite('kk000_08', 7)
    sprite('kk000_09', 7)
    sprite('kk000_10', 7)
    sprite('kk000_11', 7)
    sprite('kk000_12', 7)
    sprite('kk000_13', 7)
    sprite('kk000_14', 7)
    sprite('kk000_15', 7)
    sprite('kk000_00', 7)
    loopRest()
    gotoLabel(0)


@State
def Act3Event_vsizCamera():

    def upon_IMMEDIATE():
        AddX(200000)
    sprite('null', 32767)
    CameraControlEnable(1)


@State
def Act3Event_NagenukeEff():

    def upon_IMMEDIATE():
        AddX(210000)
        AddY(222000)
    sprite('null', 3)
    CreateParticle('ef_nagenuke', 0)


@State
def Eventoffset_Sosai():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(200000)
        DeviationX(-150000, 20000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)


@State
def Eventoffset_Sosai2():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(100000)
        DeviationX(-150000, 20000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)
