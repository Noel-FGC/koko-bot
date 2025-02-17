@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_HZ.DIG', 'ef_emb_HZ_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
        Visibility(1)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    Size(2950)
    SetScaleSpeed(-100)
    RotationAngle(120000)
    AddRotationPerFrame(-6000)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    SetScaleSpeed(0)
    AddRotationPerFrame(0)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 20)


@State
def EMB_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_HZ.DIG', 'ef_emb_HZ_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
        Visibility(1)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    Size(2950)
    SetScaleSpeed(-100)
    RotationAngle(120000)
    AddRotationPerFrame(-6000)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    SetScaleSpeed(0)
    AddRotationPerFrame(0)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 20)


@State
def EMB_AST():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_HZ.DIG', 'ef_emb_HZ_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
        Visibility(1)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    Size(2950)
    SetScaleSpeed(-100)
    RotationAngle(120000)
    AddRotationPerFrame(-6000)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4290032820, 10)
    SetScaleSpeed(0)
    AddRotationPerFrame(0)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 20)


@State
def HZEF_GuardLoop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(-16000)
        uponSendToLabel(32, 99)
    sprite('null', 20)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(32000)
        AddY(-97500)
        physicsYImpulse(20000)
        Unknown1082(4)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(16000)
        AddY(110000)
        physicsYImpulse(-40000)
        SetScaleX(-1000)
        Unknown1082(4)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(-16000)
        AddY(-100000)
        physicsYImpulse(40000)
        SetScaleX(-1000)
        Unknown1082(4)
    CreateObject('HZEF_GuardLoopParts', -1)

    def RunOnObject_1():
        AddX(-40000)
        AddY(95000)
        physicsYImpulse(-15000)
        Unknown1082(4)
    loopRest()
    ExitState()
    label(99)
    TriggerUponForState('HZEF_GuardLoopParts', 32)


@State
def HZEF_GuardLoopParts():

    def upon_IMMEDIATE():
        SetZVal(-100)
        BlendMode_Normal()
        uponSendToLabel(32, 99)
    sprite('vrhzef_guard00', 4)
    AlphaValue(100)
    sprite('vrhzef_guard00', 2)
    IgnorePauses(3)
    AlphaValue(200)
    sprite('vrhzef_guard00', 12)
    IgnorePauses(0)
    AlphaValue(120)
    ConstantAlphaModifier(-15)
    loopRest()
    ExitState()
    label(99)
    EndObject()


@State
def HZEF_HeavyGuardLoop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        TriggerUponForState('HZEF_GuardLoop', 32)
    sprite('null', 20)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(48000)
        AddY(32000)
        physicsYImpulse(10000)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(16000)
        AddY(-16000)
        physicsYImpulse(-15000)
        SetScaleX(-1000)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(-16000)
        AddY(16000)
        physicsYImpulse(15000)
        SetScaleX(-1000)
    CreateObject('HZEF_HeavyGuardLoopObj', -1)

    def RunOnObject_1():
        AddX(-48000)
        AddY(-32000)
        physicsYImpulse(-10000)


@State
def HZEF_HeavyGuardLoopObj():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        SetZVal(-100)
        BlendMode_Normal()
        AddX(-64000)
    sprite('vrhzef_guard00', 2)
    AlphaValue(250)
    sprite('vrhzef_guard00', 10)
    AlphaValue(150)
    ConstantAlphaModifier(-15)


@State
def HZEF_BBStart():
    sprite('null', 120)
    AddX(-80000)
    AddY(220000)
    ParticleSize(1400)
    ParticleColor(4278190080, 4278190080, 65280)
    CallCustomizableParticle('rgef_bloodkineR', -1)
    ParticleSize(900)
    ParticleColor(4278190080, 4278190080, 65280)
    CallCustomizableParticle('rgef_bloodkineL', -1)
    ParticleSize(1400)
    ParticleColor(4278255410, 4278255410, 65330)
    CallCustomizableParticle('rgef_bloodkineR2', -1)
    ParticleSize(900)
    ParticleColor(4278255410, 4278255410, 65330)
    CallCustomizableParticle('rgef_bloodkineL2', -1)
    CallCustomizableParticle('rgef_bkburst', -1)
    ParticleLayer(2)
    ParticleColor(4194369280, 2516647680, 65280)
    CallCustomizableParticle('rgef_bloodkineback', -1)


@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        FaceSpawnLocation()
        ColorForTransition(4278255360)
        IgnoreScreenfreeze(1)
    sprite('null', 74)


@State
def UltimateKusari():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(2)
        Damage(800)
        AttackP1(80)
        AttackP2(100)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackY(39000)
        YImpulseBeforeWallbounce(1500)
        AirUntechableTime(120)
        Hitstop(20)
        PassByArmor(1)
        ProjectileLevel(3)
        StrikeProjectileLevel(3)
        UseSlashHitspark(1)
        OnlyHitPlayer(1)
        CHStateIfCHStart(3)
        StarterRating(2)
        DefeatOpponentBehavior(1)
        RemoveOnCallStateEnd(3)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                CallPrivateFunction('KusariAngleByChain', 0, 0, 0, 0, 0, 0,
                    0, 0)
                Unknown4055(0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        EnableAfterimage(0)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        BlendMode_Normal()
        uponSendToLabel(OPPONENT_HIT, 0)
        CallPrivateFunction('UltimateKusariAtkVectorX', 0, 70, 0, 0, 0, 0, 0, 0
            )
    sprite('vr_chain_tip03DD', 1)
    PrivateSE('hzse_02')
    SetZVal(-500)
    Unknown23143(70000, 0, 70)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03DD', 80)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    CreateObject('EffUltimateChainAura', -1)
    loopRest()
    ExitState()
    label(0)
    AddX(120000)
    sprite('vr_chain_tip04', 3)
    TriggerUponForState('EffUltimateChainAura', 32)
    ObjectUpon(EVERY_FRAME, 33)
    EndMomentum(1)
    Unknown23143(0, 0, 0)
    Unknown23144(3, 0, 111, 0, 0, 0, 0, 0, 75, 0, 4)
    sprite('vr_chain_tip04', 27)
    SetActionMark(1)
    SetZVal(500)
    sprite('vr_chain_tip04', 30)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()


@State
def EffUltimateChainAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        ContinueState(20)
        AddY(-48000)

        def upon_32():
            EndObject()
    label(0)
    sprite('null', 1)
    CreateObject('EffUltimateChainAuraObj', -1)
    loopRest()
    gotoLabel(0)


@State
def EffUltimateChainAuraObj():

    def upon_IMMEDIATE():
        LinkParticle('hzef_antiairchain')
        Size(300)
        RandAddScale(0, 400)
        ParticleLayer(2)
        CallCustomizableParticle('hzef_exheadmoveopt', -1)
    sprite('null', 30)


@State
def KusariAntiAir():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        EnableAfterimage(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        BlendMode_Normal()

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_51:
                RotationSomething(-180000)
            if SLOT_2:
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('hzef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('hzef_exheadmoveopt', -1)
        uponSendToLabel(32, 0)
    sprite('vr_chain_tip03aa', 1)
    RenderLayer(1)
    Unknown23143(60000, 60000, 70)
    EnableAfterimage(1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    CreateObject('ExPortalSp', -1)

    def RunOnObject_1():
        RotationAngle(-40000)
    RotationAngle(-30000)
    sprite('vr_chain_tip03aa', 12)
    SetActionMark(1)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 5)
    SetActionMark(0)
    SLOT_51 = 1
    EnableAfterimage(0)
    TriggerUponForState('ExPortalSp', 32)
    Unknown23143(-60000, -45000, 40)
    AddRotationPerFrame(-2000)
    BlendMode_Normal()
    ConstantAlphaModifier(-5)
    sprite('vr_chain_tip04', 10)
    RenderLayer(5)
    sprite('vr_chain_tip04', 6)
    Unknown23143(100000, -50000, 25)
    sprite('vr_chain_tip04', 8)
    RenderLayer(0)
    Unknown23143(-100000, 60000, 25)
    SetZVal(-500)
    AddRotationPerFrame(0)
    RotationAngle(30000)
    ConstantAlphaModifier(-10)
    sprite('vr_chain_tip04', 1)
    EndObject()
    loopRest()
    label(0)
    sprite('vr_chain_tip04ex01', 6)
    SetActionMark(0)
    TriggerUponForState('ExPortalSp', 32)
    Unknown23143(-10000, -5000, 20)
    sprite('vr_chain_tip04ex01', 6)
    SLOT_51 = 1
    Unknown23143(-20000, 10000, 20)
    sprite('vr_chain_tip04ex01', 10)
    Unknown23143(-120000, -60000, 20)
    sprite('vr_chain_tip04ex01', 5)
    Unknown23143(0, 0, 20)
    sprite('vr_chain_tip04ex01', 30)
    Unknown23143(0, 0, 0)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 80, 0, 3)


@State
def ExBodyAuraAntiAir():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(0)
        ColorForTransition(3355473940)
        AddX(20000)
        AddY(200000)
    sprite('vref_env', 10)
    SetScaleSpeed(1200)
    sprite('vref_env', 30)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-20)


@State
def AntiAirWindSmoke():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
        AddY(120000)
        AlphaValue(160)
    sprite('null', 32767)
    CreateObject('AntiAirWindSmokeOpt', -1)
    loopRest()
    label(0)
    sprite('null', 32767)
    SetScaleSpeed(10)
    TriggerUponForState('AntiAirWindSmokeOpt', 32)
    loopRest()
    loopRest()
    label(99)
    TriggerUponForState('AntiAirWindSmokeOpt', 33)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def AntiAirWindSmokeOpt():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
        RotationAngle(-180000)
        Size(1250)
        AddScaleY(-500)
        AlphaValue(120)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 32767)
    SetScaleSpeed(10)
    loopRest()
    label(99)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def BasicDriveWindSmoke():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectRotation(2)
        IgnorePauses(2)
        uponSendToLabel(32, 99)
    sprite('null', 1)
    Unknown4055(0)
    ParticleLayer(5)
    CallCustomizableParticle('hzef_exheadmove', -1)


@State
def Kusari():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        SetXCollisionFromOrigin(10)
        ContinueState(240)
        IgnorePauses(3)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        RenderLayer(8)
        CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_51:
                CallPrivateFunction('KusariAngleByChain', 0, 0, 0, 0, 0, 0,
                    0, 0)
            if SLOT_54:
                RotationSomething(0)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 54)
            if not SLOT_52:
                if not SLOT_53:
                    DeleteObject(23)
            if SLOT_56:
                CreateObject('BasicDriveWindSmoke', -1)
                ParticleLayer(2)
                CallCustomizableParticle('hzef_exheadmoveopt', -1)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)

        def upon_LANDING():
            clearUponHandler(LANDING)
            ObjectUpon(EVERY_FRAME, 39)

        def upon_55():
            if SLOT_StateDuration > 3:
                clearUponHandler(55)
                ObjectUpon(EVERY_FRAME, 39)

        def upon_38():
            clearUponHandler(38)
            EnableAfterimage(0)

        def upon_39():
            RenderLayer(11)
            CallPrivateFunction('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)

        def upon_40():
            clearUponHandler(40)
            EndMomentum(1)
            Unknown23143(0, 0, 0)
            sendToLabel(1)

        def upon_VALUE_RECEIVED():
            if SLOT_ReceivedValue == 0:
                SetActionMark(0)
                Unknown23143(10000, 0, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 109
            if SLOT_ReceivedValue == 1:
                SetActionMark(1)
                Unknown23143(9000, 5000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 109
            if SLOT_ReceivedValue == 2:
                SetActionMark(2)
                Unknown23143(5000, 9000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 109
            if SLOT_ReceivedValue == 3:
                SetActionMark(3)
                Unknown23143(0, 10000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 109
            if SLOT_ReceivedValue == 4:
                SetActionMark(4)
                Unknown23143(10000, 0, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 0
                CallPrivateFunction('KusariMochite', 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_ReceivedValue == 5:
                SetActionMark(5)
                Unknown23143(9000, 5000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 1
                CallPrivateFunction('KusariMochite', 0, 1, 0, 0, 0, 0, 0, 0)
            if SLOT_ReceivedValue == 6:
                SetActionMark(6)
                Unknown23143(9000, -5000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 2
                CallPrivateFunction('KusariMochite', 0, 2, 0, 0, 0, 0, 0, 0)
            if SLOT_ReceivedValue == 7:
                SetActionMark(7)
                Unknown23143(5000, -9000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 3
                CallPrivateFunction('KusariMochite', 0, 3, 0, 0, 0, 0, 0, 0)
            if SLOT_ReceivedValue == 8:
                SetActionMark(8)
                Unknown23143(0, -10000, 70)
                RotationSomething(0)
                CreateObject('ExPortal', -1)
                CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
                SLOT_57 = 4
                CallPrivateFunction('KusariMochite', 0, 4, 0, 0, 0, 0, 0, 0)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        SetZVal(500)
        BlendMode_Normal()
    sprite('vr_chain_tip04', 1)
    PrivateSE('hzse_04')
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 3)
    PrivateSE('hzse_02')
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 32767)
    EnableAfterimage(1)
    AfterimageColor_1(200, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    if SLOT_2 == 0:
        Unknown23143(60000, 0, 70)
    if SLOT_2 == 1:
        Unknown23143(54000, 30000, 70)
    if SLOT_2 == 2:
        Unknown23143(30000, 54000, 70)
    if SLOT_2 == 3:
        Unknown23143(0, 60000, 70)
    if SLOT_2 == 4:
        Unknown23143(60000, 0, 70)
    if SLOT_2 == 5:
        Unknown23143(54000, 30000, 70)
    if SLOT_2 == 6:
        Unknown23143(54000, -30000, 70)
    if SLOT_2 == 7:
        Unknown23143(30000, -54000, 70)
    if SLOT_2 == 8:
        Unknown23143(0, -60000, 70)
    SLOT_56 = 1
    loopRest()
    label(0)
    sprite('vr_chain_tip04', 8)
    clearUponHandler(32)
    clearUponHandler(40)
    clearUponHandler(33)
    SLOT_56 = 0
    SLOT_51 = 1
    SLOT_54 = 0
    ConstantAlphaModifier(-5)
    Unknown23143(0, 0, 0)
    Unknown23144(3, 2, 57, 0, 0, 0, 0, 0, 80, 0, 3)
    EnableAfterimage(0)
    TriggerUponForState('ExPortal', 32)
    CreateObject('ExHeadStop', -1)
    sprite('vr_chain_tip04', 14)
    ConstantAlphaModifier(-25)
    loopRest()
    ExitState()
    label(1)
    sprite('vr_chain_tip04', 32767)
    PrivateSE('hzse_13')
    clearUponHandler(40)
    clearUponHandler(33)
    SLOT_56 = 0
    Unknown23143(0, 0, 0)
    EndMomentum(1)
    EnableAfterimage(0)
    CreateObject('ExHeadLock', -1)
    CreateObject('yugami_ring', -1)
    SLOT_51 = 0
    SLOT_54 = 0
    loopRest()
    ExitState()


@State
def ExPortal():

    def upon_IMMEDIATE():
        ParticleLayer(0)
        CallPrivateEffect('hzef_exportal')
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        uponSendToLabel(32, 99)
        ContinueState(180)
    sprite('vrexdmy', 1)
    sprite('vrexdmy', 32767)
    CreateObject('ExPortalParts', -1)
    CreateObject('ExPortalPartsOpt', 0)
    CreateObject('ExPortalPartsOpt', 1)
    CreateObject('ExPortalPartsOpt', 2)
    label(99)
    sprite('null', 20)
    clearUponHandler(32)
    TriggerUponForState('ExPortalParts', 32)
    TriggerUponForState('ExPortalPartsOpt', 32)
    BlendMode_Normal()
    AlphaValue(200)
    SetScaleSpeed(-50)


@State
def ExPortalParts():

    def upon_IMMEDIATE():
        ParticleLayer(1)
        CallPrivateEffect('hzef_exportalparts')
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        AddX(8000)
        BlendMode_Add()
        AlphaValue(255)
        uponSendToLabel(32, 99)
        ContinueState(180)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    Size(0)
    SetScaleSpeed(80)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    SetScaleSpeed(5)
    label(99)
    sprite('null', 10)
    E0EAEffectPosition(0)
    AlphaValue(50)
    ConstantAlphaModifier(-5)
    SetScaleSpeed(100)


@State
def ExPortalPartsOpt():

    def upon_IMMEDIATE():
        ParticleColor(4294967040, 4294967040, 4294967040)
        ParticleLayer(1)
        CallPrivateEffect('hzef_exportalopt')
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        AddX(8000)
        BlendMode_Add()
        AlphaValue(255)
        uponSendToLabel(32, 99)
        ContinueState(180)
    sprite('null', 10)
    Size(0)
    SetScaleSpeed(60)
    sprite('null', 32767)
    SetScaleSpeed(-3)
    label(99)
    sprite('null', 15)
    E0EAEffectPosition(0)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def ExPortalSp():

    def upon_IMMEDIATE():
        ParticleLayer(0)
        CallPrivateEffect('hzef_exportal')
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        Size(2000)
        uponSendToLabel(32, 99)
    sprite('vrexdmy', 1)
    sprite('vrexdmy', 32767)
    CreateObject('ExPortalPartsSp', -1)
    CreateObject('ExPortalPartsOptSp', 0)
    CreateObject('ExPortalPartsOptSp', 1)
    CreateObject('ExPortalPartsOptSp', 2)
    BlendMode_Normal()
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    label(99)
    sprite('null', 20)
    clearUponHandler(32)
    TriggerUponForState('ExPortalPartsSp', 32)
    TriggerUponForState('ExPortalPartsOptSp', 32)
    SetScaleSpeed(-200)


@State
def ExPortalPartsSp():

    def upon_IMMEDIATE():
        ParticleLayer(1)
        ParticleColor(4294967040, 4294967040, 4294967040)
        CallPrivateEffect('hzef_exportalparts')
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        AddX(8000)
        BlendMode_Add()
        AlphaValue(255)
        uponSendToLabel(32, 99)
    sprite('null', 10)
    ConstantAlphaModifier(-10)
    Size(0)
    SetScaleSpeed(160)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    SetScaleSpeed(5)
    label(99)
    sprite('null', 10)
    E0EAEffectPosition(0)
    AlphaValue(50)
    ConstantAlphaModifier(-5)
    SetScaleSpeed(100)


@State
def ExPortalPartsOptSp():

    def upon_IMMEDIATE():
        ParticleColor(4294967040, 4294967040, 4294967040)
        ParticleLayer(1)
        CallPrivateEffect('hzef_exportalopt')
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        AddX(8000)
        BlendMode_Add()
        AlphaValue(255)
        uponSendToLabel(32, 99)
    sprite('null', 10)
    Size(0)
    SetScaleSpeed(60)
    sprite('null', 32767)
    SetScaleSpeed(-3)
    label(99)
    sprite('null', 15)
    E0EAEffectPosition(0)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def ExHeadMove():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectRotation(2)
        IgnorePauses(2)
        uponSendToLabel(32, 99)
    label(0)
    sprite('null', 1)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    ParticleLayer(2)
    CallCustomizableParticle('hzef_exheadmoveopt', -1)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('null', 1)
    clearUponHandler(32)


@State
def ExHeadStop():

    def upon_IMMEDIATE():
        LinkParticle('hzef_exheadstop')
        Size(500)
    sprite('null', 5)
    SetScaleSpeed(100)
    sprite('null', 10)
    BlendMode_Add()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(0)


@State
def ExHeadLock():

    def upon_IMMEDIATE():
        LinkParticle('hzef_exheadlock')
        Size(500)
    sprite('null', 5)
    SetScaleSpeed(100)
    sprite('null', 10)
    BlendMode_Add()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(0)


@State
def yugami_ring():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(2000)
    sprite('vr_yugami', 5)
    SetScaleSpeed(50)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami', 10)
    SetScaleSpeed(100)
    Unknown3059(-3200)


@State
def MoveTest():
    sprite('vr_chain_tip03', 60)
    RotationAngle(20000)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 60)
    RotationAngle(30000)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 60)
    RotationAngle(60000)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 10)
    Unknown23143(40000, 40000, 70)
    AddY(400000)
    EnableAfterimage(1)
    RotationAngle(180000)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 14)
    Unknown23143(-60000, -45000, 20)
    RotationAngle(270000)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 9)
    Unknown23143(90000, -45000, 15)
    RotationAngle(90000)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    sprite('vr_chain_tip03', 9)
    Unknown23143(-60000, 80000, 15)
    sprite('vr_chain_tip03', 14)
    Unknown23143(60000, -100000, 6)


@State
def KusariTest():

    def upon_IMMEDIATE():
        E0EAEffectDirection(3)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)
            if CheckInput(0x93):
                YSpeed(800)
            if CheckInput(0x45):
                YSpeed(-800)
            if CheckInput(0x5f):
                XSpeed(-800)
            if CheckInput(0x79):
                XSpeed(800)
            if CheckInput(INPUT_HOLD_B):
                physicsXImpulse(0)
                physicsYImpulse(0)
            XImpulseAcceleration(99)
            YAccel(99)
            CallPrivateFunction('KusariAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_5():
            YAccel(-100)
        AddX(600000)
        AddY(300000)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 60, 0, 0, 0, 0, 0, 0)
    loopRest()
    label(0)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, -20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 20, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    Unknown4055(0)
    CallCustomizableParticle('hzef_exheadmove', -1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, -10, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, -20, 0, 50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, -10, 0, 55, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 0, 0, 50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 10, 0, 45, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 90, 0, -45, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 100, 0, -50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, 110, 0, -55, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 120, 0, -50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 110, 0, -10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, -10, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, -20, 0, 50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, -10, 0, 55, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 0, 0, 50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 10, 0, 45, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 60)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 90, 0, -45, 0, 0)
    CallPrivateFunction('KusariParam', 0, 2, 0, 100, 0, -50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 3, 0, 110, 0, -55, 0, 0)
    CallPrivateFunction('KusariParam', 0, 4, 0, 120, 0, -50, 0, 0)
    CallPrivateFunction('KusariParam', 0, 5, 0, 110, 0, -10, 0, 0)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 10, 0, 10)
    CallPrivateFunction('KusariSpeed', 0, 60, 0, 0, 0, 0, 0, 0)
    loopRest()
    gotoLabel(0)


@State
def ExBodyAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(0)
        ColorForTransition(3355473940)
        AddX(20000)
        AddY(200000)
        uponSendToLabel(32, 99)
        uponSendToLabel(PLAYER_DAMAGED, 99)
        ContinueState(160)
    sprite('vref_env', 10)
    SetScaleSpeed(600)
    sprite('vref_env', 40)
    SetScaleSpeed(0)
    label(99)
    sprite('vref_env', 14)
    clearUponHandler(32)
    clearUponHandler(PLAYER_DAMAGED)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def EffKnifeSignal():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    Visibility(1)
    LinkParticle('hzef_knifesignal')
    CreateParticle('hzef_knifesignalopt', -1)
    Size(900)
    RandAddRotation(-90000, 90000)


@State
def Eff5CZanzo():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(48000)
        AddY(260000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 14)
    sprite('vrhzef202_00', 1)
    sprite('vrhzef202_00', 1)
    CreateObject('Eff5CZanzo2nd', -1)
    sprite('vrhzef202_01', 12)
    AddAlpha(-100)


@State
def Eff5CZanzo2nd():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddY(-20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 14)
    sprite('vrhzef202_02', 2)
    sprite('vrhzef202_03', 12)
    AddAlpha(-100)


@State
def ShotKnife():
    sprite('null', 2)
    AddX(-30000)
    sprite('null', 2)
    CreateObject('ShotKnifeObj', -1)
    DeviationX(-16000, -32000)
    sprite('null', 1)
    CreateObject('ShotKnifeObj', -1)
    DeviationX(-16000, -32000)


@State
def ShotKnifeObj():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        BlendMode_Normal()
        EnableAfterimage(1)
        physicsXImpulse(35000)
        physicsYImpulse(-40000)
        uponSendToLabel(LANDING, 1)
    sprite('vr_6cknife00', 4)
    sprite('vr_6cknife00', 32767)
    label(1)
    sprite('vr_6cknife01', 15)
    EndMomentum(1)
    AbsoluteY(0)
    sprite('vr_6cknife01', 15)
    ConstantAlphaModifier(-15)


@State
def Eff2CZanzo():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(128000)
        AddY(280000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 18)
    sprite('vrhzef232_00', 2)
    sprite('vrhzef232_01', 16)
    AddAlpha(-100)


@State
def Eff3CZanzo():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(200000)
        AddY(100000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 10)
    sprite('vrhzef240_00', 2)
    sprite('vrhzef240_01', 8)
    AddAlpha(-100)


@State
def Eff8CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrhzef252_00', 2)
    sprite('vrhzef252_01', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrhzef252_02', 2)
    sprite('vrhzef252_03', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrhzef252_04', 2)
    sprite('vrhzef252_05', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrhzef252_06', 2)
    sprite('vrhzef252_07', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def Eff8CZanzo_5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(20000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrhzef252_08', 2)
    sprite('vrhzef252_09', 6)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def EffAir2CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(28000)
        AddY(-80000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 17)
    sprite('vrhzef253_00', 4)
    sprite('vrhzef253_01', 15)
    AddAlpha(-100)
    E0EAEffectPosition(0)


@State
def HZEF_Aura():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        LinkParticle('hzef_envaura')
        BlendMode_Add()
        Size(800)
        ContinueState(17)
    sprite('null', 17)
    ConstantAlphaModifier(-15)


@State
def HZEF_AuraDelete():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        ParticleLayer(2)
        ParticleSize(600)
        CallCustomizableParticle('hzef_deleteaura', -1)
        Size(600)
        ContinueState(1)
    sprite('null', 1)


@State
def EffUltimateAssaultBunshinA():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('hz430_00', 20)
    physicsXImpulse(32000)
    ConstantAlphaModifier(-10)


@State
def EffUltimateAssaultBunshinB():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        setInvincible(1)
    sprite('hz430_00', 20)
    physicsXImpulse(-32000)
    ConstantAlphaModifier(-10)


@State
def EffKamae():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        LinkParticle('hzef_kamaeaura')
        uponSendToLabel(56, 99)
        uponSendToLabel(32, 99)
    sprite('null', 32767)
    loopRest()
    label(99)
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def EffKamaeLand():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        ParticleLayer(5)
        CallPrivateEffect('hzef_landaura')
        uponSendToLabel(56, 99)
        uponSendToLabel(32, 99)
    sprite('null', 10)
    SetScaleSpeed(50)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(99)
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def EffLandAura():

    def upon_IMMEDIATE():
        ParticleLayer(5)
        CallPrivateEffect('hzef_landaura')
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    Size(1500)
    SetScaleSpeed(200)


@State
def EffAirAura():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    sprite('null', 10)
    ParticleLayer(5)
    CallPrivateEffect('hzef_airaura')
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    Size(1500)
    SetScaleSpeed(200)


@State
def EffCommandThrowAura():

    def upon_IMMEDIATE():
        LinkParticle('hzef_spaura')
    sprite('null', 60)


@State
def EffCommandThrowWind():

    def upon_IMMEDIATE():
        ParticleLayer(5)
        CallPrivateEffect('hzef_comthrowwind')
        Size(1200)
        RandAddScale(-200, 250)
        AlphaValue(150)
    sprite('null', 30)


@State
def EffSamaso():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('vrhzef401_00', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef401_01', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    E0EAEffectPosition(0)
    sprite('vrhzef401_02', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef401_03', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    sprite('vrhzef401_04', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    sprite('vrhzef401_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef401_06', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)


@State
def EffChudan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(40000)
        AddY(280000)
    sprite('vrhzef402_00', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef402_01', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef402_02', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef402_03', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    sprite('vrhzef402_04', 6)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    sprite('vrhzef402_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    sprite('vrhzef402_06', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)


@State
def EffGedan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(100000)
        AddY(-16000)
    sprite('vrhzef403_00', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef403_01', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef403_02', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef403_03', 6)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    sprite('vrhzef403_04', 4)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef403_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef403_06', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)


@State
def EffUchiOtoshi():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(64000)
        AddY(280000)
    sprite('vrhzef404_00', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef404_01', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef404_02', 1)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef404_03', 1)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    sprite('vrhzef404_04', 4)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef404_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef404_06', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)


@State
def EffSpKensei():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(220000)
        AddY(210000)
    sprite('vrhzef407_00', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef407_01', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    sprite('vrhzef407_02', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_Aura', 10)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    CreateObject('HZEF_AuraDelete', 10)
    sprite('vrhzef407_03', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_Aura', 10)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    CreateObject('HZEF_AuraDelete', 10)
    sprite('vrhzef407_04', 4)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_Aura', 9)
    CreateObject('HZEF_Aura', 10)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    CreateObject('HZEF_AuraDelete', 9)
    CreateObject('HZEF_AuraDelete', 10)
    sprite('vrhzef407_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef407_06', 4)


@State
def Eff410():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Normal()
        PaletteIndex(1)
    sprite('vrhzef410_00', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef410_01', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef410_02', 4)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    sprite('vrhzef410_03', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    sprite('vrhzef410_04', 6)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    sprite('vrhzef410_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef410_06', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)


@State
def hzef432_bind():

    def upon_IMMEDIATE():
        Eff3DEffect('hz_432bind.DIG', 'hzef_drainfield_motion_000.mmot')
        FaceSpawnLocation()
        TurnAround()
        RemoveOnCallStateEnd(3)
        EffectPosition(22, 103)
        Unknown23144(22, 0, 103, 0, 0, 0, 0, 0, 50, 0, 20)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 10)
    Size(0)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    SetScaleSpeed(120)
    CreateObject('hzef432_bindaura', 103)
    sprite('null', 10)
    SetScaleSpeed(-20)
    sprite('null', 1)
    ConstantAlphaModifier(0)
    Size(875)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    gotoLabel(0)
    label(1)
    DespawnEAEffect('hzef432_bindaura')
    CreateParticle('hzef_432bindaura_end', -1)
    sprite('null', 5)
    sprite('null', 10)
    SetScaleSpeed(80)
    ConstantAlphaModifier(-26)


@State
def hzef432_bindaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        LinkParticle('hzef_432bindaura')
        IgnoreScreenfreeze(1)
        uponSendToLabel(56, 99)
        uponSendToLabel(32, 99)
    sprite('null', 32767)
    loopRest()
    label(99)
    sprite('null', 10)
    BlendMode_Normal()
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def UltimateThrowCamera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
    sprite('null', 32767)
    AddX(100000)


@State
def EffUltimateLockSignal():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        CallPrivateEffect('hzef_ultimatelocksignal')
        IgnorePauses(3)
        ContinueState(200)
        if SLOT_19 > 650000:
            CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
        else:
            AddX(650000)
    sprite('null', 16)
    BlendMode_Add()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    Size(80)
    SetScaleSpeed(100)
    sprite('null', 36)
    SetScaleSpeed(5)
    sprite('null', 10)
    SetScaleSpeed(100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def EffUltimateMagicOpt():

    def upon_IMMEDIATE():
        CallPrivateEffect('hzef_eyeloop')
        ContinueState(60)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
    sprite('null', 15)
    AlphaValue(255)
    Size(500)
    SetScaleSpeed(100)
    sprite('null', 30)
    SetScaleSpeed(0)
    sprite('null', 15)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def UltimateLockMagic():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Eff3DEffect('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
        ContinueState(60)
        AbsoluteY(300000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
    sprite('null', 12)
    Size(200)
    SetScaleSpeed(40)
    ConstantAlphaModifier(20)
    CreateObject('EffUltimateMagicOpt', -1)
    CreateObject('UltimateLockMagicA', -1)
    CreateObject('UltimateLockMagicB', -1)
    CreateObject('UltimateLockMagicC', -1)
    sprite('null', 4)
    SetScaleSpeed(10)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('null', 32767)
    SetScaleSpeed(5)
    TriggerUponForState('UltimateLockMagicA', 32)
    TriggerUponForState('UltimateLockMagicB', 32)
    TriggerUponForState('UltimateLockMagicC', 32)
    loopRest()
    label(99)
    sprite('null', 10)
    CreateParticle('hzef_eyespark', -1)
    Size(1000)
    SetScaleSpeed(500)
    AlphaValue(255)
    ConstantAlphaModifier(-25)


@State
def UltimateLockMagicA():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Eff3DEffect('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
        Size(0)
        AddY(80000)
        uponSendToLabel(32, 0)
        uponSendToLabel(56, 0)
    sprite('null', 12)
    Size(300)
    SetScaleSpeed(50)
    AlphaValue(200)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('null', 5)
    physicsYImpulse(-16000)
    AlphaValue(50)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(-5)
    sprite('null', 5)
    EndMomentum(1)


@State
def UltimateLockMagicB():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Eff3DEffect('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
        Size(0)
        AddX(80000)
        AddY(-60000)
        uponSendToLabel(32, 0)
        uponSendToLabel(56, 0)
    sprite('null', 12)
    Size(300)
    SetScaleSpeed(50)
    AlphaValue(200)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('null', 5)
    physicsXImpulse(-16000)
    physicsYImpulse(12000)
    AlphaValue(50)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(-5)
    sprite('null', 20)
    EndMomentum(1)


@State
def UltimateLockMagicC():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        Eff3DEffect('hzef_lockcircleC.DIG', 'hzef_lockcircleC_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(0)
        Size(0)
        AddX(-80000)
        AddY(-60000)
        uponSendToLabel(32, 0)
        uponSendToLabel(56, 0)
    sprite('null', 12)
    Size(300)
    SetScaleSpeed(50)
    AlphaValue(200)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('null', 5)
    physicsXImpulse(16000)
    physicsYImpulse(12000)
    AlphaValue(50)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(-5)
    sprite('null', 20)
    EndMomentum(1)


@State
def EffUltimateLockPtc():

    def upon_IMMEDIATE():
        CallPrivateEffect('hzef_ultimatelock')
        IgnorePauses(3)
        ContinueState(60)
    sprite('null', 60)
    Size(1500)


@State
def UltimateLockObj():

    def upon_IMMEDIATE():
        if SLOT_19 > 650000:
            CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
        else:
            AddX(650000)
    sprite('null', 30)
    CreateObject('UltimateLockObjTop', -1)
    CreateObject('UltimateLockObjCenter', -1)
    CreateObject('UltimateLockObjBottom', -1)
    CreateObject('UltimateMagicCircle', -1)
    PrivateSE('hzse_07')


@State
def UltimateLockObjCenter():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_lockcircleA.DIG', 'hzef_lockcircleA_motion_000.mmo')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        ContinueState(120)
        uponSendToLabel(32, 99)
        uponSendToLabel(17, 99)
    sprite('null', 10)
    RunLoopUpon(17, 90)
    Size(900)
    SetScaleSpeedY(10)
    physicsYImpulse(20000)
    setGravity(800)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 20)
    SetScaleSpeed(100)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    physicsYImpulse(20000)


@State
def UltimateLockObjTop():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_lockcircleB.DIG', 'hzef_lockcircleB_motion_000.mmo')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        ContinueState(120)
        uponSendToLabel(32, 99)
        uponSendToLabel(17, 99)
    sprite('null', 10)
    RunLoopUpon(17, 90)
    Size(600)
    physicsYImpulse(32000)
    setGravity(800)
    SetScaleSpeedY(10)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 20)
    SetScaleSpeed(100)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    physicsYImpulse(32000)


@State
def UltimateLockObjBottom():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_lockcircleB.DIG', 'hzef_lockcircleB_motion_000.mmo')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        ContinueState(120)
        uponSendToLabel(32, 99)
        uponSendToLabel(17, 99)
    sprite('null', 10)
    RunLoopUpon(17, 90)
    Size(600)
    physicsYImpulse(10000)
    setGravity(800)
    SetScaleSpeedY(10)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 20)
    SetScaleSpeed(100)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    physicsYImpulse(5000)


@State
def UltimateMagicCircle():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        Hitstop(0)
        Damage(800)
        AttackP1(80)
        AttackP2(80)
        PushbackX(0)
        EnemyHitstopAddition(0, 90, 90)
        OppPositionOnHit(1, 0, 0)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        DefeatOpponentBehavior(1)
        StarterRating(2)

        def upon_OPPONENT_HIT():
            ObjectUpon(EVERY_FRAME, 32)

        def upon_EVERY_FRAME():
            if SLOT_19 > 650000:
                clearUponHandler(EVERY_FRAME)
                ObjectUpon(EVERY_FRAME, 41)
        Visibility(1)
    sprite('vr_magiccircle00', 2)
    CreateParticle('hzef_ultimatelock', -1)


@State
def EffDDZanzoA():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(0)
        AddX(220000)
        DeviationX(120000, -240000)
        AddY(220000)
        DeviationY(60000, -30000)
        RenderLayer(1)
    sprite('vrhzef431_00', 2)
    sprite('vrhzef431_00', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def EffDDZanzoB():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(0)
        AddX(240000)
        DeviationX(160000, -160000)
        AddY(240000)
        DeviationY(60000, -30000)
        RenderLayer(1)
    sprite('vrhzef431_01', 2)
    sprite('vrhzef431_01', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def EffDDZanzoC():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(0)
        AddX(220000)
        DeviationX(120000, -200000)
        AddY(260000)
        DeviationY(60000, -30000)
        RenderLayer(1)
    sprite('vrhzef431_02', 2)
    sprite('vrhzef431_02', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def EffDDZanzoD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(0)
        AddX(200000)
        DeviationX(200000, -120000)
        AddY(260000)
        DeviationY(60000, -30000)
        RenderLayer(1)
    sprite('vrhzef431_03', 2)
    sprite('vrhzef431_03', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def DDLockAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(2)
        BlendMode_Add()
        Size(0)
        ColorForTransition(4026583140)
        AbsoluteY(300000)
        uponSendToLabel(32, 99)
        uponSendToLabel(56, 99)
    sprite('vref_env', 10)
    SetScaleSpeed(600)
    sprite('vref_env', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('vref_env', 32767)
    AddX(20000)
    AddY(-100000)
    SetScaleSpeed(200)
    ColorTransition(3371840050, 10)
    loopRest()
    label(99)
    sprite('vref_env', 20)
    clearUponHandler(32)
    clearUponHandler(PLAYER_DAMAGED)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    Unknown23131()
    SetScaleSpeed(100)
    ConstantAlphaModifier(-10)


@State
def DDBodyAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RenderLayer(2)
        BlendMode_Add()
        Size(0)
        ColorForTransition(4278215830)
        AddX(20000)
        AbsoluteY(100000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
    sprite('vref_env', 10)
    SetScaleSpeed(1000)
    sprite('vref_env', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(0)
    sprite('vref_env', 30)
    ColorTransition(4294901760, 30)
    sprite('vref_env', 32767)
    Unknown23131()
    SetScaleSpeed(500)
    loopRest()
    label(99)
    sprite('vref_env', 60)
    clearUponHandler(32)
    clearUponHandler(PLAYER_DAMAGED)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    ColorTransition(25800, 60)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-5)


@State
def HZEF_DDBackAura():

    def upon_IMMEDIATE():
        ParticleLayer(5)
        RemoveOnCallStateEnd(3)
        CallPrivateEffect('hzef_ultimateaura')
        BlendMode_Add()
        Size(1500)
        uponSendToLabel(32, 99)
        uponSendToLabel(56, 99)
    sprite('null', 32767)
    CreateObject('HZEF_DDBackAuraFront', -1)
    label(99)
    sprite('null', 20)
    AlphaValue(200)
    ConstantAlphaModifier(-10)


@State
def HZEF_DDBackAuraFront():

    def upon_IMMEDIATE():
        ParticleLayer(1)
        RemoveOnCallStateEnd(3)
        CallPrivateEffect('hzef_ultimateaurafront')
        BlendMode_Add()
        Size(3000)
        AddY(12000)
        uponSendToLabel(32, 99)
        uponSendToLabel(56, 99)
    sprite('null', 32767)
    label(99)
    sprite('null', 20)
    AlphaValue(200)
    ConstantAlphaModifier(-10)


@State
def EffUltimateSnakeEye():

    def upon_IMMEDIATE():
        CallPrivateEffect('hzef_eyeloop')
        ContinueState(60)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
    sprite('null', 3)


@State
def EffDDSnakeFang():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()

        def upon_56():
            EndObject()
        AddX(120000)
        AddY(260000)
    sprite('vrhzef431atk_00', 20)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 0)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 1)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 2)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 3)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 4)
    ParticleLayer(1)
    CreateParticle('hzef_snakeeye', 5)
    sprite('vrhzef431atk_00', 10)
    sprite('vrhzef431atk_01', 3)
    TriggerUponForState('HZEF_DDBackAuraFront', 32)
    CharacterFlash2(-16764396, 3)
    CreateObject('EffUltimateSnakeEye', 0)
    CreateObject('EffUltimateSnakeEye', 1)
    CreateObject('EffUltimateSnakeEye', 2)
    CreateObject('EffUltimateSnakeEye', 3)
    CreateObject('EffUltimateSnakeEye', 4)
    CreateObject('EffUltimateSnakeEye', 5)
    sprite('vrhzef431atk_02', 3)
    CharacterFlash2(-16777216, 11)
    TriggerUponForState('EffUltimateSnakeEye', 32)
    sprite('vrhzef431atk_03', 4)
    sprite('vrhzef431atk_04', 4)
    sprite('vrhzef431atk_05', 8)
    StopCharacterFlash2()
    ConstantAlphaModifier(-20)
    physicsXImpulse(5000)
    physicsYImpulse(-2000)


@State
def EffDDSnakeFangOD():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()

        def upon_56():
            EndObject()
        AddX(120000)
        AddY(260000)
    sprite('vrhzef431atk_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    sprite('vrhzef431atk_00', 15)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 0)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 1)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 2)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 3)
    ParticleLayer(1)
    CallCustomizableParticle('hzef_snakeeye', 4)
    ParticleLayer(1)
    CreateParticle('hzef_snakeeye', 5)
    sprite('vrhzef431atk_00', 10)
    sprite('vrhzef431atk_01', 3)
    TriggerUponForState('HZEF_DDBackAuraFront', 32)
    CharacterFlash2(-16764396, 3)
    CreateObject('EffUltimateSnakeEye', 0)
    CreateObject('EffUltimateSnakeEye', 1)
    CreateObject('EffUltimateSnakeEye', 2)
    CreateObject('EffUltimateSnakeEye', 3)
    CreateObject('EffUltimateSnakeEye', 4)
    CreateObject('EffUltimateSnakeEye', 5)
    sprite('vrhzef431atk_02', 3)
    CharacterFlash2(-16777216, 11)
    TriggerUponForState('EffUltimateSnakeEye', 32)
    sprite('vrhzef431atk_03', 4)
    sprite('vrhzef431atk_04', 4)
    sprite('vrhzef431atk_05', 8)
    StopCharacterFlash2()
    ConstantAlphaModifier(-20)
    physicsXImpulse(5000)
    physicsYImpulse(-2000)


@State
def UltimateWindSmoke():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
        AddY(120000)
        AlphaValue(160)
    sprite('null', 32767)
    CreateObject('UltimateWindSmokeOpt', -1)
    loopRest()
    label(0)
    sprite('null', 32767)
    SetScaleSpeed(10)
    TriggerUponForState('UltimateWindSmokeOpt', 32)
    loopRest()
    loopRest()
    label(99)
    TriggerUponForState('UltimateWindSmokeOpt', 33)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def UltimateWindSmokeOpt():

    def upon_IMMEDIATE():
        Eff3DEffect('hzef_windsmoke.DIG', 'hzef_windsmoke_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 99)
        uponSendToLabel(56, 99)
        RotationAngle(-180000)
        Size(1250)
        AddScaleY(-500)
        AlphaValue(120)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 32767)
    SetScaleSpeed(10)
    loopRest()
    label(99)
    sprite('null', 10)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-20)
    SetScaleSpeedZ(100)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def HZEF_UltimateAssault():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(2)
        ParticleLayer(2)
        CallPrivateEffect('hzef_ultimateassault')
        IgnorePauses(3)
        Size(900)
        AddX(128000)
        AddY(-160000)

        def upon_56():
            ContinueState(10)
            BlendMode_Normal()
            ConstantAlphaModifier(-30)
    sprite('null', 110)


@State
def HZEF_UltimateAssaultOD():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('hzef_odjayoku00', '')
        AddX(150000)
        IgnoreScreenfreeze(2)
        SetScaleX(2300)
        SetScaleY(1250)
        RotationAngle(6000)
    sprite('null', 20)
    LinkParticle('hzef_odjayoku')
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def HZEF_DrainField():

    def upon_IMMEDIATE():
        AddY(300000)
        Eff3DEffect('hzef_drainfield.DIG', 'hzef_drainfield_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        TurnAround()

        def upon_EVERY_FRAME():
            CallPrivateFunction('BossHazamaDrainField', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_PLAYER_DAMAGED():
            clearUponHandler(PLAYER_DAMAGED)
            clearUponHandler(32)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(PLAYER_DAMAGED)
            clearUponHandler(32)
            sendToLabel(2)
        EffectPosition(3, 103)
        Unknown23144(3, 0, 103, 0, 0, 0, 0, 0, 50, 0, 20)
    sprite('null', 10)
    Size(0)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    SetScaleSpeed(120)
    sprite('null', 10)
    SetScaleSpeed(-20)
    sprite('null', 1)
    ConstantAlphaModifier(0)
    Size(1000)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    physicsYImpulse(-300)
    sprite('null', 30)
    physicsYImpulse(-200)
    sprite('null', 30)
    physicsYImpulse(-100)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 10)
    physicsYImpulse(300)
    sprite('null', 30)
    physicsYImpulse(200)
    sprite('null', 30)
    physicsYImpulse(100)
    sprite('null', 10)
    YAccel(0)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('null', 10)
    SetScaleSpeed(80)
    ConstantAlphaModifier(-26)


@State
def HZEF_DrainLoop():

    def upon_IMMEDIATE():
        EffectPosition(3, 103)
        LinkParticle('hzef_drainloop')
        BlendMode_Add()
        Unknown23144(3, 0, 103, 0, 0, 0, 0, 0, 50, 0, 20)
        IgnoreScreenfreeze(1)
    sprite('null', 120)


@State
def HZEF_DrainEnemy():

    def upon_IMMEDIATE():
        EffectPosition(22, 103)
        LinkParticle('hzef_drainenemy')
        BlendMode_Add()
        Unknown23144(22, 0, 103, 0, 0, 0, 0, 0, 50, 0, 20)
        IgnoreScreenfreeze(1)
    sprite('null', 120)


@State
def hzef432():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
    sprite('vrhzef432_00', 6)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrhzef432_01', 6)
    CreateParticle('hzef_432backaura_01', 0)
    CreateParticle('hzef_432backaura_01', 1)
    CreateParticle('hzef_432backaura_01', 2)
    sprite('vrhzef432_02', 6)
    CreateParticle('hzef_432backaura_01', 0)
    CreateParticle('hzef_432backaura_01', 1)
    CreateParticle('hzef_432backaura_01', 2)
    CreateParticle('hzef_432backaura_01', 3)
    sprite('vrhzef432_03', 6)
    CreateParticle('hzef_432backaura_01', 0)
    CreateParticle('hzef_432backaura_01', 1)
    CreateParticle('hzef_432backaura_01', 2)
    CreateParticle('hzef_432backaura_01', 3)
    sprite('vrhzef432_04', 6)
    RenderLayer(11)
    CreateParticle('hzef_432backaura_01', 0)
    CreateParticle('hzef_432backaura_01', 1)
    CreateParticle('hzef_432backaura_01', 2)
    sprite('vrhzef432_05', 6)
    sprite('vrhzef432_06', 3)
    Size(1100)
    AlphaValue(226)
    sprite('vrhzef432_06', 3)


@State
def HZEF_ASTBACK():

    def upon_IMMEDIATE():
        Unknown4022(2)
        ParticleLayer(5)
        CallPrivateEffect('hzef_astback')
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
        uponSendToLabel(PLAYER_DAMAGED, 99)
    sprite('null', 90)
    label(0)
    sprite('null', 30)
    ConstantAlphaModifier(-9)
    loopRest()
    ExitState()
    label(99)
    sprite('null', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def HZEF_ASTMagicCircle():

    def upon_IMMEDIATE():
        Unknown4022(2)
        ParticleLayer(2)
        CallPrivateEffect('hzef_aststartcircle')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(PLAYER_DAMAGED, 99)
    sprite('null', 120)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-2)
    CommonSE('022_magiccircle_c')
    loopRest()
    ExitState()
    label(99)
    sprite('null', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def HZEF_ASTSIGNAL():

    def upon_IMMEDIATE():
        ParticleLayer(1)
        CallPrivateEffect('hzef_astsignal')
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        AddY(280000)
    sprite('null', 70)
    CommonSE('022_magiccircle_c')


@State
def KusariAstral():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(5)
        Damage(0)
        AirPushbackX(0)
        YImpulseBeforeWallbounce(-50)
        AirUntechableTime(1200)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        OppPositionOnHit(3, 0, 64000)
        DamageFromStateOnly('AstralHeat')
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        EndMomentum(1)
        EnableAfterimage(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        BlendMode_Normal()

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            pass

        def upon_32():
            SetActionMark(0)
            SetZVal(-500)
            CallPrivateFunction('KusariMochite', 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown23143(-8000, 60000, 70)
            RotationSomething(0)
            RenderLayer(8)
            CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_33():
            SetActionMark(0)
            SetZVal(-500)
            CallPrivateFunction('KusariMochite', 0, 1, 0, 0, 0, 0, 0, 0)
            Unknown23143(-9000, 60000, 70)
            RotationSomething(0)
            RenderLayer(8)
            CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_34():
            SetActionMark(0)
            SetZVal(-500)
            CallPrivateFunction('KusariMochite', 0, 2, 0, 0, 0, 0, 0, 0)
            Unknown23143(-10000, 60000, 70)
            RotationSomething(0)
            RenderLayer(8)
            CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_35():
            SetActionMark(0)
            SetZVal(-500)
            CallPrivateFunction('KusariMochite', 0, 3, 0, 0, 0, 0, 0, 0)
            Unknown23143(0, 60000, 70)
            RotationSomething(0)
            RenderLayer(8)
            CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_36():
            SetActionMark(0)
            SetZVal(-500)
            CallPrivateFunction('KusariMochite', 0, 4, 0, 0, 0, 0, 0, 0)
            Unknown23143(3500, 60000, 70)
            RotationSomething(0)
            RenderLayer(8)
            CallPrivateFunction('KusariRenderStage', 0, 7, 0, 6, 0, 0, 0, 0)

        def upon_37():
            SetActionMark(1)
            SetZVal(500)
            CallPrivateFunction('KusariMochite', 0, 5, 0, 0, 0, 0, 0, 0)
            Unknown23143(6500, 60000, 70)
            RotationSomething(0)
            RenderLayer(11)
            CallPrivateFunction('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)

        def upon_38():
            SetActionMark(1)
            SetZVal(500)
            CallPrivateFunction('KusariMochite', 0, 6, 0, 0, 0, 0, 0, 0)
            Unknown23143(6500, 60000, 70)
            RotationSomething(0)
            RenderLayer(11)
            CallPrivateFunction('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)

        def upon_39():
            SetActionMark(1)
            SetZVal(500)
            CallPrivateFunction('KusariMochite', 0, 7, 0, 0, 0, 0, 0, 0)
            Unknown23143(1000, 60000, 70)
            RotationSomething(0)
            RenderLayer(11)
            CallPrivateFunction('KusariRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)
        uponSendToLabel(40, 0)

        def upon_OPPONENT_HIT():
            ObjectUpon(EVERY_FRAME, 32)
            HUDVisibillity(1)
            CreateObject('AST_Lock', 101)

        def upon_41():
            EndAttack()
    sprite('vr_chain_tip03', 1)
    EnableAfterimage(1)
    if SLOT_2:
        CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
        CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, -10)
        CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, -10)
        CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, -10)
        CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, -10)
        CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, -10)
        CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    else:
        CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
        CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
        CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
        CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
        CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
        CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
        CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip03', 9)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    sprite('vr_chain_tip04', 20)
    sprite('vr_chain_tip04', 6)
    sprite('vr_chain_tip04', 3)
    sprite('vr_chain_tip04', 3)
    sprite('vr_chain_tip04', 4)
    sprite('vr_chain_tip04', 14)
    sprite('vr_chain_tip04', 32767)
    loopRest()
    label(0)
    sprite('vr_chain_tip04ex01', 30)
    clearUponHandler(40)
    ConstantAlphaModifier(-20)


@State
def AST_Lock():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('hz_lock_C.DIG', 'hz_lock_C_mot_000.mmot')
        BlendMode_Add()
        Visibility(1)
        AddY(128000)
        Size(1500)
        AlphaValue(0)
        ConstantAlphaModifier(40)
    sprite('null', 5)
    SetScaleSpeed(-120)
    sprite('null', 25)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(-10)


@State
def AST_Enshutsu():

    def upon_IMMEDIATE():
        ContinueState(600)
    sprite('null', 120)
    CreateObject('AST_Circle', -1)
    CreateObject('AST_Snake', -1)

    def RunOnObject_1():
        DeviationX(256000, 420000)
        RandSpeedX(100, 500)
        DeviationY(0, 32000)
    CreateObject('AST_Snake', -1)

    def RunOnObject_1():
        DeviationX(-256000, -420000)
        RandSpeedX(-100, -500)
        DeviationY(0, 32000)
    sprite('null', 150)
    CreateObject('AST_Unite', -1)
    sprite('null', 170)
    CreateObject('AST_Body', -1)
    CreateObject('AST_Head', -1)
    sprite('null', 30)
    CreateObject('AST_Breath', -1)
    sprite('null', 60)
    CreateObject('HZAST_RedOut', -1)


@State
def AST_Circle():

    def upon_IMMEDIATE():
        FaceRight()
        IgnoreScreenfreeze(1)
        Eff3DEffect('hz_ah_A_circle.DIG', 'hz_ah_A_circle_mot_000.mmot')
        BlendMode_Add()
        Visibility(1)
    sprite('null', 150)
    SetScaleSpeed(4)


@State
def AST_Snake():

    def upon_IMMEDIATE():
        FaceRight()
        IgnoreScreenfreeze(1)
        Eff3DEffect('hz_ah_A_snake.DIG', 'hz_ah_A_snake_mot_000.mmot')
        Visibility(1)
    sprite('null', 150)


@State
def AST_Unite():

    def upon_IMMEDIATE():
        FaceRight()
        IgnoreScreenfreeze(1)
        Eff3DEffect('hz_ah_A_unite.DIG', 'hz_ah_A_unite_mot_000.mmot')
        RenderLayer(4)
        Visibility(1)
        BlendMode_Normal()
        Size(1500)
        AddY(-160000)
        AlphaValue(0)
    sprite('null', 30)
    AddRotationPerFrame(-500)
    ConstantAlphaModifier(10)
    sprite('null', 130)
    sprite('null', 50)
    ConstantAlphaModifier(-5)


@State
def AST_Body():

    def upon_IMMEDIATE():
        FaceRight()
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('hz_ah_B_body.DIG', 'hz_ah_B_body_mot_000.mmot')
        FaceSpawnLocation()
        BlendMode_Normal()
        Visibility(1)
    sprite('null', 220)


@State
def AST_Breath():

    def upon_IMMEDIATE():
        FaceRight()
        IgnoreScreenfreeze(1)
        LinkParticle('efbg_hz_breath')
        AbsoluteY(256000)
        RenderLayer(1)
        BlendMode_Add()
        Visibility(1)
        Size(500)
    sprite('null', 200)


@State
def AST_Head():

    def upon_IMMEDIATE():
        FaceRight()
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('hz_ah_B_head.DIG', 'hz_ah_B_head_mot_000.mmot')
        FaceSpawnLocation()
        BlendMode_Normal()
        Visibility(1)
    sprite('null', 220)


@State
def HZAST_RedOut():

    def upon_IMMEDIATE():
        RenderLayer(4)
        IgnoreScreenfreeze(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        BlendMode_Normal()
        ColorForTransition(4294901760)
        Size(20000)
        AlphaValue(0)
    sprite('vr_white', 40)
    ConstantAlphaModifier(40)
    sprite('vr_white', 20)
    ConstantAlphaModifier(-15)


@State
def HZAST_BlackOut():

    def upon_IMMEDIATE():
        RenderLayer(4)
        IgnoreScreenfreeze(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
        BlendMode_Normal()
        ColorForTransition(4278190080)
        Size(20000)
        AlphaValue(0)
    sprite('vr_white', 20)
    ConstantAlphaModifier(12)
    sprite('vr_white', 40)
    sprite('vr_white', 20)
    ConstantAlphaModifier(-15)


@State
def NoelEntry():

    def upon_IMMEDIATE():
        uponSendToLabel(56, 1)
        PaletteIndex(7)
        XPositionRelativeFacing(-50000)
    sprite('no602_00', 32767)
    label(1)
    sprite('no602_00', 200)
    loopRest()


@State
def NoelWarp():

    def upon_IMMEDIATE():
        SetZVal(-500)
        PaletteIndex(7)
        XPositionRelativeFacing(-50000)
        ScreenCollision(0)
        BlendMode_Normal()
    sprite('no602_00', 90)
    sprite('no602_00', 15)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 15)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_s')
    CommonSE('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 15)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 15)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_s')
    CommonSE('001_airbackdash_0')
    sprite('no602_00', 15)
    sprite('no602_00', 4)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_s')
    CommonSE('000_airdash_2')
    ConstantAlphaModifier(-10)
    sprite('no602_00', 6)
    sprite('no602_00', 6)
    sprite('no602_00', 6)
    CreateParticle('haef_event_lose_end', 0)
    sprite('no602_00', 6)
    XPositionRelativeFacing(-500000)


@State
def NoelTimeUpLose():

    def upon_IMMEDIATE():
        uponSendToLabel(56, 1)
        PaletteIndex(7)
        XPositionRelativeFacing(0)
    sprite('no620_08', 32767)
    loopRest()
    label(1)
    clearUponHandler(56)
    uponSendToLabel(56, 2)
    sprite('no620_08', 32767)
    loopRest()
    label(2)
    clearUponHandler(56)
    uponSendToLabel(56, 3)
    sprite('no620_08', 32767)
    loopRest()
    label(3)
    sprite('no620_08', 20)
    loopRest()


@State
def NoelDownUpperSet():

    def upon_IMMEDIATE():
        uponSendToLabel(56, 1)
        PaletteIndex(7)
        XPositionRelativeFacing(-130000)
        AbsoluteY(100000)
        setGravity(0)
    sprite('no062_00', 32767)
    loopRest()
    label(1)
    sprite('no062_00', 1)
    loopRest()


@State
def NoelDownUpperGo():

    def upon_IMMEDIATE():
        PaletteIndex(7)
        XPositionRelativeFacing(-130000)
        AbsoluteY(100000)
        setGravity(0)
        SetZVal(100)
        ContinueState(150)
    sprite('no062_00', 3)
    XPositionRelativeFacing(-130000)
    sprite('no062_00', 4)
    XPositionRelativeFacing(-130000)
    sprite('no062_00', 4)
    XPositionRelativeFacing(-210000)
    sprite('no062_00', 4)
    XPositionRelativeFacing(-290000)
    sprite('no062_00', 4)
    XPositionRelativeFacing(-370000)
    sprite('no062_00', 4)
    sprite('no062_00', 4)
    sprite('no062_00', 4)
    setGravity(1000)
    sprite('no062_00', 6)
    sprite('no062_00', 3)
    sprite('no062_00', 1)
    CallCustomizableParticle('ef_hitmd', 108)
    physicsYImpulse(0)
    setGravity(0)
    sprite('no062_00', 1)
    AddX(-3000)
    sprite('no062_00', 1)
    AddX(3000)
    sprite('no062_00', 1)
    AddX(-3000)
    sprite('no062_00', 1)
    AddX(3000)
    sprite('no062_00', 1)
    AddX(-3000)
    sprite('no062_00', 1)
    AddX(3000)
    sprite('no072_01', 100)
    physicsXImpulse(-22000)
    physicsYImpulse(14000)
    EndYPhysicsImpulse()


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
def KusariBurstDD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)

        def upon_31():
            CallPrivateFunction('KusariDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('KusariKansetsu', 0, 7, 0, 0, 0, 0, 0, 0)
        EnableAfterimage(1)
        AfterimageColor_1(200, 255, 255, 255)
        AfterimageColor_2(0, 255, 255, 255)
        TurnParticleColorable1(1)
        Unknown3054(56, 120)
        Unknown3054(57, 80)
        Unknown3054(58, 40)
        BlendMode_Normal()

        def upon_48():
            CallPrivateFunction('KusariIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_51:
                RotationSomething(-180000)
            if SLOT_2:
                Unknown4055(0)
                ParticleSize(500)
                CallCustomizableParticle('hzef_antiairchain', -1)
                ParticleLayer(5)
                CallCustomizableParticle('hzef_exheadmoveopt', -1)
        uponSendToLabel(32, 0)
    sprite('vr_chain_tip03aa', 1)
    RenderLayer(1)
    Unknown23143(40000, 80000, 70)
    EnableAfterimage(1)
    CallPrivateFunction('KusariParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('KusariParam', 0, 1, 0, 16, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 2, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 3, 0, 50, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 4, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 5, 0, 83, 0, 0, 0, 10)
    CallPrivateFunction('KusariParam', 0, 6, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('KusariFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    CreateObject('ExPortalSp', -1)

    def RunOnObject_1():
        RotationAngle(-40000)
    RotationAngle(-30000)
    sprite('vr_chain_tip03aa', 9)
    SetActionMark(1)
    CallPrivateFunction('KusariSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('vr_chain_tip04ex01', 6)
    SetActionMark(0)
    TriggerUponForState('ExPortalSp', 32)
    Unknown23143(-10000, -50000, 50)
    sprite('vr_chain_tip04ex01', 4)
    SLOT_51 = 1
    Unknown23143(-80000, -20000, 10)
    sprite('vr_chain_tip04ex01', 8)
    Unknown23143(-100000, -60000, 10)
    sprite('vr_chain_tip04ex01', 4)
    Unknown23143(10000, 10000, 20)
    sprite('vr_chain_tip04ex01', 10)
    Unknown23143(0, 0, 0)
    Unknown23144(3, 0, 109, 0, 0, 0, 0, 0, 80, 0, 3)


@State
def Eff440Zanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 18)
    sprite('vrhzef440_00', 2)
    AddX(-100000)
    sprite('vrhzef440_01', 16)
    E0EAEffectPosition(0)
    AddAlpha(-100)


@State
def Eff440Zanzo_b():

    def upon_IMMEDIATE():
        Unknown4022(3)
        BlendMode_Add()
        PaletteIndex(2)
        AddX(100000)
    sprite('null', 1)
    sprite('vrhzef440_10', 5)


@State
def Eff440Zanzo_b2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 18)
        AbsoluteY(0)
        AddX(100000)
    sprite('vrhzef440_11', 2)
    sprite('vrhzef440_12', 16)
    AddAlpha(-100)


@State
def Eff440snake():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(-128000)
        AbsoluteY(-32000)
    sprite('vrhzef440_30', 3)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrhzef440_31', 3)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrhzef440_32', 4)
    CreateParticle('hzef_432backaura_01', 0)
    CreateParticle('hzef_432backaura_01', 1)
    sprite('vrhzef440_33', 4)
    CreateParticle('hzef_432backaura_01', 0)
    CreateParticle('hzef_432backaura_01', 1)
    CreateParticle('hzef_432backaura_01', 2)
    sprite('vrhzef440_34', 4)
    CreateParticle('hzef_432backaura_01', 0)
    sprite('vrhzef440_35', 4)
    sprite('vrhzef440_36', 4)


@State
def Eff411():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1125)
        AddX(-35000)
        AbsoluteY(-32000)
    sprite('vrhzef411_00', 3)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    sprite('vrhzef411_01', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef411_02', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef411_03', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    sprite('vrhzef411_04', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef411_05', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)


@State
def Eff412Zanzo():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(2)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor1(255)
        PaletteColor2(1)
        PaletteColor3(254)
        PaletteColor4(1)
        AddX(7000)
        AddY(-7000)
        ColorForTransition(4294967295)
        ColorTransition(16711935, 8)
    sprite('vrhzef412_00', 2)
    sprite('vrhzef412_01', 8)
    AddAlpha(-127)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act3Event_Ragna():

    def upon_IMMEDIATE():
        LoadSpritePalette(0)
        XPositionRelativeFacing(120000)
        SetZVal(750)
        EnableCollision(0)
        ScreenCollision(0)
        Flip()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(LANDING, 2)
    sprite('rg620_05', 32767)
    label(0)
    sprite('rg620_05', 5)
    sprite('rg620_04', 5)
    sprite('rg620_03', 5)
    sprite('rg620_02', 5)
    sprite('rg620_01', 5)
    sprite('rg620_00', 5)
    label(9)
    sprite('rg000_00', 7)
    sprite('rg000_01', 7)
    sprite('rg000_02', 7)
    sprite('rg000_03', 7)
    sprite('rg000_04', 7)
    sprite('rg000_05', 7)
    sprite('rg000_06', 7)
    sprite('rg000_05', 7)
    sprite('rg000_04', 7)
    sprite('rg000_03', 7)
    sprite('rg000_02', 7)
    sprite('rg000_01', 7)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('rg033_00', 4)
    sprite('rg033_01', 4)
    PrivateSE('rgse_00')
    physicsXImpulse(-28000)
    physicsYImpulse(20000)
    setGravity(1400)
    JumpSoundEffects()
    JumpEffects(3, 100)
    label(99)
    sprite('rg033_02', 3)
    sprite('rg033_03', 3)
    loopRest()
    gotoLabel(99)
    label(2)
    sprite('null', 10)
    EndMomentum(1)
    Visibility(1)


@State
def Act3Event_EffGedan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddX(240000)
        AddY(-16000)
    sprite('vrhzef403_00', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    AlphaValue(55)
    ConstantAlphaModifier(25)
    sprite('vrhzef403_01', 3)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    sprite('vrhzef403_02', 2)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    sprite('vrhzef403_03', 18)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_Aura', 5)
    CreateObject('HZEF_Aura', 6)
    CreateObject('HZEF_Aura', 7)
    CreateObject('HZEF_Aura', 8)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    CreateObject('HZEF_AuraDelete', 5)
    CreateObject('HZEF_AuraDelete', 6)
    CreateObject('HZEF_AuraDelete', 7)
    CreateObject('HZEF_AuraDelete', 8)
    sprite('vrhzef403_04', 4)
    E0EAEffectPosition(0)
    CreateObject('HZEF_Aura', 0)
    CreateObject('HZEF_Aura', 1)
    CreateObject('HZEF_Aura', 2)
    CreateObject('HZEF_Aura', 3)
    CreateObject('HZEF_Aura', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef403_05', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)
    sprite('vrhzef403_06', 4)
    CreateObject('HZEF_AuraDelete', 0)
    CreateObject('HZEF_AuraDelete', 1)
    CreateObject('HZEF_AuraDelete', 2)
    CreateObject('HZEF_AuraDelete', 3)
    CreateObject('HZEF_AuraDelete', 4)


@State
def Eventoffset_Sosai_ntvshz():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(200000)
        DeviationX(-20000, 20000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)
